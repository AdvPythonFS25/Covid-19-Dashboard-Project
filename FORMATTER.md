# Pylint Code Improvements

## Original Pylint Output

```
************* Module maincode
maincode.py:10:0: C0301: Line too long (107/100) (line-too-long)
maincode.py:11:0: C0301: Line too long (107/100) (line-too-long)
maincode.py:12:0: C0301: Line too long (107/100) (line-too-long)
maincode.py:13:0: C0301: Line too long (107/100) (line-too-long)
maincode.py:14:0: C0301: Line too long (107/100) (line-too-long)
maincode.py:22:0: C0301: Line too long (111/100) (line-too-long)
maincode.py:30:0: C0301: Line too long (116/100) (line-too-long)
maincode.py:31:0: C0301: Line too long (117/100) (line-too-long)
maincode.py:32:0: C0301: Line too long (112/100) (line-too-long)
maincode.py:33:0: C0301: Line too long (134/100) (line-too-long)
maincode.py:57:0: C0301: Line too long (136/100) (line-too-long)
maincode.py:59:0: C0301: Line too long (102/100) (line-too-long)
maincode.py:307:0: C0301: Line too long (107/100) (line-too-long)
maincode.py:308:0: C0301: Line too long (107/100) (line-too-long)
maincode.py:309:0: C0301: Line too long (107/100) (line-too-long)
maincode.py:310:0: C0301: Line too long (107/100) (line-too-long)
maincode.py:311:0: C0301: Line too long (107/100) (line-too-long)
maincode.py:314:0: C0301: Line too long (107/100) (line-too-long)
maincode.py:315:0: C0301: Line too long (107/100) (line-too-long)
maincode.py:316:0: C0301: Line too long (107/100) (line-too-long)
maincode.py:317:0: C0301: Line too long (107/100) (line-too-long)
maincode.py:318:0: C0301: Line too long (107/100) (line-too-long)
maincode.py:350:0: C0301: Line too long (110/100) (line-too-long)
maincode.py:351:0: C0301: Line too long (102/100) (line-too-long)
maincode.py:371:0: C0301: Line too long (116/100) (line-too-long)
maincode.py:385:0: C0301: Line too long (107/100) (line-too-long)
maincode.py:386:0: C0301: Line too long (107/100) (line-too-long)
maincode.py:387:0: C0301: Line too long (107/100) (line-too-long)
maincode.py:388:0: C0301: Line too long (107/100) (line-too-long)
maincode.py:389:0: C0301: Line too long (107/100) (line-too-long)
maincode.py:392:0: C0301: Line too long (108/100) (line-too-long)
maincode.py:393:0: C0301: Line too long (108/100) (line-too-long)
maincode.py:394:0: C0301: Line too long (108/100) (line-too-long)
maincode.py:395:0: C0301: Line too long (108/100) (line-too-long)
maincode.py:396:0: C0301: Line too long (108/100) (line-too-long)
maincode.py:456:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
maincode.py:458:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
maincode.py:471:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
maincode.py:490:0: C0301: Line too long (117/100) (line-too-long)
maincode.py:494:0: C0301: Line too long (108/100) (line-too-long)
maincode.py:495:0: C0301: Line too long (108/100) (line-too-long)
maincode.py:496:0: C0301: Line too long (108/100) (line-too-long)
maincode.py:497:0: C0301: Line too long (108/100) (line-too-long)
maincode.py:498:0: C0301: Line too long (108/100) (line-too-long)
maincode.py:501:0: C0301: Line too long (113/100) (line-too-long)
maincode.py:502:0: C0301: Line too long (113/100) (line-too-long)
maincode.py:503:0: C0301: Line too long (113/100) (line-too-long)
maincode.py:504:0: C0301: Line too long (113/100) (line-too-long)
maincode.py:505:0: C0301: Line too long (113/100) (line-too-long)
maincode.py:508:0: C0301: Line too long (115/100) (line-too-long)
maincode.py:554:0: C0301: Line too long (167/100) (line-too-long)
maincode.py:556:0: C0301: Line too long (109/100) (line-too-long)
maincode.py:564:0: C0301: Line too long (103/100) (line-too-long)
maincode.py:577:0: C0301: Line too long (102/100) (line-too-long)
maincode.py:578:0: C0301: Line too long (105/100) (line-too-long)
maincode.py:584:0: C0301: Line too long (105/100) (line-too-long)
maincode.py:601:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
maincode.py:613:0: C0301: Line too long (105/100) (line-too-long)
maincode.py:630:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
maincode.py:641:0: C0301: Line too long (105/100) (line-too-long)
maincode.py:654:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
maincode.py:665:0: C0301: Line too long (105/100) (line-too-long)
maincode.py:678:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
maincode.py:733:0: C0301: Line too long (110/100) (line-too-long)
maincode.py:754:0: C0301: Line too long (105/100) (line-too-long)
maincode.py:791:0: C0301: Line too long (105/100) (line-too-long)
maincode.py:794:0: C0301: Line too long (136/100) (line-too-long)
maincode.py:797:0: C0301: Line too long (197/100) (line-too-long)
maincode.py:815:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
maincode.py:821:0: C0301: Line too long (137/100) (line-too-long)
maincode.py:824:0: C0301: Line too long (197/100) (line-too-long)
maincode.py:841:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
maincode.py:908:0: C0301: Line too long (106/100) (line-too-long)
maincode.py:978:0: C0301: Line too long (116/100) (line-too-long)
maincode.py:1003:0: C0301: Line too long (116/100) (line-too-long)
maincode.py:1012:0: C0301: Line too long (113/100) (line-too-long)
maincode.py:1013:0: C0301: Line too long (113/100) (line-too-long)
maincode.py:1014:0: C0301: Line too long (113/100) (line-too-long)
maincode.py:1015:0: C0301: Line too long (113/100) (line-too-long)
maincode.py:1016:0: C0301: Line too long (113/100) (line-too-long)
maincode.py:1019:0: C0301: Line too long (104/100) (line-too-long)
maincode.py:1021:0: C0301: Line too long (106/100) (line-too-long)
maincode.py:1022:0: C0301: Line too long (125/100) (line-too-long)
maincode.py:1023:0: C0301: Line too long (105/100) (line-too-long)
maincode.py:1044:0: C0301: Line too long (106/100) (line-too-long)
maincode.py:1:0: C0302: Too many lines in module (1048/1000) (too-many-lines)
maincode.py:1048:0: C0305: Trailing newlines (trailing-newlines)
maincode.py:1:0: C0114: Missing module docstring (missing-module-docstring)
maincode.py:16:0: C0115: Missing class docstring (missing-class-docstring)
maincode.py:49:4: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:16:0: R0903: Too few public methods (1/2) (too-few-public-methods)
maincode.py:99:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:99:0: C0103: Function name "dispatchUserQuery" doesn't conform to snake_case naming style (invalid-name)
maincode.py:99:22: W0621: Redefining name 'user_input' from outer scope (line 1025) (redefined-outer-name)
maincode.py:99:34: W0621: Redefining name 'dfs' from outer scope (line 1028) (redefined-outer-name)
maincode.py:116:4: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
maincode.py:99:0: R0911: Too many return statements (17/6) (too-many-return-statements)
maincode.py:99:0: R0912: Too many branches (17/12) (too-many-branches)
maincode.py:112:4: W0612: Unused variable 'table_data' (unused-variable)
maincode.py:194:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:194:0: C0103: Function name "plotResult" doesn't conform to snake_case naming style (invalid-name)
maincode.py:194:15: W0621: Redefining name 'result' from outer scope (line 1036) (redefined-outer-name)
maincode.py:194:23: W0621: Redefining name 'user_input' from outer scope (line 1025) (redefined-outer-name)
maincode.py:253:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:253:0: C0103: Function name "plotAgeGroupData" doesn't conform to snake_case naming style (invalid-name)
maincode.py:253:0: R0914: Too many local variables (20/15) (too-many-locals)
maincode.py:277:4: W0612: Unused variable 'fig' (unused-variable)
maincode.py:321:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:321:0: C0103: Function name "barGraph" doesn't conform to snake_case naming style (invalid-name)
maincode.py:326:4: W0612: Unused variable 'fig' (unused-variable)
maincode.py:351:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:351:0: C0103: Function name "lineGraph" doesn't conform to snake_case naming style (invalid-name)
maincode.py:351:0: R0913: Too many arguments (7/5) (too-many-arguments)
maincode.py:351:0: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
maincode.py:351:0: R0914: Too many local variables (16/15) (too-many-locals)
maincode.py:372:19: W0718: Catching too general exception Exception (broad-exception-caught)
maincode.py:352:4: W0612: Unused variable 'fig' (unused-variable)
maincode.py:402:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:402:0: C0103: Function name "DataBaseValidator" doesn't conform to snake_case naming style (invalid-name)
maincode.py:402:26: C0103: Argument name "arrayTouse" doesn't conform to snake_case naming style (invalid-name)
maincode.py:402:38: C0103: Argument name "columnChecked" doesn't conform to snake_case naming style (invalid-name)
maincode.py:403:4: C0103: Variable name "validArray" doesn't conform to snake_case naming style (invalid-name)
maincode.py:418:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:418:0: C0103: Function name "entryCounter" doesn't conform to snake_case naming style (invalid-name)
maincode.py:418:21: C0103: Argument name "arrayTouse" doesn't conform to snake_case naming style (invalid-name)
maincode.py:418:33: C0103: Argument name "columnChecked" doesn't conform to snake_case naming style (invalid-name)
maincode.py:418:48: C0103: Argument name "newColumnName" doesn't conform to snake_case naming style (invalid-name)
maincode.py:420:4: C0103: Variable name "copyDataBase" doesn't conform to snake_case naming style (invalid-name)
maincode.py:421:4: C0103: Variable name "validArray" doesn't conform to snake_case naming style (invalid-name)
maincode.py:437:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:437:0: C0103: Function name "numberAuthorizationProduct" doesn't conform to snake_case naming style (invalid-name)
maincode.py:444:4: W0621: Redefining name 'result' from outer scope (line 1036) (redefined-outer-name)
maincode.py:438:4: C0103: Variable name "fixedDF" doesn't conform to snake_case naming style (invalid-name)
maincode.py:451:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:451:0: C0103: Function name "dateRangeValidator" doesn't conform to snake_case naming style (invalid-name)
maincode.py:451:49: C0103: Argument name "columnName" doesn't conform to snake_case naming style (invalid-name)
maincode.py:464:4: W0702: No exception type(s) specified (bare-except)
maincode.py:487:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:487:0: C0103: Function name "getClosestDate" doesn't conform to snake_case naming style (invalid-name)
maincode.py:487:23: C0103: Argument name "selectedDate" doesn't conform to snake_case naming style (invalid-name)
maincode.py:487:37: C0103: Argument name "dateColumnName" doesn't conform to snake_case naming style (invalid-name)
maincode.py:509:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:509:0: C0103: Function name "deathRateCountry" doesn't conform to snake_case naming style (invalid-name)
maincode.py:528:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:528:0: C0103: Function name "averageDeathRate" doesn't conform to snake_case naming style (invalid-name)
maincode.py:539:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:539:0: C0103: Function name "deathRateRegion" doesn't conform to snake_case naming style (invalid-name)
maincode.py:540:8: C0121: Comparison 'regions == None' should be 'regions is None' (singleton-comparison)
maincode.py:543:4: C0103: Variable name "validRegions" doesn't conform to snake_case naming style (invalid-name)
maincode.py:546:8: C0121: Comparison 'validRegions == None' should be 'validRegions is None' (singleton-comparison)
maincode.py:562:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:562:0: C0103: Function name "averageDeathRateRegion" doesn't conform to snake_case naming style (invalid-name)
maincode.py:572:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:572:0: C0103: Function name "DeathRateRequest" doesn't conform to snake_case naming style (invalid-name)
maincode.py:573:4: W0621: Redefining name 'result' from outer scope (line 1036) (redefined-outer-name)
maincode.py:572:0: R1711: Useless return at end of function or method (useless-return)
maincode.py:585:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:585:0: C0103: Function name "averageDailyCases" doesn't conform to snake_case naming style (invalid-name)
maincode.py:614:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:614:0: C0103: Function name "averageDailyDeath" doesn't conform to snake_case naming style (invalid-name)
maincode.py:642:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:642:0: C0103: Function name "averageDailyRegionalCases" doesn't conform to snake_case naming style (invalid-name)
maincode.py:666:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:666:0: C0103: Function name "averageDailyRegionalDeath" doesn't conform to snake_case naming style (invalid-name)
maincode.py:691:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:691:0: C0103: Function name "vaccinationCoverageISO3" doesn't conform to snake_case naming style (invalid-name)
maincode.py:691:32: C0103: Argument name "ISO3_countries" doesn't conform to snake_case naming style (invalid-name)
maincode.py:692:7: C0121: Comparison 'ISO3_countries == None' should be 'ISO3_countries is None' (singleton-comparison)
maincode.py:695:4: C0103: Variable name "fixedDF" doesn't conform to snake_case naming style (invalid-name)
maincode.py:696:4: C0103: Variable name "fixedDF" doesn't conform to snake_case naming style (invalid-name)
maincode.py:698:7: C0121: Comparison 'validated_countries == None' should be 'validated_countries is None' (singleton-comparison)
maincode.py:711:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:711:0: C0103: Function name "totalVaccinationISO3" doesn't conform to snake_case naming style (invalid-name)
maincode.py:711:29: C0103: Argument name "ISO3_countries" doesn't conform to snake_case naming style (invalid-name)
maincode.py:712:7: C0121: Comparison 'ISO3_countries == None' should be 'ISO3_countries is None' (singleton-comparison)
maincode.py:715:4: C0103: Variable name "fixedDF" doesn't conform to snake_case naming style (invalid-name)
maincode.py:716:4: C0103: Variable name "fixedDF" doesn't conform to snake_case naming style (invalid-name)
maincode.py:718:7: C0121: Comparison 'validated_countries == None' should be 'validated_countries is None' (singleton-comparison)
maincode.py:735:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:735:0: C0103: Function name "boosterDoseRateISO3" doesn't conform to snake_case naming style (invalid-name)
maincode.py:735:28: C0103: Argument name "ISO3_countries" doesn't conform to snake_case naming style (invalid-name)
maincode.py:739:4: C0103: Variable name "fixedDF" doesn't conform to snake_case naming style (invalid-name)
maincode.py:740:4: C0103: Variable name "fixedDF" doesn't conform to snake_case naming style (invalid-name)
maincode.py:756:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:756:0: C0103: Function name "totalVaccinationSummaryISO3" doesn't conform to snake_case naming style (invalid-name)
maincode.py:756:36: C0103: Argument name "ISO3_countries" doesn't conform to snake_case naming style (invalid-name)
maincode.py:760:4: C0103: Variable name "fixedDF" doesn't conform to snake_case naming style (invalid-name)
maincode.py:761:4: C0103: Variable name "fixedDF" doesn't conform to snake_case naming style (invalid-name)
maincode.py:776:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:776:0: C0103: Function name "numberAuthorizationISO3" doesn't conform to snake_case naming style (invalid-name)
maincode.py:776:32: C0103: Argument name "ISO3_countries" doesn't conform to snake_case naming style (invalid-name)
maincode.py:789:4: W0621: Redefining name 'result' from outer scope (line 1036) (redefined-outer-name)
maincode.py:780:4: C0103: Variable name "fixedDF" doesn't conform to snake_case naming style (invalid-name)
maincode.py:799:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:799:0: C0103: Function name "AverageHospitalizationWeeklyCountry" doesn't conform to snake_case naming style (invalid-name)
maincode.py:799:44: C0103: Argument name "ISO3_countries" doesn't conform to snake_case naming style (invalid-name)
maincode.py:815:28: C0321: More than one statement on a single line (multiple-statements)
maincode.py:817:4: C0103: Variable name "avgWeekly" doesn't conform to snake_case naming style (invalid-name)
maincode.py:826:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:826:0: C0103: Function name "AverageHospitalizationMonthlyCountry" doesn't conform to snake_case naming style (invalid-name)
maincode.py:826:45: C0103: Argument name "ISO3_countries" doesn't conform to snake_case naming style (invalid-name)
maincode.py:841:28: C0321: More than one statement on a single line (multiple-statements)
maincode.py:843:4: C0103: Variable name "avgWeekly" doesn't conform to snake_case naming style (invalid-name)
maincode.py:847:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:847:0: C0103: Function name "AverageHospitalizationMonthlyAll" doesn't conform to snake_case naming style (invalid-name)
maincode.py:868:4: C0103: Variable name "avgMonthly" doesn't conform to snake_case naming style (invalid-name)
maincode.py:871:4: C0103: Variable name "avgMonthly" doesn't conform to snake_case naming style (invalid-name)
maincode.py:877:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:877:0: C0103: Function name "AverageHospitalizationWeeklyAll" doesn't conform to snake_case naming style (invalid-name)
maincode.py:899:4: C0103: Variable name "avgMonthly" doesn't conform to snake_case naming style (invalid-name)
maincode.py:902:4: C0103: Variable name "avgMonthly" doesn't conform to snake_case naming style (invalid-name)
maincode.py:908:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:908:0: C0103: Function name "timeIntervalData" doesn't conform to snake_case naming style (invalid-name)
maincode.py:908:0: R0913: Too many arguments (7/5) (too-many-arguments)
maincode.py:908:0: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
maincode.py:936:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:936:36: C0103: Argument name "ISO3_countries" doesn't conform to snake_case naming style (invalid-name)
maincode.py:947:8: R1735: Consider using '{"year": d['Year'], "month": d['Month'], "day": 1}' instead of a call to 'dict'. (use-dict-literal)
maincode.py:962:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:973:8: R1735: Consider using '{"year": dataincome['Year'], "month": dataincome['Month'], "day": 1, ... }' instead of a call to 'dict'. (use-dict-literal)
maincode.py:987:0: C0116: Missing function or method docstring (missing-function-docstring)
maincode.py:998:8: R1735: Consider using '{"year": dataregion['Year'], "month": dataregion['Month'], "day": 1, ... }' instead of a call to 'dict'. (use-dict-literal)
maincode.py:2:0: W0611: Unused month imported from calendar (unused-import)

-----------------------------------
Your code has been rated at 5.80/10
```

## Fixed Issues

I've fixed the following 5 issues reported by pylint:

###  1. Removed unused import
```python
# Before
from __future__ import annotations
from calendar import month  # Unused import
from copy import deepcopy
import numpy as np
import pandas as pd

# After
from __future__ import annotations
from copy import deepcopy
import numpy as np
import pandas as pd
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

