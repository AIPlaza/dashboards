# P2P Data Ingestion Layer - Product Requirements Document

## Executive Summary

This document outlines the architecture, specifications, and implementation requirements for a robust, scalable P2P data extraction and ingestion system that captures comprehensive trading data from Binance P2P markets at 10-minute intervals.

---

## 1. System Architecture Overview

### 1.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     INGESTION ORCHESTRATOR                       │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐   │
│  │  Job Scheduler │→ │  Batch Manager │→ │ Error Handler  │   │
│  │   (APScheduler)│  │                │  │   & Retry      │   │
│  └────────────────┘  └────────────────┘  └────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    EXTRACTION WORKERS POOL                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │ Fiat Worker  │  │ Fiat Worker  │  │ Fiat Worker  │  ...    │
│  │   (VES/USD)  │  │   (EUR/ARS)  │  │   (COP/BRL)  │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    DATA TRANSFORMATION LAYER                     │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  Validator → Normalizer → Enricher → Deduplicator     │    │
│  └────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    POSTGRESQL DATA WAREHOUSE                     │
│                     (See Schema Section 3)                       │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2 Technology Stack

- **Orchestration**: Apache Airflow / Celery + Redis
- **Worker Queue**: RabbitMQ / Redis Queue
- **Language**: Python 3.11+
- **Database**: PostgreSQL 15+ with TimescaleDB extension
- **Caching**: Redis
- **Monitoring**: Prometheus + Grafana
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana)

---

## 2. Core Requirements

### 2.1 Functional Requirements

#### FR-1: Comprehensive Data Extraction
**Priority**: P0 (Critical)

Extract ALL available P2P data including:

**Markets Coverage:**
- All supported fiat currencies (VES, USD, EUR, ARS, COP, BRL, MXN, NGN, etc.)
- All crypto assets (USDT, BTC, ETH, BNB, BUSD, USDC, DAI, etc.)
- Both trade types: BUY and SELL
- All available pages until exhaustion

**Data Points Per Offer:**
- Offer ID (unique identifier)
- Advertiser details (nickname, completion rate, total orders, merchant status)
- Pricing information (price, min/max limits)
- Volume data (available amount, total traded)
- Payment methods (all accepted methods)
- Terms and conditions
- Order completion time statistics
- Response time metrics
- Timestamp of extraction

#### FR-2: Batch Processing Architecture
**Priority**: P0

- Execute complete extraction cycle every 10 minutes
- Implement smart pagination to capture all offers
- Process fiats in parallel with configurable worker count
- Handle rate limiting gracefully with exponential backoff
- Maximum batch execution time: 8 minutes (2 min buffer)

#### FR-3: Data Quality & Validation
**Priority**: P0

- Validate data types and ranges before insertion
- Detect and flag anomalies (price spikes, volume irregularities)
- Implement checksums for data integrity
- Track extraction completeness (expected vs. actual records)
- Maintain audit trail of all transformations

#### FR-4: Error Handling & Recovery
**Priority**: P0

- Retry failed requests up to 3 times with exponential backoff
- Log all failures with context (timestamp, params, error type)
- Continue batch even if individual fiat extraction fails
- Implement circuit breaker for external API
- Alert on consecutive failures (>3)

### 2.2 Non-Functional Requirements

#### NFR-1: Performance
- Process 50,000+ offers per 10-minute cycle
- Database write throughput: >1000 records/second
- Query response time: <500ms for time-series queries
- Worker utilization: 70-85%

#### NFR-2: Scalability
- Horizontally scalable worker pool
- Database partitioning by time (daily/weekly)
- Support for 100+ concurrent fiat extractions

#### NFR-3: Reliability
- System uptime: 99.5%
- Data completeness: 99.9%
- Zero data loss on system failure (write-ahead logging)

#### NFR-4: Observability
- Real-time metrics dashboard
- Detailed logging (DEBUG level in development, INFO in production)
- Distributed tracing for batch workflows
- Alerting on SLA violations

---

## 3. Database Schema Architecture

### 3.1 Core Tables

#### 3.1.1 Dimension Tables (Slowly Changing Dimensions)

```sql
-- D1: Cryptocurrencies
CREATE TABLE dim_cryptocurrencies (
    crypto_id SERIAL PRIMARY KEY,
    symbol VARCHAR(10) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    binance_asset_code VARCHAR(20) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_crypto_symbol ON dim_cryptocurrencies(symbol);

-- D2: Fiat Currencies
CREATE TABLE dim_fiat_currencies (
    fiat_id SERIAL PRIMARY KEY,
    currency_code CHAR(3) UNIQUE NOT NULL,
    currency_name VARCHAR(100) NOT NULL,
    country_code CHAR(2),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_fiat_code ON dim_fiat_currencies(currency_code);

-- D3: Payment Methods
CREATE TABLE dim_payment_methods (
    payment_method_id SERIAL PRIMARY KEY,
    method_code VARCHAR(50) UNIQUE NOT NULL,
    method_name VARCHAR(200) NOT NULL,
    category VARCHAR(50), -- 'bank_transfer', 'e_wallet', 'cash', etc.
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_payment_method_code ON dim_payment_methods(method_code);
CREATE INDEX idx_payment_category ON dim_payment_methods(category);

-- D4: Advertisers (SCD Type 2)
CREATE TABLE dim_advertisers (
    advertiser_sk BIGSERIAL PRIMARY KEY,
    advertiser_id VARCHAR(100) NOT NULL,
    nickname VARCHAR(200) NOT NULL,
    is_merchant BOOLEAN DEFAULT FALSE,
    registration_days INTEGER,
    effective_date TIMESTAMP NOT NULL,
    expiration_date TIMESTAMP,
    is_current BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_advertiser_id_current ON dim_advertisers(advertiser_id, is_current);
CREATE INDEX idx_advertiser_nickname ON dim_advertisers(nickname);
```

#### 3.1.2 Fact Tables (Time-Series Data)

