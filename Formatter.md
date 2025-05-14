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

************* Module streamlitApp
streamlitApp.py:3:19: C0303: Trailing whitespace (trailing-whitespace)
streamlitApp.py:17:0: C0303: Trailing whitespace (trailing-whitespace)
streamlitApp.py:21:59: C0303: Trailing whitespace (trailing-whitespace)
streamlitApp.py:24:125: C0303: Trailing whitespace (trailing-whitespace)
streamlitApp.py:24:0: C0301: Line too long (125/100) (line-too-long)
streamlitApp.py:25:0: C0303: Trailing whitespace (trailing-whitespace)
streamlitApp.py:34:26: C0303: Trailing whitespace (trailing-whitespace)
streamlitApp.py:38:28: C0303: Trailing whitespace (trailing-whitespace)
streamlitApp.py:45:0: C0301: Line too long (106/100) (line-too-long)
streamlitApp.py:47:39: C0303: Trailing whitespace (trailing-whitespace)
streamlitApp.py:58:39: C0303: Trailing whitespace (trailing-whitespace)
streamlitApp.py:65:42: C0303: Trailing whitespace (trailing-whitespace)
streamlitApp.py:76:0: C0301: Line too long (109/100) (line-too-long)
streamlitApp.py:82:44: C0303: Trailing whitespace (trailing-whitespace)
streamlitApp.py:88:43: C0303: Trailing whitespace (trailing-whitespace)
streamlitApp.py:99:0: C0301: Line too long (133/100) (line-too-long)
streamlitApp.py:101:0: C0303: Trailing whitespace (trailing-whitespace)
streamlitApp.py:1:0: C0114: Missing module docstring (missing-module-docstring)
streamlitApp.py:1:0: C0103: Module name "streamlitApp" doesn't conform to snake_case naming style (invalid-name)
streamlitApp.py:4:0: W0401: Wildcard import rtStatistics (wildcard-import)
streamlitApp.py:5:0: W0401: Wildcard import deathRate (wildcard-import)
streamlitApp.py:6:0: W0401: Wildcard import importData (wildcard-import)
streamlitApp.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)
streamlitApp.py:23:4: W0621: Redefining name 'start_date' from outer scope (line 104) (redefined-outer-name)
streamlitApp.py:24:4: W0621: Redefining name 'end_date' from outer scope (line 104) (redefined-outer-name)
streamlitApp.py:31:0: C0116: Missing function or method docstring (missing-function-docstring)
streamlitApp.py:39:4: W0621: Redefining name 'who_regions' from outer scope (line 105) (redefined-outer-name)
streamlitApp.py:56:0: C0116: Missing function or method docstring (missing-function-docstring)
streamlitApp.py:79:0: C0116: Missing function or method docstring (missing-function-docstring)
streamlitApp.py:2:0: C0411: standard import "os" should be placed before third party import "streamlit" (wrong-import-order)
streamlitApp.py:4:0: W0614: Unused import(s) np, rt_country, rt_region and country_or_region from wildcard import of rtStatistics (unused-wildcard-import)
streamlitApp.py:5:0: W0614: Unused import(s) death_rate_country and death_rate_region from wildcard import of deathRate (unused-wildcard-import)
streamlitApp.py:6:0: W0614: Unused import(s) requests, DataImporter, url, filename and global_daily_data_object from wildcard import of importData (unused-wildcard-import)

************* Module importData
importData.py:2:19: C0303: Trailing whitespace (trailing-whitespace)
importData.py:3:9: C0303: Trailing whitespace (trailing-whitespace)
importData.py:29:61: C0303: Trailing whitespace (trailing-whitespace)
importData.py:33:41: C0303: Trailing whitespace (trailing-whitespace)
importData.py:1:0: C0114: Missing module docstring (missing-module-docstring)
importData.py:1:0: C0103: Module name "importData" doesn't conform to snake_case naming style (invalid-name)
importData.py:11:23: W0621: Redefining name 'url' from outer scope (line 36) (redefined-outer-name)
importData.py:11:28: W0621: Redefining name 'filename' from outer scope (line 37) (redefined-outer-name)
importData.py:19:4: C0116: Missing function or method docstring (missing-function-docstring)
importData.py:22:4: C0116: Missing function or method docstring (missing-function-docstring)
importData.py:25:19: W3101: Missing timeout argument for method 'requests.get' can cause your program to hang indefinitely (missing-timeout)
importData.py:31:4: C0116: Missing function or method docstring (missing-function-docstring)
importData.py:36:0: C0103: Constant name "url" doesn't conform to UPPER_CASE naming style (invalid-name)
importData.py:37:0: C0103: Constant name "filename" doesn't conform to UPPER_CASE naming style (invalid-name)
importData.py:3:0: C0411: standard import "os" should be placed before third party import "pandas" (wrong-import-order)
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

###  4. Improved import order
```python
#Before
************* Module streamlitApp
import streamlit as st
import os

#After
import os
import streamlit as st
```

###  5. Rename constants to conform to naming conventions
```python
************* Module importData
#Before
url = 'https://srhdpeuwpubsa.blob.core.windows.net/whdh/COVID/WHO-COVID-19-global-daily-data.csv'
filename = "WHO-COVID-19-global-daily-data.csv"

# After
URL = 'https://srhdpeuwpubsa.blob.core.windows.net/whdh/COVID/WHO-COVID-19-global-daily-data.csv'
FILENAME = "WHO-COVID-19-global-daily-data.csv"

```
## Result Pylint Score
**********Module deathRate  
Your code has been rated at 6.67/10  
   
**********Module rtStatistics  
Your code has been rated at 6.45/10  
  
************* Module countryOrRegionWrapper  
Your code has been rated at 2.50/10  
  
************* Module streamlitApp  
Your code has been rated at 5.65/10  

************* Module importData   
Your code has been rated at 6.40/10




