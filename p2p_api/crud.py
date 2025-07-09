from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from . import database as models
from . import schemas


def get_or_create_payment_method(db: Session, name: str):
    method = db.query(models.PaymentMethod).filter(models.PaymentMethod.name == name).first()
    if not method:
        method = models.PaymentMethod(name=name)
        db.add(method)
        # No commit here, commit will be handled by the calling function
    return method


def create_offer(db: Session, offer: schemas.OfferCreate):
    db_offer = models.Offer(
        id=offer.id,
        fiat=offer.fiat,
        asset=offer.asset,
        price=offer.price,
        available=offer.available,
        min_limit=offer.min_limit,
        max_limit=offer.max_limit,
        trade_type=offer.trade_type,
        advertiser=offer.advertiser,
    )

    db.add(db_offer)
    db.flush() # Flush to assign an ID to db_offer before adding relationships

    # Use a set to avoid duplicate payment methods for a single offer
    unique_payment_methods = set()
    for method_name in offer.payment_methods:
        payment_method = get_or_create_payment_method(db, name=method_name)
        unique_payment_methods.add(payment_method)

    db_offer.payment_methods.extend(list(unique_payment_methods))

    try:
        db.commit()
        db.refresh(db_offer)
    except IntegrityError:
        db.rollback()
        raise

    # Convert payment_methods to list of strings for schema compliance
    # This creates a new list of strings from the ORM objects
    # and ensures the returned object matches the schema.
    return schemas.Offer(
        id=db_offer.id,
        fiat=db_offer.fiat,
        asset=db_offer.asset,
        price=db_offer.price,
        available=db_offer.available,
        min_limit=db_offer.min_limit,
        max_limit=db_offer.max_limit,
        trade_type=db_offer.trade_type,
        advertiser=db_offer.advertiser,
        payment_methods=[pm.name for pm in db_offer.payment_methods]
    )
