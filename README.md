# P2P Dashboard API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful and flexible API for scraping P2P trading data from cryptocurrency exchanges.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Local Installation](#local-installation)
  - [Docker Usage](#docker-usage)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
  - [Get Binance Offers](#get-binance-offers)
  - [Get Binance Pairs](#get-binance-pairs)
  - [Get Bybit Offers](#get-bybit-offers)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Real-time Data:** Scrape P2P trading data from Binance and other exchanges in real-time.
- **Flexible Queries:** Filter offers by fiat currency, crypto asset, trade type, and more.
- **Extensible:** Easily add new exchanges and trading pairs.
- **Secure:** Protect your API with API key authentication.
- **Containerized Deployment:** Ready for deployment using Docker for consistent environments.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.10+ (for local development)
- PostgreSQL
- Docker (for containerized deployment)

### Local Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/P2P-Dashboard.git
   cd P2P-Dashboard
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate # On Windows, use `.venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   - **For Production:**
     Install only the packages required to run the application:
     ```bash
     pip install -r requirements.txt
     ```

   - **For Development & Testing:**
     This command installs all production packages plus development tools like `pytest`.
     ```bash
     pip install -r requirements-dev.txt
     ```

4. **Set up PostgreSQL Database (for production-like setup only):**

   - Ensure you have a running PostgreSQL server and create a database.
   - Copy the `.env.example` file to `.env` and update the `DATABASE_URL` with your database connection string.

5. **Generate an API key:**

   - Run the following command to generate a secure API key:

     ```bash
     python -c "import secrets; print(secrets.token_hex(32))"
     ```

   - Add the generated key to your `.env` file as `API_KEY`.

6. **Troubleshooting Installation (Windows):**

   The `psycopg2-binary` package is required for PostgreSQL support. Sometimes, its installation can fail on Windows if `pip` cannot find a pre-compiled binary for your system. If you see an error related to `Microsoft Visual C++` or `pg_config`, try the following solutions in order:

   - **Solution 1 (Update Pip):** Ensure you have the latest version of pip, which can help it find the correct package version.
     ```bash
     python -m pip install --upgrade pip
     pip install -r requirements.txt
     ```

   - **Solution 2 (Install Build Tools):** If updating pip doesn't work, you will need to install the necessary build tools.
     1. Download and install the Visual Studio Build Tools. During installation, select the **"C++ build tools"** workload.
     2. Download and install PostgreSQL for Windows.
     3. After installation, try installing the project dependencies again.

### Docker Usage

Alternatively, you can build and run the application using Docker for a containerized environment.

1. **Build the Docker image:**

   ```bash
   docker build -t p2p-dashboard-api .
   ```

2. **Run the Docker container:**

   Ensure your `.env` file is correctly configured with your `DATABASE_URL` and `API_KEY`.

   ```bash
   docker run -d --name p2p-dashboard -p 8000:8000 --env-file ./.env p2p-dashboard-api
   ```

   - `-d`: Runs the container in detached mode (in the background).
   - `--name p2p-dashboard`: Assigns a name to your container for easy reference.
   - `-p 8000:8000`: Maps port 8000 on your host to port 8000 in the container.
   - `--env-file ./.env`: Mounts your local `.env` file into the container to provide environment variables.

## Usage

To run the application locally (after local installation):

```bash
uvicorn p2p_api.main:app --reload
```

If running via Docker, the application will start automatically when the container runs.

The API will be available at `http://127.0.0.1:8000`.

You can view the auto-generated interactive API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints (Manual Examples)

### Get Binance Offers

- **Endpoint:** `/api/v1/binance/offers`
- **Method:** `GET`
- **Description:** Get a list of P2P offers from Binance.
- **Query Parameters:**
  - `fiat` (string, required): Fiat currency (e.g., `VES`, `USD`).
  - `asset` (string, required): Crypto asset (e.g., `USDT`, `BTC`).
  - `trade_type` (string, required): Trade type (`BUY` or `SELL`).
  - `page` (integer, optional): Page number (default: `1`).
  - `rows` (integer, optional): Number of rows per page (default: `20`).
- **Headers:**
  - `X-API-Key` (string, required): Your API key.
- **Example:**

  ```bash
  curl -X GET "http://127.0.0.1:8000/api/v1/binance/offers?fiat=VES&asset=USDT&trade_type=BUY" -H "X-API-Key: your-api-key"
  ```

### Get Binance Pairs

- **Endpoint:** `/api/v1/binance/pairs`
- **Method:** `GET`
- **Description:** Get a list of available trading pairs from Binance.
- **Headers:**
  - `X-API-Key` (string, required): Your API key.
- **Example:**

  ```bash
  curl -X GET "http://127.0.0.1:8000/api/v1/binance/pairs" -H "X-API-Key: your-api-key"
  ```

### Get Bybit Offers

- **Endpoint:** `/api/v1/bybit/offers`
- **Method:** `GET`
- **Description:** Get a list of P2P offers from Bybit.
- **Note:** This endpoint is not yet implemented.

## Testing

To run the tests, use the following command:

```bash
python -m pytest
```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.