```sql
-- F1: Offers Snapshot (Main Fact Table)
CREATE TABLE fact_offers (
    offer_id BIGSERIAL,
    offer_external_id VARCHAR(100) NOT NULL,
    batch_id UUID NOT NULL,
    extraction_timestamp TIMESTAMP NOT NULL,
    
    -- Dimensions
    crypto_id INTEGER REFERENCES dim_cryptocurrencies(crypto_id),
    fiat_id INTEGER REFERENCES dim_fiat_currencies(fiat_id),
    advertiser_sk BIGINT REFERENCES dim_advertisers(advertiser_sk),
    trade_type VARCHAR(4) NOT NULL CHECK (trade_type IN ('BUY', 'SELL')),
    
    -- Pricing Metrics
    price NUMERIC(20, 8) NOT NULL,
    price_float_rate NUMERIC(10, 4), -- Premium/discount vs. market
    
    -- Volume Metrics
    available_amount NUMERIC(20, 8) NOT NULL,
    min_limit NUMERIC(20, 8) NOT NULL,
    max_limit NUMERIC(20, 8) NOT NULL,
    tradable_quantity NUMERIC(20, 8),
    
    -- Advertiser Performance (denormalized for query performance)
    completion_rate NUMERIC(5, 2),
    total_orders_count INTEGER,
    avg_response_time_seconds INTEGER,
    avg_completion_time_minutes INTEGER,
    
    -- Metadata
    terms_conditions TEXT,
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    PRIMARY KEY (offer_id, extraction_timestamp)
);

-- Convert to hypertable for time-series optimization (TimescaleDB)
SELECT create_hypertable('fact_offers', 'extraction_timestamp', 
    chunk_time_interval => INTERVAL '1 day');

-- Indexes for common query patterns
CREATE INDEX idx_offers_batch ON fact_offers(batch_id);
CREATE INDEX idx_offers_timestamp ON fact_offers(extraction_timestamp DESC);
CREATE INDEX idx_offers_crypto_fiat ON fact_offers(crypto_id, fiat_id, trade_type);
CREATE INDEX idx_offers_advertiser ON fact_offers(advertiser_sk);
CREATE INDEX idx_offers_price_range ON fact_offers(crypto_id, fiat_id, price) 
    WHERE is_available = TRUE;

-- F2: Offer Payment Methods (Bridge Table)
CREATE TABLE fact_offer_payment_methods (
    offer_payment_id BIGSERIAL PRIMARY KEY,
    offer_id BIGINT NOT NULL,
    extraction_timestamp TIMESTAMP NOT NULL,
    payment_method_id INTEGER REFERENCES dim_payment_methods(payment_method_id),
    is_primary BOOLEAN DEFAULT FALSE,
    
    FOREIGN KEY (offer_id, extraction_timestamp) 
        REFERENCES fact_offers(offer_id, extraction_timestamp) ON DELETE CASCADE
);

CREATE INDEX idx_offer_payments ON fact_offer_payment_methods(offer_id, extraction_timestamp);
CREATE INDEX idx_payment_offers ON fact_offer_payment_methods(payment_method_id);

-- F3: Market Depth Snapshots (Aggregated)
CREATE TABLE fact_market_depth (
    depth_id BIGSERIAL,
    extraction_timestamp TIMESTAMP NOT NULL,
    crypto_id INTEGER REFERENCES dim_cryptocurrencies(crypto_id),
    fiat_id INTEGER REFERENCES dim_fiat_currencies(fiat_id),
    trade_type VARCHAR(4) NOT NULL,
    
    -- Aggregate Metrics
    total_offers_count INTEGER NOT NULL,
    total_available_volume NUMERIC(20, 8) NOT NULL,
    weighted_avg_price NUMERIC(20, 8) NOT NULL,
    min_price NUMERIC(20, 8) NOT NULL,
    max_price NUMERIC(20, 8) NOT NULL,
    price_std_dev NUMERIC(20, 8),
    
    -- Top 10 Liquidity Metrics
    top10_total_volume NUMERIC(20, 8),
    top10_avg_price NUMERIC(20, 8),
    
    -- Spread Metrics
    best_bid NUMERIC(20, 8),
    best_ask NUMERIC(20, 8),
    spread_absolute NUMERIC(20, 8),
    spread_percentage NUMERIC(10, 4),
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    PRIMARY KEY (depth_id, extraction_timestamp)
);

SELECT create_hypertable('fact_market_depth', 'extraction_timestamp',
    chunk_time_interval => INTERVAL '1 day');

CREATE INDEX idx_market_depth_pair ON fact_market_depth(crypto_id, fiat_id, trade_type);
```

#### 3.1.3 Operational Tables

```sql
-- O1: Batch Execution Tracking
CREATE TABLE ops_batch_runs (
    batch_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    batch_start_time TIMESTAMP NOT NULL,
    batch_end_time TIMESTAMP,
    status VARCHAR(20) NOT NULL CHECK (status IN (
        'running', 'completed', 'failed', 'partial'
    )),
    total_fiats_processed INTEGER,
    total_offers_extracted INTEGER,
    total_offers_inserted INTEGER,
    total_offers_updated INTEGER,
    total_errors INTEGER,
    error_summary JSONB,
    execution_time_seconds INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_batch_status ON ops_batch_runs(status, batch_start_time DESC);

-- O2: Extraction Errors Log
CREATE TABLE ops_extraction_errors (
    error_id BIGSERIAL PRIMARY KEY,
    batch_id UUID REFERENCES ops_batch_runs(batch_id),
    error_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fiat_code CHAR(3),
    crypto_symbol VARCHAR(10),
    trade_type VARCHAR(4),
    page_number INTEGER,
    error_type VARCHAR(50),
    error_message TEXT,
    stack_trace TEXT,
    retry_count INTEGER DEFAULT 0,
    is_resolved BOOLEAN DEFAULT FALSE
);

CREATE INDEX idx_errors_batch ON ops_extraction_errors(batch_id);
CREATE INDEX idx_errors_unresolved ON ops_extraction_errors(is_resolved, error_timestamp DESC);

-- O3: Data Quality Metrics
CREATE TABLE ops_data_quality (
    quality_id BIGSERIAL PRIMARY KEY,
    batch_id UUID REFERENCES ops_batch_runs(batch_id),
    check_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    metric_name VARCHAR(100) NOT NULL,
    metric_value NUMERIC(20, 4),
    threshold_value NUMERIC(20, 4),
    passed BOOLEAN NOT NULL,
    details JSONB
);

CREATE INDEX idx_quality_batch ON ops_data_quality(batch_id);
CREATE INDEX idx_quality_failed ON ops_data_quality(passed, check_timestamp DESC) 
    WHERE passed = FALSE;
```

### 3.2 Views for Common Queries

```sql
-- V1: Latest Market State
CREATE MATERIALIZED VIEW mv_latest_market_state AS
SELECT DISTINCT ON (fo.crypto_id, fo.fiat_id, fo.trade_type, fo.advertiser_sk)
    fo.offer_external_id,
    dc.symbol AS crypto_symbol,
    df.currency_code AS fiat_code,
    fo.trade_type,
    da.nickname AS advertiser,
    da.is_merchant,
    fo.price,
    fo.available_amount,
    fo.min_limit,
    fo.max_limit,
    fo.completion_rate,
    fo.total_orders_count,
    fo.extraction_timestamp,
    ARRAY_AGG(dpm.method_name) AS payment_methods
FROM fact_offers fo
JOIN dim_cryptocurrencies dc ON fo.crypto_id = dc.crypto_id
JOIN dim_fiat_currencies df ON fo.fiat_id = df.fiat_id
JOIN dim_advertisers da ON fo.advertiser_sk = da.advertiser_sk
LEFT JOIN fact_offer_payment_methods fopm 
    ON fo.offer_id = fopm.offer_id 
    AND fo.extraction_timestamp = fopm.extraction_timestamp
LEFT JOIN dim_payment_methods dpm ON fopm.payment_method_id = dpm.payment_method_id
WHERE fo.extraction_timestamp > NOW() - INTERVAL '15 minutes'
    AND fo.is_available = TRUE
GROUP BY fo.offer_external_id, dc.symbol, df.currency_code, fo.trade_type,
    da.nickname, da.is_merchant, fo.price, fo.available_amount, fo.min_limit,
    fo.max_limit, fo.completion_rate, fo.total_orders_count, fo.extraction_timestamp,
    fo.crypto_id, fo.fiat_id, fo.advertiser_sk
ORDER BY fo.crypto_id, fo.fiat_id, fo.trade_type, fo.advertiser_sk, 
    fo.extraction_timestamp DESC;

CREATE INDEX idx_mv_latest_pair ON mv_latest_market_state(crypto_symbol, fiat_code);

-- V2: Price History Time-Series
CREATE VIEW v_price_history AS
SELECT 
    dc.symbol AS crypto_symbol,
    df.currency_code AS fiat_code,
    fo.trade_type,
    DATE_TRUNC('minute', fo.extraction_timestamp) AS time_bucket,
    AVG(fo.price) AS avg_price,
    MIN(fo.price) AS min_price,
    MAX(fo.price) AS max_price,
    STDDEV(fo.price) AS price_volatility,
    SUM(fo.available_amount) AS total_volume,
    COUNT(*) AS offer_count
FROM fact_offers fo
JOIN dim_cryptocurrencies dc ON fo.crypto_id = dc.crypto_id
JOIN dim_fiat_currencies df ON fo.fiat_id = df.fiat_id
WHERE fo.is_available = TRUE
GROUP BY dc.symbol, df.currency_code, fo.trade_type, 
    DATE_TRUNC('minute', fo.extraction_timestamp);
```

