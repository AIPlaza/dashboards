import logging
import uuid
from typing import Any, Dict, List, Optional
from datetime import datetime, timedelta

from sqlalchemy.orm import Session
from sqlalchemy import func

from . import crud, schemas
from . import database as models

logger = logging.getLogger(__name__)

def _parse_numeric_value(value_str: Any) -> Optional[float]:
    """
    Safely parses a numeric string like '1,234.56 USD' into a float.
    Returns None if parsing fails.
    """
    if not isinstance(value_str, str) or not value_str:
        return None
    try:
        return float(value_str.split(" ")[0].replace(",", ""))
    except (ValueError, IndexError):
        return None

def process_binance_offers(
    db: Session,
    offers_data: List[Dict[str, Any]],
    fiat: str,
    asset: str,
    trade_type: str,
    run_id: int | None = None,
) -> List[schemas.Offer]:
    """
    Processes a list of raw offer data from Binance, parses them,
    and saves them to the database.
    """
    db_offers = []
    created = 0
    for offer_data in offers_data:
        try:
            price_value = _parse_numeric_value(offer_data.get("price"))
            available_value = _parse_numeric_value(offer_data.get("available"))

            if price_value is None or available_value is None:
                logger.warning(
                    f"Skipping offer due to unparseable price or available amount: "
                    f"Price='{offer_data.get('price')}', Available='{offer_data.get('available')}'"
                )
                continue

            limits_str = offer_data.get("limits", "").replace(",", "")
            if " - " not in limits_str:
                raise ValueError("Limits format is missing ' - ' separator")
            min_limit_value, max_limit_value = [_parse_numeric_value(v) for v in limits_str.split(" - ")]

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
            db_offer = crud.create_offer(db, offer=offer_to_create, run_id=run_id)
            created += 1

        except (ValueError, IndexError, KeyError, AttributeError) as e:
            logger.warning(
                f"Skipping offer due to parsing error: {e}",
                extra={"offer_data": offer_data},
            )
            continue

    return created

def get_run_stats(db: Session) -> Dict[str, Any]:
    """
    Returns summary statistics of ingestion runs and offer activity.
    """
    now = datetime.utcnow()
    last_24_hours = now - timedelta(hours=24)

    # Last successful run
    last_successful_run = db.query(func.max(models.Run.fetched_at)).filter(models.Run.error_message == None).scalar()

    # Error count in last 24 hours
    error_count_last_24h = db.query(models.Run).filter(
        models.Run.fetched_at >= last_24_hours,
        models.Run.error_message != None
    ).count()

    # Offers in last 24 hours
    offers_last_24h_query = db.query(
        models.Offer.asset,
        models.Offer.fiat,
        models.Offer.trade_type,
        func.count(models.Offer.id).label("count"),
        func.sum(models.Offer.available).label("available"),
        func.avg(models.Offer.price).label("avg_price")
    ).filter(
        models.Offer.timestamp >= last_24_hours
    ).group_by(
        models.Offer.asset,
        models.Offer.fiat,
        models.Offer.trade_type
    ).all()

    offers_last_24h = []
    for row in offers_last_24h_query:
        offers_last_24h.append({
            "asset": row.asset,
            "fiat": row.fiat,
            "trade_type": row.trade_type,
            "count": row.count,
            "available": float(row.available),  # Convert Decimal to float
            "avg_price": float(row.avg_price)    # Convert Decimal to float
        })

    return {
        "last_successful_run": last_successful_run.isoformat() + "Z" if last_successful_run else None,
        "error_count_last_24h": error_count_last_24h,
        "offers_last_24h": offers_last_24h
    }
