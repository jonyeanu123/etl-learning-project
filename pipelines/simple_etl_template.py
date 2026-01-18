"""
Simple ETL Pipeline Template
This is a starter template for building ETL pipelines.
Modify this template for your specific use cases.
"""

import pandas as pd
import logging
from datetime import datetime
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('../logs/etl_pipeline.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class SimpleETLPipeline:
    """
    A simple ETL pipeline template with extract, transform, and load methods.
    """

    def __init__(self, source_path, target_path):
        """
        Initialize the ETL pipeline.

        Args:
            source_path (str): Path to source data file
            target_path (str): Path to save processed data
        """
        self.source_path = source_path
        self.target_path = target_path
        self.data = None
        self.run_id = datetime.now().strftime('%Y%m%d_%H%M%S')

    def extract(self):
        """
        Extract data from source.
        Modify this method based on your data source (CSV, JSON, API, Database, etc.)
        """
        try:
            logger.info(f"Starting extraction from {self.source_path}")

            # Example: Reading CSV file
            self.data = pd.read_csv(self.source_path)

            logger.info(f"Successfully extracted {len(self.data)} records")
            logger.info(f"Columns: {list(self.data.columns)}")

            return self.data

        except FileNotFoundError:
            logger.error(f"Source file not found: {self.source_path}")
            raise
        except Exception as e:
            logger.error(f"Error during extraction: {str(e)}")
            raise

    def transform(self):
        """
        Transform the extracted data.
        Add your transformation logic here.
        """
        try:
            logger.info("Starting data transformation")

            if self.data is None:
                raise ValueError("No data to transform. Run extract() first.")

            initial_count = len(self.data)

            # Example transformations:

            # 1. Remove duplicates
            self.data = self.data.drop_duplicates()
            logger.info(f"Removed {initial_count - len(self.data)} duplicate records")

            # 2. Handle missing values
            missing_before = self.data.isnull().sum().sum()
            self.data = self.data.fillna('')  # or dropna(), depending on requirements
            logger.info(f"Handled {missing_before} missing values")

            # 3. Data type conversions (example)
            # self.data['date_column'] = pd.to_datetime(self.data['date_column'])

            # 4. Add derived columns (example)
            # self.data['full_name'] = self.data['first_name'] + ' ' + self.data['last_name']

            # 5. Filter data (example)
            # self.data = self.data[self.data['status'] == 'active']

            logger.info(f"Transformation complete. Final record count: {len(self.data)}")

            return self.data

        except Exception as e:
            logger.error(f"Error during transformation: {str(e)}")
            raise

    def load(self):
        """
        Load the transformed data to target destination.
        Modify this method based on your target (CSV, Database, API, etc.)
        """
        try:
            logger.info(f"Starting load to {self.target_path}")

            if self.data is None:
                raise ValueError("No data to load. Run extract() and transform() first.")

            # Ensure target directory exists
            Path(self.target_path).parent.mkdir(parents=True, exist_ok=True)

            # Example: Save to CSV
            self.data.to_csv(self.target_path, index=False)

            logger.info(f"Successfully loaded {len(self.data)} records to {self.target_path}")

            return True

        except Exception as e:
            logger.error(f"Error during load: {str(e)}")
            raise

    def run(self):
        """
        Run the complete ETL pipeline.
        """
        try:
            logger.info(f"Starting ETL pipeline - Run ID: {self.run_id}")
            start_time = datetime.now()

            # Execute ETL steps
            self.extract()
            self.transform()
            self.load()

            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()

            logger.info(f"ETL pipeline completed successfully in {duration:.2f} seconds")

            return True

        except Exception as e:
            logger.error(f"ETL pipeline failed: {str(e)}")
            return False


def main():
    """
    Main function to run the ETL pipeline.
    """
    # Configure your source and target paths
    source_path = '../data/raw/customers.csv'
    target_path = '../data/processed/customers_processed.csv'

    # Create and run pipeline
    pipeline = SimpleETLPipeline(source_path, target_path)
    success = pipeline.run()

    if success:
        print("ETL Pipeline completed successfully!")
    else:
        print("ETL Pipeline failed. Check logs for details.")


if __name__ == "__main__":
    main()
