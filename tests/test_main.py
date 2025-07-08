import os
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from p2p_api.database import Base, init_db
from p2p_api.main import app, get_db

API_KEY = os.getenv("API_KEY", "test-key")


@pytest.fixture()
def client():
    os.environ["TESTING"] = "1"
    # Use an in-memory SQLite database for testing
    SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
    _engine, _SessionLocal = init_db(SQLALCHEMY_DATABASE_URL) # Initialize the global engine and SessionLocal
    Base.metadata.create_all(bind=_engine)  # Create tables for the test session using the global engine

    def override_get_db():
        try:
            db = _SessionLocal() # Use the global SessionLocal
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)

    Base.metadata.drop_all(bind=_engine)  # Drop tables after the test session using the global engine
    app.dependency_overrides.clear()
    del os.environ["TESTING"]


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