---

## 4. Extraction Bot Architecture

### 4.1 Component Structure

```
p2p_ingestion_bot/
├── config/
│   ├── __init__.py
│   ├── settings.py              # Configuration management
│   └── logging_config.py        # Logging setup
├── core/
│   ├── __init__.py
│   ├── orchestrator.py          # Main batch coordinator
│   ├── scheduler.py             # Job scheduling logic
│   └── worker_pool.py           # Worker management
├── extractors/
│   ├── __init__.py
│   ├── base_extractor.py        # Abstract base class
│   ├── binance_extractor.py    # Binance-specific logic
│   └── rate_limiter.py          # Rate limiting utilities
├── transformers/
│   ├── __init__.py
│   ├── validator.py             # Data validation
│   ├── normalizer.py            # Data normalization
│   ├── enricher.py              # Data enrichment
│   └── deduplicator.py          # Duplicate detection
├── loaders/
│   ├── __init__.py
│   ├── db_loader.py             # Database insertion logic
│   └── bulk_inserter.py         # Optimized bulk operations
├── monitoring/
│   ├── __init__.py
│   ├── metrics.py               # Prometheus metrics
│   └── health_check.py          # Health check endpoint
├── utils/
│   ├── __init__.py
│   ├── retry.py                 # Retry decorators
│   ├── circuit_breaker.py       # Circuit breaker pattern
│   └── helpers.py               # General utilities
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── main.py                       # Application entry point
├── requirements.txt
└── docker-compose.yml
```

### 4.2 Core Implementation Specifications

#### 4.2.1 Orchestrator (Pseudocode Logic)

```python
class IngestionOrchestrator:
    """
    Main coordinator for batch extraction process.
    Manages worker pool, error handling, and batch lifecycle.
    """
    
    def execute_batch(self):
        """
        Execute one complete extraction cycle (10-minute batch).
        
        Steps:
        1. Initialize batch tracking
        2. Discover all active trading pairs
        3. Distribute extraction tasks to workers
        4. Monitor progress and handle errors
        5. Aggregate results and compute metrics
        6. Finalize batch and trigger alerts
        """
        
        batch_id = create_batch_run()
        
        try:
            # Discovery Phase
            trading_pairs = discover_all_trading_pairs()
            # Returns: [(VES, USDT, BUY), (VES, USDT, SELL), ...]
            
            # Extraction Phase (Parallel)
            with ThreadPoolExecutor(max_workers=20) as executor:
                futures = [
                    executor.submit(extract_pair_data, pair, batch_id)
                    for pair in trading_pairs
                ]
                
                results = []
                for future in as_completed(futures):
                    try:
                        result = future.result(timeout=120)
                        results.append(result)
                    except Exception as e:
                        log_error(batch_id, e)
                        continue
            
            # Transformation & Loading Phase
            transformed_data = transform_pipeline(results)
            load_to_database(transformed_data, batch_id)
            
            # Aggregation Phase
            compute_market_depth_metrics(batch_id)
            
            # Finalization
            finalize_batch_run(batch_id, status='completed')
            refresh_materialized_views()
            
        except Exception as e:
            finalize_batch_run(batch_id, status='failed', error=str(e))
            raise
```

#### 4.2.2 Extractor Specifications

```python
class BinanceP2PExtractor:
    """
    Handles extraction from Binance P2P API with pagination,
    rate limiting, and error recovery.
    """
    
    # Configuration
    BASE_URL = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"
    RATE_LIMIT = 100  # requests per minute
    MAX_RETRIES = 3
    TIMEOUT = 30  # seconds
    
    def extract_all_offers(self, fiat: str, crypto: str, trade_type: str, batch_id: UUID):
        """
        Extract ALL offers for a given trading pair across all pages.
        
        Implements:
        - Smart pagination (continues until no more data)
        - Rate limiting with token bucket algorithm
        - Exponential backoff on failures
        - Request deduplication
        - Partial success handling
        """
        
        page = 1
        all_offers = []
        consecutive_errors = 0
        
        while True:
            # Rate limiting
            await rate_limiter.acquire()
            
            try:
                offers = fetch_page(fiat, crypto, trade_type, page)
                
                if not offers or len(offers) == 0:
                    break  # No more data
                
                all_offers.extend(offers)
                consecutive_errors = 0
                page += 1
                
            except RateLimitException:
                sleep_duration = calculate_backoff(consecutive_errors)
                await asyncio.sleep(sleep_duration)
                consecutive_errors += 1
                
            except APIException as e:
                log_extraction_error(batch_id, fiat, crypto, page, e)
                
                if consecutive_errors >= self.MAX_RETRIES:
                    break  # Give up on this pair
                
                consecutive_errors += 1
                continue
        
        return all_offers
    
    def fetch_page(self, fiat, crypto, trade_type, page, rows=20):
        """
        Fetch a single page of offers.
        """
        payload = {
            "fiat": fiat,
            "asset": crypto,
            "tradeType": trade_type,
            "page": page,
            "rows": rows,
            "proMerchantAds": False,
            "publisherType": None,
            "payTypes": [],
            "countries": []
        }
        
        response = requests.post(
            self.BASE_URL,
            json=payload,
            headers=self._get_headers(),
            timeout=self.TIMEOUT
        )
        
        response.raise_for_status()
        data = response.json()
        
        return self._parse_response(data)
```

#### 4.2.3 Transformation Pipeline

```python
class DataTransformationPipeline:
    """
    Multi-stage pipeline for data validation, normalization,
    enrichment, and deduplication.
    """
    
    def transform(self, raw_offers: List[Dict]) -> List[OfferRecord]:
        """
        Execute full transformation pipeline.
        
        Stages:
        1. Validation - Ensure data integrity
        2. Normalization - Standardize formats
        3. Enrichment - Add computed fields
        4. Deduplication - Remove duplicates
        """
        
        validated = [self.validate(offer) for offer in raw_offers]
        normalized = [self.normalize(offer) for offer in validated if offer]
        enriched = [self.enrich(offer) for offer in normalized]
        deduplicated = self.deduplicate(enriched)
        
        return deduplicated
    
    def validate(self, offer: Dict) -> Optional[Dict]:
        """
        Validate offer data against business rules.
        
        Checks:
        - Required fields present
        - Numeric fields in valid ranges
        - Enum fields have valid values
        - Price is positive
        - Limits are logical (min < max)
        """
        
        required_fields = ['adv', 'advertiser']
        if not all(field in offer for field in required_fields):
            return None
        
        adv = offer['adv']
        
        # Price validation
        try:
            price = float(adv['price'])
            if price <= 0:
                return None
        except (ValueError, KeyError):
            return None
        
        # Volume validation
        try:
            available = float(adv['surplusAmount'])
            min_limit = float(adv['minSingleTransAmount'])
            max_limit = float(adv['maxSingleTransAmount'])
            
            if available < 0 or min_limit < 0 or max_limit < 0:
                return None
            if min_limit > max_limit:
                return None
        except (ValueError, KeyError):
            return None
        
        return offer
    
    def normalize(self, offer: Dict) -> Dict:
        """
        Standardize data formats.
        
        Normalizations:
        - Convert all numeric strings to proper types
        - Standardize payment method names
        - Convert timestamps to UTC
        - Trim whitespace from strings
        """
        
        normalized = {
            'external_id': offer['adv']['advNo'],
            'advertiser_id': offer['advertiser']['userNo'],
            'advertiser_nickname': offer['advertiser']['nickName'].strip(),
            'is_merchant': offer['advertiser'].get('isMerchant', False),
            'price': Decimal(offer['adv']['price']),
            'available_amount': Decimal(offer['adv']['surplusAmount']),
            'min_limit': Decimal(offer['adv']['minSingleTransAmount']),
            'max_limit': Decimal(offer['adv']['maxSingleTransAmount']),
            'completion_rate': float(offer['advertiser'].get('monthFinishRate', 0)),
            'total_orders': int(offer['advertiser'].get('monthOrderCount', 0)),
            'payment_methods': self._normalize_payment_methods(
                offer['adv'].get('tradeMethods', [])
            )
        }
        
        return normalized
    
    def enrich(self, offer: Dict) -> Dict:
        """
        Add computed/derived fields.
        
        Enrichments:
        - Calculate effective spread
        - Compute liquidity score
        - Add market rank
        - Flag suspicious patterns
        """
        
        offer['liquidity_score'] = self._calculate_liquidity_score(
            offer['available_amount'],
            offer['completion_rate'],
            offer['total_orders']
        )
        
        offer['trust_score'] = self._calculate_trust_score(
            offer['completion_rate'],
            offer['total_orders'],
            offer['is_merchant']
        )
        
        return offer
```

