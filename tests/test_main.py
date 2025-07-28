from unittest.mock import patch

import pytest

# The client fixture is now provided by conftest.py

def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "P2P Dashboard API is running!"}

@patch('p2p_api.main.get_binance_offers')
def test_get_binance_offers_success(mock_get_binance_offers, client, db_session, sample_payment_methods):
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
        "/api/v1/binance/offers?fiat=VES&asset=USDT&trade_type=BUY",
        headers={"X-API-Key": "test-api-key"},
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Successfully processed 1 offers for run 1"}

def test_get_binance_offers_missing_api_key(client_no_auth):
    response = client_no_auth.get("/api/v1/binance/offers")
    assert response.status_code == 401


def test_get_binance_offers_invalid_api_key(client_no_auth):
    response = client_no_auth.get(
        "/api/v1/binance/offers", headers={"X-API-Key": "invalid-key"}
    )
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
        "/api/v1/binance/offers?fiat=VES&asset=USDT&trade_type=BUY",
        headers={"X-API-Key": "test-api-key"},
    )

    assert response.status_code == 200
    data = response.json()
    assert data == {"message": "Successfully processed 0 offers for run 1"}

@patch('p2p_api.main.get_binance_offers')
def test_get_binance_offers_api_error(mock_get_binance_offers, client):
    mock_get_binance_offers.side_effect = Exception("Binance API is down")

    response = client.get(
        "/api/v1/binance/offers?fiat=VES&asset=USDT&trade_type=BUY",
        headers={"X-API-Key": "test-api-key"},
    )

    assert response.status_code == 503
    assert response.json()["detail"] == (
        "Could not fetch data from the external source. Please try again later."
    )

@patch("p2p_api.main.get_binance_pairs")
def test_get_binance_pairs_success(mock_get_binance_pairs, client):
    mock_get_binance_pairs.return_value = [
        {"fiat": "VES", "asset": "USDT", "tradeType": "BUY"}
    ]

    response = client.get(
        "/api/v1/binance/pairs", headers={"X-API-Key": "test-api-key"}
    )
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_bybit_offers_not_implemented(client):
    # The client fixture mocks authentication, so we don't need a real key.
    # The header is still required for the dependency to be triggered.
    response = client.get("/api/v1/bybit/offers", headers={"X-API-Key": "any-key"})
    assert response.status_code == 501