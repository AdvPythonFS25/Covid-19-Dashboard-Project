import unittest
import pandas as pd
import numpy as np
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from deathRate import death_rate_country

class TestCovidFunctions(unittest.TestCase):
    """
    Unit tests for the COVID-19 Dashboard functions.
    
    These tests focus on functions that could potentially produce unexpected results,
    including edge cases like:
    - Division by zero in death rate calculations
    - Date range validation
    - Data filtering
    
    The tests use a synthetic dataset created in the setUp method, which provides
    a controlled environment for testing without requiring access to the real
    COVID-19 data files.
    """
    
    def setUp(self):
        # Create sample test data
        dates = pd.date_range(start='2020-01-01', end='2020-03-01')
        countries = ['United States', 'United Kingdom', 'France', 'Germany']
        
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
                    'Country': country,
                    'Country_code': {'United States': 'US', 'United Kingdom': 'UK', 'France': 'FR', 'Germany': 'DE'}[country],
                    'WHO_region': 'EURO' if country in ['United Kingdom', 'France', 'Germany'] else 'AMRO',
                    'New_cases': new_cases,
                    'Cumulative_cases': cases,
                    'New_deaths': new_deaths,
                    'Cumulative_deaths': deaths
                })
        
        # Add an edge case: a country with zero cases but some deaths
        data.append({
            'Date_reported': pd.to_datetime('2020-03-01'),
            'Country': 'Test Country',
            'Country_code': 'ZZ',
            'WHO_region': 'TEST',
            'New_cases': 0,
            'Cumulative_cases': 0,  # Zero cases
            'New_deaths': 5,
            'Cumulative_deaths': 5  # But some deaths
        })
        
        self.test_df = pd.DataFrame(data)
    
    def test_death_rate_country_calculation(self):
        """Test that death_rate_country correctly calculates death rates."""
        countries = ['United States', 'United Kingdom']
        start_date = '2020-01-15'
        end_date = '2020-02-15'
        
        result, filtered_data = death_rate_country(
            self.test_df, 
            countries, 
            start_date, 
            end_date
        )
        
        # Check the result has the right format
        self.assertIsInstance(result, pd.DataFrame)
        self.assertTrue('AverageDeathRate' in result.columns)
        self.assertTrue('Country' in result.columns)
        
        # Check that only the requested countries are included
        self.assertEqual(set(result['Country']), set(countries))
        
        # Manually calculate and verify for one country
        us_data = filtered_data[filtered_data['Country'] == 'United States']
        expected_avg_rate = us_data['death_rate'].mean()
        actual_avg_rate = result[result['Country'] == 'United States']['AverageDeathRate'].values[0]
        self.assertAlmostEqual(actual_avg_rate, expected_avg_rate)
    
    def test_death_rate_country_zero_cases(self):
        """Test that death_rate_country handles countries with zero cases but some deaths."""
        countries = ['Test Country']  # Our edge case country
        start_date = '2020-01-01'
        end_date = '2020-03-01'
        
        result, filtered_data = death_rate_country(
            self.test_df, 
            countries, 
            start_date, 
            end_date
        )
        
        # Check that the country is included in the result
        self.assertTrue('Test Country' in result['Country'].values)
        
        # The function should handle division by zero gracefully by setting it to 0
        # as specified in the function implementation
        test_country_rate = result[result['Country'] == 'Test Country']['AverageDeathRate'].values[0]
        self.assertEqual(test_country_rate, 0.0)
    
    def test_death_rate_country_date_filtering(self):
        """Test that death_rate_country correctly filters by date."""
        countries = ['United States']
        start_date = '2020-01-15'
        end_date = '2020-02-15'
        
        result, filtered_data = death_rate_country(
            self.test_df, 
            countries, 
            start_date, 
            end_date
        )
        
        # Check date range of filtered data
        min_date = filtered_data['Date_reported'].min()
        max_date = filtered_data['Date_reported'].max()
        self.assertGreaterEqual(min_date, pd.to_datetime(start_date))
        self.assertLessEqual(max_date, pd.to_datetime(end_date))
    
    def test_death_rate_country_nonexistent_country(self):
        """Test that death_rate_country handles nonexistent countries properly."""
        countries = ['Nonexistent Country']
        start_date = '2020-01-15'
        end_date = '2020-02-15'
        
        result, filtered_data = death_rate_country(
            self.test_df, 
            countries, 
            start_date, 
            end_date
        )
        
        # Should return an empty DataFrame if country doesn't exist
        self.assertTrue(result.empty)
        self.assertTrue(filtered_data.empty)

if __name__ == '__main__':
    unittest.main() 