#### 4.2.4 Database Loader

```python
class BulkDatabaseLoader:
    """
    Optimized database loading with batch inserts and UPSERT logic.
    """
    
    BATCH_SIZE = 1000  # Records per insert
    
    def load_offers(self, offers: List[OfferRecord], batch_id: UUID):
        """
        Load offers to database using optimized bulk insert.
        
        Strategy:
        - Use COPY command for maximum throughput
        - Implement UPSERT for idempotency
        - Maintain referential integrity
        - Update dimensions incrementally
        """
        
        with self.db.begin():
            # Upsert dimensions first
            self._upsert_advertisers(offers)
            self._upsert_payment_methods(offers)
            
            # Prepare fact records
            fact_records = self._prepare_fact_records(offers, batch_id)
            
            # Bulk insert using COPY
            self._bulk_insert_offers(fact_records)
            self._bulk_insert_payment_method_associations(offers, batch_id)
            
            # Update aggregates
            self._update_market_depth(batch_id)
    
    def _bulk_insert_offers(self, records: List[Dict]):
        """
        Use PostgreSQL COPY for maximum insert performance.
        """
        
        # Create temporary CSV buffer
        buffer = StringIO()
        writer = csv.writer(buffer)
        
        for record in records:
            writer.writerow([
                record['offer_external_id'],
                record['batch_id'],
                record['extraction_timestamp'],
                record['crypto_id'],
                record['fiat_id'],
                record['advertiser_sk'],
                record['trade_type'],
                record['price'],
                record['available_amount'],
                # ... all fields
            ])
        
        buffer.seek(0)
        
        # Execute COPY
        cursor = self.db.cursor()
        cursor.copy_from(
            buffer,
            'fact_offers',
            sep=',',
            columns=[...list of all columns...]
        )
```

---

## 5. Operational

5. Operational Requirements
5.1 Scheduling & Execution
python# Scheduler Configuration
SCHEDULER_CONFIG = {
    'trigger': 'interval',
    'minutes': 10,
    'max_instances': 1,  # Prevent overlapping runs
    'coalesce': True,    # Merge missed runs
    'misfire_grace_time': 120  # 2 minutes grace period
}

# Execution SLAs
SLA_TARGETS = {
    'batch_duration_max': 480,  # 8 minutes
    'extraction_timeout_per_pair': 60,  # 1 minute
    'database_load_max': 120,  # 2 minutes
    'completeness_threshold': 0.995  # 99.5% of expected pairs
}
5.2 Rate Limiting Strategy
pythonclass AdaptiveRateLimiter:
    """
    Intelligent rate limiter that adapts to API responses.
    
    Features:
    - Token bucket algorithm
    - Dynamic rate adjustment based on 429 responses
    - Priority queue for critical extractions
    - Circuit breaker integration
    """
    
    INITIAL_RATE = 100  # requests/minute
    MIN_RATE = 10
    MAX_RATE = 200
    
    def __init__(self):
        self.current_rate = self.INITIAL_RATE
        self.bucket_tokens = self.INITIAL_RATE
        self.last_refill = time.time()
        self.consecutive_429s = 0
    
    async def acquire(self, priority: int = 5):
        """
        Acquire permission to make a request.
        Higher priority gets preferential treatment.
        """
        
        # Refill bucket
        self._refill_bucket()
        
        # Wait if no tokens available
        while self.bucket_tokens < 1:
            await asyncio.sleep(0.1)
            self._refill_bucket()
        
        self.bucket_tokens -= 1
    
    def on_rate_limit_hit(self):
        """
        Called when 429 response received.
        Reduces rate by 50% and enables backoff.
        """
        self.consecutive_429s += 1
        self.current_rate = max(
            self.MIN_RATE,
            self.current_rate * 0.5
        )
        
        logger.warning(
            f"Rate limit hit. Reducing to {self.current_rate} req/min"
        )
    
    def on_success(self):
        """
        Called on successful request.
        Gradually increases rate if stable.
        """
        self.consecutive_429s = 0
        
        # Increase rate by 10% every 100 successful requests
        if random.random() < 0.01:
            self.current_rate = min(
                self.MAX_RATE,
                self.current_rate * 1.1
            )
5.3 Error Handling Matrix
Error TypeDetectionActionRetryAlertNetwork TimeoutRequest timeout (30s)Retry with backoff3xAfter 3 failuresRate Limit (429)HTTP 429 responseReduce rate, backoffIndefiniteAfter 10 consecutiveInvalid ResponseJSON parse errorLog, skip record1xAfter 10 in batchDatabase ConnectionConnection errorReconnect pool3xImmediateData ValidationSchema mismatchLog, quarantine0xAfter 100 in batchAPI Structure ChangeMissing expected fieldAlert, fallback parser0xImmediateDuplicate KeyDB unique constraintUpdate instead0xNoneDisk FullWrite failureStop batch, alert0xImmediate
5.4 Monitoring & Alerting
5.4.1 Key Performance Indicators
python# Prometheus Metrics
METRICS = {
    'batch_duration_seconds': Histogram(
        'p2p_batch_duration_seconds',
        'Time taken for complete batch execution',
        buckets=[60, 120, 240, 480, 600]
    ),
    
    'offers_extracted_total': Counter(
        'p2p_offers_extracted_total',
        'Total offers extracted',
        ['fiat', 'crypto', 'trade_type']
    ),
    
    'extraction_errors_total': Counter(
        'p2p_extraction_errors_total',
        'Total extraction errors',
        ['error_type', 'fiat', 'crypto']
    ),
    
    'api_request_duration_seconds': Histogram(
        'p2p_api_request_duration_seconds',
        'API request latency',
        buckets=[0.1, 0.5, 1.0, 2.0, 5.0, 10.0]
    ),
    
    'database_write_duration_seconds': Histogram(
        'p2p_db_write_duration_seconds',
        'Database write operation duration'
    ),
    
    'data_completeness_ratio': Gauge(
        'p2p_data_completeness_ratio',
        'Ratio of successfully extracted pairs vs expected'
    ),
    
    'active_workers': Gauge(
        'p2p_active_workers',
        'Number of active extraction workers'
    )
}
5.4.2 Alert Rules
yaml# alerts.yml
groups:
  - name: p2p_ingestion
    interval: 1m
    rules:
      # Critical Alerts
      - alert: BatchExecutionFailed
        expr: p2p_batch_status{status="failed"} > 0
        for: 1m
        severity: critical
        annotations:
          summary: "Batch execution failed"
          
      - alert: DataCompletenessLow
        expr: p2p_data_completeness_ratio < 0.95
        for: 5m
        severity: critical
        annotations:
          summary: "Data completeness below 95%"
          
      - alert: DatabaseWriteErrors
        expr: rate(p2p_db_write_errors_total[5m]) > 10
        severity: critical
        
      # Warning Alerts
      - alert: BatchDurationHigh
        expr: p2p_batch_duration_seconds > 480
        for: 2m
        severity: warning
        annotations:
          summary: "Batch taking longer than 8 minutes"
          
      - alert: HighErrorRate
        expr: rate(p2p_extraction_errors_total[10m]) > 50
        severity: warning
        
      - alert: APILatencyHigh
        expr: histogram_quantile(0.95, p2p_api_request_duration_seconds) > 5
        for: 5m
        severity: warning
