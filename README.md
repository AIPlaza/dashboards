# P2P Data Ingestion Worker

## Introduction

This document provides instructions on how to deploy and run the P2P data ingestion worker. The worker extracts data from Binance P2P and loads it into a PostgreSQL database.

## Prerequisites

- Python 3.7+
- PostgreSQL database
- `.venv` virtual environment
- Required Python packages (see `requirements.txt`)

## Deployment

### 1. Clone the repository

```bash
git clone <repository_url>
cd <repository_directory>
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

```bash
# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the worker

Create a `.env` file in the root directory with the following variables:

```env
# Database
WORKER_DATABASE_URL=postgresql://<user>:<password>@<host>:<port>/<database>

# Rate Limiting
WORKER_RATE_LIMIT_REQUESTS_PER_MINUTE=100

# Extraction
WORKER_EXTRACTION_INTERVAL_MINUTES=10
WORKER_MAX_WORKERS=20

# Monitoring
WORKER_LOG_LEVEL=INFO
```

Replace the placeholders with your actual values.

### 6. Create database schema

Run the SQL script in `schema.sql` to create the database schema. You can use a tool like `psql` to run the script:

```bash
psql -U <user> -h <host> -d <database> -f schema.sql
```

### 7. Run the worker

```bash
python worker/main.py
```

The worker will start extracting data from Binance P2P and loading it into the PostgreSQL database.

## Monitoring

The worker exposes Prometheus metrics on port 9090. You can use Prometheus to monitor the worker's performance.

## Logging

The worker uses the logging module to log events. The log level can be configured using the `WORKER_LOG_LEVEL` environment variable.

## Contributing

Contributions are welcome! Please submit a pull request with your changes.