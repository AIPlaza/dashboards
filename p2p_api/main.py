import os
import secrets
import uuid
from contextlib import asynccontextmanager
from typing import List

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, Query, status
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session

from . import crud, schemas, database
from .database import Offer, PaymentMethod
from .binance_scraper import get_binance_offers, get_binance_pairs
from .database import init_db, DATABASE_URL
from . import database

load_dotenv()

API_KEY = os.getenv("API_KEY")
engine = None
SessionLocal = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global engine, SessionLocal

    # Initialize the database engine and session factory
    db_url_for_lifespan = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    print(f"Lifespan: DATABASE_URL is {db_url_for_lifespan}")

    # FIXED: Properly assign to globals
    engine, SessionLocal = init_db(db_url_for_lifespan)
    print("Lifespan: Calling database.Base.metadata.create_all")

    # Create all tables
    database.Base.metadata.create_all(bind=engine)

    yield

    # Cleanup on shutdown
    if engine:
        engine.dispose()

app = FastAPI(
    title="P2P Dashboard API",
    description="An API for scraping P2P trading data from cryptocurrency exchanges.",
    version="1.0.0",
    lifespan=lifespan,
)


api_key_header = APIKeyHeader(name="X-API-Key")
async def get_api_key(api_key: str = Depends(api_key_header)):
    if not api_key or not secrets.compare_digest(api_key, API_KEY):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key"
        )


# Dependency to get DB session
def get_db():
    # IMPROVED: More robust dependency with error handling
    if SessionLocal is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database not initialized"
        )
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "P2P Dashboard API is running!"}


@app.get(
    "/api/v1/binance/offers",
    response_model=List[schemas.Offer],
    dependencies=[Depends(get_api_key)],
    tags=["Binance"],
)
async def get_binance_p2p_offers(
    fiat: str = Query("VES", description="Fiat currency (e.g., VES, USD)"),
    asset: str = Query("USDT", description="Crypto asset (e.g., USDT, BTC)"),
    tradeType: str = Query("BUY", description="Trade type (BUY or SELL)"),
    page: int = Query(1, description="Page number"),
    rows: int = Query(20, description="Number of rows per page"),
    db: Session = Depends(get_db),
):
    try:
        offers_data = get_binance_offers(
            fiat=fiat, asset=asset, tradeType=tradeType, page=page, rows=rows
        )

        db_offers = []
        for offer_data in offers_data:
            try:
                # IMPROVED: More robust parsing with validation
                price_parts = offer_data["price"].split(" ")
                if len(price_parts) < 1:
                    raise ValueError("Invalid price format")
                price_value = float(price_parts[0].replace(",", ""))

                available_parts = offer_data["available"].split(" ")
                if len(available_parts) < 1:
                    raise ValueError("Invalid available format")
                available_value = float(available_parts[0].replace(",", ""))

                limits_str = offer_data["limits"].replace(",", "")
                if " - " not in limits_str:
                    raise ValueError("Invalid limits format")

                min_limit_str, max_limit_str = limits_str.split(" - ")
                min_limit_value = float(min_limit_str.split(" ")[0])
                max_limit_value = float(max_limit_str.split(" ")[0])

                print(f"price_value: {price_value}")
                print(f"available_value: {available_value}")
                print(f"min_limit_value: {min_limit_value}")
                print(f"max_limit_value: {max_limit_value}")
                offer_to_create = schemas.OfferCreate(
                    id=str(uuid.uuid4()),
                    fiat=fiat,
                    price=price_value,
                    available=available_value,
                    min_limit=min_limit_value,
                    max_limit=max_limit_value,
                    payment_methods=offer_data["payment_methods"],
 trade_type=tradeType,
 advertiser=offer_data["advertiser"],
                    asset=asset,
                )
                db_offer = crud.create_offer(db, offer=offer_to_create)
                db_offers.append(db_offer)

            except (ValueError, IndexError, KeyError) as e:
                # IMPROVED: Log error but continue processing other offers
                print(f"Error parsing offer data: {e}. Data: {offer_data}")
                continue

        return db_offers

    except Exception as e:
        # IMPROVED: Better error handling for external API calls
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching Binance offers: {str(e)}"
        )


@app.get(
    "/api/v1/binance/pairs",
    dependencies=[Depends(get_api_key)],
    tags=["Binance"],
)
async def get_binance_p2p_pairs():
    pairs = get_binance_pairs()
    return pairs


@app.get(
    "/api/v1/bybit/offers",
    dependencies=[Depends(get_api_key)],
    tags=["Bybit"],
)
async def get_bybit_p2p_offers():
    # This will be implemented in the future
    raise HTTPException(
        status_code=501, detail="Bybit integration is not yet implemented."
    )