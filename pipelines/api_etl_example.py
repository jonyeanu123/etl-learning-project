"""
API ETL Pipeline Example
Demonstrates extracting data from a REST API, transforming, and loading to a file.
"""

import requests
import pandas as pd
import logging
from datetime import datetime
import time
import json

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class APIETLPipeline:
    """
    ETL Pipeline for extracting data from REST APIs.
    """

    def __init__(self, api_url, output_path, max_retries=3):
        """
        Initialize API ETL pipeline.

        Args:
            api_url (str): API endpoint URL
            output_path (str): Path to save extracted data
            max_retries (int): Maximum number of retry attempts
        """
        self.api_url = api_url
        self.output_path = output_path
        self.max_retries = max_retries
        self.data = None

    def extract_with_retry(self):
        """
        Extract data from API with retry logic.
        """
        for attempt in range(self.max_retries):
            try:
                logger.info(f"Attempt {attempt + 1}: Calling API {self.api_url}")

                response = requests.get(self.api_url, timeout=10)

                # Check response status
                if response.status_code == 200:
                    self.data = response.json()
                    logger.info(f"Successfully extracted data from API")
                    return self.data
                elif response.status_code == 429:  # Rate limit
                    wait_time = 2 ** attempt  # Exponential backoff
                    logger.warning(f"Rate limited. Waiting {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    logger.error(f"API returned status code: {response.status_code}")

            except requests.exceptions.Timeout:
                logger.warning(f"Request timed out on attempt {attempt + 1}")
                time.sleep(2 ** attempt)
            except requests.exceptions.RequestException as e:
                logger.error(f"Request failed: {str(e)}")
                time.sleep(2 ** attempt)

        raise Exception(f"Failed to extract data after {self.max_retries} attempts")

    def transform(self):
        """
        Transform the API response data.
        """
        try:
            logger.info("Starting transformation")

            # Convert to DataFrame
            df = pd.DataFrame(self.data)

            # Example transformations for JSONPlaceholder users API
            if 'address' in df.columns:
                # Flatten nested address structure
                df['city'] = df['address'].apply(lambda x: x.get('city', '') if isinstance(x, dict) else '')
                df['zipcode'] = df['address'].apply(lambda x: x.get('zipcode', '') if isinstance(x, dict) else '')

            if 'company' in df.columns:
                # Extract company name
                df['company_name'] = df['company'].apply(lambda x: x.get('name', '') if isinstance(x, dict) else '')

            # Select and rename columns
            columns_to_keep = ['id', 'name', 'email', 'phone', 'city', 'company_name']
            df = df[[col for col in columns_to_keep if col in df.columns]]

            self.data = df
            logger.info(f"Transformation complete. {len(df)} records processed")

            return df

        except Exception as e:
            logger.error(f"Transformation failed: {str(e)}")
            raise

    def load(self):
        """
        Load transformed data to output file.
        """
        try:
            logger.info(f"Loading data to {self.output_path}")

            if isinstance(self.data, pd.DataFrame):
                self.data.to_json(self.output_path, orient='records', indent=2)
            else:
                with open(self.output_path, 'w') as f:
                    json.dump(self.data, f, indent=2)

            logger.info(f"Data successfully saved to {self.output_path}")

        except Exception as e:
            logger.error(f"Load failed: {str(e)}")
            raise

    def run(self):
        """
        Execute the complete ETL pipeline.
        """
        try:
            logger.info("Starting API ETL Pipeline")
            start_time = datetime.now()

            self.extract_with_retry()
            self.transform()
            self.load()

            duration = (datetime.now() - start_time).total_seconds()
            logger.info(f"Pipeline completed in {duration:.2f} seconds")

            return True

        except Exception as e:
            logger.error(f"Pipeline failed: {str(e)}")
            return False


def main():
    """
    Example usage of API ETL Pipeline.
    """
    # Example: Extract users from JSONPlaceholder API
    api_url = "https://jsonplaceholder.typicode.com/users"
    output_path = "../data/raw/api_users.json"

    pipeline = APIETLPipeline(api_url, output_path)
    success = pipeline.run()

    if success:
        print("API ETL completed successfully!")
    else:
        print("API ETL failed!")


if __name__ == "__main__":
    main()
