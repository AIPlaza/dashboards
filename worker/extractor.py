"""
Modular data extraction orchestrator.
Handles parallel extraction of all trading pairs from Binance P2P.
"""
import json
import logging
import uuid
import time
from datetime import datetime
from typing import List, Dict, Optional, Any
from concurrent.futures import ThreadPoolExecutor, as_completed
from decimal import Decimal

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .config import settings
from .db import db_manager
from .rate_limiter import rate_limiter

logger = logging.getLogger(__name__)

class BinanceP2PExtractor:
    """Extracts P2P trading data from Binance."""

    def __init__(self):
        self.base_url = settings.binance_base_url
        self.search_url = f"{self.base_url}{settings.binance_search_endpoint}"


        # Create session with retry strategy
        self.session = self._create_session()

    def _create_session(self) -> requests.Session:
        """Create requests session with retry logic."""
        session = requests.Session()

        retry_strategy = Retry(
            total=settings.max_retries,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["POST", "GET"]
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)

        return session

    def _get_headers(self) -> Dict[str, str]:
        """Returns headers that mimic a real browser request."""
        return {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Origin": "https://p2p.binance.com",
            "Referer": "https://p2p.binance.com/", # CRITICAL: Binance requires this
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/131.0.0.0 Safari/537.36" # Updated to Dec 2024
            ),
        }

    def get_all_trading_pairs(self) -> List[Dict[str, str]]:
        """
        Discover all available trading pairs from Binance.

        Returns:
            List of dicts: [{"fiat": "VES", "asset": "USDT", "trade_type": "BUY"}, ...]
        """
        logger.info("Fetching all trading pairs...")

        logger.info("Generating trading pairs from p2p_config.json...")

        pairs = []
        configured_fiats = settings.p2p_config["FIATS"]
        cryptos_by_fiat = settings.p2p_config["CRYPTOS_BY_FIAT"]

        for fiat in configured_fiats:
            if fiat in cryptos_by_fiat:
                for asset in cryptos_by_fiat[fiat]:
                    pairs.append({
                        "fiat": fiat,
                        "asset": asset,
                        "trade_type": "BUY"
                    })
                    pairs.append({
                        "fiat": fiat,
                        "asset": asset,
                        "trade_type": "SELL"
                    })
            else:
                logger.warning(f"No crypto assets configured for fiat: {fiat}. Skipping.")

        logger.info(f"Generated {len(pairs)} trading pairs from configuration.")
        return pairs

    def extract_pair_offers(
        self,
        fiat: str,
        asset: str,
        trade_type: str
    ) -> List[Dict[str, Any]]:
        """
        Extract all offers for a single trading pair.

        Args:
            fiat: Fiat currency code (e.g., "VES")
            asset: Crypto asset code (e.g., "USDT")
            trade_type: "BUY" or "SELL"

        Returns:
            List of offer dictionaries with raw data
        """
        all_offers = []
        page = 1

        logger.info(f"Extracting {fiat}/{asset}/{trade_type}")

        while True:
            # Rate limit
            rate_limiter.acquire()

            payload = {
                "page": page,
                "rows": settings.binance_p2p_until_page,
                "tradeType": trade_type,
                "asset": asset,
                "fiat": fiat,
                "publisherType": None,
                "payTypes": [],
                "proMerchantAds": False,
                "countries": [],
                "shieldMerchantAds": False,
                "filterType": "all",
                "periods": [],
                "additionalKycVerifyFilter": 0,
                "classifies": ["mass", "profession", "fiat_trade"],
                "tradedWith": False,
                "followed": False
            }

            logger.info(f"Binance API request to {self.search_url}")
            logger.debug(f"Payload: {json.dumps(payload, indent=2)}")
            try:
                response = self.session.post(
                    self.search_url,
                    headers=self._get_headers(),
                    json=payload,
                    timeout=settings.request_timeout_seconds
                )
                logger.info(f"Response status: {response.status_code}")
                logger.debug(f"Full Response body: {response.text}")
                response.raise_for_status()
                data = response.json()

                if data.get("code") != "000000":
                    logger.error(
                        f"Failed to extract {fiat}/{asset}/{trade_type}: "
                        f"{data.get('message')}"
                    )
                    break

                offers = data.get("data", [])
                if not offers:
                    logger.info(f"No offers found for {fiat}/{asset}/{trade_type}")
                    break

                # Parse offers
                for ad in offers:
                    parsed_offer = self._parse_offer(ad)
                    if parsed_offer:
                        all_offers.append(parsed_offer)

                page += 1

                if page > settings.binance_p2p_until_page:
                    logger.warning(
                        f"Reached max pages per pair "
                        f"({settings.binance_p2p_until_page}) for "
                        f"{fiat}/{asset}/{trade_type}"
                    )
                    break

            except Exception as e:
                logger.error(
                    f"Error extracting {fiat}/{asset}/{trade_type}: {e}"
                )
                break

        logger.info(
            f"Extracted {len(all_offers)} offers for "
            f"{fiat}/{asset}/{trade_type}"
        )
        return all_offers

    def _parse_offer(self, ad: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Parse raw offer data from Binance API.

        Returns:
            Dictionary with cleaned, typed data ready for database insertion
        """
        try:
            adv = ad["adv"]
            advertiser = ad["advertiser"]

            # Extract and validate numeric fields
            try:
                price = Decimal(str(adv.get("price", 0)))
                available_amount = Decimal(str(adv.get("surplusAmount", 0)))
                min_limit = Decimal(str(adv.get("minSingleTransAmount", 0)))
                max_limit = Decimal(str(adv.get("maxSingleTransAmount", 0)))

                if price <= 0 or available_amount <= 0:
                    logger.warning(f"Skipping offer with invalid price/amount")
                    return None

            except (ValueError, TypeError):
                logger.warning(f"Skipping offer due to invalid numeric format")
                return None

            # Extract payment methods
            payment_methods = [
                {
                    "identifier": str(method.get("identifier", "")),
                    "tradeMethodName": str(method.get("tradeMethodName", ""))
                }
                for method in adv.get("tradeMethods", [])
            ]

            # Get advNo, which will be the external ID
            offer_id = adv.get("advNo")
            if not offer_id:
                logger.warning("Skipping offer due to missing 'advNo'.")
                return None

            # Create parsed offer
            parsed_offer = {
                "id": offer_id, # Use advNo from Binance API as the external ID
                "advertiser": { # Nested advertiser dictionary
                    "id": advertiser.get("userNo"), # Assuming userNo is the ID
                    "nickname": advertiser.get("nickName"),
                    "completion_rate": advertiser.get("completionRate", 0),
                    "total_orders": advertiser.get("totalOrderNum", 0),
                },
                "price": price,
                "available_amount": available_amount,
                "min_limit": min_limit,
                "max_limit": max_limit,
                "payment_methods": payment_methods,
                "asset": adv.get("asset"),
                "fiat": adv.get("fiatUnit"),
                "trade_type": adv.get("tradeType")
            }

            return parsed_offer

        except KeyError as e:
            logger.error(f"Missing key in offer data: {e}")
            return None

        except Exception as e:
            logger.error(f"Error parsing offer data: {e}")
            return None

    def extract_all_offers(self) -> List[Dict[str, Any]]:
        """
        Extract offers from ALL trading pairs in parallel.

        Returns:
            List of all offers across all pairs
        """
        # Get all trading pairs
        pairs = self.get_all_trading_pairs()

        if not pairs:
            logger.error("No trading pairs found")
            return []

        logger.info(f"Starting parallel extraction for {len(pairs)} pairs...")

        all_offers = []

        # Extract in parallel
        with ThreadPoolExecutor(max_workers=settings.max_workers) as executor:
            # Submit all extraction tasks
            future_to_pair = {
                executor.submit(
                    self.extract_pair_offers,
                    pair["fiat"],
                    pair["asset"],
                    pair["trade_type"]
                ): pair
                for pair in pairs
            }

            # Collect results as they complete
            for future in as_completed(future_to_pair):
                pair = future_to_pair[future]
                try:
                    offers = future.result()
                    all_offers.extend(offers)
                except Exception as e:
                    logger.error(
                        f"Extraction failed for "
                        f"{pair['fiat']}/{pair['asset']}/{pair['trade_type']}: {e}"
                    )

        logger.info(f"Total offers extracted: {len(all_offers)}")
        return all_offers

# Global extractor instance
extractor = BinanceP2PExtractor()