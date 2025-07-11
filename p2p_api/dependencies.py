from typing import Generator

from sqlalchemy.orm import Session, sessionmaker

_SessionLocal: sessionmaker | None = None


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
