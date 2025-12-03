"""
Main entry point for the P2P data ingestion worker.
"""
import logging
import time
import schedule
import uuid

from worker.config import settings
from worker.extractor import extractor
from worker.loader import loader

# Configure logging
logging.basicConfig(
    level=settings.log_level,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

def job():
    """The main job to be scheduled."""
    logger.info("Starting P2P data extraction job...")
    batch_id = uuid.uuid4()
    
    try:
        # 1. Extract data
        offers = extractor.extract_all_offers()
        
        # 2. Load data
        if offers:
            loader.load_offers(offers, batch_id)
        
        logger.info("P2P data extraction job finished successfully.")
    
    except Exception as e:
        logger.error(f"An error occurred during the job: {e}", exc_info=True)

def main():
    """
    Main function to run the worker.
    Schedules the job to run at the specified interval.
    """
    logger.info(f"Worker starting. Job will run every {settings.extraction_interval_minutes} minutes.")
    
    # Run the job once immediately
    job()
    
    # Then schedule it to run at the specified interval
    schedule.every(settings.extraction_interval_minutes).minutes.do(job)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
