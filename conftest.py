import pytest
import os
import tempfile

# Set the API_KEY environment variable for testing before importing the app
original_api_key = os.environ.get("API_KEY")
os.environ["API_KEY"] = "test-api-key"

# Define cleanup function for API_KEY
def cleanup_api_key():
    if original_api_key:
        os.environ["API_KEY"] = original_api_key
    elif "API_KEY" in os.environ:
        del os.environ["API_KEY"]
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

# Import your application components
from p2p_api.main import app, get_db
from p2p_api.database import Base, PaymentMethod
from p2p_api import crud, schemas


@pytest.fixture(scope="function")
def test_db():
    """Create a clean test database for each test."""
    # Create a temporary database file
    with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as tmp:
        test_db_url = f"sqlite:///{tmp.name}"

        # Create engine with proper SQLite configuration
        engine = create_engine(
            test_db_url,
            connect_args={"check_same_thread": False},
            echo=False
        )

        # Create session factory
        TestingSessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=engine
        )

        # Create all tables
        Base.metadata.create_all(bind=engine)

        yield TestingSessionLocal, engine, test_db_url

        # Cleanup
        engine.dispose()
        os.unlink(tmp.name)


@pytest.fixture(scope="function")
def client(test_db):
    """Create a test client with isolated database."""
    TestingSessionLocal, engine, test_db_url = test_db

    # Override the get_db dependency
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    # Override the database URL environment variable
    original_db_url = os.environ.get("DATABASE_URL")
    os.environ["DATABASE_URL"] = test_db_url

    # Set the API_KEY environment variable for testing
    original_api_key = os.environ.get("API_KEY")
    os.environ["API_KEY"] = "test-api-key"
    # Override the dependency
    app.dependency_overrides[get_db] = override_get_db

    # Create client
    with TestClient(app) as client:
        yield client

    # Restore original API_KEY environment variable
    if original_api_key:
        os.environ["API_KEY"] = original_api_key
    elif "API_KEY" in os.environ:
        del os.environ["API_KEY"]

    # Cleanup
    app.dependency_overrides.clear()

    # Restore original environment
    if original_db_url:
        os.environ["DATABASE_URL"] = original_db_url
    elif "DATABASE_URL" in os.environ:
        del os.environ["DATABASE_URL"]


@pytest.fixture(scope="function")
def db_session(test_db):
    """Provide a database session for direct database testing."""
    TestingSessionLocal, engine, test_db_url = test_db

    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

# Additional fixture for creating test data
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
        db_method = PaymentMethod(name=name)
        db_session.add(db_method)
        db_payment_methods.append(db_method)

    db_session.commit()
    return db_payment_methods