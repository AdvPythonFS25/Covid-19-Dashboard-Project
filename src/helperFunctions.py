
from __future__ import annotations
from copy import deepcopy
import pandas as pd

#Checks for the elements of given array in the database
#Removes if the given input is not in the dataBase, and prints out that.
#Used in the old code as a one python file, in the streamlit is not essential but in the terminal it was handling wrong input.
def DataBaseValidator(df: pd.DataFrame, arrayTouse, columnChecked):
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

#Counts the entries of the given column in the databas based on the given arrays elements
def entryCounter(df: pd.DataFrame, arrayTouse, columnChecked, newColumnName):
    copyDataBase = deepcopy(df)
    validArray = DataBaseValidator(copyDataBase, arrayTouse, columnChecked)

    if validArray is None or len(validArray) == 0:
        return None

    df_filtered = copyDataBase[copyDataBase[columnChecked].isin(validArray)].copy()
    counts = df_filtered[columnChecked].value_counts()

    result_df = pd.DataFrame({newColumnName: counts})
    result_df.index.name = columnChecked
    return result_df


# Gets the closest date in the database to the given date
# If the given date is not in the database, it returns the closest date possible
def getClosestDate(df: pd.DataFrame, selectedDate, dateColumnName):
    selectedDate = pd.to_datetime(selectedDate)
    closest = min(df[dateColumnName], key=lambda x: abs(x - selectedDate))
    return closest



#First checks if the user entered normal data or not if not it sets the start and end date to the min and max date in the database
#Secondly, it checks if the given date is in the database or not using get closest date function
# Also as a debugging method it has print statements to show the user what date range was set
def dateRangeValidator(df: pd.DataFrame,
                       start_date,
                       end_date,
                       columnName: str = "Date_reported"):

    df = df.copy()
    df[columnName] = pd.to_datetime(df[columnName])

    if end_date is None:
        end_date = df[columnName].max()
    if start_date is None:
        start_date = df[columnName].min()

    try:
        start_date = pd.to_datetime(start_date)
        end_date   = pd.to_datetime(end_date)
    except Exception:
        print("Dates are invalid – please check the format")
        return None, None

    min_date, max_date = df[columnName].min(), df[columnName].max()

    if start_date > end_date:
        start_date = min_date
    if start_date < min_date or start_date > max_date:
        start_date = min_date
    if end_date   < min_date or end_date   > max_date:
        end_date   = max_date

    end_date   = getClosestDate(df, end_date,   columnName)
    start_date = getClosestDate(df, start_date, columnName)
    '''
    print("─────────────────────────────────────────────────────────────")
    print(f" Date range applied by the system : {start_date} – {end_date}")
    print("─────────────────────────────────────────────────────────────")
    '''
    return start_date, end_date