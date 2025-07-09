class ScraperError(Exception):
    """Custom exception for scraper-related errors."""
    def __init__(self, message="A scraping operation failed."):
        self.message = message
        super().__init__(self.message)

class DataParsingError(Exception):
    """Custom exception for data parsing errors."""
    def __init__(self, message="Failed to parse data."):
        self.message = message
        super().__init__(self.message)
