import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Add the parent directory to the sys.path to import p2p_api modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'p2p_api')))

from p2p_api.database import Base, PaymentMethod # Import Base and models
from p2p_api.crud import get_or_create_payment_method, create_offer
from p2p_api.schemas import OfferCreate
import uuid

def debug_crud_operations():
    # Setup in-memory SQLite database
    test_db_url = "sqlite://"
    engine = create_engine(
        test_db_url,
        connect_args={"check_same_thread": False},
        echo=True # Enable SQL echoing for debugging
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    print("--- Creating tables ---")
    Base.metadata.create_all(bind=engine)
    print("--- Tables created ---")

    db = SessionLocal()
    try:
        print("--- Testing get_or_create_payment_method ---")
        # Test creating a payment method
        method1 = get_or_create_payment_method(db, name="Bank Transfer")
        print(f"Retrieved/Created method: {method1.name}, ID: {method1.id}")

        # Test getting an existing payment method
        method1_again = get_or_create_payment_method(db, name="Bank Transfer")
        print(f"Retrieved existing method: {method1_again.name}, ID: {method1_again.id}")

        # Test creating another payment method
        method2 = get_or_create_payment_method(db, name="PayPal")
        print(f"Retrieved/Created method: {method2.name}, ID: {method2.id}")

        print("--- Testing create_offer ---")
        # Create a dummy offer
        offer_data = {
            "id": str(uuid.uuid4()),
            "fiat": "VES",
            "asset": "USDT",
            "price": 100.00,
            "available": 1000.00,
            "min_limit": 100.00,
            "max_limit": 1000.00,
            "payment_methods": ["Bank Transfer", "PayPal"],
            "trade_type": "BUY",
            "advertiser": "TestUser",
        }
        offer_to_create = OfferCreate(**offer_data)

        db_offer = create_offer(db, offer=offer_to_create)
        print(f"Created offer ID: {db_offer.id}")
        print(f"Offer payment methods: {[pm.name for pm in db_offer.payment_methods]}")

    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()
        engine.dispose()

if __name__ == "__main__":
    debug_crud_operations()