5.5 Data Quality Checks
pythonclass DataQualityChecker:
    """
    Automated data quality validation suite.
    """
    
    def run_quality_checks(self, batch_id: UUID):
        """
        Execute all quality checks and record results.
        """
        
        checks = [
            self.check_completeness,
            self.check_price_anomalies,
            self.check_volume_consistency,
            self.check_duplicates,
            self.check_temporal_consistency,
            self.check_referential_integrity
        ]
        
        results = []
        for check in checks:
            result = check(batch_id)
            results.append(result)
            self._record_quality_metric(batch_id, result)
        
        return results
    
    def check_completeness(self, batch_id: UUID) -> QualityCheckResult:
        """
        Verify expected number of trading pairs were extracted.
        """
        
        expected_pairs = self._get_expected_pairs_count()
        actual_pairs = self._get_actual_pairs_count(batch_id)
        
        completeness_ratio = actual_pairs / expected_pairs
        
        return QualityCheckResult(
            name='completeness',
            passed=completeness_ratio >= 0.995,
            metric_value=completeness_ratio,
            threshold=0.995,
            details={
                'expected': expected_pairs,
                'actual': actual_pairs,
                'missing_pairs': self._identify_missing_pairs(batch_id)
            }
        )
    
    def check_price_anomalies(self, batch_id: UUID) -> QualityCheckResult:
        """
        Detect unusual price movements (>20% from moving average).
        """
        
        query = """
        WITH price_stats AS (
            SELECT 
                crypto_id,
                fiat_id,
                trade_type,
                price,
                AVG(price) OVER (
                    PARTITION BY crypto_id, fiat_id, trade_type
                    ORDER BY extraction_timestamp
                    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
                ) as avg_price_7periods
            FROM fact_offers
            WHERE extraction_timestamp > NOW() - INTERVAL '1 hour'
        )
        SELECT COUNT(*) as anomaly_count
        FROM price_stats
        WHERE ABS(price - avg_price_7periods) / avg_price_7periods > 0.20
        """
        
        anomaly_count = self.db.execute(query).scalar()
        
        return QualityCheckResult(
            name='price_anomalies',
            passed=anomaly_count < 10,
            metric_value=anomaly_count,
            threshold=10
        )
    
    def check_volume_consistency(self, batch_id: UUID) -> QualityCheckResult:
        """
        Verify total market volume hasn't dropped dramatically.
        """
        
        current_volume = self._get_total_volume(batch_id)
        avg_volume_last_day = self._get_avg_volume_last_24h()
        
        drop_percentage = (avg_volume_last_day - current_volume) / avg_volume_last_day
        
        return QualityCheckResult(
            name='volume_consistency',
            passed=drop_percentage < 0.50,  # Max 50% drop
            metric_value=drop_percentage,
            threshold=0.50
        )

6. Implementation Phases
Phase 1: Core Infrastructure (Weeks 1-2)
Deliverables:

Database schema implemented and tested
Basic extraction bot with single-threaded execution
Simple scheduler (cron-based)
Logging infrastructure

Success Criteria:

Successfully extract and store data for 5 fiat currencies
Database can handle 10,000 inserts without performance degradation
Zero data loss during normal operation

Phase 2: Parallelization & Scale (Weeks 3-4)
Deliverables:

Multi-threaded worker pool
Rate limiting implementation
Error recovery mechanisms
All dimension tables populated

Success Criteria:

Extract all trading pairs within 8-minute window
Handle rate limiting gracefully (no 429 errors block execution)
99.5% data completeness

Phase 3: Quality & Monitoring (Week 5)
Deliverables:

Data quality checks
Prometheus metrics
Grafana dashboards
Alert system integration

Success Criteria:

All quality checks passing
Real-time visibility into extraction process
Alerts fire within 1 minute of issue

Phase 4: Optimization & Hardening (Week 6)
Deliverables:

Database query optimization
Materialized views with refresh strategy
Circuit breaker implementation
Comprehensive testing suite

Success Criteria:

Query response time <500ms for 95th percentile
System recovers automatically from transient failures
95% test coverage


7. Configuration Management
python# config/settings.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str
    DB_POOL_SIZE: int = 20
    DB_MAX_OVERFLOW: int = 10
    
    # Extraction
    EXTRACTION_INTERVAL_MINUTES: int = 10
    MAX_WORKERS: int = 20
    REQUEST_TIMEOUT_SECONDS: int = 30
    MAX_RETRIES: int = 3
    
    # Rate Limiting
    INITIAL_RATE_LIMIT: int = 100  # req/min
    RATE_LIMIT_BACKOFF_FACTOR: float = 0.5
    
    # Binance API
    BINANCE_BASE_URL: str = "https://p2p.binance.com"
    BINANCE_SEARCH_ENDPOINT: str = "/bapi/c2c/v2/friendly/c2c/adv/search"
    BINANCE_PAIRS_ENDPOINT: str = "/bapi/c2c/v2/public/c2c/asset-order/getAllSupportAsset"
    
    # Monitoring
    PROMETHEUS_PORT: int = 9090
    ENABLE_METRICS: bool = True
    LOG_LEVEL: str = "INFO"
    
    # Alerting
    SLACK_WEBHOOK_URL: str = ""
    PAGERDUTY_API_KEY: str = ""
    ALERT_ON_FAILURES: bool = True
    
    # Data Quality
    COMPLETENESS_THRESHOLD: float = 0.995
    PRICE_ANOMALY_THRESHOLD: float = 0.20
    VOLUME_DROP_THRESHOLD: float = 0.50
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

8. Testing Strategy
8.1 Unit Tests

Test each extractor method independently
Mock external API calls
Validate transformation logic
Test error handling paths

8.2 Integration Tests

Test database operations with test database
Test worker pool coordination
Test rate limiter behavior
Test end-to-end data flow

8.3 Load Tests

Simulate 50+ concurrent extractions
Test database write throughput (target: 1000/sec)
Verify memory usage under load
Test recovery from system overload

8.4 Chaos Engineering

Random worker failures
Database connection drops
Network timeouts
API rate limit responses


9. Deployment Strategy
yaml# docker-compose.yml
version: '3.8'

services:
  postgres:
    image: timescale/timescaledb:latest-pg15
    environment:
      POSTGRES_DB: p2p_data_warehouse
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./schema:/docker-entrypoint-initdb.d
    ports:
      - "5432:5432"
    command: postgres -c max_connections=200 -c shared_buffers=2GB
  
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
  
  ingestion_bot:
    build: .
    depends_on:
      - postgres
      - redis
    environment:
      DATABASE_URL: postgresql://${DB_USER}:${DB_PASSWORD}@postgres:5432/p2p_data_warehouse
      REDIS_URL: redis://redis:6379
    volumes:
      - ./logs:/app/logs
    restart: unless-stopped
  
  prometheus:
    image: prom/prometheus:latest
    volumes:
      - ./monitoring/prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    ports:
      - "9090:9090"
  
  grafana:
    image: grafana/grafana:latest
    depends_on:
      - prometheus
    volumes:
      - grafana_data:/var/lib/grafana
      - ./monitoring/dashboards:/etc/grafana/provisioning/dashboards
    ports:
      - "3000:3000"

