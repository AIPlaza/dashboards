from typing import Optional

import json
import logging
import os
from functools import lru_cache

import requests
from dotenv import load_dotenv

from .config import Settings

load_dotenv()

logger = logging.getLogger(__name__)

settings = Settings()

def _get_default_headers():
    """Returns a dictionary of default headers for Binance P2P requests."""
    return {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Host": "p2p.binance.com",
        "Origin": "https://p2p.binance.com",
        "Pragma": "no-cache",
        "TE": "Trailers",
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        ),
    }


def _make_binance_request(url: str, payload: dict) -> Optional[dict]:
    """
    Makes a POST request to a Binance P2P endpoint, handles common errors,
    and returns the full JSON response on success.
    """
    headers = _get_default_headers()
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        if data.get("code") == "000000":
            return data  # Return the whole successful response
        else:
            logger.error(f"Binance API returned an error: {data.get('message')}")
            return None
    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred during Binance request to {url}: {e}")
    except json.JSONDecodeError:
        logger.error(f"Failed to decode Binance response from {url} as JSON.")
    except KeyError as e:
        logger.error(
            f"Could not find expected data in Binance response from {url}: {e}"
        )
    return None


@lru_cache(maxsize=128)
def get_binance_offers(
    fiat: str = "VES",
    asset: str = "USDT",
    tradeType: str = "BUY",
    page: int = 1,
    rows: int = 20,
):
    """
    Fetches a single page of P2P offers from Binance for on-demand API requests.

    Args:
        fiat: The fiat currency (e.g., 'VES', 'USD').
        asset: The crypto asset (e.g., 'USDT', 'BTC').
        tradeType: The trade type ('BUY' or 'SELL').
        page: The page number to fetch.
        rows: The number of results per page.

    Returns:
        A list of dictionaries, where each dictionary represents a P2P offer.
    """
    url = settings.binance_p2p_search_url
    data = {
        "proMerchantAds": False,
        "page": page,
        "rows": rows,
        "payTypes": [],
        "countries": [],
        "tradeType": tradeType,
        "asset": asset,
        "fiat": fiat,
        "publisherType": None,
    }

    logger.info(
        f"Fetching single page of Binance offers: page={page}, fiat={fiat}, "
        f"asset={asset}, tradeType={tradeType}"
    )
    p2p_data = _make_binance_request(url, data)

    if not p2p_data or not p2p_data.get("data"):
        return []

    offers = []
    try:
        for ad in p2p_data["data"]:
            adv = ad["adv"]
            advertiser = ad["advertiser"]
            try:
                price = float(adv.get('price'))
                available = float(adv.get('surplusAmount'))
            except (ValueError, TypeError):
                logger.warning(
                    f"Skipping offer due to invalid price or available amount: "
                    f"Price='{adv.get('price')}', Available='{adv.get('surplusAmount')}'"
                )
                continue

            offer_details = {
                "advertiser": advertiser.get("nickName"),
                "price": f"{price} {data['fiat']}",
                "available": f"{available} {data['asset']}",
                "limits": (
                    f"{adv.get('minSingleTransAmount')} - "
                    f"{adv.get('maxSingleTransAmount')} {data['fiat']}"
                ),
                "payment_methods": [
                    method.get("payType")
                    for method in adv.get("tradeMethods", [])
                ],
            }
            offers.append(offer_details)
    except KeyError as e:
        logger.error(
            f"Could not find expected data in Binance response: {e}. "
            "The API structure may have changed."
        )
    return offers


def scrape_all_binance_offers(
    fiat: str, asset: str, tradeType: str, max_pages: int = 10
):
    """
    Scrapes multiple pages of P2P offers from Binance until no more data is found
    or max_pages is reached. Intended for background jobs.

    Args:
        fiat: The fiat currency.
        asset: The crypto asset.
        tradeType: The trade type ('BUY' or 'SELL').
        max_pages: A safeguard to prevent infinite loops.

    Yields:
        A dictionary representing a single P2P offer.
    """
    for page_num in range(1, max_pages + 1):
        logger.info(
            f"Bulk scraping Binance offers: page={page_num}/{max_pages}, fiat={fiat}, "
            f"asset={asset}, tradeType={tradeType}"
        )
        page_offers = get_binance_offers(
            fiat=fiat, asset=asset, tradeType=tradeType, page=page_num, rows=20
        )

        if not page_offers:
            logger.info(f"No more offers found on page {page_num}. Stopping scrape.")
            break

        for offer in page_offers:
            yield offer

    else:  # This 'else' belongs to the 'for' loop
        logger.warning(
            f"Reached max_pages limit ({max_pages}) for {fiat}-{asset}-{tradeType}. "
            "There might be more data available."
        )


@lru_cache(maxsize=4)
def get_binance_pairs():
    """
    Fetches all supported fiat/asset trading pairs from Binance P2P.

    Returns:
        A list of dictionaries, each representing a supported trading pair.
    """
    logger.info("Fetching Binance pairs...")
    url = settings.binance_p2p_pairs_url
    response_data = _make_binance_request(url, payload={})

    if not response_data or not response_data.get("data"):
        return []

    pairs = []
    try:
        for item in response_data["data"]:
            fiat = item["fiatUnit"]
            assets = item.get("assetList", [])
            for asset in assets:
                pairs.append({"fiat": fiat, "asset": asset, "tradeType": "BUY"})
                pairs.append({"fiat": fiat, "asset": asset, "tradeType": "SELL"})
        return pairs
    except KeyError as e:
        logger.error(f"Unexpected structure in Binance pairs response: missing key {e}")
        return []
