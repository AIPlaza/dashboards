import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = "logs"
LOG_FILE = "p2p_api.log"

def setup_logging():
    os.makedirs(LOG_DIR, exist_ok=True)

    log_format = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

    handlers = [
        logging.StreamHandler(),  # consola
        RotatingFileHandler(
            os.path.join(LOG_DIR, LOG_FILE),
            maxBytes=2 * 1024 * 1024,  # 2MB por archivo
            backupCount=5  # guarda hasta 5 archivos rotados
        )
    ]

    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=handlers
    )

    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)