# COVID-19 Dashboard Unit Testing Documentation

## Overview

This document describes the unit tests implemented for the COVID-19 Dashboard project, focusing on functions that could potentially produce unexpected results. The unit tests are designed to ensure these functions handle edge cases correctly and produce reliable outputs.

## Key Functions Being Tested

### death_rate_country

**Potential unexpected results:**
- This function calculates death rates for specified countries as (deaths/cases)*100.
- If a country has zero cases, this would lead to a division by zero error.
- If invalid country names are provided, the function might return empty or incomplete results.
- The calculation might produce unexpected results if there are inconsistencies in the cumulative data.

**Test cases:**
- `test_death_rate_country_calculation`: Verifies that death rates are calculated correctly
- `test_death_rate_country_zero_cases`: Tests the function with a country that has zero cases but some deaths
- `test_death_rate_country_date_filtering`: Verifies date filtering works properly
- `test_death_rate_country_nonexistent_country`: Tests how the function handles nonexistent countries

## Critical Edge Case: Division by Zero in Death Rate Calculation

One particularly important edge case we've tested is what happens when a country has zero reported cases but some reported deaths. This could occur due to:

1. Data collection issues or reporting delays
2. Misclassification of deaths
3. Deaths being attributed to COVID-19 after the fact, without corresponding case counts

In the `death_rate_country` function, this scenario would lead to a division by zero when calculating the death rate as (deaths/cases)*100. 

The function uses a lambda function to handle this case:
```python
df_countries['death_rate'] = df_countries.apply(lambda row: ((row['Cumulative_deaths']/row['Cumulative_cases'])*100) if row['Cumulative_cases'] > 0 else 0, axis= 1)
```

Our test `test_death_rate_country_zero_cases` verifies that the function handles this gracefully by returning 0 for the affected country's death rate, preventing division by zero errors and allowing the rest of the data to be processed correctly.

## Test Implementation Strategy

The unit tests use Python's unittest framework to systematically test the function with various inputs. The tests use a synthetic dataset created in the setUp method, which provides a controlled environment for testing without requiring access to the real COVID-19 data files.

Each test method focuses on a specific aspect of the function's behavior, with assertions to verify that the output matches the expected results. This helps identify any discrepancies or bugs in the implementation.

## Running the Tests

To run the tests, execute:

```python
python -m unittest tests/test_covid_functions.py
```

The tests will report any failures, which would indicate potential issues in the implementation of the tested functions. 