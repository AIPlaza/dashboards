# P2P Data Ingestion Worker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful and flexible worker for scraping P2P trading data from cryptocurrency exchanges and loading it into a PostgreSQL database.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setting up the .env file](#setting-up-the-env-file)
  - [Easy Deployment with Docker Compose](#easy-deployment-with-docker-compose)
  - [Alternative Deployment (Without Docker)](#alternative-deployment-without-docker)
- [Logging and Error Handling](#logging-and-error-handling)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Automated Data Extraction:** Scrapes P2P trading data from Binance and other exchanges.
- **PostgreSQL Integration:** Loads the extracted data into a PostgreSQL database.
- **Scalable:** Designed for horizontal scalability to handle large volumes of data.
- **Reliable:** Implements error recovery mechanisms to ensure data integrity.
- **Containerized Deployment:** Ready for deployment using Docker for consistent environments.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.10+
- PostgreSQL
- Docker
- Docker Compose

Before you begin, make sure you have the following:

1.  **Install Docker:** Follow the instructions on the [Docker website](https://docs.docker.com/get-docker/) to install Docker on your system.
2.  **Install Docker Compose:** Docker Compose is a tool for defining and running multi-container Docker applications. Follow the instructions on the [Docker website](https://docs.docker.com/compose/install/) to install Docker Compose on your system.

### Setting up the .env file

The `.env` file is used to store sensitive information, such as your PostgreSQL credentials. To set up the `.env` file, follow these steps:

1.  Copy the `.env.template` file to `.env`:

    ```bash
    cp .env.template .env
    ```
2.  Update the `.env` file with your PostgreSQL credentials. The `.env` file should contain the following variables:

    ```
    DATABASE_URL=postgresql://p2p_dashboard_user:4scr5XwawprE0cHtx7TJe6w8F7e994q5@dpg-d1omv9ffte5s73bhth20-a.oregon-postgres.render.com/p2p_dashboard
    DB_USER=p2p_dashboard_user
    DB_PASSWORD=4scr5XwawprE0cHtx7TJe6w8F7e994q5
    ```

    **Note:** This is the ONLY information that needs to be in the `.env` file.

### .gitignore

The `.gitignore` file is used to prevent sensitive information from being committed to the repository. Make sure that the `.gitignore` file includes the `.env` file to prevent your PostgreSQL credentials from being exposed.

### Easy Deployment with Docker Compose

This project is designed for easy deployment using Docker Compose. With just a few commands, you can have the entire system up and running, including the PostgreSQL database, Redis cache, data ingestion worker, Prometheus monitoring, and Grafana dashboards.

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/P2P-Dashboard.git
    cd P2P-Dashboard
    ```

2.  **Set up the .env file:**

    Follow the instructions in the [Setting up the .env file](#setting-up-the-env-file) section to create and configure the `.env` file.

3.  **Run the application:**

    ```bash
    docker-compose up -d
    ```

    This command will start all the services defined in the `docker-compose.yml` file.

4.  **Access the application:**

    The Grafana dashboard will be available at `http://127.0.0.1:3000`.

### Alternative Deployment (Without Docker)

If you prefer not to use Docker, you can deploy the application directly on your system.

1.  **Install Python 3.10+ and PostgreSQL:** Make sure you have Python 3.10 or higher and PostgreSQL installed on your system.
2.  **Create a virtual environment:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate # On Windows, use `.venv\Scripts\activate`
    ```

3.  **Install Dependencies:**

    **Important:** After following the troubleshooting steps for the `pydantic-core` installation issue, make sure to install the dependencies again:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up PostgreSQL Database:**

    - Ensure you have a running PostgreSQL server and create a database.
    - Copy the `.env.example` file to `.env` and update the `DATABASE_URL` with your database connection string.
    - Execute the SQL code in the `devlog.md` file to create the database schema and populate the dimension tables.

5.  **Run the application:**

    ```bash
    uvicorn p2p_api.main:app --reload
    ```

6.  **Run the scheduler:**

    Open a new terminal and run the following command:

    ```bash
    python worker/extractor.py
    ```

### Troubleshooting Deployment Issues

If you encounter a `net/http: TLS handshake timeout` error during deployment, this indicates a network issue. Try the following:

*   Check your internet connection.
*   Try again later, as the Docker registry may be temporarily unavailable.

If you encounter an error related to `pydantic-core` during dependency installation, it indicates that Rust and Cargo are required. To resolve this, follow these steps:

1.  **Install Rust and Cargo:** Follow the instructions on the [Rust website](https://rustup.rs/) to install Rust and Cargo on your system.
2.  **Add Cargo to PATH:** Ensure that the `cargo` executable is in your system's PATH environment variable.
3.  **Try installing the dependencies again:**

    ```bash
    pip install -r requirements.txt
    ```

### Logging and Error Handling

The application uses the `logging` module to log messages to a file called `worker.log`. This file can be used to troubleshoot any issues that may occur.

The application also implements a circuit breaker to prevent cascading failures. If there are too many consecutive errors, the circuit breaker will be tripped and the application will stop trying to extract data.

### Testing

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