volumes:
  postgres_data:
  prometheus_data:
  grafana_data:

10. Success Metrics
10.1 Operational Metrics

Uptime: 99.5% system availability
Data Completeness: 99.9% of expected trading pairs captured
Latency: 95th percentile batch completion <480 seconds
Error Rate: <0.5% of extraction attempts fail

10.2 Data Quality Metrics

Accuracy: 100% of loaded records pass validation
Freshness: Data delay <10 minutes from real-time
Consistency: Zero referential integrity violations
Uniqueness: Zero duplicate offers in same batch

10.3 Business Metrics

Coverage: 100% of Binance P2P trading pairs
Historical Depth: 30+ days of continuous data
Query Performance: <500ms for 95% of analytical queries


11. Risk Mitigation
RiskImpactProbabilityMitigationBinance API changesHighMediumVersioned extractors, automated structure detection, alertsRate limiting blocks extractionHighMediumAdaptive rate limiter, distributed IPs, backoff strategyDatabase performance degradationHighLowPartitioning, indexes, query optimization, monitoringData loss during failureCriticalLowWAL, replication, backup strategy, idempotent operationsMemory overflow on large batchesMediumMediumStreaming processing, memory limits, chunkingScheduler drift/overlapMediumLowSingle instance enforcement, coalescing, SLA monitoring

12. Future Enhancements (Post-MVP)

Machine Learning Integration

Predictive models for market movements
Anomaly detection using ML
Price forecasting


Multi-Exchange Support

Bybit P2P integration
Paxful data
LocalBitcoins (if available)


Real-Time Streaming

WebSocket connections for live updates
Apache Kafka for event streaming
Sub-second data freshness


Advanced Analytics

Arbitrage opportunity detection
Merchant reputation scoring
Market maker identification




Appendix A: Sample Queries
sql-- Q1: Current best prices for VES/USDT
SELECT 
    trade_type,
    MIN(price) as best_price,
    SUM(available_amount) as total_liquidity
FROM mv_latest_market_state
WHERE fiat_code = 'VES' 
    AND crypto_symbol = 'USDT'
GROUP BY trade_type;

-- Q2: Top 10 merchants by volume (last 24h)
SELECT 
    advertiser,
    SUM(available_amount) as total_volume,
    AVG(completion_rate) as avg_completion_rate,
    COUNT(DISTINCT offer_external_id) as offer_count
FROM fact_offers fo
JOIN dim_advertisers da ON fo.advertiser_sk = da.advertiser_sk
WHERE extraction_timestamp > NOW() - INTERVAL '24 hours'
    AND da.is_merchant = TRUE
GROUP BY advertiser
ORDER BY total_volume DESC
LIMIT 10;

-- Q3: Price volatility by payment method
SELECT 
    dpm.method_name,
    STDDEV(fo.price) as price_volatility,
    AVG(fo.price) as avg_price
FROM fact_offers fo
JOIN fact_offer_payment_methods fopm 
    ON fo.offer_id = fopm.offer_id
JOIN dim_payment_methods dpm 
    ON fopm.payment_method_id = dpm.payment_method_id
WHERE fo.fiat_id = (SELECT fiat_id FROM dim_fiat_currencies WHERE currency_code = 'VES')
    AND fo.crypto_id = (SELECT crypto_id FROM dim_cryptocurrencies WHERE symbol = 'USDT')
    AND fo.extraction_timestamp > NOW() - INTERVAL '24 hours'
GROUP BY dpm.method_name
ORDER BY price_volatility DESC;

# Backend Architecture Audit & Bot Integration Guide

## 🔴 CRITICAL ISSUES IDENTIFIED

### Issue 1: Data Format Mismatch
**Location:** `p2p_api/binance_scraper.py:109-121`

**Current Implementation:**
```python
offer_details = {
    "advertiser": advertiser.get("nickName"),
    "price": f"{price} {data['fiat']}",        # ❌ String format
    "available": f"{available} {data['asset']}", # ❌ String format
    "limits": f"{adv.get('minSingleTransAmount')} - {adv.get('maxSingleTransAmount')} {data['fiat']}", # ❌ String format
    "payment_methods": [...]
}
```

**Problem:** Bot needs `NUMERIC(20,8)` but gets `"40.00 VES"` strings.

**Impact:** Your ingestion bot would need to:
1. Parse strings back to decimals
2. Extract fiat/asset from formatted strings
3. Split limit ranges
4. Handle parsing errors

**Severity:** 🔴 BLOCKER for bot development

---

### Issue 2: Missing Advertiser Metadata
**Location:** `p2p_api/binance_scraper.py`

**Currently NOT Captured:**
- `completion_rate` (advertiser.monthFinishRate)
- `total_orders` (advertiser.monthOrderCount)  
- `is_merchant` (advertiser.isMerchant)
- `response_time` statistics
- `registration_days`

**Required by Database Schema:**
```sql
-- Your PRD database expects:
completion_rate NUMERIC(5, 2)
total_orders_count INTEGER
avg_response_time_seconds INTEGER
```

**Severity:** 🟡 HIGH - Missing business-critical data

---

### Issue 3: No Pagination Support for Bulk Extraction
**Location:** `p2p_api/binance_scraper.py:156-188`

**Current Function:** `scrape_all_binance_offers()` exists but:
- ❌ Not exposed via API endpoint
- ❌ Uses same formatted string output
- ❌ No progress tracking
- ❌ No batch_id correlation

**What Bot Needs:**
- Endpoint that returns ALL pages for a given pair
- Raw numeric data
- Batch tracking ID
- Error recovery for partial failures

**Severity:** 🟡 HIGH - Bot would need to manually paginate

---

### Issue 4: Rate Limiting Not Coordinated
**Location:** `p2p_api/binance_scraper.py:40-56`

**Current:** Each API call hits Binance independently
**Problem:** Bot making 100+ parallel requests will trigger rate limits

**What's Missing:**
- Centralized rate limiter
- Request queue
- Backoff strategy shared between API and bot
- Circuit breaker pattern

**Severity:** 🟡 MEDIUM - Bot might get IP banned

---

## ✅ RECOMMENDED SOLUTION: INTERNAL BULK ENDPOINT

### Phase 1: Create Raw Data Scraper (Week 1)

**New File:** `p2p_api/binance_scraper_raw.py`

