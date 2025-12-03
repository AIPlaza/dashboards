"""
SQLAlchemy ORM models for the P2P data warehouse.
"""
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    Index,
    Numeric,
    Text,
    CHAR,
    BIGINT,
    CheckConstraint,
    ForeignKeyConstraint,
)
from sqlalchemy.dialects.postgresql import UUID, JSONB, INTERVAL
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func
import uuid

Base = declarative_base()

class DimCryptocurrencies(Base):
    __tablename__ = 'dim_cryptocurrencies'
    crypto_id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String(10), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    binance_asset_code = Column(String(20), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    __table_args__ = (Index('idx_crypto_symbol', 'symbol'),)

class DimFiatCurrencies(Base):
    __tablename__ = 'dim_fiat_currencies'
    fiat_id = Column(Integer, primary_key=True, autoincrement=True)
    currency_code = Column(CHAR(3), unique=True, nullable=False)
    currency_name = Column(String(100), nullable=False)
    country_code = Column(CHAR(2))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    __table_args__ = (Index('idx_fiat_code', 'currency_code'),)

class DimPaymentMethods(Base):
    __tablename__ = 'dim_payment_methods'
    payment_method_id = Column(Integer, primary_key=True, autoincrement=True)
    method_code = Column(String(50), unique=True, nullable=False)
    method_name = Column(String(200), nullable=False)
    category = Column(String(50))
    description = Column(Text)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    __table_args__ = (
        Index('idx_payment_method_code', 'method_code'),
        Index('idx_payment_category', 'category'),
    )

class DimAdvertisers(Base):
    __tablename__ = 'dim_advertisers'
    advertiser_sk = Column(BIGINT, primary_key=True, autoincrement=True)
    advertiser_id = Column(String(100), nullable=False)
    nickname = Column(String(200), nullable=False)
    is_merchant = Column(Boolean, default=False)
    registration_days = Column(Integer)
    effective_date = Column(DateTime, nullable=False)
    expiration_date = Column(DateTime)
    is_current = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    __table_args__ = (
        Index('idx_advertiser_id_current', 'advertiser_id', 'is_current'),
        Index('idx_advertiser_nickname', 'nickname'),
    )

class FactOffers(Base):
    __tablename__ = 'fact_offers'
    offer_id = Column(BIGINT, primary_key=True, autoincrement=True)
    offer_external_id = Column(String(100), nullable=False)
    batch_id = Column(UUID(as_uuid=True), nullable=False)
    extraction_timestamp = Column(DateTime, nullable=False, primary_key=True)
    crypto_id = Column(Integer, ForeignKey('dim_cryptocurrencies.crypto_id'))
    fiat_id = Column(Integer, ForeignKey('dim_fiat_currencies.fiat_id'))
    advertiser_sk = Column(BIGINT, ForeignKey('dim_advertisers.advertiser_sk'))
    trade_type = Column(String(4), nullable=False)
    price = Column(Numeric(20, 8), nullable=False)
    price_float_rate = Column(Numeric(10, 4))
    available_amount = Column(Numeric(20, 8), nullable=False)
    min_limit = Column(Numeric(20, 8), nullable=False)
    max_limit = Column(Numeric(20, 8), nullable=False)
    tradable_quantity = Column(Numeric(20, 8))
    completion_rate = Column(Numeric(5, 2))
    total_orders_count = Column(Integer)
    avg_response_time_seconds = Column(Integer)
    avg_completion_time_minutes = Column(Integer)
    terms_conditions = Column(Text)
    is_available = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    __table_args__ = (
        CheckConstraint(trade_type.in_(['BUY', 'SELL'])),
        Index('idx_offers_batch', 'batch_id'),
        Index('idx_offers_timestamp', 'extraction_timestamp', postgresql_using='brin'),
        Index('idx_offers_crypto_fiat', 'crypto_id', 'fiat_id', 'trade_type'),
        Index('idx_offers_advertiser', 'advertiser_sk'),
    )

class FactOfferPaymentMethods(Base):
    __tablename__ = 'fact_offer_payment_methods'
    offer_payment_id = Column(BIGINT, primary_key=True, autoincrement=True)
    offer_id = Column(BIGINT, nullable=False)
    extraction_timestamp = Column(DateTime, nullable=False)
    payment_method_id = Column(Integer, ForeignKey('dim_payment_methods.payment_method_id'))
    is_primary = Column(Boolean, default=False)
    __table_args__ = (
        ForeignKeyConstraint(
            ['offer_id', 'extraction_timestamp'],
            ['fact_offers.offer_id', 'fact_offers.extraction_timestamp'],
            ondelete='CASCADE'
        ),
        Index('idx_offer_payments', 'offer_id', 'extraction_timestamp'),
        Index('idx_payment_offers', 'payment_method_id'),
    )
