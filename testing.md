# COVID-19 Dashboard Unit Testing Documentation

## Overview

This document describes the unit tests implemented for the COVID-19 Dashboard project, focusing on functions that could potentially produce unexpected results. The unit tests are designed to ensure these functions handle edge cases correctly and produce reliable outputs.

## Key Functions Being Tested

### 1. database_validator

**Potential unexpected results:**
- The function is responsible for validating if input values exist in a specified column of a dataframe. 
- If a user provides invalid country codes, region names, or other identifiers, this could lead to empty results or processing errors.
- The function might need to handle cases where the specified column doesn't exist in the dataframe.

**Test cases:**
- Test with valid inputs: All inputs exist in the specified column
- Test with invalid inputs: Some inputs don't exist in the specified column
- Test with a nonexistent column: The specified column doesn't exist

### 2. dateRangeValidator

**Potential unexpected results:**
- The function is designed to validate date ranges and adjust them to the closest available dates in the dataset.
- If a user provides dates outside the range of the available data, this could lead to empty results.
- If a user provides invalid date formats, this could cause errors.
- If the start date is after the end date, this could produce unexpected behavior.

**Test cases:**
- Test with valid dates: Dates within the range of the dataset
- Test with out-of-range dates: Dates outside the range of the dataset
- Test with swapped dates: Start date later than end date (should be automatically fixed)

### 3. deathRateCountry

**Potential unexpected results:**
- This function calculates death rates for specified countries as (deaths/cases)*100.
- If a country has zero cases, this would lead to a division by zero error.
- If invalid country codes are provided, the function might return empty or incomplete results.
- The calculation might produce unexpected results if there are inconsistencies in the cumulative data.

**Test cases:**
- Test with valid country codes: Should calculate death rates correctly
- Test the calculation logic: Verify that the death rate calculation matches the expected formula
- Test with zero cases: Verify the function handles division by zero gracefully when a country has zero cases but some deaths

### 4. timeIntervalData

**Potential unexpected results:**
- This function filters data based on date ranges and specific identifiers.
- If the data_wanted column doesn't exist, this could lead to errors.
- If the date range doesn't contain any data, the function might return empty results.
- If invalid identifiers are provided, the function might process only a subset of the requested data.

**Test cases:**
- Test the basic functionality: Verify that data is correctly filtered by date range and identifiers
- Test with nonexistent data column: Verify the function handles this scenario gracefully by returning None
- Test with edge dates: Verify the function handles boundary dates correctly

## Critical Edge Case: Division by Zero in Death Rate Calculation

One particularly important edge case we've tested is what happens when a country has zero reported cases but some reported deaths. This could occur due to:

1. Data collection issues or reporting delays
2. Misclassification of deaths
3. Deaths being attributed to COVID-19 after the fact, without corresponding case counts

In the `deathRateCountry` function, this scenario would lead to a division by zero when calculating the death rate as (deaths/cases)*100. Our test verifies that the function handles this gracefully by either:

1. Returning NaN or Infinity for the affected country, or
2. Excluding the country from the results entirely

Both approaches prevent the function from crashing with a division by zero error and allow the rest of the data to be processed correctly.

## Test Implementation Strategy

The unit tests use Python's unittest framework to systematically test each function with various inputs. The tests use a synthetic dataset created in the setUp method, which provides a controlled environment for testing without requiring access to the real COVID-19 data files.

Each test method focuses on a specific aspect of a function's behavior, with assertions to verify that the output matches the expected results. This helps identify any discrepancies or bugs in the implementation.

## Running the Tests

To run the tests, execute the `test_covid_functions.py` file:

```python
python test_covid_functions.py
```

The tests will report any failures, which would indicate potential issues in the implementation of the tested functions. 