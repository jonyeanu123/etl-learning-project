"""
Data Quality Utilities
Reusable functions for data validation and quality checks.
"""

import pandas as pd
import re
import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)


class DataQualityChecker:
    """
    A class to perform various data quality checks.
    """

    def __init__(self, dataframe: pd.DataFrame):
        """
        Initialize the quality checker with a DataFrame.

        Args:
            dataframe: pandas DataFrame to check
        """
        self.df = dataframe
        self.issues = []

    def check_completeness(self, required_columns: List[str]) -> Dict[str, Any]:
        """
        Check if required columns have no missing values.

        Args:
            required_columns: List of column names that should not have nulls

        Returns:
            Dictionary with check results
        """
        missing_data = {}

        for col in required_columns:
            if col in self.df.columns:
                null_count = self.df[col].isnull().sum()
                if null_count > 0:
                    missing_data[col] = null_count
                    self.issues.append(f"Column '{col}' has {null_count} missing values")

        return {
            'check': 'completeness',
            'passed': len(missing_data) == 0,
            'missing_data': missing_data
        }

    def check_uniqueness(self, unique_columns: List[str]) -> Dict[str, Any]:
        """
        Check if specified columns have unique values (no duplicates).

        Args:
            unique_columns: List of columns that should have unique values

        Returns:
            Dictionary with check results
        """
        duplicate_data = {}

        for col in unique_columns:
            if col in self.df.columns:
                duplicate_count = self.df[col].duplicated().sum()
                if duplicate_count > 0:
                    duplicate_data[col] = duplicate_count
                    self.issues.append(f"Column '{col}' has {duplicate_count} duplicate values")

        return {
            'check': 'uniqueness',
            'passed': len(duplicate_data) == 0,
            'duplicates': duplicate_data
        }

    def check_email_validity(self, email_column: str) -> Dict[str, Any]:
        """
        Validate email addresses using regex.

        Args:
            email_column: Name of the column containing email addresses

        Returns:
            Dictionary with check results
        """
        if email_column not in self.df.columns:
            return {'check': 'email_validity', 'passed': False, 'error': 'Column not found'}

        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        # Check for non-null emails
        emails = self.df[email_column].dropna()
        invalid_emails = ~emails.astype(str).str.match(email_pattern)
        invalid_count = invalid_emails.sum()

        if invalid_count > 0:
            self.issues.append(f"{invalid_count} invalid email addresses found")

        return {
            'check': 'email_validity',
            'passed': invalid_count == 0,
            'invalid_count': invalid_count
        }

    def check_numeric_range(self, column: str, min_value: float = None,
                           max_value: float = None) -> Dict[str, Any]:
        """
        Check if numeric values are within expected range.

        Args:
            column: Name of numeric column
            min_value: Minimum acceptable value
            max_value: Maximum acceptable value

        Returns:
            Dictionary with check results
        """
        if column not in self.df.columns:
            return {'check': 'numeric_range', 'passed': False, 'error': 'Column not found'}

        issues_found = 0

        if min_value is not None:
            below_min = (self.df[column] < min_value).sum()
            if below_min > 0:
                issues_found += below_min
                self.issues.append(f"{below_min} values in '{column}' below minimum {min_value}")

        if max_value is not None:
            above_max = (self.df[column] > max_value).sum()
            if above_max > 0:
                issues_found += above_max
                self.issues.append(f"{above_max} values in '{column}' above maximum {max_value}")

        return {
            'check': 'numeric_range',
            'passed': issues_found == 0,
            'out_of_range_count': issues_found
        }

    def check_date_validity(self, date_column: str, future_allowed: bool = False) -> Dict[str, Any]:
        """
        Check if dates are valid and optionally not in the future.

        Args:
            date_column: Name of the date column
            future_allowed: Whether future dates are acceptable

        Returns:
            Dictionary with check results
        """
        if date_column not in self.df.columns:
            return {'check': 'date_validity', 'passed': False, 'error': 'Column not found'}

        try:
            dates = pd.to_datetime(self.df[date_column], errors='coerce')
            invalid_dates = dates.isnull().sum()

            future_dates = 0
            if not future_allowed:
                future_dates = (dates > pd.Timestamp.now()).sum()
                if future_dates > 0:
                    self.issues.append(f"{future_dates} dates in future found in '{date_column}'")

            if invalid_dates > 0:
                self.issues.append(f"{invalid_dates} invalid dates in '{date_column}'")

            return {
                'check': 'date_validity',
                'passed': invalid_dates == 0 and future_dates == 0,
                'invalid_dates': invalid_dates,
                'future_dates': future_dates
            }

        except Exception as e:
            return {'check': 'date_validity', 'passed': False, 'error': str(e)}

    def generate_report(self) -> str:
        """
        Generate a summary report of all quality issues found.

        Returns:
            String containing the quality report
        """
        report = f"\n{'='*60}\n"
        report += "DATA QUALITY REPORT\n"
        report += f"{'='*60}\n"
        report += f"Total Records: {len(self.df)}\n"
        report += f"Total Columns: {len(self.df.columns)}\n"
        report += f"Issues Found: {len(self.issues)}\n"
        report += f"{'='*60}\n\n"

        if self.issues:
            report += "ISSUES:\n"
            for i, issue in enumerate(self.issues, 1):
                report += f"{i}. {issue}\n"
        else:
            report += "No data quality issues found!\n"

        report += f"\n{'='*60}\n"

        return report


def validate_email(email: str) -> bool:
    """
    Validate a single email address.

    Args:
        email: Email address string

    Returns:
        True if valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, str(email)))


def remove_duplicates(df: pd.DataFrame, subset: List[str] = None) -> pd.DataFrame:
    """
    Remove duplicate rows from DataFrame.

    Args:
        df: Input DataFrame
        subset: List of columns to consider for duplicates

    Returns:
        DataFrame with duplicates removed
    """
    initial_count = len(df)
    df_clean = df.drop_duplicates(subset=subset)
    removed_count = initial_count - len(df_clean)

    if removed_count > 0:
        logger.info(f"Removed {removed_count} duplicate records")

    return df_clean


def handle_missing_values(df: pd.DataFrame, strategy: str = 'drop',
                         fill_value: Any = None) -> pd.DataFrame:
    """
    Handle missing values in DataFrame.

    Args:
        df: Input DataFrame
        strategy: 'drop', 'fill', or 'forward_fill'
        fill_value: Value to use when strategy is 'fill'

    Returns:
        DataFrame with missing values handled
    """
    if strategy == 'drop':
        return df.dropna()
    elif strategy == 'fill':
        return df.fillna(fill_value)
    elif strategy == 'forward_fill':
        return df.fillna(method='ffill')
    else:
        raise ValueError(f"Unknown strategy: {strategy}")


# Example usage
if __name__ == "__main__":
    # Create sample data
    sample_data = {
        'id': [1, 2, 3, 3, 5],
        'email': ['valid@email.com', 'invalid-email', 'test@example.com', 'test@example.com', None],
        'amount': [100, -50, 200, 200, 500],
        'date': ['2024-01-01', '2026-12-31', '2024-03-15', '2024-03-15', 'invalid-date']
    }

    df = pd.DataFrame(sample_data)

    # Run quality checks
    checker = DataQualityChecker(df)
    checker.check_completeness(['id', 'email', 'amount'])
    checker.check_uniqueness(['id'])
    checker.check_email_validity('email')
    checker.check_numeric_range('amount', min_value=0)
    checker.check_date_validity('date', future_allowed=False)

    # Print report
    print(checker.generate_report())
