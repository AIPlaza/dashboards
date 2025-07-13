import datetime
import os

from dotenv import load_dotenv
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric, String, Table, create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker




Base = declarative_base()
engine = None
SessionLocal = None

def init_db():
    """Initialize database engine and session factory from environment variable."""
    global engine, SessionLocal

    # Read the database URL from environment variable
    database_url = os.environ.get("DATABASE_URL") # Use the environment variable name you will set on Render

    if not database_url:
        # Handle the case where the environment variable is not set (e.g., raise an error or log a warning)
        # For production on Render, this variable *should* be set.
        raise ValueError("DATABASE_URL environment variable not set.")

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


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    # Relationship to APIKey
    api_keys = relationship("APIKey", back_populates="user", cascade="all, delete-orphan")


class APIKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    prefix = Column(String, unique=True, index=True, nullable=False)
    hashed_key = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    is_active = Column(Boolean, default=True)
    name = Column(String)  # A user-friendly name for the key, e.g., "My App"

    user = relationship("User", back_populates="api_keys")
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