```python
"""
Raw data scraper for internal bulk extraction.
Returns unformatted numeric data suitable for database insertion.
"""
import logging
from typing import Dict, List, Optional
from decimal import Decimal
from .config import Settings

logger = logging.getLogger(__name__)
settings = Settings()

def get_binance_offers_raw(
    fiat: str,
    asset: str, 
    tradeType: str,
    page: int = 1,
    rows: int = 20
) -> List[Dict]:
    """
    Fetch raw offer data with numeric types preserved.
    
    Returns:
        List of dicts with structure:
        {
            "offer_id": "12345...",
            "advertiser_id": "abc123",
            "advertiser_nickname": "TradeMaster",
            "is_merchant": True,
            "price": Decimal("40.15"),
            "available_amount": Decimal("5000.00"),
            "min_limit": Decimal("100.00"),
            "max_limit": Decimal("10000.00"),
            "completion_rate": Decimal("98.5"),
            "total_orders": 1247,
            "avg_response_time_seconds": 45,
            "trade_methods": ["BankTransfer", "Zelle"],
            "fiat": "VES",
            "asset": "USDT",
            "trade_type": "BUY"
        }
    """
    url = settings.binance_p2p_search_url
    payload = {
        "proMerchantAds": False,
        "page": page,
        "rows": rows,
        "payTypes": [],
        "countries": [],
        "tradeType": tradeType,
        "asset": asset,
        "fiat": fiat,
        "publisherType": None,
    }
    
    response_data = _make_binance_request(url, payload)
    
    if not response_data or not response_data.get("data"):
        return []
    
    offers = []
    for ad in response_data["data"]:
        try:
            adv = ad["adv"]
            advertiser = ad["advertiser"]
            
            offer = {
                # Core identifiers
                "offer_id": adv.get("advNo"),
                "advertiser_id": advertiser.get("userNo"),
                "advertiser_nickname": advertiser.get("nickName"),
                "is_merchant": advertiser.get("isMerchant", False),
                
                # Pricing (keep as Decimal for precision)
                "price": Decimal(str(adv.get("price"))),
                "available_amount": Decimal(str(adv.get("surplusAmount"))),
                "min_limit": Decimal(str(adv.get("minSingleTransAmount"))),
                "max_limit": Decimal(str(adv.get("maxSingleTransAmount"))),
                "tradable_quantity": Decimal(str(adv.get("tradableQuantity", 0))),
                
                # Advertiser metrics
                "completion_rate": Decimal(str(advertiser.get("monthFinishRate", 0))),
                "total_orders": int(advertiser.get("monthOrderCount", 0)),
                
                # Payment methods
                "trade_methods": [
                    method.get("payType") 
                    for method in adv.get("tradeMethods", [])
                ],
                
                # Context
                "fiat": fiat,
                "asset": asset,
                "trade_type": tradeType,
                
                # Additional fields
                "terms_conditions": adv.get("dynamicMaxSingleTransAmount"),
                "price_float_rate": Decimal(str(adv.get("priceFloatingRatio", 0)))
            }
            
            offers.append(offer)
            
        except (ValueError, KeyError, TypeError) as e:
            logger.warning(f"Skipping malformed offer: {e}", extra={"ad": ad})
            continue
    
    return offers


def scrape_all_offers_raw(
    fiat: str,
    asset: str,
    tradeType: str,
    max_pages: int = 50  # Binance typically has 20-30 pages per pair
) -> List[Dict]:
    """
    Scrape ALL pages for a given trading pair.
    Designed for batch ingestion bot.
    """
    all_offers = []
    
    for page in range(1, max_pages + 1):
        logger.info(f"Fetching {fiat}/{asset}/{tradeType} page {page}")
        
        page_offers = get_binance_offers_raw(fiat, asset, tradeType, page)
        
        if not page_offers:
            logger.info(f"No more offers at page {page}. Total: {len(all_offers)}")
            break
        
        all_offers.extend(page_offers)
    
    return all_offers
```

---

### Phase 2: Create Internal Bulk Endpoint (Week 1)

**New File:** `p2p_api/routers/internal.py`

```python
"""
Internal endpoints for batch ingestion bot.
These endpoints are NOT exposed to public API documentation.
"""
from typing import List, Dict
from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session

from .. import auth
from ..binance_scraper_raw import get_binance_offers_raw, scrape_all_offers_raw
from ..dependencies import get_db
from ..config import Settings

router = APIRouter(
    prefix="/internal",
    tags=["Internal"],
    include_in_schema=False  # Hide from public docs
)

settings = Settings()


async def verify_service_account_key(
    x_service_key: str = Header(...),
    db: Session = Depends(get_db)
):
    """
    Verify service account API key.
    Bot should use a dedicated API key with 'service_account' name.
    """
    # Reuse existing API key validation
    if "_" not in x_service_key:
        raise HTTPException(status_code=401, detail="Invalid service key format")
    
    prefix, _, secret = x_service_key.rpartition("_")
    db_key = auth.get_api_key_by_prefix(db, prefix=prefix)
    
    if not db_key or not db_key.is_active:
        raise HTTPException(status_code=401, detail="Invalid service key")
    
    # Verify it's a service account key
    if not db_key.name.startswith("ingestion_bot"):
        raise HTTPException(
            status_code=403, 
            detail="This endpoint requires service account credentials"
        )
    
    if not auth.pwd_context.verify(secret, db_key.hashed_key):
        raise HTTPException(status_code=401, detail="Invalid service key")
    
    return db_key


@router.get("/bulk/binance/offers/raw")
async def get_bulk_offers_raw(
    fiat: str,
    asset: str,
    trade_type: str,
    max_pages: int = 50,
    _: str = Depends(verify_service_account_key)
) -> Dict[str, any]:
    """
    Bulk extraction endpoint for ingestion bot.
    Returns ALL pages of raw numeric data for a trading pair.
    
    Response format:
    {
        "fiat": "VES",
        "asset": "USDT", 
        "trade_type": "BUY",
        "total_offers": 847,
        "pages_fetched": 43,
        "offers": [
            {
                "offer_id": "...",
                "price": "40.15",  # String for JSON, but original Decimal
                "available_amount": "5000.00",
                ...
            }
        ]
    }
    """
    try:
        offers = scrape_all_offers_raw(fiat, asset, trade_type, max_pages)
        
        # Convert Decimals to strings for JSON serialization
        serialized_offers = []
        for offer in offers:
            serialized = offer.copy()
            for key, value in serialized.items():
                if isinstance(value, Decimal):
                    serialized[key] = str(value)
            serialized_offers.append(serialized)
        
        return {
            "fiat": fiat,
            "asset": asset,
            "trade_type": trade_type,
            "total_offers": len(serialized_offers),
            "pages_fetched": (len(serialized_offers) // 20) + 1,
            "offers": serialized_offers
        }
        
    except Exception as e:
        logger.error(f"Bulk extraction failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/bulk/binance/pairs")
async def get_all_trading_pairs(
    _: str = Depends(verify_service_account_key)
) -> List[Dict]:
    """
    Get all available trading pairs for bot to iterate through.
    """
    from ..binance_scraper import get_binance_pairs
    return get_binance_pairs()
```

**Register in `p2p_api/main.py`:**

```python
# In lifespan function
from .routers import admin, internal

app.include_router(admin.router)
app.include_router(internal.router)  # NEW
```

---

### Phase 3: Bot Authentication Setup (Week 1)

**Steps for Admin:**

1. **Generate Service Account Key:**

```bash
# In FastAPI docs at /docs
POST /admin/keys/
Body: {
  "name": "ingestion_bot_service_account"
}

# Save the returned key: p2p_abc123_xyz...
```

2. **Configure Bot `.env`:**

```env
# p2p_ingestion_bot/.env
FASTAPI_BASE_URL=http://127.0.0.1:8000
SERVICE_API_KEY=p2p_abc123_xyz...
DATABASE_URL=postgresql://user:pass@localhost/p2p_warehouse
```

3. **Bot Client Example:**

```python
# p2p_ingestion_bot/client.py
import requests
from typing import List, Dict

class P2PAPIClient:
    def __init__(self, base_url: str, service_key: str):
        self.base_url = base_url
        self.headers = {"X-Service-Key": service_key}
    
    def get_all_pairs(self) -> List[Dict]:
        """Get list of all tradable pairs."""
        response = requests.get(
            f"{self.base_url}/internal/bulk/binance/pairs",
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()
    
    def get_bulk_offers(
        self, 
        fiat: str, 
        asset: str, 
        trade_type: str
    ) -> Dict:
        """
        Get ALL offers for a trading pair.
        Returns raw numeric data ready for database insertion.
        """
        response = requests.get(
            f"{self.base_url}/internal/bulk/binance/offers/raw",
            params={
                "fiat": fiat,
                "asset": asset,
                "trade_type": trade_type,
                "max_pages": 50
            },
            headers=self.headers,
            timeout=180  # 3 minutes for bulk operation
        )
        response.raise_for_status()
        return response.json()
```

