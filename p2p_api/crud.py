from sqlalchemy.orm import Session

from . import database as models
from . import schemas


def get_or_create_payment_method(db: Session, name: str):
    method = db.query(models.PaymentMethod).filter(models.PaymentMethod.name == name).first()
    if not method:
        method = models.PaymentMethod(name=name)
        db.add(method)
        db.commit()
        db.refresh(method)
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

    for method_name in offer.payment_methods:
        payment_method = get_or_create_payment_method(db, name=method_name)
        db_offer.payment_methods.append(payment_method)

    db.add(db_offer)
    db.commit()
    db.refresh(db_offer)
    return db_offer
