import datetime
import os

from dotenv import load_dotenv
from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Table,
    create_engine,
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

Base = declarative_base()

def init_db(db_url: str = None):
    if db_url is None:
        db_url = DATABASE_URL
    engine = create_engine(db_url, connect_args={"check_same_thread": False} if "sqlite" in db_url else {})
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return engine, SessionLocal

# Association Table for Offer and PaymentMethod
offer_payment_methods = Table(
    "offer_payment_methods",
    Base.metadata,
    Column("offer_id", String, ForeignKey("offers.id"), primary_key=True),
    Column(
        "payment_method_id",
        Integer,
        ForeignKey("payment_methods.id"),
        primary_key=True,
    ),
)


class Offer(Base):
    __tablename__ = "offers"

    id = Column(String, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    fiat = Column(String, index=True)
    asset = Column(String, index=True)
    price = Column(Numeric(20, 8))
    available = Column(Numeric(20, 8))
    min_limit = Column(Numeric(20, 8))
    max_limit = Column(Numeric(20, 8))
    trade_type = Column(String)
    advertiser = Column(String)

    # Many-to-Many relationship with PaymentMethod
    payment_methods = relationship(
        "PaymentMethod", secondary=offer_payment_methods, back_populates="offers"
    )

    def __repr__(self):
        return f"<Offer(fiat='{self.fiat}', asset='{self.asset}', price={self.price})>"


class PaymentMethod(Base):
    __tablename__ = "payment_methods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    # Relationship to Offer
    offers = relationship(
        "Offer", secondary=offer_payment_methods, back_populates="payment_methods"
    )

    def __repr__(self):
        return f"<PaymentMethod(name='{self.name}')>"