---

## 🔧 ADDITIONAL BACKEND IMPROVEMENTS

### 1. Add Rate Limiter Middleware

**New File:** `p2p_api/middleware/rate_limiter.py`

```python
"""
Shared rate limiter to prevent bot + API from overwhelming Binance.
"""
import asyncio
from datetime import datetime, timedelta
from collections import deque

class BinanceRateLimiter:
    """
    Token bucket rate limiter shared across all Binance requests.
    Limit: 100 requests per minute per IP.
    """
    def __init__(self, rate_limit: int = 100, period: int = 60):
        self.rate_limit = rate_limit
        self.period = period
        self.requests = deque()
        self.lock = asyncio.Lock()
    
    async def acquire(self):
        """Wait until a request slot is available."""
        async with self.lock:
            now = datetime.now()
            
            # Remove requests older than period
            while self.requests and (now - self.requests[0]) > timedelta(seconds=self.period):
                self.requests.popleft()
            
            # Wait if at limit
            if len(self.requests) >= self.rate_limit:
                sleep_time = (self.requests[0] + timedelta(seconds=self.period) - now).total_seconds()
                await asyncio.sleep(sleep_time)
                return await self.acquire()
            
            self.requests.append(now)

# Global instance
binance_limiter = BinanceRateLimiter()
```

**Use in scrapers:**

```python
# In binance_scraper_raw.py
from .middleware.rate_limiter import binance_limiter

async def get_binance_offers_raw(...):
    await binance_limiter.acquire()  # Wait for slot
    response = requests.post(url, ...)
```

---

### 2. Add Health Check Endpoint

**In `p2p_api/main.py`:**

```python
@app.get("/health", tags=["System"])
async def health_check(db: Session = Depends(get_db)):
    """
    Health check for monitoring bot uptime.
    Returns 200 if API and database are healthy.
    """
    try:
        # Test database
        db.execute("SELECT 1")
        
        return {
            "status": "healthy",
            "timestamp": datetime.utcnow().isoformat(),
            "database": "connected"
        }
    except Exception as e:
        return JSONResponse(
            status_code=503,
            content={
                "status": "unhealthy",
                "error": str(e)
            }
        )
```

---

### 3. Add Logging for Bot Operations

**In `p2p_api/logging_config.py`:**

```python
# Add bot-specific logger
bot_handler = RotatingFileHandler(
    os.path.join(LOG_DIR, "bot_operations.log"),
    maxBytes=10 * 1024 * 1024,  # 10MB
    backupCount=10
)
bot_logger = logging.getLogger("p2p_api.internal")
bot_logger.addHandler(bot_handler)
bot_logger.setLevel(logging.INFO)
```

---

## 📋 IMPLEMENTATION CHECKLIST

### Week 1: Core Infrastructure
- [ ] Create `binance_scraper_raw.py` with raw data functions
- [ ] Create `routers/internal.py` with bulk endpoints
- [ ] Add service account key verification
- [ ] Test bulk extraction with single pair (VES/USDT/BUY)
- [ ] Verify numeric data types in response

### Week 2: Rate Limiting & Monitoring
- [ ] Implement `BinanceRateLimiter` middleware
- [ ] Add health check endpoint
- [ ] Set up bot-specific logging
- [ ] Test parallel requests don't exceed rate limits
- [ ] Add Prometheus metrics (optional)

### Week 3: Bot Integration Testing
- [ ] Bot can authenticate with service key
- [ ] Bot can fetch all trading pairs
- [ ] Bot can extract bulk offers for all pairs
- [ ] Test complete 10-minute batch cycle
- [ ] Verify data quality in PostgreSQL

### Week 4: Error Handling & Recovery
- [ ] Add circuit breaker for Binance API
- [ ] Implement exponential backoff
- [ ] Add retry logic for transient failures
- [ ] Test partial batch failure recovery
- [ ] Document error scenarios

---

## 🚨 CRITICAL WARNINGS

### 1. DO NOT Modify Existing Endpoints
- Keep `/api/v1/binance/offers` unchanged
- Streamlit app depends on formatted strings
- Public API contract must remain stable

### 2. Service Account Key Security
```python
# ❌ NEVER commit this
SERVICE_API_KEY=p2p_abc123_xyz...

# ✅ Use environment variables
SERVICE_API_KEY=${SERVICE_API_KEY}
```

### 3. Rate Limit Monitoring
- Monitor Binance response headers: `X-MBX-USED-WEIGHT`
- If approaching 1200/minute, implement aggressive backoff
- Consider using multiple IPs for production

### 4. Database Connection Pooling
```python
# In bot, limit concurrent database writes
from sqlalchemy.pool import QueuePool

engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=10,
    max_overflow=20
)
```

---

## 📊 TESTING STRATEGY

### Unit Tests
```python
# tests/test_scraper_raw.py
def test_raw_scraper_returns_decimals():
    offers = get_binance_offers_raw("VES", "USDT", "BUY", page=1)
    assert isinstance(offers[0]["price"], Decimal)
    assert isinstance(offers[0]["available_amount"], Decimal)

def test_bulk_endpoint_requires_service_key():
    response = client.get("/internal/bulk/binance/offers/raw")
    assert response.status_code == 401
```

### Integration Tests
```python
# tests/test_bot_integration.py
def test_bot_can_fetch_all_pairs():
    client = P2PAPIClient(BASE_URL, SERVICE_KEY)
    pairs = client.get_all_pairs()
    assert len(pairs) > 100  # Binance has 100+ pairs

def test_bot_bulk_extraction():
    client = P2PAPIClient(BASE_URL, SERVICE_KEY)
    result = client.get_bulk_offers("VES", "USDT", "BUY")
    assert result["total_offers"] > 0
    assert all(isinstance(o["price"], str) for o in result["offers"])
```

---

## 🎯 ESTIMATED EFFORT

| Phase | Duration | Complexity |
|-------|----------|------------|
| Raw scraper implementation | 2 days | Medium |
| Internal endpoint setup | 1 day | Low |
| Rate limiter middleware | 1 day | Medium |
| Testing & validation | 2 days | High |
| Documentation | 1 day | Low |
| **Total** | **7 days** | **Medium** |

---

## 📚 NEXT STEPS

After backend modifications:

1. **Bot Development** (Separate PRD needed)
   - Implement extraction orchestrator
   - Build database loader
   - Set up scheduling (APScheduler)

2. **Infrastructure**
   - Deploy PostgreSQL with TimescaleDB
   - Set up monitoring (Prometheus + Grafana)
   - Configure CI/CD for bot

3. **Production Readiness**
   - Load testing with 100+ concurrent pairs
   - Failover strategy
   - Backup & recovery procedures

---

## ❓ QUESTIONS FOR YOUR TEAM

1. **Authentication**: Should bot use same API key system or separate service tokens?
2. **Deployment**: Will bot run on same server as FastAPI or separate?
3. **Database**: Existing PostgreSQL or new TimescaleDB instance?
4. **Monitoring**: What alerting channels (Slack, PagerDuty, email)?
5. **Rate Limits**: Have you tested Binance rate limits from your IP?

---

## 📞 SUPPORT RESOURCES

- **Binance P2P API Docs**: https://binance-docs.github.io/apidocs/spot/en/#p2p-endpoints
- **FastAPI Best Practices**: https://fastapi.tiangolo.com/advanced/
- **Rate Limiting Patterns**: https://www.nginx.com/blog/rate-limiting-nginx/
- **TimescaleDB Time-Series**: https://docs.timescale.com/


