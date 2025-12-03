# Binance P2P Data Ingestion Worker Troubleshooting Report

## Introduction
This report details the systematic troubleshooting and proposed fixes for the Binance P2P data ingestion worker located in the `worker/` directory. The primary goal is to ensure the worker can correctly extract trading data from the Binance P2P API and prepare it for loading into a database.

## Phase 1: Initial Setup and Problem Identification

### Step 1: Clarifying the Target Component
Initially, the testing protocol (`test.md`) was configured for a FastAPI application within the `p2p_api/` directory. Upon user clarification that the intended target for testing was the data ingestion worker in `worker/`, the `test.md` protocol was revised to focus on the worker's specific functionalities (data extraction, loading, and scheduling).

### Step 2: Python Environment Check
1.  **Python Version Verification:**
    *   Command: `python --version`
    *   Result: `Python 3.13.5` - Confirmed correct Python version.
2.  **Dependency Check:**
    *   Initial `pip list` revealed `schedule` was missing, while `requirements.txt` listed `APScheduler`.
    *   **Action:** Installed `schedule` manually: `pip install schedule`.
    *   `pip list` also showed `sqlalchemy` missing, despite `requirements.txt` listing it.
    *   **Action:** Attempted to install all dependencies from `requirements.txt`: `pip install -r requirements.txt`.
    *   **Outcome:** This installation failed due to `pydantic-core` requiring Rust and Cargo for compilation (`error: subprocess-exited-with-error`, `Cargo, the Rust package manager, is not installed or is not on PATH`).
    *   **Action:** Notified the user about the missing Rust/Cargo dependency. The user subsequently resolved this system-level dependency.
    *   **Outcome:** A subsequent `pip list` confirmed that all necessary Python packages were successfully installed.

### Step 3: Verify File Structure
*   Commands executed: `Get-ChildItem worker/`, `Get-Content worker/main.py`, `Get-Content worker/extractor.py`, `Get-Content worker/loader.py`.
*   Outcome: Confirmed the presence of expected files and reviewed the initial lines of the core worker scripts, which appeared consistent with their intended roles.

## Phase 2: Worker Execution - Initial Attempts and Endpoint Discovery

### Step 1: First Worker Run Attempt (after environment setup)
*   Command: `python worker/main.py`
*   Issue: `ModuleNotFoundError: No module named 'worker'`
*   Reason: The script was executed as a file, not as a Python module, leading to incorrect import path resolution.
*   **Action:** The command was corrected to `python -m worker.main` for subsequent runs.

### Step 2: Second Worker Run (using `python -m worker.main`)
*   Log reference: User provided logs for "second run" in `logs.md`.
*   Observation: The worker started successfully and initiated the data extraction job.
*   Critical Error: `worker.extractor - ERROR - Error fetching trading pairs: 404 Client Error: Not Found for url: https://p2p.binance.com/bapi/c2c/v2/public/c2c/asset-order/getAllSupportAsset`
*   Conclusion: The Binance P2P API endpoint configured for fetching trading pairs (`binance_pairs_endpoint` in `worker/config.py`) was incorrect or no longer valid, returning a `404 Not Found` error.

### Step 3: Diagnosing Endpoint Issues - Network Analysis
*   **Method:** A Playwright script (`temp_playwright_script/network_analyzer.py`) was created to simulate browser activity on `https://p2p.binance.com/` and capture XHR/Fetch requests.
*   **Initial Playwright Script Setup:** Created directory and script, installed `playwright` and `chromium`.
*   **Playwright Run Iterations:**
    *   Initial runs failed due to timeouts and overly strict filtering.
    *   **Action:** Timeouts and sleep durations were increased, and filtering was removed to capture *all* XHR/Fetch requests.
*   **Key Finding:** Among the captured requests, `https://p2p.binance.com/bapi/c2c/v1/friendly/c2c/trade-rule/fiat-list` (POST method with empty payload) was identified as a highly probable endpoint for retrieving a list of supported fiat currencies.

### Step 4: Endpoint Update - Fiat List (Configuration & Extraction Logic)
*   **Action:** Modified `worker/config.py`:
    *   Renamed `binance_pairs_endpoint` to `binance_fiat_list_endpoint`.
    *   Updated its value to `"/bapi/c2c/v1/friendly/c2c/trade-rule/fiat-list"`.
*   **Action:** Modified `worker/extractor.py`:
    *   Updated the `__init__` method to use `self.fiat_list_url`.
    *   Rewrote the `get_all_trading_pairs` method to use `self.fiat_list_url` and temporarily generate dummy trading pairs by combining extracted fiats with hardcoded assets (`USDT`, `BTC`, `ETH`).

