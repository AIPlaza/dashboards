# P2P Dashboard API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful and flexible API for scraping P2P trading data from cryptocurrency exchanges.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
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

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.9+
- PostgreSQL

### Installation

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

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   - Create a PostgreSQL database.
   - Copy the `.env.example` file to `.env` and update the `DATABASE_URL` with your database connection string.

5. **Generate an API key:**

   - Run the following command to generate a secure API key:

     ```bash
     python -c "import secrets; print(secrets.token_hex(32))"
     ```

   - Add the generated key to your `.env` file as `API_KEY`.

## Usage

To run the application, use the following command:

```bash
uvicorn p2p_api.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Get Binance Offers

- **Endpoint:** `/api/v1/binance/offers`
- **Method:** `GET`
- **Description:** Get a list of P2P offers from Binance.
- **Query Parameters:**
  - `fiat` (string, required): Fiat currency (e.g., `VES`, `USD`).
  - `asset` (string, required): Crypto asset (e.g., `USDT`, `BTC`).
  - `tradeType` (string, required): Trade type (`BUY` or `SELL`).
  - `page` (integer, optional): Page number (default: `1`).
  - `rows` (integer, optional): Number of rows per page (default: `20`).
- **Headers:**
  - `X-API-Key` (string, required): Your API key.
- **Example:**

  ```bash
  curl -X GET "http://127.0.0.1:8000/api/v1/binance/offers?fiat=VES&asset=USDT&tradeType=BUY" -H "X-API-Key: your-api-key"
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
