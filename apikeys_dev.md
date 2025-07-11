# API Key Management - Development Plan

This document outlines the recommended architecture for building a dedicated dashboard to manage API keys for the P2P Dashboard API as it moves towards commercialization.

## Recommended Architecture

The plan is to extend the existing FastAPI application rather than building a completely separate service. This approach is efficient because it allows the reuse of database models, connection logic, and overall configuration.

The architecture will consist of:

1.  **Admin Dashboard (Frontend)**: A simple, secure web interface served directly from the FastAPI backend using **Jinja2 templates**. This is the fastest way to build a robust admin panel without needing a separate JavaScript frontend framework.
2.  **Admin API (Backend)**: A new set of protected API endpoints within the existing FastAPI app (e.g., under `/admin/...`). These endpoints will handle user authentication for the dashboard and CRUD (Create, Read, Update, Delete) operations for API keys.
3.  **User Authentication**: A standard **OAuth2 Password Flow with JWT tokens** to secure the admin dashboard. This ensures only registered administrators can log in and manage keys.
4.  **Database Models**: Two new SQLAlchemy models, `User` and `APIKey`, to store administrator credentials and the generated API keys.

---

## Step-by-Step Implementation Plan

### 1. Update the Database Schema (`p2p_api/database.py`)

New models are required to represent administrators (`User`) and the API keys they generate (`APIKey`). A key will be tied to a user.

**Key Security Consideration:** Raw API keys should never be stored in the database. Instead, a key will be generated and shown to the user *once*. A secure hash of the key will be stored. The key will be split into a `prefix` (stored in plaintext) and a `secret` (hashed).

**Recommended SQLAlchemy Models:**

```python
# c:\Users\DELL\P2P-Dashboard\p2p_api\database.py

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
import datetime

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
    name = Column(String) # A user-friendly name for the key, e.g., "My App"

    user = relationship("User", back_populates="api_keys")
```

### 2. Implement User Authentication and Key Generation

A new module, `p2p_api/auth.py`, will be created to handle security logic:

*   **Password Hashing**: Use the `passlib` library to securely hash and verify user passwords.
*   **API Key Generation**: A function will generate a new key (`prefix` + `secret`), hash the secret part, and return the full key for the user to see once.
*   **JWT Tokens**: Functions will be implemented to create and decode JWT tokens for managing admin dashboard sessions.

### 3. Create Admin API Endpoints

In a new router (e.g., `p2p_api/routers/admin.py`), endpoints will be defined for:
*   **Login**: An endpoint that takes a username and password and returns a JWT access token.
*   **API Key Management**: Secure endpoints for creating, listing, and revoking API keys for the logged-in user.

### 4. Update the Core API Authentication

The `get_api_key` dependency in `p2p_api/main.py` will be updated to validate keys against the new `APIKey` table in the database instead of the single key from the `.env` file.

**Example of updated `get_api_key`:**

```python
# c:\Users\DELL\P2P-Dashboard\p2p_api\main.py

from passlib.context import CryptContext

# ...

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def get_api_key(
    api_key: str = Depends(api_key_header), db: Session = Depends(get_db)
):
    if "_" not in api_key:
        raise HTTPException(status_code=401, detail="Invalid API Key format")

    prefix, _, secret = api_key.rpartition("_")
    db_key = db.query(models.APIKey).filter(models.APIKey.prefix == prefix).first()

    if not db_key or not db_key.is_active or not pwd_context.verify(secret, db_key.hashed_key):
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")
    
    return db_key
```