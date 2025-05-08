# Pylint Code Improvements

## Original Pylint Output

```
************* Module deathRate
deathRate.py:1:19: C0303: Trailing whitespace (trailing-whitespace)
deathRate.py:17:0: C0301: Line too long (168/100) (line-too-long)
deathRate.py:20:0: C0301: Line too long (123/100) (line-too-long)
deathRate.py:21:0: C0303: Trailing whitespace (trailing-whitespace)
deathRate.py:23:0: C0301: Line too long (105/100) (line-too-long)
deathRate.py:38:0: C0301: Line too long (162/100) (line-too-long)
deathRate.py:41:0: C0301: Line too long (114/100) (line-too-long)
deathRate.py:42:0: C0303: Trailing whitespace (trailing-whitespace)
deathRate.py:44:0: C0301: Line too long (108/100) (line-too-long)
deathRate.py:1:0: C0114: Missing module docstring (missing-module-docstring)
deathRate.py:1:0: C0103: Module name "deathRate" doesn't conform to snake_case naming style (invalid-name)
deathRate.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
deathRate.py:27:0: C0116: Missing function or method docstring (missing-function-docstring)
deathRate.py:48:0: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 4.17/10
```

## Fixed Issues

We've fixed the following 5 issues reported by pylint:

###  1. Added proper DocString to function
```python
# Before
def death_rate_country(df, country_names, start_date, end_date):
    ...
    return averages, df_filtered

# After
def death_rate_country(df, country_names, start_date, end_date):
    """Calculate death rate by region

    Args:
        df (Pandas dataframe)
        country_names (List)
        start_date (Datetime obj)
        end_date (Datetime obj)

    Returns:
        Value, Dataframe: 
    """

```

###  2. Added proper docstring to function
```python
# Before
# DEATH RATE CALCULATION FUNCTION COUNTRY CODE BASED
# Death rate = Deaths / Cases * 100
# This function will calculate the death rate for a given list of country codes (e.g., ['US', 'DE']). 2 letter code
def deathRateCountry(df, country_codes):
    if country_codes is None or len(country_codes) == 0:
        return None

# After
def deathRateCountry(df, country_codes):
    """
    Calculate the death rate (CFR) for a given list of country codes.
    
    Death rate = (Cumulative deaths / Cumulative cases) * 100
    
    Args:
        df (DataFrame): DataFrame containing COVID-19 data
        country_codes (list): List of 2-letter country codes (e.g., ['US', 'DE'])
    
    Returns:
        Series: A Series with country codes as index and death rates as values
               Returns None if country_codes is None, empty, or no valid codes found
    """
    if country_codes is None or len(country_codes) == 0:
        return None
```

###  3. Renamed function and parameters to follow snake_case naming convention
```python
# Before
def DataBaseValidator(df, arrayTouse, columnChecked):
    validArray = []
    if columnChecked not in df.columns:
        return None
    if not df[columnChecked].isin(arrayTouse).all():
        for c in arrayTouse:
            if c not in df[columnChecked].unique():
                print(f"{c} is not in the dataframe")
            else:
                validArray.append(c)
    return validArray

# After
def database_validator(df, array_to_use, column_checked):
    """
    Validates which items in the input array exist in the specified column of the dataframe.
    
    Args:
        df (DataFrame): The dataframe to check against
        array_to_use (list): List of values to validate
        column_checked (str): Name of the column to check for values
        
    Returns:
        list: List of valid values that exist in the dataframe column
        None: If the column doesn't exist in the dataframe
    """
    valid_array = []
    if column_checked not in df.columns:
        return None
    if not df[column_checked].isin(array_to_use).all():
        for c in array_to_use:
            if c not in df[column_checked].unique():
                print(f"{c} is not in the dataframe")
            else:
                valid_array.append(c)
    return valid_array
```

###  4. Fixed singleton comparison with None
```python
# Before
def vaccinationCoverageISO3(df, ISO3_countries):
    if ISO3_countries == None or len(ISO3_countries) == 0:
        return None
    # Check if the all countries are in the dataframe
    fixedDF = df.copy()
    fixedDF = fixedDF.rename(columns={"COUNTRY": "Country"})
    validated_countries = database_validator(fixedDF, ISO3_countries, "ISO3")
    if validated_countries == None or len(validated_countries) == 0:
        return None

# After
def vaccinationCoverageISO3(df, ISO3_countries):
    if ISO3_countries is None or len(ISO3_countries) == 0:
        return None
    # Check if the all countries are in the dataframe
    fixedDF = df.copy()
    fixedDF = fixedDF.rename(columns={"COUNTRY": "Country"})
    validated_countries = database_validator(fixedDF, ISO3_countries, "ISO3")
    if validated_countries is None or len(validated_countries) == 0:
        return None
```

###  5. Removed unnecessary parentheses in if statements
```python
# Before
def averageDailyCases(df, country_codes, start_date, end_date=None):
    # ...
    df_countries_filtered = df_countries[
        (df_countries["Date_reported"] >= start_date) & (df_countries["Date_reported"] <= end_date)]
    if (df_countries_filtered.empty):
        print("Could not find any countries within the date range")
        return None

# After
def averageDailyCases(df, country_codes, start_date, end_date=None):
    # ...
    df_countries_filtered = df_countries[
        (df_countries["Date_reported"] >= start_date) & (df_countries["Date_reported"] <= end_date)]
    if df_countries_filtered.empty:
        print("Could not find any countries within the date range")
        return None
```
## Result Pylint Score
Your code has been rated at 6.02/10

