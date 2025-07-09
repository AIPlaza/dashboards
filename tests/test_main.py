from unittest.mock import patch

import pytest
from p2p_api.main import API_KEY, HTTPException
from p2p_api import schemas

# The client fixture is now provided by conftest.py

def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "P2P Dashboard API is running!"}

@patch('p2p_api.main.get_binance_offers')
@patch('p2p_api.crud.create_offer')
def test_get_binance_offers_success(mock_create_offer, mock_get_binance_offers, client, db_session, sample_payment_methods):
    mock_get_binance_offers.return_value = [
        {
            "advertiser": "TestUser",
            "price": "100.00 VES",
            "available": "1000.00 USDT",
            "limits": "100 - 1000 VES",
            "payment_methods": ["Bank Transfer"],
        }
    ]
    mock_create_offer.return_value = schemas.Offer(
        id="test-id",
        fiat="VES",
        asset="USDT",
        price=100.00,
        available=1000.00,
        min_limit=100.00,
        max_limit=1000.00,
        trade_type="BUY",
        advertiser="TestUser",
        payment_methods=["Bank Transfer"],
    )

    response = client.get(
 "api/v1/binance/offers?fiat=VES&asset=USDT&tradeType=BUY",
 headers={"X-API-Key": "test-api-key"}
    )

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["advertiser"] == "TestUser"

def test_get_binance_offers_no_api_key(client_no_auth):
    response = client_no_auth.get("/api/v1/binance/offers")
    assert response.status_code == 401
    

@patch('p2p_api.main.get_binance_offers')
def test_get_binance_offers_parsing_error(mock_get_binance_offers, client):
    mock_get_binance_offers.return_value = [
        {
            "price": "invalid_price",
            "available": "1000.00 USDT",
            "limits": "500.00 VES - 10000.00 VES",
            "payment_methods": ["Bank Transfer"],
            "advertiser": "TestUser123"
        }
    ]

    response = client.get(
 "api/v1/binance/offers?fiat=VES&asset=USDT&tradeType=BUY",
 headers={"X-API-Key": "test-api-key"}
    )

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 0

@patch('p2p_api.main.get_binance_offers')
def test_get_binance_offers_api_error(mock_get_binance_offers, client):
    mock_get_binance_offers.side_effect = Exception("External API error")

    response = client.get(
 "api/v1/binance/offers?fiat=VES&asset=USDT&tradeType=BUY",
 headers={"X-API-Key": "test-api-key"}
    )

    assert response.status_code == 500
    assert "Error fetching Binance offers" in response.json()["detail"]

@patch("p2p_api.main.get_binance_pairs")
def test_get_binance_pairs_success(mock_get_binance_pairs, client):
    mock_get_binance_pairs.return_value = [
        {"fiat": "VES", "asset": "USDT", "tradeType": "BUY"}
    ]

    response = client.get(
 "/api/v1/binance/pairs",
 headers={"X-API-Key": "test-api-key"}
 )
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_bybit_offers_not_implemented(client):
    response = client.get("/api/v1/bybit/offers", headers={"X-API-Key": API_KEY})
    assert response.status_code == 501