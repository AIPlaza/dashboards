# Project Initialization Guide for LLMs

This document provides instructions for LLMs to understand the project context and proceed with development.

## Project Description

This project is a P2P data ingestion system that extracts data from Binance P2P, transforms it, and loads it into a PostgreSQL database. The system consists of a backend API and a data ingestion worker.

## Project Structure

The project has the following directory structure:

*   `p2p_api/`: Contains the code for the backend API.
*   `worker/`: Contains the code for the data ingestion worker.
*   `alembic/`: Contains the database migration scripts.
*   `docs/`: Contains the documentation for the project.
*   `docker-compose.yml`: Defines the services required to run the project.
*   `devlog.md`: Tracks the development process.

## Key Files and Their Purpose

*   `p2p_ingestion_worker_prd.md`: Contains the product requirements document for the data ingestion worker.
*   `worker/__init__.py`: Makes the `worker/` directory a Python package.
*   `docs/worker.md`: Contains the documentation for the data ingestion worker.
*   `docs/SUMMARY.md`: Contains the table of contents for the documentation.
*   `docker-compose.yml`: Defines the services required to run the project.
*   `devlog.md`: Tracks the development process.

## Development Environment Setup

To set up the development environment, follow these steps:

1.  Install Docker and Docker Compose.
2.  Clone the repository.
3.  Create a `.env` file with the necessary environment variables (e.g., `DATABASE_URL`, `DB_USER`, `DB_PASSWORD`).
4.  Run `docker-compose up -d` to start the services.

## Running Tests

To run the tests, execute the following command:

```bash
pytest
```

## Deployment

Before deploying the application to production, make sure to:

*   Install the `APScheduler` and `prometheus_client` libraries by running `pip install -r requirements.txt`.
*   Create a `.env` file with the necessary environment variables (e.g., `DATABASE_URL`, `DB_USER`, `DB_PASSWORD`).
*   Execute the SQL code in the `devlog.md` file to create the database schema and populate the dimension tables.
*   Import the `monitoring/dashboards/p2p-dashboard.yaml` file into Grafana.

To deploy the application, execute the following command:

```bash
docker-compose up -d
```

## Development Log

The `devlog.md` file contains a detailed log of the development process. Please refer to this file to understand the design decisions, implementation details, and any issues encountered.