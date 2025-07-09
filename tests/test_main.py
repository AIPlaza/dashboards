import os
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from p2p_api.database import Base, init_db
from p2p_api.main import app, get_db

API_KEY = os.getenv("API_KEY", "test-key")





def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "P2P Dashboard API is running!"}


@patch("p2p_api.main.get_binance_offers")
def test_get_binance_offers_success(mock_get_binance_offers, client):
    mock_get_binance_offers.return_value = [
        {
            "advertiser": "TestUser",
            "price": "100.00 VES",
            "available": "1000.00 USDT",
            "limits": "100 - 1000 VES",
            "payment_methods": ["Bank Transfer"],
        }
    ]

    response = client.get(
        "/api/v1/binance/offers", headers={"X-API-Key": API_KEY}
    )
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["advertiser"] == "TestUser"


def test_get_binance_offers_no_api_key(client):
    response = client.get("/api/v1/binance/offers")
    assert response.status_code == 403


@patch("p2p_api.main.get_binance_pairs")
def test_get_binance_pairs_success(mock_get_binance_pairs, client):
    mock_get_binance_pairs.return_value = [
        {"fiat": "VES", "asset": "USDT", "tradeType": "BUY"}
    ]

    response = client.get("/api/v1/binance/pairs", headers={"X-API-Key": API_KEY})
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_bybit_offers_not_implemented(client):
    response = client.get("/api/v1/bybit/offers", headers={"X-API-Key": API_KEY})
    assert response.status_code == 501