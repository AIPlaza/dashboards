"""
Worker configuration - independent from FastAPI config.
Reads from environment variables, no imports from p2p_api.
"""
import os
import json
import os
from typing import Optional
from pydantic_settings import BaseSettings


class WorkerSettings(BaseSettings):
    """Configuration for P2P data ingestion worker."""

    # Database
    database_url: str
    db_pool_size: int = 20
    db_max_overflow: int = 10

    # P2P Configuration File
    p2p_config_path: str = "p2p_config.json"

    # Binance API
    binance_base_url: str = "https://p2p.binance.com"
    binance_search_endpoint: str = "/bapi/c2c/v2/friendly/c2c/adv/search"

    # P2P Configuration from JSON
    _p2p_config: Optional[dict] = None

    @property
    def p2p_config(self) -> dict:
        if self._p2p_config is None:
            if not os.path.exists(self.p2p_config_path):
                raise FileNotFoundError(f"P2P configuration file not found at {self.p2p_config_path}")
            with open(self.p2p_config_path, 'r', encoding='utf-8') as f:
                self._p2p_config = json.load(f)
        return self._p2p_config

    @property
    def binance_p2p_until_page(self) -> int:
        return self.p2p_config["DEFAULTS"]["BINANCE_P2P_UNTIL_PAGE"]

    # Extraction
    extraction_interval_minutes: int = 10
    max_workers: int = 20
    request_timeout_seconds: int = 30
    max_retries: int = 3

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