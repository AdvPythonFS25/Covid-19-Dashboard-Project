import unittest
import pandas as pd
import numpy as np
from maincode import (
    dateRangeValidator,
    database_validator,
    deathRateCountry,
    timeIntervalData
)

class TestCovidFunctions(unittest.TestCase):
    """
    Unit tests for the COVID-19 Dashboard functions.
    
    These tests focus on functions that could potentially produce unexpected results,
    including edge cases like:
    - Invalid input validation
    - Date range validation
    - Division by zero in death rate calculations
    - Processing of nonexistent data columns
    
    The tests use a synthetic dataset created in the setUp method, which provides
    a controlled environment for testing without requiring access to the real
    COVID-19 data files.
    """
    
    def setUp(self):
        # Create sample test data
        dates = pd.date_range(start='2020-01-01', end='2020-03-01')
        countries = ['US', 'UK', 'FR', 'DE']
        
        data = []
        for date in dates:
            for country in countries:
                # Generate some random data for testing
                cases = np.random.randint(100, 5000)
                new_cases = np.random.randint(10, 500)
                deaths = np.random.randint(1, 100)
                new_deaths = np.random.randint(0, 20)
                
                data.append({
                    'Date_reported': date,
                    'Country_code': country,
                    'Country': {'US': 'United States', 'UK': 'United Kingdom', 'FR': 'France', 'DE': 'Germany'}[country],
                    'WHO_region': 'EURO' if country in ['UK', 'FR', 'DE'] else 'AMRO',
                    'New_cases': new_cases,
                    'Cumulative_cases': cases,
                    'New_deaths': new_deaths,
                    'Cumulative_deaths': deaths
                })
        
        # Add an edge case: a country with zero cases but some deaths
        data.append({
            'Date_reported': pd.to_datetime('2020-03-01'),
            'Country_code': 'ZZ',
            'Country': 'Test Country',
            'WHO_region': 'TEST',
            'New_cases': 0,
            'Cumulative_cases': 0,  # Zero cases
            'New_deaths': 5,
            'Cumulative_deaths': 5  # But some deaths
        })
        
        self.test_df = pd.DataFrame(data)
    
    def test_database_validator_valid_inputs(self):
        """Test that database_validator correctly identifies valid inputs."""
        valid_countries = ['US', 'UK', 'FR']
        result = database_validator(self.test_df, valid_countries, 'Country_code')
        self.assertEqual(result, valid_countries)
    
    def test_database_validator_invalid_inputs(self):
        """Test that database_validator correctly handles invalid inputs."""
        countries = ['US', 'INVALID', 'FR']
        result = database_validator(self.test_df, countries, 'Country_code')
        self.assertEqual(result, ['US', 'FR'])
    
    def test_database_validator_nonexistent_column(self):
        """Test that database_validator handles nonexistent columns properly."""
        countries = ['US', 'UK', 'FR']
        result = database_validator(self.test_df, countries, 'NonExistentColumn')
        self.assertIsNone(result)
    
    def test_dateRangeValidator_valid_dates(self):
        """Test dateRangeValidator with valid date inputs."""
        start_date = '2020-01-15'
        end_date = '2020-02-15'
        result_start, result_end = dateRangeValidator(self.test_df, start_date, end_date)
        
        expected_start = pd.to_datetime('2020-01-15')
        expected_end = pd.to_datetime('2020-02-15')
        
        self.assertEqual(result_start, expected_start)
        self.assertEqual(result_end, expected_end)
    
    def test_dateRangeValidator_out_of_range_dates(self):
        """Test dateRangeValidator with out-of-range dates."""
        # Dates outside the range of our test data
        start_date = '2019-01-01'  # Before our data range
        end_date = '2021-01-01'    # After our data range
        
        result_start, result_end = dateRangeValidator(self.test_df, start_date, end_date)
        
        # Should be adjusted to the min/max dates in our dataset
        expected_start = self.test_df['Date_reported'].min()
        expected_end = self.test_df['Date_reported'].max()
        
        self.assertEqual(result_start, expected_start)
        self.assertEqual(result_end, expected_end)

    def test_dateRangeValidator_swapped_dates(self):
        """Test dateRangeValidator when start_date is after end_date."""
        # Start date is after end date
        start_date = '2020-02-15'
        end_date = '2020-01-15'
        
        result_start, result_end = dateRangeValidator(self.test_df, start_date, end_date)
        
        # According to the implementation, start_date should be reset to the minimum date
        expected_start = self.test_df['Date_reported'].min()
        expected_end = pd.to_datetime('2020-01-15')
        
        self.assertEqual(result_start, expected_start)
        self.assertEqual(result_end, expected_end)
    
    def test_deathRateCountry_calculation(self):
        """Test that deathRateCountry correctly calculates death rates."""
        result = deathRateCountry(self.test_df, ['US', 'UK'])
        
        # Check the result has the right format
        self.assertIsInstance(result, pd.Series)
        self.assertEqual(result.name, 'Death Rate')
        self.assertEqual(set(result.index), {'US', 'UK'})
        
        # Verify calculation logic for a specific country
        latest_us_data = self.test_df[self.test_df['Country_code'] == 'US'].sort_values('Date_reported').iloc[-1]
        expected_us_rate = (latest_us_data['Cumulative_deaths'] / latest_us_data['Cumulative_cases']) * 100
        self.assertAlmostEqual(result['US'], expected_us_rate)
    
    def test_deathRateCountry_zero_cases(self):
        """Test that deathRateCountry handles countries with zero cases but some deaths."""
        # This test checks if the function handles division by zero gracefully
        result = deathRateCountry(self.test_df, ['ZZ'])
        
        # If the function handles this case by returning NaN or None, test accordingly
        if result is not None and not result.empty:
            self.assertTrue(pd.isna(result['ZZ']) or np.isinf(result['ZZ']))
        else:
            # If the function returns None or empty result for invalid cases, that's acceptable too
            self.assertTrue(result is None or result.empty)
    
    def test_timeIntervalData_functionality(self):
        """Test that timeIntervalData correctly filters data."""
        country_codes = ['US', 'UK']
        start_date = '2020-01-15'
        end_date = '2020-02-15'
        
        result = timeIntervalData(
            self.test_df, 
            country_codes, 
            start_date, 
            end_date, 
            'Date_reported', 
            'Country_code', 
            'New_cases'
        )
        
        # Check that the result contains only the requested columns
        self.assertEqual(set(result.columns), {'Date_reported', 'Country_code', 'New_cases'})
        
        # Check that only the requested countries are included
        self.assertEqual(set(result['Country_code'].unique()), set(country_codes))
        
        # Check date range
        min_date = result['Date_reported'].min()
        max_date = result['Date_reported'].max()
        self.assertGreaterEqual(min_date, pd.to_datetime(start_date))
        self.assertLessEqual(max_date, pd.to_datetime(end_date))
    
    def test_timeIntervalData_nonexistent_column(self):
        """Test that timeIntervalData handles nonexistent data columns properly."""
        country_codes = ['US', 'UK']
        start_date = '2020-01-15'
        end_date = '2020-02-15'
        
        result = timeIntervalData(
            self.test_df, 
            country_codes, 
            start_date, 
            end_date, 
            'Date_reported', 
            'Country_code', 
            'NonexistentColumn'  # This column doesn't exist
        )
        
        # The function should return None or an appropriate error indicator
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main() 