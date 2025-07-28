from typing import List

from pydantic import BaseModel, ConfigDict
import datetime

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


class RunBase(BaseModel):
    exchange: str
    fetched_at: datetime.datetime | None = None
    total_offers: int | None = None
    error_message: str | None = None

class RunCreate(RunBase):
    pass

class Run(RunBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class PaymentMethodBase(BaseModel):
    name: str


class PaymentMethodCreate(PaymentMethodBase):
    pass


class PaymentMethod(PaymentMethodBase):
    id: int
    offers: List[Offer] = []

    model_config = ConfigDict(from_attributes=True)


# User schemas
class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    api_keys: List["APIKey"] = []

    model_config = ConfigDict(from_attributes=True)


# API Key schemas
class APIKeyBase(BaseModel):
    name: str


class APIKeyCreate(APIKeyBase):
    pass


class APIKey(APIKeyBase):
    prefix: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class APIKeyCreateResponse(BaseModel):
    name: str
    key: str


# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str


from typing import List, Optional

class TokenData(BaseModel):
    username: Optional[str] = None
