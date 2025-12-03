# Binance P2P API Endpoint Testing Protocol

You are a skilled DevOps engineer conducting API endpoint testing. You have access to terminal commands and need to systematically test a FastAPI application's Binance P2P integration endpoints.

## Context
A Python FastAPI application at `p2p_api/` has endpoints for fetching Binance P2P trading data. The REST API calls were previously failing, and code fixes have been applied. Your task is to validate the fixes work correctly.

## Your Mission
Execute a comprehensive test suite to verify the Binance P2P endpoints are functional, with detailed diagnostics at each step.

---

## Test Protocol

### Phase 1: Environment Setup & Validation

**1.1 Navigate to project directory**
```bash
cd /path/to/dashboards
pwd  # Confirm location
```

**1.2 Check Python environment**
```bash
python --version
pip list | grep -E "fastapi|requests|uvicorn"
```

**1.3 Verify file structure**
```bash
ls -la p2p_api/
cat p2p_api/binance_scraper.py | head -50  # Check if fixes applied
```

**Expected output**: Should see updated User-Agent with Chrome 131 and Referer header

---

### Phase 2: Server Startup

**2.1 Start FastAPI server with detailed logging**
```bash
# Terminal 1 (keep this running)
export LOG_LEVEL=DEBUG
uvicorn p2p_api.main:app --reload --host 0.0.0.0 --port 8000 --log-level debug
```

**Wait for**: `Uvicorn running on http://0.0.0.0:8000`

**2.2 Verify server health (in new terminal)**
```bash
# Terminal 2
curl -X GET http://localhost:8000/health || echo "Health check failed"
```

---

### Phase 3: Test Binance Pairs Endpoint

**3.1 Test pairs endpoint**
```bash
curl -X GET "http://localhost:8000/api/v1/binance/pairs" \
  -H "Accept: application/json" \
  -w "\n\nHTTP Status: %{http_code}\nTime: %{time_total}s\n" \
  -o pairs_response.json
```

**3.2 Analyze response**
```bash
# Check if response is valid JSON
cat pairs_response.json | python -m json.tool | head -30

# Count trading pairs
cat pairs_response.json | python -c "import json, sys; data=json.load(sys.stdin); print(f'Total pairs: {len(data)}')"

# Show first 3 pairs
cat pairs_response.json | python -c "import json, sys; data=json.load(sys.stdin); [print(p) for p in data[:3]]"
```

**Expected output**: 
- HTTP Status: 200
- Valid JSON array
- Multiple fiat/asset pairs like `{"fiat": "ARS", "asset": "USDT", "tradeType": "BUY"}`

**If fails**: Check Terminal 1 logs for errors. Look for:
- `❌ HTTP error: 403` → Headers issue
- `❌ HTTP error: 429` → Rate limited
- `❌ Request timeout` → Network issue

---

### Phase 4: Test Binance Offers Endpoint

**4.1 Test ARS/USDT/BUY offers**
```bash
curl -X GET "http://localhost:8000/api/v1/binance/offers?fiat=ARS&asset=USDT&tradeType=BUY&page=1&rows=10" \
  -H "Accept: application/json" \
  -w "\n\nHTTP Status: %{http_code}\nTime: %{time_total}s\n" \
  -o offers_ars_buy.json
```

**4.2 Validate offer structure**
```bash
# Pretty print first offer
cat offers_ars_buy.json | python -c "
import json, sys
data = json.load(sys.stdin)
if data:
    print('✅ Offers fetched successfully')
    print(f'Total offers: {len(data)}')
    print('\nFirst offer:')
    print(json.dumps(data[0], indent=2))
else:
    print('❌ No offers returned')
"
```

**Expected fields in each offer**:
- `advertiser` (string)
- `price` (string with fiat)
- `available` (string with asset)
- `limits` (string with range)
- `payment_methods` (array)

**4.3 Test multiple fiat pairs**
```bash
# Test COP (Colombian Peso)
curl -s "http://localhost:8000/api/v1/binance/offers?fiat=COP&asset=USDT&tradeType=SELL&rows=5" | \
  python -c "import json, sys; data=json.load(sys.stdin); print(f'COP/USDT/SELL: {len(data)} offers')"

# Test VES (Venezuelan Bolívar)
curl -s "http://localhost:8000/api/v1/binance/offers?fiat=VES&asset=USDT&tradeType=BUY&rows=5" | \
  python -c "import json, sys; data=json.load(sys.stdin); print(f'VES/USDT/BUY: {len(data)} offers')"

# Test USD (US Dollar)
curl -s "http://localhost:8000/api/v1/binance/offers?fiat=USD&asset=BTC&tradeType=BUY&rows=5" | \
  python -c "import json, sys; data=json.load(sys.stdin); print(f'USD/BTC/BUY: {len(data)} offers')"
```

