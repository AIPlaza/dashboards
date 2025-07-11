# How to Run the P2P Dashboard Locally

This guide provides a complete, step-by-step walkthrough for setting up and running both the FastAPI backend and the Streamlit frontend on your local machine.

---

## Part 1: Running the Backend (FastAPI API)

First, we need to get the server running. This server is the "brain" of your application; it handles the logic for fetching data and managing users.

### Step 1: Set up the Backend Environment

1.  **Open your terminal** in the project's root directory (`P2P-Dashboard`).
2.  **Create a virtual environment** for the backend. This keeps its dependencies separate.
    ```bash
    python -m venv .venv
    ```
3.  **Activate the virtual environment.**
    *   On Windows:
        ```bash
        .\.venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        source .venv/bin/activate
        ```
    Your terminal prompt should now start with `(.venv)`.
4.  **Install the required Python packages.**
    ```bash
    pip install -r requirements-dev.txt
    ```
    > **Note:** We use `requirements-dev.txt` for local development because it includes all packages needed to run the application, plus extra tools for testing.

### Step 2: Configure the Backend

1.  **Create a `.env` file** in the main `P2P-Dashboard` directory.
2.  **Add the database configuration** to your new `.env` file. For local development, we'll use a simple file-based database (SQLite), which requires no extra setup.

    ```dotenv
    # c:\Users\DELL\P2P-Dashboard\.env
    DATABASE_URL="sqlite:///./p2p_dashboard.db"
    SECRET_KEY="a_very_secret_key_for_jwt_tokens_change_this"
    ALGORITHM="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```
    > **Note:** You can change the `SECRET_KEY` to any random string for better security.
    The easiest way to generate a strong, random key is to use Python's built-in secrets module.

Open your terminal (it doesn't matter which one or if a virtual environment is active).

Run the following command to generate a cryptographically secure 64-character hexadecimal string:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
This will output a long random string, something like this: c8b9a2f1d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2
```

This is your secret key.

### Step 3: Run the Backend Server

1.  In your terminal (where the `(.venv)` is active), run the following command:
    ```bash
    uvicorn p2p_api.main:app --reload
    ```
2.  You should see output indicating the server is running on `http://127.0.0.1:8000`.

**Leave this terminal running!** The backend is now live.

---

## Part 2: Creating a User and API Key

Now that the server is running, we'll use its built-in documentation page to create a user and then generate an API key for that user.

1.  **Open your web browser** and go to http://127.0.0.1:8000/docs.
2.  **Create a user:**
    *   Find the "Admin" section and expand the `POST /admin/users/` endpoint.
    *   Click "Try it out".
    *   In the "Request body" box, enter a username and password (e.g., `{"username": "admin", "password": "a_strong_password"}`).
    *   Click "Execute". A `200` response means it was successful.
3.  **Log in to get an access token:**
    *   Expand the `POST /admin/token` endpoint.
    *   Click "Try it out".
    *   Enter the same username and password you just created into the form fields.
    *   Click "Execute". The response will contain an `access_token`. **Copy this entire token string.**
4.  **Authorize your session:**
    *   At the top right of the page, click the "Authorize" button.
    *   In the "Value" box, type `Bearer ` (with a space after "Bearer") and then paste the access token you copied.
    *   Click "Authorize" and then "Close".
5.  **Generate the API Key:**
    *   Expand the `POST /admin/keys/` endpoint.
    *   Click "Try it out".
    *   In the "Request body", give your key a name (e.g., `{"name": "streamlit-app-key"}`).
    *   Click "Execute".
    *   The response will contain your new API key (e.g., `p2p_...`). **Copy this key and save it somewhere safe. It will not be shown again!**

---

## Part 3: Running the Frontend (Streamlit App)

Now we'll set up and run the visual dashboard, which will use the API key you just generated.

### Step 1: Set up the Frontend Environment

1.  **Open a new, separate terminal.**
2.  **Navigate to the `streamlit_app` directory.**
    ```bash
    cd streamlit_app
    ```
3.  **Create a virtual environment** for the frontend.
    ```bash
    python -m venv venv
    ```
4.  **Activate this new virtual environment.**
    *   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    Your prompt in this second terminal should now start with `(venv)`.
5.  **Install the frontend's Python packages.**
    ```bash
    pip install -r requirements.txt
    ```

### Step 2: Configure the Frontend

1.  **Create a `.env` file** inside the `streamlit_app` directory.
2.  **Add your API key** to this new file. Paste the key you saved from Part 2.
    ```dotenv
    # c:\Users\DELL\P2P-Dashboard\streamlit_app\.env
    API_KEY="p2p_...the_full_key_you_copied"
    ```

### Step 3: Run the Frontend Application

1.  In your second terminal (the one for the frontend), run the following command:
    ```bash
    streamlit run app.py
    ```
2.  This will automatically open a new tab in your web browser with the P2P Dashboard.

You're all set! You now have both the backend and frontend running locally.




