import pytest
import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from p2p_api.main import app, get_db
from p2p_api.database import Offer, PaymentMethod # Explicitly import models
from p2p_api import database # Import the database module

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Use an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(name="session")
def session_fixture():
    database.Base.metadata.create_all(bind=engine)  # Create tables
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        database.Base.metadata.drop_all(bind=engine)  # Drop tables after tests


@pytest.fixture(name="client")
def client_fixture(session):
    os.environ["DATABASE_URL"] = SQLALCHEMY_DATABASE_URL
    print(f"Conftest: Setting DATABASE_URL to {os.environ['DATABASE_URL']}")

    def override_get_db():
        yield session

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()
    del os.environ["DATABASE_URL"]
    print("Conftest: Deleted DATABASE_URL from environment")
