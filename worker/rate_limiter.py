"""
Token bucket rate limiter for Binance API requests.
Thread-safe implementation that allows burst requests up to a limit.
"""
import asyncio
import time
import logging
from threading import Lock
from typing import Optional

from .config import settings

logger = logging.getLogger(__name__)

class TokenBucketRateLimiter:
    """
    Token bucket algorithm for rate limiting.

    Allows bursts up to bucket size, then enforces average rate.
    Thread-safe for use with concurrent workers.
    """

    def __init__(
        self,
        rate: int = None,
        burst_size: int = None
    ):
        """
        Initialize rate limiter.

        Args:
            rate: Requests per minute (default from config)
            burst_size: Maximum burst size (default from config)
        """
        self.rate = rate or settings.rate_limit_requests_per_minute
        self.burst_size = burst_size or settings.rate_limit_burst_size

        # Convert rate to tokens per second
        self.tokens_per_second = self.rate / 60.0

        # Current token count (starts full)
        self.tokens = float(self.burst_size)

        # Last refill timestamp
        self.last_refill = time.time()

        # Thread lock for thread safety
        self.lock = Lock()

        # Statistics
        self.total_requests = 0
        self.total_waits = 0

        logger.info(
            f"Rate limiter initialized: {self.rate} req/min, "
            f"burst={self.burst_size}"
        )

    def acquire(self, tokens: int = 1) -> float:
        """
        Acquire tokens (blocks if necessary).

        Args:
            tokens: Number of tokens to acquire

        Returns:
            Wait time in seconds (0 if no wait needed)
        """
        with self.lock:
            # Refill bucket based on elapsed time
            now = time.time()
            elapsed = now - self.last_refill
            self.tokens = min(
                self.burst_size,
                self.tokens + (elapsed * self.tokens_per_second)
            )
            self.last_refill = now

            # Check if we have enough tokens
            if self.tokens >= tokens:
                self.tokens -= tokens
                self.total_requests += 1
                return 0.0

            # Calculate wait time
            tokens_needed = tokens - self.tokens
            wait_time = tokens_needed / self.tokens_per_second

            # Wait and then consume tokens
            time.sleep(wait_time)
            self.tokens = 0 # Consumed all tokens
            self.last_refill = time.time()
            self.total_requests += 1
            self.total_waits += 1

            if self.total_waits % 10 == 0:
                logger.warning(
                    f"Rate limiter active: {self.total_waits} waits, "
                    f"{self.total_requests} total requests"
                )

            return wait_time

    def get_stats(self) -> dict:
        """Get rate limiter statistics."""
        with self.lock:
            return {
                "total_requests": self.total_requests,
                "total_waits": self.total_waits,
                "current_tokens": self.tokens,
                "wait_percentage": (
                    (self.total_waits / self.total_requests * 100)
                    if self.total_requests > 0 else 0
                )
            }

# Global rate limiter instance
rate_limiter = TokenBucketRateLimiter()