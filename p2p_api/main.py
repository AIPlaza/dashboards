import logging
import secrets
import uuid
from contextlib import asynccontextmanager
from typing import List, Literal

from fastapi import Depends, FastAPI, HTTPException, Query, Request, status
from fastapi.responses import JSONResponse
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session

from . import (
    crud,
    schemas,
)
from .binance_scraper import get_binance_offers, get_binance_pairs
from .config import Settings
from .database import init_db
from .exceptions import ScraperError
from .logging_config import setup_logging

logger = logging.getLogger(__name__)

api_key_header = APIKeyHeader(name="X-API-Key")

_engine = None
_SessionLocal = None

def configure_database(db_url: str, engine_override=None, session_override=None):
    global _engine, _SessionLocal
    if engine_override and session_override:
        _engine = engine_override
        _SessionLocal = session_override
    else:
        _engine, _SessionLocal = init_db(db_url)


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    logger.info("Starting P2P Dashboard API...")
    global global_settings
    global_settings = Settings()
    if not global_settings.testing:
        configure_database(global_settings.database_url)
    yield

    logger.info("Shutting down P2P Dashboard API...")
    global _engine
    if not global_settings.testing and _engine:
        _engine.dispose()

tags_metadata = [
    {
        "name": "Binance",
        "description": "Endpoints for fetching P2P data from Binance.",
    },
    {
        "name": "Bybit",
        "description": "Endpoints for fetching P2P data from Bybit.",
    },
    {
        "name": "System",
        "description": "System health and status endpoints.",
    },
]

app = FastAPI(
    title="P2P Dashboard API",
    description="A unified, high-performance API for fetching P2P cryptocurrency trading data from major exchanges.",
    version="1.0.0",
    lifespan=lifespan,
    openapi_tags=tags_metadata,
    contact={
        "name": "P2P Dashboard Support",
        "url": "https://github.com/your-username/P2P-Dashboard",
        "email": "support@example.com",
    },
    license_info={"name": "MIT License"},
)

@app.exception_handler(ScraperError)
async def scraper_exception_handler(request: Request, exc: ScraperError):
    logger.error(f"Scraper error for request {request.url}: {exc.message}")
    return JSONResponse(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        content={
            "detail": "Could not fetch data from the external source. Please try again later."
        },
    )


async def get_api_key(api_key: str = Depends(api_key_header)):
    if not secrets.compare_digest(api_key, global_settings.api_key):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing API Key"
        )

# Dependency to get DB session
def get_db(db: Session = Depends(lambda: None)):
    if _SessionLocal is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database not initialized"
        )
    db = _SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", tags=["System"])
async def read_root():
    return {"message": "P2P Dashboard API is running!"}

@app.get(
    "/api/v1/binance/offers",
    response_model=List[schemas.Offer],
    dependencies=[Depends(get_api_key)],
    summary="Fetch Binance P2P Offers",
    description="Retrieves a list of active P2P offers from Binance, with robust filtering and pagination.",
    tags=["Binance"],
)
async def get_binance_p2p_offers(
    fiat: str = Query("VES", description="Fiat currency code (e.g., VES, USD, EUR).", examples=["USD"]),
    asset: str = Query("USDT", description="Crypto asset code (e.g., USDT, BTC, ETH).", examples=["BTC"]),
    trade_type: Literal["BUY", "SELL"] = Query(
        "BUY", description="The type of trade, either BUY or SELL."
    ),
    page: int = Query(1, ge=1, description="Page number for pagination, starting from 1."),
    rows: int = Query(20, ge=1, le=100, description="Number of results per page (1-100)."),
    db: Session = Depends(get_db),
):
    try:
        offers_data = get_binance_offers(
            fiat=fiat, asset=asset, tradeType=trade_type, page=page, rows=rows
        )
    except Exception as e:
        # As per the audit, wrap scraper exceptions.
        raise ScraperError(f"An unexpected error occurred with the Binance scraper: {str(e)}")

    db_offers = []
    for offer_data in offers_data:
        try:
            price_str = offer_data.get("price", "")
            price_value = float(price_str.split(" ")[0].replace(",", ""))

            available_str = offer_data.get("available", "")
            available_value = float(available_str.split(" ")[0].replace(",", ""))

            limits_str = offer_data.get("limits", "").replace(",", "")
            if " - " not in limits_str:
                raise ValueError("Limits format is missing ' - ' separator")

            min_limit_str, max_limit_str = limits_str.split(" - ")
            min_limit_value = float(min_limit_str.split(" ")[0])
            max_limit_value = float(max_limit_str.split(" ")[0])

            offer_to_create = schemas.OfferCreate(
                id=str(uuid.uuid4()),
                fiat=fiat,
                price=price_value,
                available=available_value,
                min_limit=min_limit_value,
                max_limit=max_limit_value,
                payment_methods=offer_data.get("payment_methods", []),
                trade_type=trade_type,
                advertiser=offer_data.get("advertiser"),
                asset=asset,
            )
            db_offer = crud.create_offer(db, offer=offer_to_create)
            db_offers.append(db_offer)

        except (ValueError, IndexError, KeyError, AttributeError) as e:
            # Use structured logging instead of print
            logger.warning(
                f"Skipping offer due to parsing error: {e}", extra={"offer_data": offer_data}
            )
            continue

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
    raise HTTPException(
        status_code=501, detail="Bybit integration is not yet implemented."
    )
