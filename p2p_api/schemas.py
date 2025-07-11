from typing import List

from pydantic import BaseModel, ConfigDict


class OfferBase(BaseModel):
    fiat: str
    asset: str
    price: float
    available: float
    min_limit: float
    max_limit: float
    trade_type: str
    advertiser: str
    payment_methods: List[str]


class OfferCreate(OfferBase):
    id: str


class Offer(OfferBase):
    id: str

    model_config = ConfigDict(from_attributes=True)
