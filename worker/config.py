"""
Worker configuration - independent from FastAPI config.
Reads from environment variables, no imports from p2p_api.
"""
import os
from typing import Optional
from pydantic_settings import BaseSettings


class WorkerSettings(BaseSettings):
    """Configuration for P2P data ingestion worker."""

    # Database
    database_url: str
    db_pool_size: int = 20
    db_max_overflow: int = 10

    # Binance API
    binance_base_url: str = "https://p2p.binance.com"
    binance_search_endpoint: str = "/bapi/c2c/v2/friendly/c2c/adv/search"
    binance_pairs_endpoint: str = "/bapi/c2c/v2/public/c2c/asset-order/getAllSupportAsset"

    # Extraction
    extraction_interval_minutes: int = 10
    max_workers: int = 20
    request_timeout_seconds: int = 30
    max_retries: int = 3
    max_pages_per_pair: int = 50

    # Rate Limiting
    rate_limit_requests_per_minute: int = 100
    rate_limit_burst_size: int = 20

    # Monitoring
    prometheus_port: int = 9090
    log_level: str = "INFO"

    class Config:
        env_file = ".env"
        env_prefix = "WORKER_" # All env vars start with WORKER_

# Global settings instance
settings = WorkerSettings()