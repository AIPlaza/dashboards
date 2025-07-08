# P2P Dashboard API

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.116.0-009688.svg)](https://fastapi.tiangolo.com/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-0.35.0-orange.svg)](https://www.uvicorn.org/)

This project provides a robust backend API for scraping P2P (Peer-to-Peer) trading data from various cryptocurrency exchanges, with an initial focus on Binance. Built with FastAPI, it offers a high-performance and modern solution for accessing real-time P2P offer data, complete with filtering capabilities.

## ✨ Features

*   **Binance P2P Scraper:** Efficiently fetches real-time P2P offers directly from Binance.
*   **FastAPI Endpoints:** Exposes scraped data through well-defined, easy-to-use API endpoints.
*   **Flexible Filtering:** Allows dynamic filtering of offers based on fiat currency, crypto asset, and trade type (BUY/SELL).
*   **Modular & Scalable:** Designed with a clear, modular structure for easy maintenance and future expansion.
*   **Robust Error Handling:** Incorporates detailed logging for better error tracking and debugging.

## 🚀 Technologies Used

*   **Python 3.x:** The core programming language.
*   **FastAPI:** A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
*   **Uvicorn:** An ASGI server that powers the FastAPI application.
*   **Requests:** A popular HTTP library for making requests to external APIs.
*   **Playwright:** (Installed for future Bybit integration) A library for browser automation, useful for scraping dynamic content.

## 📂 Project Structure

The project is organized as follows:

```
P2P-Dashboard/
├── p2p_api/
│   ├── venv/                 # Python virtual environment
│   ├── __init__.py           # Makes p2p_api a Python package
│   ├── main.py               # Main FastAPI application
│   ├── binance_scraper.py    # Contains the Binance P2P scraping logic
│   └── bybit_scraper.py      # Placeholder for future Bybit P2P scraping logic
├── docs/
│   └── api/                  # API documentation in Markdown format
│       ├── root_endpoint.md
│       └── binance_offers.md
└── README.md                 # Project README file
```

*   `p2p_api/`: Contains the core backend application code.
    *   `venv/`: The Python virtual environment, isolating project dependencies.
    *   `__init__.py`: An empty file that signifies `p2p_api` as a Python package, allowing for proper imports.
    *   `main.py`: The entry point for the FastAPI application, defining API routes and integrating scraper functions.
    *   `binance_scraper.py`: Encapsulates the logic for fetching P2P offers from Binance.
    *   `bybit_scraper.py`: A placeholder for future integration of Bybit P2P scraping.
*   `docs/api/`: Stores detailed Markdown documentation for each API endpoint.
*   `README.md`: This file, providing an overview and instructions for the project.

## ⚙️ Setup

To get the project up and running on your local machine, follow these steps:

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <repository_url>
    cd P2P-Dashboard
    ```
    *(Assuming you are already in the `C:/Users/DELL/P2P-Dashboard` directory)*

2.  **Create a Python virtual environment:**
    It's highly recommended to use a virtual environment to manage project dependencies.
    ```bash
    python -m venv p2p_api/venv
    ```

3.  **Activate the virtual environment:**

    *   **On Windows:**
        ```bash
        .\p2p_api\venv\Scripts\activate
        ```
    *   **On macOS/Linux:**
        ```bash
        source p2p_api/venv/bin/activate
        ```

4.  **Install project dependencies:**
    With your virtual environment activated, install the required Python packages:
    ```bash
    pip install fastapi uvicorn requests playwright
    ```
    Then, install the necessary browser binaries for Playwright:
    ```bash
    playwright install
    ```

## 🏃 Running the Application

Once the setup is complete, you can start the FastAPI server:

1.  **Ensure your virtual environment is activated.**
2.  **Run the Uvicorn server:**
    ```bash
    uvicorn p2p_api.main:app --host 0.0.0.0 --port 8000
    ```
    This command starts the server, making the API accessible. The `--host 0.0.0.0` makes the server accessible from other devices on your network, and `--port 8000` sets the port.

The API will be accessible in your web browser or API client at `http://127.0.0.1:8000`.

## 🌐 API Endpoints

Detailed documentation for each API endpoint can be found in the `docs/api/` directory, including guidance on [Binance P2P Pair Discovery](docs/api/binance_pair_discovery.md).

### 1. Root Endpoint

*   **URL:** `/`
*   **Method:** `GET`
*   **Description:** A simple health check endpoint to confirm the API is operational.
*   **Response:**
    ```json
    {"message": "P2P Dashboard API is running!"}
    ```

### 2. Binance P2P Offers

*   **URL:** `/api/v1/binance/offers`
*   **Method:** `GET`
*   **Description:** Fetches real-time P2P offers from Binance based on specified criteria.
*   **Query Parameters:**
    *   `fiat` (string, optional, default: `VES`): The fiat currency (e.g., `VES`, `USD`, `EUR`).
    *   `asset` (string, optional, default: `USDT`): The crypto asset (e.g., `USDT`, `BTC`, `ETH`).
    *   `tradeType` (string, optional, default: `BUY`): The type of trade (`BUY` or `SELL`).
    *   `page` (integer, optional, default: `1`): The page number for pagination.
    *   `rows` (integer, optional, default: `20`): The number of results to return per page.
*   **Example Usage:**
    ```
    http://127.0.0.1:8000/api/v1/binance/offers?fiat=USD&asset=BTC&tradeType=SELL&page=1&rows=50
    ```
*   **Response:** A JSON array of P2P offers, each containing details such as `advertiser`, `price`, `available` amount, `limits` per transaction, and `payment_methods`.

## 💡 Future Enhancements

*   **Bybit Integration:** Implement the Bybit P2P scraper to expand data sources.
*   **Database Persistence:** Integrate a database (e.g., using SQLAlchemy) for storing historical offer data and managing configurations.
*   **Advanced Filtering & Sorting:** Introduce more sophisticated filtering and sorting options for P2P offers.
*   **Caching:** Implement caching mechanisms for API responses to improve performance.
*   **Enhanced Error Handling:** Further refine error handling and logging for production environments.
*   **Frontend Integration:** Develop a simple frontend dashboard to visualize the P2P data.