import logging
import os
from worker.db import db_manager
from sqlalchemy import text # Import text

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

SCHEMA_FILE = "schema.sql"

def execute_sql_schema():
    if not os.path.exists(SCHEMA_FILE):
        logger.error(f"Schema file not found: {SCHEMA_FILE}")
        return

    with open(SCHEMA_FILE, 'r', encoding='utf-8') as f:
        sql_script = f.read()

    try:
        with db_manager.engine.connect() as connection:
            # Execute the entire script as a single transaction
            connection.execute(text(sql_script))
            connection.commit()
        logger.info(f"Successfully executed schema from {SCHEMA_FILE}")
    except Exception as e:
        logger.error(f"Error executing schema from {SCHEMA_FILE}: {e}", exc_info=True)
        # Rollback in case of error
        with db_manager.engine.connect() as connection:
            connection.rollback()
        raise

if __name__ == "__main__":
    try:
        execute_sql_schema()
        # After successful schema execution, you might want to close the db_manager
        db_manager.close()
    except Exception as e:
        logger.error(f"Schema execution failed: {e}")