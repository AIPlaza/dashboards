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
api_key_header = APIKeyHeader(name="X-API-Key")


engine = None
SessionLocal = None

engine = None
SessionLocal = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global engine, SessionLocal
    # Initialize the database engine and session factory
    db_url_for_lifespan = os.getenv("DATABASE_URL")
    print(f"Lifespan: DATABASE_URL is {db_url_for_lifespan}")
    _engine, _SessionLocal = init_db(db_url_for_lifespan)
    print("Lifespan: Calling database.Base.metadata.create_all")
    database.Base.metadata.create_all(bind=_engine)
    yield


app = FastAPI(
    title="P2P Dashboard API",
    description="An API for scraping P2P trading data from cryptocurrency exchanges.",
    version="1.0.0",
    lifespan=lifespan,
)


async def get_api_key(api_key: str = Depends(api_key_header)):
    if not api_key or not secrets.compare_digest(api_key, API_KEY):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key"
        )


# Dependency to get DB session
def get_db():
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
    offers_data = get_binance_offers(
        fiat=fiat, asset=asset, tradeType=tradeType, page=page, rows=rows
    )

    db_offers = []
    for offer_data in offers_data:
        try:
            price_value = float(offer_data["price"].split(" ")[0])
            available_value = float(offer_data["available"].split(" ")[0])
            limits_str = offer_data["limits"].replace(",", "")
            min_limit_str, max_limit_str = limits_str.split(" - ")
            min_limit_value = float(min_limit_str.split(" ")[0])
            max_limit_value = float(max_limit_str.split(" ")[0])

            offer_to_create = schemas.OfferCreate(
                id=str(uuid.uuid4()),
                fiat=fiat,
                asset=asset,
                price=price_value,
                available=available_value,
                min_limit=min_limit_value,
                max_limit=max_limit_value,
                payment_methods=offer_data["payment_methods"],
                trade_type=tradeType,
                advertiser=offer_data["advertiser"],
            )
            db_offer = crud.create_offer(db, offer=offer_to_create)
            db_offers.append(db_offer)

        except (ValueError, IndexError) as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error parsing offer data from Binance: {e}. Data: {offer_data}",
            )

    return db_offers


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