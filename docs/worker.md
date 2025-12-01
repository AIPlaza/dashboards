# Data Ingestion Worker

## Architecture

The data ingestion worker is responsible for extracting data from Binance P2P, transforming it, and loading it into the PostgreSQL database. The worker is integrated into the existing backend and consists of the following components:

*   **Scheduler:** Triggers the worker to run at regular intervals.
*   **Extractor:** Extracts data from Binance P2P using the internal scraping logic.
*   **Transformer:** Transforms the extracted data into a format suitable for loading into PostgreSQL.
*   **Loader:** Loads the transformed data into the PostgreSQL database.
*   **Data Quality Checker:** Validates the extracted data and ensures that it meets certain quality standards.
*   **Error Handler:** Catches and logs any errors that occur during the extraction, transformation, or loading process.

## Configuration

The worker can be configured using the following environment variables:

*   `DATABASE_URL`: The URL of the PostgreSQL database.
*   `BINANCE_API_KEY`: The API key for the Binance P2P API.
*   `EXTRACTION_INTERVAL`: The interval at which the worker should run (in minutes).

## Usage

To deploy the worker, execute the following command:

```bash
docker-compose up -d
```

This command will start the PostgreSQL database, the Redis cache, the data ingestion worker, the Prometheus monitoring system, and the Grafana dashboard.

To stop the worker, execute the following command:

```bash
docker-compose down
```

## Troubleshooting

### Issue: The worker is not running.

Solution: Check the logs for any errors. Make sure that the `DATABASE_URL` and `BINANCE_API_KEY` environment variables are set correctly.

### Issue: The worker is exceeding the Binance P2P API rate limits.

Solution: Implement a rate limiter to prevent the worker from making too many requests to the Binance P2P API.
## Monitoring

The worker exposes Prometheus metrics that can be used to monitor its performance. To visualize these metrics, you can import the `monitoring/dashboards/p2p-dashboard.yaml` file into Grafana.

To import the dashboard, follow these steps:

1.  In Grafana, click on the "+" icon in the left-hand menu and select "Import".
2.  Click on the "Upload .json file" button and select the `monitoring/dashboards/p2p-dashboard.yaml` file.
3.  Select the Prometheus data source.
4.  Click on the "Import" button.