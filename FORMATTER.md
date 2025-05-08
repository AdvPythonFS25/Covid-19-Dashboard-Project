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

************* Module countryOrRegionWrapper
countryOrRegionWrapper.py:1:19: C0303: Trailing whitespace (trailing-whitespace)
countryOrRegionWrapper.py:6:63: C0303: Trailing whitespace (trailing-whitespace)
countryOrRegionWrapper.py:8:0: C0303: Trailing whitespace (trailing-whitespace)
countryOrRegionWrapper.py:10:69: C0303: Trailing whitespace (trailing-whitespace)
countryOrRegionWrapper.py:12:0: C0303: Trailing whitespace (trailing-whitespace)
countryOrRegionWrapper.py:14:69: C0303: Trailing whitespace (trailing-whitespace)
countryOrRegionWrapper.py:16:0: C0303: Trailing whitespace (trailing-whitespace)
countryOrRegionWrapper.py:18:0: C0301: Line too long (104/100) (line-too-long)
countryOrRegionWrapper.py:21:0: C0305: Trailing newlines (trailing-newlines)
countryOrRegionWrapper.py:1:0: C0114: Missing module docstring (missing-module-docstring)
countryOrRegionWrapper.py:1:0: C0103: Module name "countryOrRegionWrapper" doesn't conform to snake_case naming style (invalid-name)
countryOrRegionWrapper.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
countryOrRegionWrapper.py:3:0: R0913: Too many arguments (7/5) (too-many-arguments)
countryOrRegionWrapper.py:3:0: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
countryOrRegionWrapper.py:5:4: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
countryOrRegionWrapper.py:1:0: W0611: Unused pandas imported as pd (unused-import)

-----------------------------------
Your code has been rated at 0.00/10
```

## Fixed Issues

We've fixed the following 5 issues reported by pylint:

###  1. Added proper DocString to function
```python
************* Module deathRate
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

###  2. Removed trailing white spaces  
```python
#Before
************* Module deathRate
#filter by date range
df_filtered = df_region[(df_region["Date_reported"] >= start_date) & (df_region["Date_reported"] <= end_date)]
   #There were trailing white spaces here
#Return average Rt and last Rt in date range per country
averages = df_filtered.groupby('WHO_region').agg(AverageDeathRate =('death_rate', 'mean')).reset_index()

# After
#filter by date range
df_filtered = df_region[(df_region["Date_reported"] >= start_date) & (df_region["Date_reported"] <= end_date)]

#Return average Rt and last Rt in date range per country
averages = df_filtered.groupby('WHO_region').agg(AverageDeathRate =('death_rate', 'mean')).reset_index()
```

###  3. Removed unused import
```python
# Before
************* Module countryOrRegionWrapper
import pandas as pd
# After

```

###  4. Fixed singleton comparison with None
```python
#Before

#After
```

###  5. Removed unnecessary parentheses in if statements
```python
# After

```
## Result Pylint Score
**********Moodule deathRate
Your code has been rated at 6.67/10
**********Moodule rtStatistics
Your code has been rated at 6.45/10
************* Module countryOrRegionWrapper
Your code has been rated at 2.50/10



