import logging
import uuid
from typing import Any, Dict, List

from sqlalchemy.orm import Session

from . import crud, schemas

logger = logging.getLogger(__name__)

def _parse_numeric_value(value_str: Any) -> float | None:
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
) -> List[schemas.Offer]:
    """
    Processes a list of raw offer data from Binance, parses them,
    and saves them to the database.
    """
    db_offers = []
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
            db_offer = crud.create_offer(db, offer=offer_to_create)
            db_offers.append(db_offer)

        except (ValueError, IndexError, KeyError, AttributeError) as e:
            logger.warning(
                f"Skipping offer due to parsing error: {e}",
                extra={"offer_data": offer_data},
            )
            continue

    return db_offers