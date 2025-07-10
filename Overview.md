# System Architecture Overview

This document provides a high-level, beginner-friendly explanation of the P2P Dashboard system architecture and workflow.

## The Big Picture: A Three-Part System

The project has three main parts that work together:

1.  **The Backend API (The Engine):** This is the FastAPI application. Its main job is to do the heavy lifting: scraping data from exchanges and storing it. It exposes this data to the world through a set of secure URLs (API endpoints).
2.  **The Admin Dashboard (The Control Panel):** This is a special, protected part of the Backend API. It's not for regular users; it's for the administrator. Its only purpose is to allow the creation, viewing, and deletion of the API keys that grant access to the data.
3.  **The Streamlit App (The Customer's View):** This is a "client" application. It consumes the data from the Backend API and presents it to a user in a friendly way. It needs a valid API key to be able to talk to the backend.

---

## How It All Works, Step-by-Step

### 1. Starting the Backend (The Engine)

First, the FastAPI server is started. This is the heart of the whole operation.

```bash
uvicorn p2p_api.main:app --reload
```

When this command is run, the API is live at `http://127.0.0.1:8000` and is listening for requests.

### 2. Accessing and Managing the Admin Dashboard (The Control Panel)

The Admin Dashboard is not a webpage; it's a set of API endpoints under the `/admin/` path. It is managed using an API tool like Insomnia, Postman, or `curl`.

Here is the administrator's workflow:

**Step A: Create Your Admin Account**
This is a one-time setup to create a username and password for the control panel.

*   **Endpoint:** `POST /admin/users/`
*   **What you send:** A JSON object with your desired username and password.
    ```json
    {
      "username": "my_admin_user",
      "password": "a_very_strong_password"
    }
    ```
*   **What happens:** The backend securely hashes the password and saves the user account in the `users` table in the database.

**Step B: Log In to Get a Temporary Pass (JWT Token)**
Logging in provides a temporary, secure pass called a **JWT Token**.

*   **Endpoint:** `POST /admin/token`
*   **What you send:** Your username and password (as form data, not JSON).
*   **What you get back:** An access token, which is a long, encrypted string.
    ```json
    {
      "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
      "token_type": "bearer"
    }
    ```

**Step C: Generate an API Key for a "Customer"**
With the token, you can perform admin actions like generating a new API key.

*   **Endpoint:** `POST /admin/keys/`
*   **How you authenticate:** Include the `access_token` in the request header: `Authorization: Bearer eyJhbGciOiJIUzI1Ni...`
*   **What you send (optional):** A name for the key, e.g., `{ "name": "My First Customer App" }`.
*   **What you get back:** A brand new API key. **This is the only time you will see the full key!**
    ```json
    {
      "name": "My First Customer App",
      "key": "p2p_a1b2c3d4e5f6a7b8_...long_random_string..."
    }
    ```
*   **What happens in the background:** The backend creates a unique prefix (`p2p_...`), securely hashes the secret part, and saves the prefix and the hash in the `api_keys` database table, linked to your admin user.

This full key (`p2p_...`) should be copied and provided to the client application (e.g., the Streamlit app).

### 3. How the Streamlit App Uses the API Key

The Streamlit app is the "customer" and needs an API key to get data.

#### The `.env` File and a Needed Refactoring

The `streamlit_app/utils/api.py` file should be refactored to decouple the API functions from the key's source. The functions should accept the key as an argument, and the main Streamlit app should be responsible for getting that key from the user.

Here is the necessary refactoring for `streamlit_app/utils/api.py`:

```python
import requests
import os
from dotenv import load_dotenv

load_dotenv()

FASTAPI_BASE_URL = "http://127.0.0.1:8000"

def get_binance_pairs(api_key: str):
    """Fetches available trading pairs from the backend API."""
    if not api_key:
        return []
    headers = {"X-API-Key": api_key}
    response = requests.get(f"{FASTAPI_BASE_URL}/api/v1/binance/pairs", headers=headers)
    response.raise_for_status()
    return response.json()

def get_binance_offers(api_key: str, fiat: str, asset: str, trade_type: str):
    """Fetches P2P offers from the backend API."""
    if not api_key:
        return []
    headers = {"X-API-Key": api_key}
    params = {"fiat": fiat, "asset": asset, "trade_type": trade_type}
    response = requests.get(f"{FASTAPI_BASE_URL}/api/v1/binance/offers", params=params, headers=headers)
    response.raise_for_status()
    return response.json()
```

With this change, the main Streamlit `app.py` can ask the user for their key (e.g., with `st.text_input`) and then pass it to these functions, making the system ready for real users.