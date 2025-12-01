import requests
import json
import logging
from functools import lru_cache
from typing import Any, Dict, List, Optional
import uuid
import datetime
import concurrent.futures
import time

import psycopg2
from psycopg2.extras import execute_batch
from apscheduler.schedulers import BackgroundScheduler
from prometheus_client import start_http_server, Summary, Gauge, Counter

from p2p_api.config import Settings
#from . import crud, schemas
#from .database import get_db

logger = logging.getLogger(__name__)

settings = Settings()

RATE_LIMIT = 10 # requests per minute

# Define Prometheus metrics
REQUEST_TIME = Summary('p2p_extraction_request_processing_seconds', 'Time spent processing single extraction request')
DATA_COMPLETENESS = Gauge('p2p_extraction_data_completeness', 'Data completeness ratio')
ERROR_COUNT = Counter('p2p_extraction_errors_total', 'Total extraction errors')

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
    retries = 3
    for i in range(retries):
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
        finally:
            time.sleep(60 / RATE_LIMIT) # sleep to prevent rate limiting
        logger.info(f"Retrying request to {url} (attempt {i+1}/{retries})")
        time.sleep(1) # wait before retrying
    return None

@lru_cache(maxsize=128)
def get_binance_offers(
    fiat: str = "VES",
    asset: str = "USDT",
    tradeType: str = "BUY",
):
    """
    Fetches a single page of P2P offers from Binance for on-demand API requests.

    Args:
        fiat: The fiat currency (e.g., 'VES', 'USD').
        asset: The crypto asset (e.g., 'USDT', 'BTC').
        tradeType: The trade type ('BUY' or 'SELL').

    Returns:
        A list of dictionaries, where each dictionary represents a P2P offer.
    """
    url = settings.binance_p2p_search_url
    data = {
        "proMerchantAds": False,
        "page": 1,
        "rows": 20,
        "payTypes": [],
        "countries": [],
        "tradeType": tradeType,
        "asset": asset,
        "fiat": fiat,
        "publisherType": None,
    }

    logger.info(
        f"Fetching single page of Binance offers: page=1, fiat={fiat}, "
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

def extract_data():
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
    fiat = "VES"
    asset = "USDT"
    tradeType = "BUY"
    max_pages = 10
    
    def scrape_page(page_num):
        logger.info(
            f"Bulk scraping Binance offers: page={page_num}/{max_pages}, fiat={fiat}, "
            f"asset={asset}, tradeType={tradeType}"
        )
        page_offers = get_binance_offers(
            fiat=fiat, asset=asset, tradeType=tradeType
        )
        return page_offers

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        page_numbers = range(1, max_pages + 1)
        results = executor.map(scrape_page, page_numbers)

        all_offers = []
        for page_offers in results:
            if not page_offers:
                logger.info(f"No more offers found. Stopping scrape.")
                break
            all_offers.extend(page_offers)
    return all_offers

def _parse_numeric_value(value_str: Any) -> Optional[float]:
    """
    Safely parses a numeric string like '1,234.56 USD' into a float.
    Returns None if parsing fails.
    """
    if not isinstance(value_str, str) or not value_str:
        return None
    try:
        return float(value_str.split(" ")[0].replace(",", ""))
    except (ValueError, IndexError):
        return None

def transform_data(offers_data: List[Dict[str, Any]]):
    """Transforms the extracted data into a format suitable for loading into PostgreSQL."""
    db_offers = []
    for offer_data in offers_data:
        try:
            price_value = _parse_numeric_value(offer_data.get("price"))
            available_value = _parse_numeric_value(offer_data.get("available"))

            if price_value is None or available_value is None:
                logger.warning(
                    f"Skipping offer due to unparseable price or available amount: "
                    f"Price='{offer_data.get('price')}', Available='{offer_data.get('available')}'"
                )
                continue

            limits_str = offer_data.get("limits", "").replace(",", "")
            if " - " not in limits_str:
                logger.warning(f"Skipping offer due to invalid limits format: {offer_data.get('limits')}")
                continue
            min_limit_value, max_limit_value = [
                _parse_numeric_value(v) for v in limits_str.split(" - ")
            ]

            if min_limit_value is None or max_limit_value is None:
                 logger.warning(f"Skipping offer due to unparseable min or max limit: Limits='{offer_data.get('limits')}'")
                 continue

            offer_to_create = {
                "fiat": "VES", #fiat,
                "price": price_value,
                "available": available_value,
                "min_limit": min_limit_value,
                "max_limit": max_limit_value,
                "payment_methods": offer_data.get("payment_methods", []),
                "trade_type": "BUY", #trade_type,
                "advertiser": offer_data.get("advertiser"),
                "asset": "USDT" #asset,
            }
            db_offers.append(offer_to_create)

        except (ValueError, IndexError, KeyError, AttributeError) as e:
            logger.warning(
                f"Skipping offer due to parsing error: {e}",
                extra={"offer_data": offer_data},
            )
            continue
    return db_offers

def load_data(data):
    """Loads the transformed data into the PostgreSQL database."""
    # TODO: Implement data loading logic
    # Connect to the PostgreSQL database
    DATABASE_URL = "postgresql://postgres:password@localhost:5432/p2p_data_warehouse"
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    # Prepare the SQL query
    query = """
    INSERT INTO fact_offers (offer_external_id, batch_id, extraction_timestamp, crypto_id, fiat_id, advertiser_sk, trade_type, price, available_amount, min_limit, max_limit, terms_conditions, is_available)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    # Prepare the data for insertion
    data_to_insert = []
    for offer in data:
        data_to_insert.append((
            str(uuid.uuid4()),  # offer_external_id
            str(uuid.uuid4()),  # batch_id
            datetime.datetime.now(),      # extraction_timestamp
            1,                  # crypto_id (assuming USDT is always 1)
            1,                  # fiat_id (assuming VES is always 1)
            1,                  # advertiser_sk (assuming a default advertiser)
            offer["trade_type"],
            offer["price"],
            offer["available"],
            offer["min_limit"],
            offer["max_limit"],
            "terms",
            True
        ))

    # Execute the query
    execute_batch(cur, query, data_to_insert)

    # Commit the changes
    conn.commit()

    # Close the connection
    cur.close()
    conn.close()

def data_quality_checks(data):
    """Performs data quality checks on the extracted data."""
    logger.info("Performing data quality checks...")

    # Completeness check
    if not data:
        logger.warning("No offers were extracted.")
        DATA_COMPLETENESS.set(0)
        ERROR_COUNT.inc() # Increment error count for completeness check failure
        return

    DATA_COMPLETENESS.set(1) # Assuming all expected pairs were extracted

    # Price anomaly check (basic)
    for offer in data:
        if offer["price"] > 1000000:  # example threshold
            logger.warning(f"Price anomaly detected: {offer['price']}")
            ERROR_COUNT.inc()
            logger.error("Price anomaly detected. Please investigate.") # Added alert

    logger.info("Data quality checks completed.")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(extract_and_process, 'interval', minutes=10)
    scheduler.start()

consecutive_errors = 0
CIRCUIT_BREAKER_THRESHOLD = 5

def circuit_breaker():
    global consecutive_errors
    if consecutive_errors >= CIRCUIT_BREAKER_THRESHOLD:
        logger.warning(f"Circuit breaker tripped. Too many consecutive errors ({consecutive_errors}).")
        return False
    return True

def extract_and_process():
    global consecutive_errors
    if not circuit_breaker():
        time.sleep(60) # wait for a minute before retrying
        return

    data = extract_data()
    if data:
        transformed_data = transform_data(data)
        load_data(transformed_data)
        data_quality_checks(transformed_data)
        consecutive_errors = 0 # reset error count on success
    else:
        consecutive_errors += 1
        logger.error(f"Extraction failed. Consecutive errors: {consecutive_errors}")

if __name__ == "__main__":
    start_http_server(8000)
    start_scheduler()
    while True:
        time.sleep(1)

consecutive_errors = 0
CIRCUIT_BREAKER_THRESHOLD = 5

def circuit_breaker():
    global consecutive_errors
    if consecutive_errors >= CIRCUIT_BREAKER_THRESHOLD:
        logger.warning(f"Circuit breaker tripped. Too many consecutive errors ({consecutive_errors}).")
        return False
    return True

def extract_and_process():
    global consecutive_errors
    if not circuit_breaker():
        time.sleep(60) # wait for a minute before retrying
        return

    data = extract_data()
    if data:
        transformed_data = transform_data(data)
        load_data(transformed_data)
        data_quality_checks(transformed_data)
        consecutive_errors = 0 # reset error count on success
    else:
        consecutive_errors += 1
        logger.error(f"Extraction failed. Consecutive errors: {consecutive_errors}")