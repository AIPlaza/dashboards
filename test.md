# P2P Data Ingestion Worker Testing Protocol

You are a skilled DevOps engineer testing the data ingestion worker. You have access to terminal commands and need to systematically test the worker's data extraction and loading functionality.

## Context
A Python worker at `worker/` is responsible for extracting P2P trading data from the Binance API and loading it into a database. Your task is to validate that the worker runs correctly, extracts data, and loads it as expected.

## Your Mission
Execute a comprehensive test suite to verify the P2P data ingestion worker is functional, with detailed diagnostics at each step.

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
pip list | findstr "schedule requests sqlalchemy"
```

**1.3 Verify file structure**
```bash
ls -la worker/
cat worker/main.py | head -30  # Check worker's main logic
cat worker/extractor.py | head -30 # Check extractor's logic
cat worker/loader.py | head -30 # Check loader's logic
```

---

### Phase 2: Worker Execution

**2.1 Run the worker manually**
```bash
# Run the worker's main function directly
python -m worker.main
```

**Wait for**: The worker to start, run the job once, and then enter the scheduling loop. You should see log messages indicating the job is running. You will need to manually stop the execution after you see the job has run.

**2.2 Check the logs for successful execution**
Look for log messages like:
- "Worker starting. Job will run every X minutes."
- "Starting P2P data extraction job..."
- "P2P data extraction job finished successfully."

---

### Phase 3: Data Extraction Validation

**3.1 Analyze worker logs for extraction details**
Check the logs for messages from the `extractor` module. Look for:
- Logs indicating which pairs are being extracted.
- Any error messages during extraction (e.g., from network requests).

**3.2 (Optional) Add temporary debugging to the extractor**
If the logs are not detailed enough, you can temporarily add print statements to `worker/extractor.py` to see the extracted data.
```python
# In worker/extractor.py, inside extract_all_offers()
...
print(f"Extracted {len(all_offers)} offers.")
if all_offers:
    print("Sample offer:", all_offers[0])
...
```

---

### Phase 4: Data Loading Validation

**4.1 Analyze worker logs for loading details**
Check the logs for messages from the `loader` module. Look for:
- "Loading X offers into the database."
- Any error messages during loading (e.g., database connection errors, constraint violations).

**4.2 Verify data in the database**
This step requires access to the database. The connection details should be in `worker/config.py` or a similar configuration file.
```sql
-- Example SQL query to verify data was loaded
SELECT COUNT(*) FROM offers WHERE batch_id = '<the_batch_id_from_the_logs>';
SELECT * FROM offers ORDER BY created_at DESC LIMIT 5;
```

---

### Phase 5: Scheduling Validation

**5.1 Observe the worker over time**
Let the worker run for a while (e.g., for `2 * extraction_interval_minutes`).

**5.2 Check the logs for multiple job executions**
You should see the log messages for the job starting and finishing multiple times, at the interval defined in the configuration.

---

## Test Results Summary Template

After completing all phases, provide a summary in this format:

```
=== P2P DATA INGESTION WORKER TEST RESULTS ===

✅ PASSED:
- Environment setup
- Worker startup
- Data extraction (X offers extracted)
- Data loading (X offers loaded into the database)
- Scheduling (Job ran multiple times at the correct interval)
- [List other successes]

❌ FAILED:
- [List failures with error messages]

⚠️  WARNINGS:
- [List any concerning patterns, e.g., occasional extraction failures]

🔍 RECOMMENDATIONS:
- [Next steps based on the results, e.g., "Increase log verbosity in extractor", "Add monitoring for database load"]
```
---

## Final Task

After running all tests, create a file `worker_test_report.md` with:
1. All test results
2. Example logs from a successful run
3. Any errors encountered
4. Your assessment: "Ready for production" or "Requires fixes"

```bash
cat > worker_test_report.md << 'EOF'
# P2P Data Ingestion Worker Test Report
Date: $(date)
Tester: LLM Agent

## Results
[Paste your findings here]
EOF
```

---

## Your Instructions

1. Execute each phase sequentially.
2. Document every command output.
3. If a phase fails, analyze the logs and code to diagnose the issue before proceeding.
4. Provide the final test report with a clear pass/fail status.

**Begin testing now.**
