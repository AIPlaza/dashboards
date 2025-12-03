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
        self.pairs_url = f"{self.base_url}{settings.binance_pairs_endpoint}"

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
        """Get default headers for Binance requests."""
        return {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Origin": "https://p2p.binance.com",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
        }

    def get_all_trading_pairs(self) -> List[Dict[str, str]]:
        """
        Discover all available trading pairs from Binance.

        Returns:
            List of dicts: [{"fiat": "VES", "asset": "USDT", "trade_type": "BUY"}, ...]
        """
        logger.info("Fetching all trading pairs...")

        # Rate limit
        rate_limiter.acquire()

        try:
            response = self.session.post(
                self.pairs_url,
                json={},
                headers=self._get_headers(),
                timeout=settings.request_timeout_seconds
            )
            response.raise_for_status()
            data = response.json()

            if data.get("code") != "000000":
                logger.error(f"Failed to fetch pairs: {data.get('message')}")
                return []

            pairs = []
            for item in data.get("data", []):
                fiat = item.get("fiatUnit")
                assets = item.get("assetList", [])

                for asset in assets:
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

            logger.info(f"Found {len(pairs)} trading pairs")
            return pairs

        except Exception as e:
            logger.error(f"Error fetching trading pairs: {e}")
            return []

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
                "rows": settings.max_pages_per_pair,
                "tradeType": trade_type,
                "asset": asset,
                "fiat": fiat,
                "publisherType": None,
                "payTypes": [],
                "proMerchantAds": False
            }

            try:
                response = self.session.post(
                    self.search_url,
                    headers=self._get_headers(),
                    json=payload,
                    timeout=settings.request_timeout_seconds
                )
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

                if page > settings.max_pages_per_pair:
                    logger.warning(
                        f"Reached max pages per pair "
                        f"({settings.max_pages_per_pair}) for "
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
                method.get("payType") for method in adv.get("tradeMethods", [])
            ]

            # Create parsed offer
            parsed_offer = {
                "offer_external_id": str(uuid.uuid4()),
                "advertiser_nickname": advertiser.get("nickName"),
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