### Step 5: Third Worker Run (after fiat endpoint and logic update)
*   Log reference: User provided logs for "Third run" in `logs.md`.
*   Observation: The worker successfully called the new `fiat-list` endpoint.
*   New Warning: `worker.extractor - WARNING - No fiat currencies found from the fiat list endpoint.`
*   Conclusion: The `fiat-list` endpoint was reached, but the parsing logic for extracting fiat codes from its response was incorrect.

### Step 6: Parsing Logic Fix
*   **Diagnosis:** Direct `Invoke-RestMethod` (PowerShell `curl` equivalent) to `https://p2p.binance.com/bapi/c2c/v1/friendly/c2c/trade-rule/fiat-list` revealed fiat currency codes were under the `currencyCode` key, not `fiatUnit`.
*   **Action:** Modified `worker/extractor.py` to change `item.get("fiatUnit")` to `item.get("currencyCode")` in the `get_all_trading_pairs` method.

### Step 7: Fourth Worker Run (after parsing logic fix)
*   Log reference: User provided logs for "Fourth run" in `logs.md`.
*   Observation: Fiat currency extraction was successful (`Found 119 fiat currencies`). Dummy trading pairs were generated.
*   Persistent Error: `worker.extractor - ERROR - Failed to extract AFN/USDT/BUY: illegal parameter` for almost all offer extraction requests. This indicated that while the fiat list was being fetched, the subsequent requests to the offer search endpoint (`/bapi/c2c/v2/friendly/c2c/adv/search`) were still being rejected.

### Step 8: Offer Search Payload & Header Refinement
*   **Diagnosis:** Compared the worker's `extract_pair_offers` payload and headers against those observed in successful browser requests (from Playwright analysis and `refactor.md`). Identified missing fields in the payload and critical headers (`Referer`, updated `User-Agent`).
*   **Action:** Modified `worker/extractor.py`:
    *   Updated the `_get_headers` method to include the latest `User-Agent` (`Chrome/131.0.0.0`) and the `Referer: https://p2p.binance.com/` header, along with other `Sec-Fetch-*` headers.
    *   Expanded the `payload` in `extract_pair_offers` to include all fields observed in browser requests, setting default values for `countries`, `shieldMerchantAds`, `filterType`, `periods`, `additionalKycVerifyFilter`, `classifies`, `tradedWith`, and `followed`.
    *   Added detailed logging (request URL, payload, response status, response body) and explicit `timeout` to API calls in both `get_all_trading_pairs` and `extract_pair_offers`.

### Step 9: Integrate `p2p_config.json` for Pair Generation
*   **Diagnosis:** The "illegal parameter" errors persisted, suggesting the generated pairs were still not entirely valid or that Binance API has stricter validation. User provided `p2p_config.json` as a source of truth for valid pairs.
*   **Action:** Modified `worker/config.py`:
    *   Added `p2p_config_path: str = "p2p_config.json"` to `WorkerSettings`.
    *   Added a property `p2p_config` to `WorkerSettings` to load and parse the `p2p_config.json` file.
    *   Removed `binance_fiat_list_endpoint`.
    *   Replaced `max_pages_per_pair` with `binance_p2p_until_page` (read from `p2p_config.json`).
*   **Action:** Modified `worker/extractor.py`:
    *   Removed `self.fiat_list_url` from `__init__`.
    *   Rewrote `get_all_trading_pairs` to dynamically generate trading pairs based on `FIATS` and `CRYPTOS_BY_FIAT` defined in `settings.p2p_config`.
    *   Updated `rows` parameter in `extract_pair_offers` payload to use `settings.binance_p2p_until_page`.

## Phase 3: Data Loading and Final Validation

### Step 10: Resolve Data Loading `NotNullViolation`
*   **Diagnosis:** The `NotNullViolation` indicated that the `advertiser_id` being passed to the `dim_advertisers` table was `null`.
*   **Action:** Modified `worker/extractor.py`'s `_parse_offer` method to use `advertiser.get("userNo")` for the `id` field within the nested `advertiser` dictionary.

## Current State & Next Steps

### Current State (After Eleventh Worker Run):

*   **Fiat/Crypto pair generation:** **SUCCESS**. The `get_all_trading_pairs` method now correctly reads from `p2p_config.json` and generates trading pairs based on the configured fiats and cryptos.
*   **Offer extraction from Binance:** **SUCCESS**. The worker successfully extracted `689` offers for all configured pairs from the Binance P2P API. The `illegal parameter` errors previously observed have been fully resolved.
*   **Data loading to DB:** **SUCCESS**. The worker successfully loaded the extracted `689` offers into the database. The `NotNullViolation` for `advertiser_id` has been resolved.

### Conclusion:
The Binance P2P data ingestion worker is now functioning correctly, extracting and loading data into the database as intended.
