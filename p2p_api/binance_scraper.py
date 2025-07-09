import json
import logging
import os
from functools import lru_cache

import requests
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants
MAX_PAGES = 5  # Safeguard to prevent excessive pagination

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


@lru_cache(maxsize=128)
def get_binance_offers(
    fiat: str = "VES",
    asset: str = "USDT",
    tradeType: str = "BUY",
    page: int = 1,
    rows: int = 20,
):
    """
    Fetches P2P offers from Binance with pagination.

    Args:
        fiat: The fiat currency (e.g., 'VES', 'USD').
        asset: The crypto asset (e.g., 'USDT', 'BTC').
        tradeType: The trade type ('BUY' or 'SELL').
        page: The starting page number.
        rows: The number of results per page.

    Returns:
        A list of dictionaries, where each dictionary represents a P2P offer.
    """
    url = os.getenv("BINANCE_P2P_SEARCH_URL")
    headers = _get_default_headers()
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

    all_offers = []
    current_page = page
    pages_fetched = 0

    while pages_fetched < MAX_PAGES:
        data["page"] = current_page
        logging.info(
            f"Fetching Binance offers: page={current_page}, fiat={fiat}, "
            f"asset={asset}, tradeType={tradeType}"
        )
        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            p2p_data = response.json()

            if p2p_data.get("code") == "000000" and p2p_data.get("data"):
                for ad in p2p_data["data"]:
                    adv = ad["adv"]
                    advertiser = ad["advertiser"]
                    offer_details = {
                        "advertiser": advertiser.get("nickName"),
                        "price": f"{adv.get('price')} {data['fiat']}",
                        "available": f"{adv.get('surplusAmount')} {data['asset']}",
                        "limits": (
                            f"{adv.get('minSingleTransAmount')} - "
                            f"{adv.get('maxSingleTransAmount')} {data['fiat']}"
                        ),
                        "payment_methods": [
                            method.get("payType")
                            for method in adv.get("tradeMethods", [])
                        ],
                    }
                    all_offers.append(offer_details)

                current_page += 1
                pages_fetched += 1
            else:
                if p2p_data.get("code") != "000000":
                    logging.error(
                        f"Binance API returned an error: {p2p_data.get('message')}"
                    )
                break  # Exit loop if no more data or API error

        except requests.exceptions.RequestException as e:
            logging.error(f"An error occurred during Binance request: {e}")
            break
        except KeyError as e:
            logging.error(
                f"Could not find expected data in Binance response: {e}. "
                "The API structure may have changed."
            )
            break
        except json.JSONDecodeError:
            logging.error("Failed to decode Binance response as JSON.")
            break

    if pages_fetched >= MAX_PAGES:
        logging.warning(f"Reached max pages ({MAX_PAGES}) for this request.")

    return all_offers


@lru_cache(maxsize=4)
def get_binance_pairs():
    """
    Fetches all supported fiat/asset trading pairs from Binance P2P.

    Returns:
        A list of dictionaries, each representing a supported trading pair.
    """
    logging.info("Fetching Binance pairs...")
    url = os.getenv("BINANCE_P2P_PAIRS_URL")
    headers = _get_default_headers()

    try:
        response = requests.post(url, headers=headers, json={})
        response.raise_for_status()
        data = response.json()

        if data.get("code") == "000000" and data.get("data"):
            pairs = []
            for item in data["data"]:
                fiat = item.get("fiatUnit")
                assets = item.get("assetList", [])
                for asset in assets:
                    pairs.append({"fiat": fiat, "asset": asset, "tradeType": "BUY"})
                    pairs.append({"fiat": fiat, "asset": asset, "tradeType": "SELL"})
            return pairs
        else:
            logging.error(
                f"Binance API for pairs returned an error: {data.get('message')}"
            )
            return []
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred during Binance pairs request: {e}")
        return []
    except json.JSONDecodeError:
        logging.error("Failed to decode Binance pairs response as JSON.")
        return []
