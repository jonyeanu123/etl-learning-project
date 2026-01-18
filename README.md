# ETL Learning Project

Welcome to your Data Engineering learning journey! This project is designed to help you learn and practice building ETL (Extract, Transform, Load) pipelines with Python.

## Project Structure

```
etl-learning-project/
├── data/
│   ├── raw/              # Source data files
│   ├── processed/        # Transformed data
│   └── final/            # Final output data
├── notebooks/            # Jupyter notebooks for exploration
├── pipelines/            # ETL pipeline scripts
├── utils/                # Reusable utility functions
├── logs/                 # Pipeline execution logs
├── LEARNING_PLAN.md      # 6-week structured learning plan
├── EXERCISES.md          # Practice exercises
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Getting Started

### 1. Set Up Your Environment

Create a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Follow the Learning Plan

Open `LEARNING_PLAN.md` for a detailed 6-week learning path covering:
- Week 1: ETL Fundamentals
- Week 2: Data Extraction
- Week 3: Data Transformation
- Week 4: Data Loading
- Week 5: Pipeline Orchestration
- Week 6: Advanced Topics

### 4. Practice with Exercises

Work through `EXERCISES.md` which contains 10 progressive exercises from beginner to advanced.

## Quick Start - Run Your First Pipeline

Try the simple ETL template:

```bash
cd pipelines
python simple_etl_template.py
```

This will:
1. Extract data from `data/raw/customers.csv`
2. Remove duplicates and clean the data
3. Save results to `data/processed/customers_processed.csv`

## Sample Data Files

The project includes sample data files for practice:
- `customers.csv` - Customer information (with duplicates and formatting issues)
- `sales_data.csv` - Sales transactions (with data quality issues)
- `customer_orders.csv` - Orders with validation problems
- `orders.json` - Order data in JSON format

## Pipeline Templates

### 1. Simple ETL Template (`pipelines/simple_etl_template.py`)
Basic ETL pipeline demonstrating extract, transform, and load operations.

### 2. API ETL Example (`pipelines/api_etl_example.py`)
Extract data from REST APIs with retry logic and error handling.

## Utilities

### Data Quality Checker (`utils/data_quality.py`)
Reusable functions for:
- Completeness checks
- Uniqueness validation
- Email validation
- Numeric range checks
- Date validation

Example usage:
```python
from utils.data_quality import DataQualityChecker
import pandas as pd

df = pd.read_csv('data/raw/customers.csv')
checker = DataQualityChecker(df)
checker.check_completeness(['email', 'customer_id'])
print(checker.generate_report())
```

## Learning Resources

### Primary Book
**"Building ETL Pipelines with Python"** by Brij Kishore Pandey & Emily Ro Schoof
- Located in your Books/python directory
- Follow along with code examples
- Apply concepts to the exercises

### Complementary Books
1. "Python Data Cleaning and Preparation Best Practices" - for data quality
2. "Python for Data Analysis" - for pandas mastery
3. "Data Quality Fundamentals" - for data pipeline best practices

## Best Practices

1. **Always log your pipeline operations**
   - Use Python's logging module
   - Track record counts, errors, and execution time

2. **Handle errors gracefully**
   - Use try/except blocks
   - Implement retry logic for external services
   - Validate data before processing

3. **Make pipelines idempotent**
   - Running the pipeline multiple times should produce the same result
   - Important for reliability and debugging

4. **Document your code**
   - Add docstrings to functions
   - Comment complex logic
   - Maintain a README for each pipeline

5. **Test your pipelines**
   - Write unit tests for transformation logic
   - Test with sample data before production

## Daily Learning Routine

1. **Morning (30 min)**: Read book chapters
2. **Afternoon (1 hour)**: Complete exercises
3. **Evening (30 min)**: Build/improve practice projects

## Progress Tracking

Use the checklists in `LEARNING_PLAN.md` to track your weekly progress.

## Common Commands

```bash
# Activate environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Run a pipeline
python pipelines/simple_etl_template.py

# Install new package
pip install package-name

# Update requirements
pip freeze > requirements.txt

# Run tests (when you create them)
pytest tests/
```

## Tips for Success

1. **Start simple** - Don't try to build complex pipelines immediately
2. **Practice daily** - Consistency is key to learning
3. **Break problems down** - Tackle one piece at a time
4. **Read error messages** - They usually tell you what's wrong
5. **Experiment** - Modify the templates and try new approaches
6. **Build projects** - Apply what you learn to real-world scenarios

## Next Steps

1. Complete Week 1 readings and exercises
2. Run the sample pipelines
3. Start modifying templates for your own use cases
4. Build your first end-to-end pipeline

## Questions or Issues?

- Review the book chapters related to your current topic
- Check Python documentation
- Search for similar examples online
- Break the problem into smaller steps

## Good Luck!

Remember: Data engineering is learned by doing. Work through the exercises, build projects, and don't be afraid to make mistakes. Each error is a learning opportunity!

Happy coding!
