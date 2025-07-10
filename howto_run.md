# How to Run the P2P Dashboard Locally (with PostgreSQL)

This guide provides a complete, step-by-step walkthrough for setting up and running both the FastAPI backend (which will use PostgreSQL) and the Streamlit frontend on your local machine.

---

## Prerequisites

Before you start, make sure you have:

*   **Python 3.8 or higher** installed on your system.
*   **Git** installed.
*   A **PostgreSQL database** running and accessible (either locally or remotely). You'll need the database connection details (hostname, port, database name, username, and password).

---

## Part 1: Running the Backend (FastAPI API) with PostgreSQL

First, we need to get the server running and connected to your PostgreSQL database. This server is the "brain" of your application; it handles the logic for fetching data and managing users.

### Step 1: Set up the Backend Environment

1.  **Open your terminal** in the project's root directory (`P2P-Dashboard`).
2.  **Create a virtual environment** for the backend. This keeps its dependencies separate.

```
bash
python -m venv .venv
```
3.  **Activate the virtual environment.**
    *   On Windows:
```
bash
.\.venv\Scripts\activate
```
*   On macOS/Linux:
```
bash
source .venv/bin/activate
```
Your terminal prompt should now start with `(.venv)`.
4.  **Install the required Python packages, including the PostgreSQL adapter.**
```
bash
pip install -r requirements-dev.txt psycopg2-binary
```
> **Note:** We use `requirements-dev.txt` for local development. We're also adding `psycopg2-binary` which is a popular library that allows Python to talk to PostgreSQL databases.

### Step 2: Configure the Backend for PostgreSQL

