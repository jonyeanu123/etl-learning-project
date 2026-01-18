# ETL Practice Exercises

## Exercise 1: Basic CSV Processing
**Difficulty**: Beginner
**Time**: 30 minutes

### Objective
Read a CSV file, perform basic transformations, and write to a new file.

### Tasks
1. Read `data/raw/customers.csv`
2. Remove duplicate records
3. Convert all email addresses to lowercase
4. Add a new column `full_name` combining first and last names
5. Save to `data/processed/customers_clean.csv`

### Expected Output
Clean CSV file with no duplicates and proper formatting.

### Hints
- Use pandas `read_csv()` and `to_csv()`
- `drop_duplicates()` for removing duplicates
- String methods: `.str.lower()`

---

## Exercise 2: API Data Extraction
**Difficulty**: Beginner
**Time**: 45 minutes

### Objective
Extract data from a public API and save to JSON.

### Tasks
1. Call the JSONPlaceholder API (https://jsonplaceholder.typicode.com/users)
2. Extract all users
3. Transform: Keep only id, name, email, and company name
4. Save to `data/raw/api_users.json`
5. Add error handling for failed requests

### Expected Output
JSON file with transformed user data.

### Hints
- Use `requests` library
- Handle status codes (200, 404, 500)
- Use try/except for error handling

---

## Exercise 3: Data Type Conversion
**Difficulty**: Beginner
**Time**: 45 minutes

### Objective
Fix data type issues in a messy dataset.

### Tasks
1. Read `data/raw/sales_data.csv`
2. Convert date strings to datetime objects
3. Convert price strings (e.g., "$19.99") to float
4. Convert quantity to integer
5. Handle any conversion errors gracefully
6. Save to `data/processed/sales_data_typed.csv`

### Expected Output
CSV with correct data types.

### Hints
- `pd.to_datetime()` for dates
- String manipulation to remove currency symbols
- `pd.to_numeric()` with errors='coerce'

---

## Exercise 4: Data Validation
**Difficulty**: Intermediate
**Time**: 1 hour

### Objective
Implement data quality checks and validation rules.

### Tasks
1. Read `data/raw/customer_orders.csv`
2. Validate:
   - Email addresses are in valid format
   - Order amounts are positive numbers
   - Dates are not in the future
   - Required fields are not null
3. Separate valid and invalid records
4. Save valid records to `data/processed/valid_orders.csv`
5. Save invalid records to `data/processed/invalid_orders.csv` with error reasons

### Expected Output
Two CSV files: valid and invalid records with error annotations.

### Hints
- Use regex for email validation
- Create custom validation functions
- Add an 'error_reason' column for invalid records

---

## Exercise 5: Multi-Source Data Integration
**Difficulty**: Intermediate
**Time**: 1.5 hours

### Objective
Combine data from multiple sources and formats.

### Tasks
1. Read customer data from `data/raw/customers.csv`
2. Read order data from `data/raw/orders.json`
3. Read product data from a SQLite database
4. Join all three datasets
5. Calculate total order value for each customer
6. Save enriched data to `data/final/customer_analytics.csv`

### Expected Output
Single CSV with customer, order, and product information combined.

### Hints
- Use pandas `merge()` or `join()`
- `sqlalchemy` for database connection
- Aggregate functions: `groupby()` and `sum()`

---

## Exercise 6: Incremental Data Loading
**Difficulty**: Intermediate
**Time**: 1.5 hours

### Objective
Implement incremental loading to avoid reprocessing all data.

### Tasks
1. Create a tracking table to store last processing timestamp
2. Extract only new/modified records since last run
3. Transform the incremental data
4. Load to target database using upsert logic
5. Update the tracking table

### Expected Output
Database with only new/changed records processed.

### Hints
- Use a separate metadata table for tracking
- Filter source data by timestamp
- Use `INSERT OR REPLACE` for SQLite or `ON CONFLICT` for PostgreSQL

---

## Exercise 7: Error Handling & Logging
**Difficulty**: Intermediate
**Time**: 1 hour

### Objective
Add robust error handling and logging to an ETL pipeline.

### Tasks
1. Take an existing pipeline (from Exercise 5)
2. Add comprehensive logging (INFO, WARNING, ERROR levels)
3. Implement retry logic for failed operations
4. Create error summary report
5. Save logs to `logs/pipeline_run.log`

### Expected Output
Pipeline with detailed logs and error recovery.

### Hints
- Use Python's `logging` module
- Implement decorator for retry logic
- Log start/end times, record counts, errors

---

## Exercise 8: Data Quality Monitoring
**Difficulty**: Advanced
**Time**: 2 hours

### Objective
Build data quality checks and monitoring.

### Tasks
1. Create quality checks for a dataset:
   - Completeness (no nulls in key fields)
   - Uniqueness (no duplicate IDs)
   - Validity (values in expected ranges)
   - Consistency (cross-field validation)
2. Generate a data quality report
3. Alert if quality thresholds are not met
4. Save report to `data/reports/quality_report.html`

### Expected Output
HTML report showing data quality metrics and test results.

### Hints
- Create a DataQualityChecker class
- Use pandas profiling or custom functions
- Generate HTML using pandas `.to_html()`

---

## Exercise 9: Parallel Processing
**Difficulty**: Advanced
**Time**: 2 hours

### Objective
Speed up ETL pipeline using parallel processing.

### Tasks
1. Process 10 large CSV files sequentially (baseline)
2. Refactor to process files in parallel
3. Measure and compare execution times
4. Combine results from all parallel processes
5. Save consolidated output

### Expected Output
Faster pipeline execution with performance metrics.

### Hints
- Use `concurrent.futures` or `multiprocessing`
- Process each file in separate worker
- Use `ProcessPoolExecutor` for CPU-bound tasks

---

## Exercise 10: End-to-End Pipeline
**Difficulty**: Advanced
**Time**: 3 hours

### Objective
Build a complete, production-ready ETL pipeline.

### Tasks
1. Extract data from API, database, and files
2. Implement data validation and cleaning
3. Apply business transformations
4. Load to data warehouse with proper schema
5. Add configuration file for parameters
6. Implement logging and error handling
7. Create pipeline documentation
8. Schedule to run automatically

### Expected Output
Fully functional, documented, and automated ETL pipeline.

### Hints
- Use config.yaml for configuration
- Separate concerns: extract, transform, load modules
- Create a main orchestrator script
- Use `schedule` library for automation

---

## Bonus Challenges

### Challenge 1: CDC Implementation
Implement Change Data Capture to track and process only changed records.

### Challenge 2: Data Lineage Tracking
Add metadata to track data lineage (source, transformations, destination).

### Challenge 3: API Rate Limiting
Handle API rate limits with exponential backoff.

### Challenge 4: Data Anonymization
Implement PII anonymization for sensitive fields.

### Challenge 5: Real-time Streaming
Process streaming data using event-driven architecture.

---

## How to Use These Exercises

1. **Start with Exercise 1** and progress sequentially
2. **Complete exercises** from your reading each week
3. **Build incrementally** - each exercise adds complexity
4. **Review solutions** after attempting on your own
5. **Modify exercises** to match your interests
6. **Create variations** to reinforce learning

---

## Submission Checklist

For each exercise, ensure you have:
- [ ] Working code with proper structure
- [ ] Comments explaining key logic
- [ ] Error handling implemented
- [ ] Test with sample data
- [ ] Documentation (README or docstrings)
- [ ] Logging where appropriate

---

## Getting Help

1. Review the book chapter related to the exercise
2. Check Python documentation
3. Search for similar examples online
4. Break the problem into smaller steps
5. Test each component individually

Good luck with your learning journey!
