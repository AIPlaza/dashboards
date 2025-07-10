import requests

FASTAPI_BASE_URL = "http://127.0.0.1:8000"

def get_binance_pairs():
    try:
        response = requests.get(f"{FASTAPI_BASE_URL}/api/v1/binance/pairs")
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Binance pairs: {e}")
        return []

def get_binance_offers(fiat: str, crypto: str, trade_type: str):
    try:
        response = requests.get(f"{FASTAPI_BASE_URL}/api/v1/binance/offers", params={
            "fiat": fiat,
            "crypto": crypto,
            "trade_type": trade_type
        })
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Binance offers: {e}")
        return []