from typing import Generator
from functools import lru_cache

from sqlalchemy.orm import Session, sessionmaker

from .config import Settings

_SessionLocal: sessionmaker | None = None

@lru_cache()
def get_settings():
    return Settings()


def set_session_local(session_local: sessionmaker):
    """
    Sets the session factory for the dependency.
    This should be called once at application startup.
    """
    global _SessionLocal
    _SessionLocal = session_local


def get_db() -> Generator[Session, None, None]:
    """
    FastAPI dependency to get a database session.
    """
    if _SessionLocal is None:
        raise RuntimeError("Database session factory has not been initialized.")

    db = _SessionLocal()
    try:
        yield db
    finally:
        db.close()
