import logging
import uuid
from contextlib import asynccontextmanager
from typing import List, Literal

from fastapi import Depends, FastAPI, HTTPException, Query, Request, status
from fastapi.responses import JSONResponse
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session

from . import (
    crud,
    database as models,
    schemas,
    services,
)
from .binance_scraper import get_binance_offers, get_binance_pairs
from .config import Settings
from .database import Base, init_db
from .exceptions import ScraperError
from .logging_config import setup_logging
from .dependencies import get_db, set_session_local
from .auth import pwd_context

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
        # Make the session factory available to the dependency injector
        set_session_local(_SessionLocal)
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
    {
        "name": "Admin",
        "description": "Endpoints for user and API key management.",
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


async def get_api_key(
    api_key: str = Depends(api_key_header), db: Session = Depends(get_db)
):
    """Dependency to validate API Key. Key format should be 'prefix_secret'."""
    if "_" not in api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key format"
        )

    prefix, _, secret = api_key.rpartition("_")
    db_key = crud.get_api_key_by_prefix(db, prefix=prefix)

    if not db_key or not db_key.is_active or not pwd_context.verify(secret, db_key.hashed_key):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing API Key"
        )
    return db_key

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

    return services.process_binance_offers(
        db=db,
        offers_data=offers_data,
        fiat=fiat,
        asset=asset,
        trade_type=trade_type,
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
    raise HTTPException(
        status_code=501, detail="Bybit integration is not yet implemented."
    )

# Include the admin router
from .routers import admin

app.include_router(admin.router)