---

### Phase 5: Performance & Rate Limiting

**5.1 Test rapid requests (check rate limiting)**
```bash
echo "Testing rapid requests..."
for i in {1..10}; do
  curl -s -o /dev/null -w "Request $i: %{http_code} - %{time_total}s\n" \
    "http://localhost:8000/api/v1/binance/offers?fiat=ARS&asset=USDT&tradeType=BUY&page=$i"
  sleep 0.5
done
```

**Expected**: All should return 200 (or 429 if Binance rate limits kick in)

**5.2 Test pagination**
```bash
# Fetch 3 pages and count unique offers
for page in 1 2 3; do
  curl -s "http://localhost:8000/api/v1/binance/offers?fiat=ARS&asset=USDT&tradeType=BUY&page=$page&rows=20" \
    -o "page_$page.json"
done

# Count total unique offers
python -c "
import json
offers = []
for i in [1,2,3]:
    with open(f'page_{i}.json') as f:
        offers.extend(json.load(f))
print(f'Total offers across 3 pages: {len(offers)}')
"
```

---

### Phase 6: Error Handling Tests

**6.1 Test invalid parameters**
```bash
# Invalid fiat
curl -w "\nStatus: %{http_code}\n" "http://localhost:8000/api/v1/binance/offers?fiat=INVALID&asset=USDT&tradeType=BUY"

# Invalid trade type
curl -w "\nStatus: %{http_code}\n" "http://localhost:8000/api/v1/binance/offers?fiat=ARS&asset=USDT&tradeType=INVALID"

# Missing parameters
curl -w "\nStatus: %{http_code}\n" "http://localhost:8000/api/v1/binance/offers"
```

**Expected**: Should handle gracefully with proper error messages or empty arrays

---

### Phase 7: Log Analysis

**7.1 Check server logs in Terminal 1**

Look for these success indicators:
- `✅ Binance request successful`
- `Response status: 200`
- `✅ Parsed X offers successfully`

Look for these failure indicators:
- `❌ HTTP error: 403` → Authentication/headers issue
- `❌ HTTP error: 429` → Rate limit hit
- `❌ Request timeout` → Slow network
- `❌ Binance API error: code=XXX` → Business logic error

**7.2 Extract error patterns**
```bash
# In Terminal 2, analyze logs if server logs to file
grep "❌" logs/app.log | sort | uniq -c
```

---

## Test Results Summary Template

After completing all phases, provide a summary in this format:

```
=== BINANCE P2P API TEST RESULTS ===

✅ PASSED:
- Environment setup
- Server startup
- Pairs endpoint (X pairs fetched)
- Offers endpoint ARS/USDT (X offers)
- [List other successes]

❌ FAILED:
- [List failures with error codes]

⚠️  WARNINGS:
- [List any concerning patterns]

📊 PERFORMANCE:
- Average response time: X.XXs
- Rate limiting: [Observed/Not observed]

🔍 RECOMMENDATIONS:
- [Next steps based on results]
```

---

## Diagnostic Commands for Failures

**If you see 403 errors:**
```bash
# Check if Binance is blocking your IP
curl -I https://p2p.binance.com/
curl -I https://api.binance.com/api/v3/ping

# Test headers
curl -v "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search" \
  -H "Referer: https://p2p.binance.com/" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" \
  -d '{"page":1,"rows":10,"tradeType":"BUY","asset":"USDT","fiat":"ARS"}'
```

**If you see timeout errors:**
```bash
# Test network connectivity
ping -c 3 p2p.binance.com
traceroute p2p.binance.com
```

**If you see JSON parse errors:**
```bash
# Check raw response
curl -v "http://localhost:8000/api/v1/binance/offers?fiat=ARS&asset=USDT&tradeType=BUY" 2>&1 | grep -A 20 "< HTTP"
```

---

## Final Task

After running all tests, create a file `test_report.md` with:
1. All test results
2. Example responses from successful endpoints
3. Any errors encountered
4. Your assessment: "Ready for production" or "Requires fixes"

```bash
cat > test_report.md << 'EOF'
# Binance P2P API Test Report
Date: $(date)
Tester: LLM Agent

## Results
[Paste your findings here]
EOF
```

---

## Your Instructions

1. Execute each phase sequentially
2. Document every command output
3. If a phase fails, run diagnostics before proceeding
4. Provide the final test report with clear pass/fail status
5. If endpoints work, test at least 4 different fiat pairs (ARS, COP, VES, USD)

**Begin testing now.**