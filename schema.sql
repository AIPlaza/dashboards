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