1.  **Create a `.env` file** in the main `P2P-Dashboard` directory if you don't have one already.
2.  **Add your PostgreSQL database configuration** to your `.env` file. This tells the backend how to connect to your database.
```
dotenv
# .env file in the project root
DATABASE_URL="postgresql://your_db_user:your_db_password@your_db_host:your_db_port/your_db_name"

# Replace with your actual PostgreSQL connection details:
# your_db_user: The username to connect to your PostgreSQL database.
# your_db_password: The password for the database user.
# your_db_host: The address where your PostgreSQL database is running (e.g., localhost, an IP address, or a hostname).
# your_db_port: The port your PostgreSQL database is listening on (the default is usually 5432).
# your_db_name: The name of the specific database you want to connect to.

# Configure your secret key and other settings:
SECRET_KEY="a_very_secret_key_for_jwt_tokens_change_this" # Change this to a strong, random key!
ALGORITHM="HS256" # Or your chosen algorithm
ACCESS_TOKEN_EXPIRE_MINUTES=30 # Or your desired expiry time
```
> **Note:** To generate a strong `SECRET_KEY`, you can use this command in your terminal (it doesn't matter which one or if a virtual environment is active):
```
bash
python -c "import secrets; print(secrets.token_hex(32))"
```
Copy the output and use it as your `SECRET_KEY`.

3.  **Initialize the Database (if needed):**
    *   This project uses SQLAlchemy for interacting with the database. If this is the first time you're connecting to this PostgreSQL database with this application, you might need to create the necessary tables.
    *   Look for a script or instructions in the project that handle database initialization or migrations. If there isn't an automated way (like Alembic), you might need to run a script that imports your SQLAlchemy models (from `p2p_api/database.py`) and creates the tables using `Base.metadata.create_all(engine)`. **(Self-correction: I should verify if such a script exists or if this needs to be added).**
    *   For apprentices: This step is like setting up the empty shelves and containers in your database before you start putting data in them.

### Step 3: Run the Backend Server

1.  In your terminal (where the `(.venv)` is active), run the following command:

```
bash
uvicorn p2p_api.main:app --reload
```
2.  You should see output indicating the server is running, likely on `http://127.0.0.1:8000`. Look for messages that confirm it's connecting to your PostgreSQL database.

**Leave this terminal running!** The backend is now live and connected to your PostgreSQL database.

---

## Part 2: Creating a User and API Key

Now that the server is running and connected to your database, we'll use its built-in documentation page to create a user and then generate an API key for that user.

1.  **Open your web browser** and go to `http://127.0.0.1:8000/docs`.
2.  **Create a user:**
    *   Find the "Admin" section and expand the `POST /admin/users/` endpoint.
    *   Click "Try it out".
    *   In the "Request body" box, enter a username and password (e.g., `{"username": "admin", "password": "a_strong_password"}`).
    *   Click "Execute". A `200` response means it was successful. This user is now created in your PostgreSQL database.
3.  **Log in to get an access token:**
    *   Expand the `POST /admin/token` endpoint.
    *   Click "Try it out".
    *   Enter the same username and password you just created into the form fields.
    *   Click "Execute". The response will contain an `access_token`. **Copy this entire token string.** This token is temporary and proves you are logged in.
4.  **Authorize your session:**
    *   At the top right of the page, click the "Authorize" button.
    *   In the "Value" box, type `Bearer ` (with a space after "Bearer") and then paste the access token you copied.
    *   Click "Authorize" and then "Close". This tells the documentation page that you are authenticated and can access protected endpoints.
5.  **Generate the API Key:**
    *   Expand the `POST /admin/keys/` endpoint.
    *   Click "Try it out".
    *   In the "Request body", give your key a name (e.g., `{"name": "streamlit-app-key"}`).
    *   Click "Execute".
    *   The response will contain your new API key (e.g., `p2p_...`). **Copy this key and save it somewhere safe. It will not be shown again!** This API key is a more permanent "password" that your Streamlit app will use.

---

## Part 3: Running the Frontend (Streamlit App)

Now we'll set up and run the visual dashboard, which will use the API key you just generated to communicate with the backend.

### Step 1: Set up the Frontend Environment

1.  **Open a new, separate terminal.**
2.  **Navigate to the `streamlit_app` directory.**

```
bash
cd streamlit_app
```
3.  **Create a virtual environment** for the frontend.
```
bash
python -m venv venv
```
4.  **Activate this new virtual environment.**
    *   On Windows:
```
bash
.\venv\Scripts\activate
```
*   On macOS/Linux:
```
bash
source venv/bin/activate
```
Your prompt in this second terminal should now start with `(venv)`.
5.  **Install the frontend's Python packages.**
```
bash
pip install -r requirements.txt
```
### Step 2: Configure the Frontend with the API Key

1.  **Create a `.env` file** inside the `streamlit_app` directory if you don't have one.
2.  **Add your API key** to this new file. Paste the key you saved from Part 2.
```
dotenv
# .env file in the streamlit_app directory
API_KEY="p2p_...the_full_key_you_copied"
```
Replace `"p2p_...the_full_key_you_copied"` with the actual API key you copied.

### Step 3: Run the Frontend Application

1.  In your second terminal (the one for the frontend), run the following command:
```
bash
streamlit run app.py
```
2.  This will automatically open a new tab in your web browser with the P2P Dashboard, which should now be communicating with your backend using the API key.

<<<<<<< HEAD
You're all set! You now have both the backend (connected to PostgreSQL) and frontend running locally.

---

**Potential Enhancements/Notes for Production:**

*   **Database Migrations:** For managing database schema changes over time in a production environment, consider using a tool like Alembic.
*   **Secure .env Files:** Ensure `.env` files are never committed to version control and are handled securely in your production deployment process.
*   **Production Server:** For production, you would typically use a more robust web server like Gunicorn or Uvicorn with multiple workers, and potentially a process manager like Systemd or Supervisor.
*   **HTTPS:** In production, always use HTTPS to encrypt communication between the frontend and backend.
=======
You're all set! You now have both the backend (connected to PostgreSQL) and frontend running locally.

---

**Potential Enhancements/Notes for Production:**

*   **Database Migrations:** For managing database schema changes over time in a production environment, consider using a tool like Alembic.
*   **Secure .env Files:** Ensure `.env` files are never committed to version control and are handled securely in your production deployment process.
*   **Production Server:** For production, you would typically use a more robust web server like Gunicorn or Uvicorn with multiple workers, and potentially a process manager like Systemd or Supervisor.
*   **HTTPS:** In production, always use HTTPS to encrypt communication between the frontend and backend.
>>>>>>> 4700fa9d33cb50e2aa0f9c450b50116069dc126b
