# Fintech database architecture and prompt engineering PRD

Source: [Claude Chat](https://claude.ai/chat/57b329fe-0ffd-4aeb-ab36-1f76c1697439)
Extracted: 2025-12-01T19:55:23.634Z
🚀 Exported with [Save my Chatbot](https://save.hugocolin.com)!

---

## User

lets continue with the work that previous agent was making and writte in .md file a prompt engineering like prd and audit so the coder agent can work on the app and apply fixes, you are a great developer inetracting always with fintech and postgresql great architecture always focus on functionality and value percepcion with great modular and professional interaction watching type hints, structure, architecture, best practices. As per last conversation theses were my answers:"1. The point is i need something highky functional and simpler considering i want to feed my data base because after that i will create an app for extracting and processing this data
2. As i told you maybe i need the fastapi later not now
3. Considering the context i am giving you, you tell me, i think nothing.
so as per the analogy:"🏪 Binance P2P = Public Library (anyone can read books)
🏢 Your FastAPI = Your Bookstore (you control who buys)
📚 Worker = Your Personal Reading (just go to library!)
👥 Streamlit Users = Customers (must buy from YOUR store)" it will be "🏪 Binance P2P = Public Library (anyone can read books)
📚 Worker = Your Personal Reading (just go to library!)
🏢 Your FastAPI = Your Bookstore (you control who buys)
👥 Streamlit Users = Customers (must buy from YOUR store)""

##### Inputs:
- md
- GITHUB

## Claude

# P2P Data Ingestion Worker - Critical Architecture Audit & Development PRD

## Executive Summary

**Current State:** You have a basic worker skeleton that attempts to extract P2P data, but it has **critical architectural flaws** that will prevent production deployment.

**Goal:** Build a highly functional, simple worker that directly extracts from Binance → PostgreSQL, with FastAPI added later for serving data to applications.

**Architecture Decision:** Worker operates independently, FastAPI is built separately afterward to serve the data.

## 🎯 Clarified Architecture (Based on Your Responses)

```
┌─────────────────────────────────────────────────────────┐
│ PHASE 1: DATA INGESTION │
│ │
│ 📚 Worker ─────→ 🏪 Binance P2P ─────→ 🗄️ PostgreSQL │
│ (Your code) (Public API) (Your warehouse)│
│ │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ PHASE 2: DATA ACCESS (Later) │
│ │
│ 👥 Streamlit ───→ 🏢 FastAPI ───→ 🗄️ PostgreSQL │
│ (Customers) (Your Store) (Your data) │
│ │
└─────────────────────────────────────────────────────────┘
```

**Key Insight:** You're building a data collection pipeline first, application layer second.

## User

Continue

## Message



## User

what happended

## Claude

# P2P Data Ingestion Worker - Critical Architecture Audit & Development PRD (Continued)

## 🚨 CRITICAL ISSUES IN CURRENT CODE

### Issue 1: **Circular Import Deadlock** 🔴 BLOCKER

**Location:** `worker/extractor.py:9-10`

python

```python
from p2p_api.config import Settings
#from . import crud, schemas
#from .database import get_db
```

**Problem:** Your worker is trying to import from `p2p_api`, but worker is INSIDE `p2p_api` structure. This creates:
```
p2p_api → worker → p2p_api (CIRCULAR!)
```

**Impact:** Application will crash on startup with `ImportError: cannot import name...`

**Why This Happened:** You're mixing FastAPI web layer with worker logic in the same module.

### Issue 2: **Hardcoded Single Trading Pair** 🔴 BLOCKER

**Location:** `worker/extractor.py:154-157`

python

```python
def extract_data():
 fiat = "VES" # ❌ Hardcoded
 asset = "USDT" # ❌ Hardcoded
 tradeType = "BUY" # ❌ Hardcoded
```

**Problem:** Your PRD requires extracting **ALL** trading pairs (100+ combinations), but the code only extracts ONE pair.

**Missing Logic:**

1. Discovery of available pairs from Binance

2. Iteration over all fiat/crypto/trade_type combinations

3. Progress tracking per pair

4. Parallel extraction of multiple pairs

**Impact:** You'll only get VES/USDT/BUY data, missing 99% of the market.

### Issue 3: **Database Connection Anti-Pattern** 🔴 CRITICAL

**Location:** `worker/extractor.py:229-231`

python

```python
def load_data(data):
 DATABASE_URL = "postgresql://postgres:password@localhost:5432/p2p_data_warehouse"
 conn = psycopg2.connect(DATABASE_URL)
```

**Problems:**

1. **Creates NEW connection for EVERY batch** - Memory leak

2. **Hardcoded credentials** - Security violation

3. **No connection pooling** - Poor performance

4. **Connections never closed on error** - Resource exhaustion

**What Will Happen:** After ~10 runs, PostgreSQL will hit "too many connections" error and refuse all new connections.

### Issue 4: **Non-Functional Rate Limiting** 🟡 HIGH

**Location:** `worker/extractor.py:13` and `worker/extractor.py:73`

python

```python
RATE_LIMIT = 10 # requests per minute

# But in _make_binance_request():
time.sleep(60 / RATE_LIMIT) # Sleep 6 seconds AFTER every request
```

**Problem:** This creates a **fixed delay**, not rate limiting.

- With `ThreadPoolExecutor(max_workers=10)`, you'll make 10 parallel requests **immediately**

- The sleep happens AFTER the request

- Binance will see 10 requests in 1 second → IP ban

**What You Need:** Token bucket algorithm or semaphore-based limiter.

### Issue 5: **Duplicate Function Definitions** 🟡 MEDIUM

**Location:** `worker/extractor.py:290-310`

python

```python
# Lines 290-305: circuit_breaker() defined
def circuit_breaker():
 ...

# Lines 307-322: SAME circuit_breaker() defined AGAIN!
def circuit_breaker():
 ...
```

**Impact:** Second definition overwrites first, causing confusion and dead code.

### Issue 6: **Incomplete Data Transformation** 🟡 HIGH

**Location:** `worker/extractor.py:231-258`

python

```python
data_to_insert.append((
 str(uuid.uuid4()), # offer_external_id
 str(uuid.uuid4()), # batch_id
 datetime.datetime.now(),
 1, # ❌ crypto_id (assuming USDT is always 1)
 1, # ❌ fiat_id (assuming VES is always 1)
 1, # ❌ advertiser_sk (assuming a default advertiser)
 ...
))
```

**Problems:**

1. Assumes USDT always has `crypto_id=1` - not guaranteed

2. Assumes VES always has `fiat_id=1` - not guaranteed

3. Uses dummy `advertiser_sk=1` - violates referential integrity

4. Missing payment methods insertion

5. No dimension table lookups

**Impact:** Foreign key violations, data corruption, incomplete records.

### Issue 7: **Prometheus Metrics Never Updated** 🟢 LOW

**Location:** `worker/extractor.py:21-23`

python

```python
REQUEST_TIME = Summary('p2p_extraction_request_processing_seconds', ...)
# ❌ Never used with @REQUEST_TIME.time() decorator

ERROR_COUNT = Counter('p2p_extraction_errors_total', ...)
# ✅ Only incremented in data_quality_checks(), not in actual error paths
```

**Impact:** Monitoring dashboard will show zeros.

---

## ✅ CORRECT ARCHITECTURE: Independent Worker

### **Recommended Structure**
```
project/
├── p2p_api/ # FastAPI web API (future)
│ ├── main.py
│ ├── binance_scraper.py
│ └── ...
│
├── worker/ # Independent worker package
│ ├── __init__.py
│ ├── config.py # Worker-specific config
│ ├── extractor.py # Extraction orchestration
│ ├── db.py # Database connection pool
│ ├── rate_limiter.py # Proper rate limiting
│ └── main.py # Worker entry point
│
├── requirements.txt
└── .env
```

**Key Principle:** Worker has ZERO dependencies on `p2p_api`. It's a standalone data pipeline.

## 🛠️ IMPLEMENTATION ROADMAP

### **Phase 1: Core Infrastructure** (Days 1-2)

#### Step 1.1: Create Independent Worker Configuration

**File:** `worker/config.py`

python

```python
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
```

**`.env` file:**

env

```env
# Database
WORKER_DATABASE_URL=postgresql://p2p_dashboard_user:4scr5XwawprE0cHtx7TJe6w8F7e994q5@dpg-d1omv9ffte5s73bhth20-a.oregon-postgres.render.com/p2p_dashboard

# Rate Limiting
WORKER_RATE_LIMIT_REQUESTS_PER_MINUTE=100

# Extraction
WORKER_EXTRACTION_INTERVAL_MINUTES=10
WORKER_MAX_WORKERS=20

# Monitoring
WORKER_LOG_LEVEL=INFO
```

#### Step 1.2: Create Database Connection Pool

**File:** `worker/db.py`

python

```python
"""
Database connection management with connection pooling.
Uses SQLAlchemy for proper connection lifecycle management.
"""
import logging
from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine, event, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import QueuePool

from .config import settings

logger = logging.getLogger(__name__)

class DatabaseManager:
 """Manages database connections with pooling and lifecycle."""
 
 def __init__(self):
 self.engine: Engine = None
 self.SessionLocal: sessionmaker = None
 self._initialize_engine()
 
 def _initialize_engine(self):
 """Create SQLAlchemy engine with connection pooling."""
 logger.info(f"Initializing database engine: {settings.database_url.split('@')[1]}")
 
 self.engine = create_engine(
 settings.database_url,
 poolclass=QueuePool,
 pool_size=settings.db_pool_size,
 max_overflow=settings.db_max_overflow,
 pool_pre_ping=True, # Verify connections before using
 pool_recycle=3600, # Recycle connections after 1 hour
 echo=False, # Set to True for SQL debugging
 )
 
 self.SessionLocal = sessionmaker(
 autocommit=False,
 autoflush=False,
 bind=self.engine,
 expire_on_commit=False
 )
 
 # Configure connection events
 self._setup_connection_events()
 
 # Test connection
 self._test_connection()
 
 def _setup_connection_events(self):
 """Configure SQLAlchemy connection event listeners."""
 
 @event.listens_for(self.engine, "connect")
 def receive_connect(dbapi_conn, connection_record):
 """Called when a new DB connection is created."""
 logger.debug("New database connection established")
 
 @event.listens_for(self.engine, "checkout")
 def receive_checkout(dbapi_conn, connection_record, connection_proxy):
 """Called when connection is retrieved from pool."""
 pass # Add custom logic if needed
 
 def _test_connection(self):
 """Verify database connectivity on startup."""
 try:
 with self.engine.connect() as conn:
 conn.execute(text("SELECT 1"))
 logger.info("Database connection test successful")
 except Exception as e:
 logger.error(f"Database connection test failed: {e}")
 raise
 
 @contextmanager
 def get_session(self) -> Generator[Session, None, None]:
 """
 Context manager for database sessions.
 
 Usage:
 with db_manager.get_session() as session:
 session.execute(...)
 session.commit()
 """
 session = self.SessionLocal()
 try:
 yield session
 session.commit()
 except Exception as e:
 session.rollback()
 logger.error(f"Database session error: {e}")
 raise
 finally:
 session.close()
 
 def close(self):
 """Close all database connections."""
 if self.engine:
 self.engine.dispose()
 logger.info("Database connections closed")

# Global database manager instance
db_manager = DatabaseManager()
```

#### Step 1.3: Implement Token Bucket Rate Limiter

**File:** `worker/rate_limiter.py`

python

```python
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
```

### **Step 1.4: Refactor Extraction Logic**

**File:** `worker/extractor.py` (Complete Rewrite)

python

```python
"""
Modular data extraction orchestrator.
Handles parallel extraction of all trading pairs from Binance P2P.
"""
import json
import logging
import uuid
import time
from datetime import datetime
from typing import List, Dict, Optional, Any
from concurrent.futures import ThreadPoolExecutor, as_completed
from decimal import Decimal

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .config import settings
from .db import db_manager
from .rate_limiter import rate_limiter

logger = logging.getLogger(__name__)

class BinanceP2PExtractor:
 """Extracts P2P trading data from Binance."""
 
 def __init__(self):
 self.base_url = settings.binance_base_url
 self.search_url = f"{self.base_url}{settings.binance_search_endpoint}"
 self.pairs_url = f"{self.base_url}{settings.binance_pairs_endpoint}"
 
 # Create session with retry strategy
 self.session = self._create_session()
 
 def _create_session(self) -> requests.Session:
 """Create requests session with retry logic."""
 session = requests.Session()
 
 retry_strategy = Retry(
 total=settings.max_retries,
 backoff_factor=1,
 status_forcelist=[429, 500, 502, 503, 504],
 allowed_methods=["POST", "GET"]
 )
 
 adapter = HTTPAdapter(max_retries=retry_strategy)
 session.mount("http://", adapter)
 session.mount("https://", adapter)
 
 return session
 
 def _get_headers(self) -> Dict[str, str]:
 """Get default headers for Binance requests."""
 return {
 "Accept": "*/*",
 "Accept-Encoding": "gzip, deflate, br",
 "Accept-Language": "en-US,en;q=0.9",
 "Cache-Control": "no-cache",
 "Connection": "keep-alive",
 "Content-Type": "application/json",
 "Origin": "https://p2p.binance.com",
 "User-Agent": (
 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
 "AppleWebKit/537.36 (KHTML, like Gecko) "
 "Chrome/120.0.0.0 Safari/537.36"
 ),
 }
 
 def get_all_trading_pairs(self) -> List[Dict[str, str]]:
 """
 Discover all available trading pairs from Binance.
 
 Returns:
 List of dicts: [{"fiat": "VES", "asset": "USDT", "trade_type": "BUY"}, ...]
 """
 logger.info("Fetching all trading pairs...")
 
 # Rate limit
 rate_limiter.acquire()
 
 try:
 response = self.session.post(
 self.pairs_url,
 json={},
 headers=self._get_headers(),
 timeout=settings.request_timeout_seconds
 )
 response.raise_for_status()
 data = response.json()
 
 if data.get("code") != "000000":
 logger.error(f"Failed to fetch pairs: {data.get('message')}")
 return []
 
 pairs = []
 for item in data.get("data", []):
 fiat = item.get("fiatUnit")
 assets = item.get("assetList", [])
 
 for asset in assets:
 pairs.append({
 "fiat": fiat,
 "asset": asset,
 "trade_type": "BUY"
 })
 pairs.append({
 "fiat": fiat,
 "asset": asset,
 "trade_type": "SELL"
 })
 
 logger.info(f"Found {len(pairs)} trading pairs")
 return pairs
 
 except Exception as e:
 logger.error(f"Error fetching trading pairs: {e}")
 return []
 
 def extract_pair_offers(
 self,
 fiat: str,
 asset: str,
 trade_type: str
 ) -> List[Dict[str, Any]]:
 """
 Extract all offers for a single trading pair.
 
 Args:
 fiat: Fiat currency code (e.g., "VES")
 asset: Crypto asset code (e.g., "USDT")
 trade_type: "BUY" or "SELL"
 
 Returns:
 List of offer dictionaries with raw data
 """
 all_offers = []
 page = 1
 
 logger.info(f"Extracting {fiat}/{asset}/{trade_type}")
 
 while page Optional[Dict[str, Any]]:
 """
 Parse raw offer data from Binance API.
 
 Returns:
 Dictionary with cleaned, typed data ready for database insertion
 """
 try:
 adv = ad["adv"]
 advertiser = ad["advertiser"]
 
 # Extract and validate numeric fields
 try:
 price = Decimal(str(adv.get("price", 0)))
 available_amount = Decimal(str(adv.get("surplusAmount", 0)))
 min_limit = Decimal(str(adv.get("minSingleTransAmount", 0)))
 max_limit = Decimal(str(adv.get("maxSingleTransAmount", 0)))
 
 if price List[Dict[str, Any]]:
 """
 Extract offers from ALL trading pairs in parallel.
 
 Returns:
 List of all offers across all pairs
 """
 # Get all trading pairs
 pairs = self.get_all_trading_pairs()
 
 if not pairs:
 logger.error("No trading pairs found")
 return []
 
 logger.info(f"Starting parallel extraction for {len(pairs)} pairs...")
 
 all_offers = []
 
 # Extract in parallel
 with ThreadPoolExecutor(max_workers=settings.max_workers) as executor:
 # Submit all extraction tasks
 future_to_pair = {
 executor.submit(
 self.extract_pair_offers,
 pair["fiat"],
 pair["asset"],
 pair["trade_type"]
 ): pair
 for pair in pairs
 }
 
 # Collect results as they complete
 for future in as_completed(future_to_pair):
 pair = future_to_pair[future]
 try:
 offers = future.result()
 all_offers.extend(offers)
 except Exception as e:
 logger.error(
 f"Extraction failed for "
 f"{pair['fiat']}/{pair['asset']}/{pair['trade_type']}: {e}"
 )
 
 logger.info(f"Total offers extracted: {len(all_offers)}")
 return all_offers

# Global extractor instance
extractor = BinanceP2PExtractor()
```

## 📋 NEXT STEPS FOR IMPLEMENTATION

1. **Create the files above** in the structure shown

2. **Install missing dependencies:**

bash

```bash
 pip install sqlalchemy psycopg2-binary pydantic-settings
```

1. **Create database schema** (run SQL from devlog.md)

2. **Create `worker/loader.py`** for database insertion (next artifact)

3. **Create `worker/main.py`** for scheduler and orchestration

Would you like me to continue with the **Loader** and **Main** implementations, or would you prefer to review and test these components first?

