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
 create_engine, event
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.engine import Engine
from typing import Tuple

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

Base = declarative_base()

def init_db(db_url: str = None):
    """Initialize database engine and session factory."""
    effective_url = db_url or DATABASE_URL
    
    # Configure engine based on database type
    if "sqlite" in effective_url:
        engine = create_engine(
            effective_url,
            connect_args={
                "check_same_thread": False,
                "timeout": 30,
            },
            pool_pre_ping=True,
            pool_recycle=300,
            echo=False,  # Set to True for debugging
        )
    else:
        # PostgreSQL or other databases
        engine = create_engine(
            effective_url,
            pool_pre_ping=True,
            pool_recycle=300,
            echo=False,
        )
    
    SessionLocal = sessionmaker(
        autocommit=False, 
        autoflush=False, 
        bind=engine,
        expire_on_commit=False,  # Prevent issues with accessing objects after commit
    )
    
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
    timestamp = Column(DateTime, default=datetime.datetime.utcnow, index=True)
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
 , lazy="selectin"  # Optimize loading
 )

    def __repr__(self):
        return f"<Offer(fiat='{self.fiat}', asset='{self.asset}', price={self.price})>"


class PaymentMethod(Base):
    __tablename__ = "payment_methods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)

    # Relationship to Offer
    offers = relationship(
        "Offer", secondary=offer_payment_methods, back_populates="payment_methods"
 , lazy="selectin"
 )

    def __repr__(self):
        return f"<PaymentMethod(name='{self.name}')>"

# SQLite-specific configuration for better concurrency
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    """Configure SQLite for better concurrency and performance."""
    if 'sqlite' in str(dbapi_connection):
        cursor = dbapi_connection.cursor()
        # Enable WAL mode for better concurrency
        cursor.execute("PRAGMA journal_mode=WAL")
        # Enable foreign key support
        cursor.execute("PRAGMA foreign_keys=ON")
        # Set reasonable timeout
        cursor.execute("PRAGMA busy_timeout=30000")
        cursor.close()