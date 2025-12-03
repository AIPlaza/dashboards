"""
Database connection management with connection pooling.
Uses SQLAlchemy for proper connection lifecycle management.
"""
import logging
from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine, event, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import QueuePool

from .config import settings

logger = logging.getLogger(__name__)

class DatabaseManager:
    """Manages database connections with pooling and lifecycle."""

    def __init__(self):
        self.engine: Engine = None
        self.SessionLocal: sessionmaker = None
        self._initialize_engine()

    def _initialize_engine(self):
        """Create SQLAlchemy engine with connection pooling."""
        logger.info(f"Initializing database engine: {settings.database_url.split('@')[1]}")

        self.engine = create_engine(
            settings.database_url,
            poolclass=QueuePool,
            pool_size=settings.db_pool_size,
            max_overflow=settings.db_max_overflow,
            pool_pre_ping=True, # Verify connections before using
            pool_recycle=3600, # Recycle connections after 1 hour
            echo=False, # Set to True for SQL debugging
        )

        self.SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine,
            expire_on_commit=False
        )

        # Configure connection events
        self._setup_connection_events()

        # Test connection
        self._test_connection()

    def _setup_connection_events(self):
        """Configure SQLAlchemy connection event listeners."""

        @event.listens_for(self.engine, "connect")
        def receive_connect(dbapi_conn, connection_record):
            """Called when a new DB connection is created."""
            logger.debug("New database connection established")

        @event.listens_for(self.engine, "checkout")
        def receive_checkout(dbapi_conn, connection_record, connection_proxy):
            """Called when connection is retrieved from pool."""
            pass # Add custom logic if needed

    def _test_connection(self):
        """Verify database connectivity on startup."""
        try:
            with self.engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            logger.info("Database connection test successful")
        except Exception as e:
            logger.error(f"Database connection test failed: {e}")
            raise

    @contextmanager
    def get_session(self) -> Generator[Session, None, None]:
        """
        Context manager for database sessions.

        Usage:
        with db_manager.get_session() as session:
            session.execute(...)
            session.commit()
        """
        session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            logger.error(f"Database session error: {e}")
            raise
        finally:
            session.close()

    def close(self):
        """Close all database connections."""
        if self.engine:
            self.engine.dispose()
        logger.info("Database connections closed")

# Global database manager instance
db_manager = DatabaseManager()