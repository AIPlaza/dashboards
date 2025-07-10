# Administrator Workflow for API Key Management

This document outlines the end-to-end process for an administrator to generate an API key and configure the internal Streamlit application to use it.

This workflow is designed for an internal tool where the application itself is the "user" of the API, and its credentials (the API key) are managed as a secret environment variable.

---

## Step 1: Start the Backend API

Ensure your FastAPI server is running. From the project root, execute:

```bash
uvicorn p2p_api.main:app --reload
```

## Step 2: Create Your Admin Account (One-Time Setup)

You need to create a username and password for yourself to access the administrative endpoints.

1.  Navigate to the interactive API documentation at `http://127.0.0.1:8000/docs`.
2.  Find the `POST /admin/users/` endpoint under the "Admin User Management" tag.
3.  Click "Try it out" and provide a JSON body with your desired admin username and password.
4.  Execute the request.

## Step 3: Log In and Get Your Admin Token

Now that you have an account, you need to log in to get a temporary access token (JWT).

1.  In the API docs, find the `POST /admin/token` endpoint.
2.  Provide your username and password in the `application/x-www-form-urlencoded` fields.
3.  Execute the request and copy the `access_token` from the response body.

## Step 4: Generate a New API Key

1.  In the API docs, click the "Authorize" button at the top right.
2.  In the dialog, paste your token in the format `Bearer <your_token>`.
3.  Find the `POST /admin/keys/` endpoint under "Admin API Key Management".
4.  Click "Try it out" and optionally provide a name for the key (e.g., `{"name": "Streamlit App Key"}`).
5.  Execute the request.
6.  Copy the full API key (e.g., `p2p_...`) from the response. **This is the only time the full key will be shown.**

## Step 5: Set the API Key for the Streamlit App

1.  In the root of your project (`c:\Users\DELL\P2P-Dashboard\`), create or open a file named `.env`.
2.  Add the API key you just generated to this file:

    ```env
    API_KEY="p2p_...the_full_key_you_just_generated"
    ```

## Step 6: Run the Streamlit App

Now, when you run your Streamlit application, it will automatically load the `API_KEY` from your `.env` file, and all requests to your secure backend will be authenticated successfully.

```bash
streamlit run streamlit_app/app.py
```