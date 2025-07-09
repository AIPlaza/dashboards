import pytest
import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from fastapi import HTTPException

# Set TESTING environment variable BEFORE importing the app
os.environ["TESTING"] = "1"

from p2p_api.main import app, get_db, get_api_key, configure_database
from p2p_api.database import Offer, PaymentMethod, Base  # Import Base explicitly
from p2p_api import database  # Import the database module

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture(name="session", scope="function")
def session_fixture():
    # Use an in-memory SQLite database for testing
    test_db_url = "sqlite://"
    
    engine = create_engine(
        test_db_url,
        connect_args={"check_same_thread": False},
        echo=False
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    # Ensure all models are imported before creating tables
    # This forces the metadata to be aware of all table definitions
    from p2p_api.database import Offer, PaymentMethod, offer_payment_methods
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    print("Conftest: Tables created in test database.")
    print(f"Conftest: Available tables: {list(Base.metadata.tables.keys())}")
    
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)  # Drop tables after tests
        engine.dispose()  # Dispose of the engine


def mock_get_api_key_success():
    """Mock API key dependency that returns a valid key"""
    return "test-api-key"


def mock_get_api_key_failure():
    """Mock API key dependency that raises 401 for missing/invalid key"""
    raise HTTPException(status_code=401, detail="Invalid or missing API key")


@pytest.fixture(name="client")
def client_fixture(session):  # This now depends on session fixture
    # Configure the database for the FastAPI app
    configure_database("sqlite://")
    
    def override_get_db():
        yield session
    
    app.dependency_overrides[get_db] = override_get_db
    # Default to successful API key validation
    app.dependency_overrides[get_api_key] = mock_get_api_key_success
    
    with TestClient(app) as client:
        yield client
    
    # Cleanup
    app.dependency_overrides.clear()


@pytest.fixture(name="client_no_auth")
def client_no_auth_fixture(session):
    """Client fixture that simulates missing/invalid API key"""
    configure_database("sqlite://")
    
    def override_get_db():
        yield session
    
    app.dependency_overrides[get_db] = override_get_db
    # Override to simulate missing API key
    app.dependency_overrides[get_api_key] = mock_get_api_key_failure
    
    with TestClient(app) as client:
        yield client
    
    # Cleanup
    app.dependency_overrides.clear()


@pytest.fixture(scope="function")
def db_session(session):
    """Provide a database session for direct database testing."""
    print("Conftest: db_session fixture providing a session.")
    yield session


@pytest.fixture
def sample_payment_methods(db_session):
    """Create sample payment methods for testing."""
    payment_method_names = [
        "Bank Transfer",
        "PayPal",
        "Zelle",
    ]
    
    db_payment_methods = []
    for name in payment_method_names:
        try:
            # Check if payment method already exists
            existing = db_session.query(PaymentMethod).filter_by(name=name).first()
            if existing:
                db_payment_methods.append(existing)
                continue
                
            db_method = PaymentMethod(name=name)
            db_session.add(db_method)
            db_session.commit()
            db_session.refresh(db_method)
            db_payment_methods.append(db_method)
            print(f"Conftest: Created payment method '{name}' with ID {db_method.id}")
        except Exception as e:
            print(f"Error adding payment method '{name}': {e}")
            db_session.rollback()
            raise
    return db_payment_methods


# Cleanup function to run after all tests
def pytest_sessionfinish(session, exitstatus):
    """Clean up environment variables after all tests complete."""
    if "TESTING" in os.environ:
        del os.environ["TESTING"]