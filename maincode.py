from __future__ import annotations
from copy import deepcopy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ---------------------------------------------INPUT FUNCTIONS--------------------------------------------#
# ---------------------------------------------INPUT FUNCTIONS--------------------------------------------#
# ---------------------------------------------INPUT FUNCTIONS--------------------------------------------#
# ---------------------------------------------INPUT FUNCTIONS--------------------------------------------#
# ---------------------------------------------INPUT FUNCTIONS--------------------------------------------#

class UserInput:
    def __init__(self):
        self.stat_map = {
            '1': 'DR', '2': 'RT', '3': 'AVG_CASES', '4': 'AVG_DEATHS', '5': 'REGIONAL_DR',
            '6': 'VAX_COVERAGE', '7': 'BOOSTER_RATE', '8': 'VAX_SUMMARY', '9': 'AUTH_ISO3',
            '10': 'AUTH_PRODUCT', '11': 'AVG_HOSP_WEEK', '12': 'AVG_HOSP_MONTH',
            '13': 'TIME_SERIES', '14': 'AGE_DEATH_ANALYSIS', '15': 'AGE_DEATH_INCOME', '16': 'AGE_DEATH_REGION'
        }

        self.stat_labels = {
            'DR': 'Death Rate (CFR)', 'RT': 'Rt (Reproduction Number) not working yet',
            'AVG_CASES': 'Average Daily Cases', 'AVG_DEATHS': 'Average Daily Deaths',
            'REGIONAL_DR': 'Regional Death Rate', 'VAX_COVERAGE': 'Vaccination Coverage',
            'BOOSTER_RATE': 'Booster Dose Rate', 'VAX_SUMMARY': 'Total Vaccination Summary',
            'AUTH_ISO3': 'Vaccine Authorisations by ISO3', 'AUTH_PRODUCT': 'Vaccine Authorisations by Product Name',
            'AVG_HOSP_WEEK': 'Average Weekly Hospitalisations', 'AVG_HOSP_MONTH': 'Average Monthly Hospitalisations',
            'TIME_SERIES': 'Daily Time-Series', 'AGE_DEATH_ANALYSIS': 'Monthly Deaths by Age Group (countries)',
            'AGE_DEATH_INCOME': 'Monthly Deaths by Age Group (income)', 'AGE_DEATH_REGION': 'Monthly Deaths by Age Group (WHO region)'
        }

        self.input_type_labels = {
            '1': 'ISO3 code (3-letter)', '2': 'Country code (2-letter)',
            '3': 'WHO region', '4': 'Vaccine product name', '5': 'World-Bank income group'
        }

        self.allowed_input_map = {
            'DR': ['2'], 'RT': ['2'], 'AVG_CASES': ['2'], 'AVG_DEATHS': ['2'],
            'REGIONAL_DR': ['3'], 'VAX_COVERAGE': ['1'], 'BOOSTER_RATE': ['1'],
            'VAX_SUMMARY': ['1'], 'AUTH_ISO3': ['1'], 'AUTH_PRODUCT': ['4'],
            'AVG_HOSP_WEEK': ['1'], 'AVG_HOSP_MONTH': ['1'], 'TIME_SERIES': ['2'],
            'AGE_DEATH_ANALYSIS': ['1'], 'AGE_DEATH_INCOME': ['5'], 'AGE_DEATH_REGION': ['3']
        }

    def prompt_user(self):
        number = input("Select statistic to compute: \n")
        while number not in self.stat_map:
            number = input("Invalid input. Please try again: ")

        stat_code = self.stat_map[number]
        input_type = input("\nChoose identifier type: ")
        while input_type not in self.allowed_input_map[stat_code]:
            input_type = input(f"Invalid for {self.stat_labels[stat_code]}. Allowed: {', '.join(self.allowed_input_map[stat_code])} → ")

        ids = [v.strip() for v in input("\nEnter values (comma-separated): ").split(",") if v.strip()]
        if not ids:
            ids = ['USA']

        date_needed = stat_code in {
            'AVG_CASES', 'AVG_DEATHS', 'AVG_HOSP_WEEK', 'AVG_HOSP_MONTH',
            'TIME_SERIES', 'AGE_DEATH_ANALYSIS', 'AGE_DEATH_INCOME', 'AGE_DEATH_REGION'
        }
        start_date = end_date = None
        if date_needed:
            start_date = input("\nStart date (YYYY-MM-DD): ")
            end_date = input("End date   (YYYY-MM-DD): ")

        data_wanted = None
        if stat_code == 'TIME_SERIES':
            data_wanted = input("\nWhich column? e.g. New_cases, New_deaths → ") or 'New_cases'

        print("\n─────────────────────────────────────────────────────────────")
        print(f" Statistic   : {self.stat_labels[stat_code]}")
        print(f" IDs type    : {self.input_type_labels[input_type]}")
        print(f" IDs         : {', '.join(ids)}")
        if date_needed:
            print(f" Date range  : {start_date} – {end_date} (auto-fixed if invalid)")
        if data_wanted:
            print(f" Column      : {data_wanted}")
        print("─────────────────────────────────────────────────────────────")

        return {
            "stat": stat_code,
            "input_type": input_type,
            "values": ids,
            "start_date": start_date,
            "end_date": end_date,
            "data_wanted": data_wanted,
        }





def dispatchUserQuery(user_input, dfs):
    stat = user_input["stat"]
    input_type = user_input["input_type"]
    values = user_input["values"]
    start_date = user_input.get("start_date")
    end_date = user_input.get("end_date")
    data_wanted = user_input.get("data_wanted")

    # unpack required data frames
    vaccination_metadata = dfs["vaccination_metadata"]
    vaccination_data = dfs["vaccination_data"]
    global_daily = dfs["global_daily"]
    global_hosp = dfs["global_hosp"]
    table_data = dfs["table_data"]
    monthly_death_age = dfs["monthly_death_age"]  # Add this line

    # ── per-stat routing ────────────────────────────────────────────────
    if stat == "DR" and input_type == "2":
        return deathRateCountry(global_daily, values)

    elif stat == "REGIONAL_DR" and input_type == "3":
        return deathRateRegion(global_daily, values)

    elif stat == "AVG_CASES" and input_type == "2":
        return averageDailyCases(global_daily, values, start_date, end_date)

    elif stat == "AVG_DEATHS" and input_type == "2":
        return averageDailyDeath(global_daily, values, start_date, end_date)

    elif stat == "VAX_COVERAGE" and input_type == "1":
        return vaccinationCoverageISO3(vaccination_data, values)

    elif stat == "BOOSTER_RATE" and input_type == "1":
        return boosterDoseRateISO3(vaccination_data, values)

    elif stat == "VAX_SUMMARY" and input_type == "1":
        return totalVaccinationSummaryISO3(vaccination_data, values)

    elif stat == "AUTH_ISO3" and input_type == "1":
        return numberAuthorizationISO3(vaccination_metadata, values)

    elif stat == "AUTH_PRODUCT" and input_type == "4":
        return numberAuthorizationProduct(vaccination_metadata, values)

    elif stat == "AVG_HOSP_WEEK" and input_type == "1":
        return AverageHospitalizationWeeklyCountry(
            global_hosp, values, start_date, end_date
        )

    elif stat == "AVG_HOSP_MONTH" and input_type == "1":
        return AverageHospitalizationMonthlyCountry(
            global_hosp, values, start_date, end_date
        )

    elif stat == "TIME_SERIES" and input_type == "2":
        raw = timeIntervalData(
            df=global_daily,
            df_array=values,
            start_date=start_date,
            end_date=end_date,
            time_column_name="Date_reported",
            data_column_name="Country_code",
            data_wanted=data_wanted
        )

        if raw is None or raw.empty:
            print("No data found or the data column name is not valid.")
            return None

        raw[data_wanted] = (
            pd.to_numeric(raw[data_wanted], errors="coerce")
            .groupby(raw["Country_code"])
            .transform(lambda s: s.fillna(s.mean()))
        )
        return raw.pivot(index="Date_reported",
                         columns="Country_code",
                         values=data_wanted)

    elif stat == "AGE_DEATH_ANALYSIS" and input_type == "1":
        return deaths_by_age_group_country(monthly_death_age, values, start_date, end_date)

    elif stat == "AGE_DEATH_INCOME" and input_type == "5":
        return deaths_by_income(monthly_death_age, values,
                                start_date, end_date)

    elif stat == "AGE_DEATH_REGION" and input_type == "3":
        return deaths_by_age_group_region(monthly_death_age, values,
                                          start_date, end_date)
    else:
        print("❌ Combination not supported (yet).")
        return None


# General plot function to ddecide whether the returned data is plotted in a certain way

def plotResult(result, user_input):
    # Decides whether to draw a bar chart (Series / 1-col DF) or
    # a line chart (time series DataFrame).  Uses barGraph / lineGraph
    # helpers you already defined.

    stat_titles = {
        "AVG_CASES": "Average Daily Cases",
        "AVG_DEATHS": "Average Daily Deaths",
        "DR": "Death Rate (%)",
        "REGIONAL_DR": "Regional Death Rate (%)",
        "VAX_COVERAGE": "Vaccination Coverage (%)",
        "BOOSTER_RATE": "Booster Dose Coverage (%)",
        "VAX_SUMMARY": "Vaccination Summary",
        "AUTH_ISO3": "Vaccine Authorisations (ISO3)",
        "AUTH_PRODUCT": "Vaccine Authorisations (Product)",
        "AVG_HOSP_WEEK": "Avg Weekly Hospitalisations",
        "AVG_HOSP_MONTH": "Avg Monthly Hospitalisations",
        "TIME_SERIES": f"{user_input['data_wanted']} (Daily)",
        "AGE_DEATH_ANALYSIS": "COVID-19 Deaths by Age Group (countries)",
        "AGE_DEATH_INCOME": "COVID-19 Deaths by Age Group (income)",
        "AGE_DEATH_REGION": "COVID-19 Deaths by Age Group (WHO region)"
    }
    title = stat_titles.get(user_input["stat"], "Statistical Summary")

    # ── Age-based death DataFrame → grouped bar chart ───────────────────
    if user_input["stat"] in ["AGE_DEATH_ANALYSIS", "AGE_DEATH_INCOME", "AGE_DEATH_REGION"]:
        plotAgeGroupData(result, title)

    # ── SERIES → bar chart ───────────────────────────────────────────────
    elif isinstance(result, pd.Series):
        barGraph(result.to_dict(),
                 x_axis_label="Category",
                 y_axis_label=result.name or "Value",
                 title=title)

    # ── wide DataFrame with date index → line chart ─────────────────────
    elif isinstance(result, pd.DataFrame) and \
            pd.api.types.is_datetime64_any_dtype(result.index):
        lineGraph(statistical_data=result,
                  index_array=result.index,
                  x_axis="Date",
                  y_axis=title,
                  title=title,
                  error_data=None,
                  show_trend=True)

    # ── 1-column DF (non-date index) → bar chart ───────────────────────
    elif isinstance(result, pd.DataFrame) and result.shape[1] == 1:
        data_dict = result.iloc[:, 0].to_dict()
        y_label = result.columns[0]
        barGraph(data_dict,
                 x_axis_label=result.index.name or "Category",
                 y_axis_label=y_label,
                 title=title)

    else:
        print("❌ Unsupported data type for plotting.")


def plotAgeGroupData(df, title):


    df_plot = df.copy()           # just in case
    if isinstance(df_plot, pd.Series):
        df_plot = df_plot.reset_index()

    entity_col = 'Group'          # x-axis groups
    age_col    = 'Agegroup'       # hue
    value_col  = 'Deaths'         # bar height

    if not all(c in df_plot.columns for c in [entity_col, age_col, value_col]):
        print("Expected columns missing – got:", df_plot.columns.tolist())
        return

    # ── plotting ──────────────────────────────────────────────────────
    bar_width = 0.15
    entities  = df_plot[entity_col].unique()
    ages_pref = ['0_4', '5_14', '15_64', '65+']
    ages      = [a for a in ages_pref if a in df_plot[age_col].unique()] + \
                [a for a in df_plot[age_col].unique() if a not in ages_pref]

    colors = ['#4B0082', '#32CD32', '#1E90FF', '#FFD700']

    fig, ax = plt.subplots(figsize=(14, 8))
    positions = np.arange(len(entities))

    for i, age in enumerate(ages):
        sub = df_plot[df_plot[age_col] == age]
        heights = [sub.loc[sub[entity_col] == e, value_col].sum() for e in entities]
        x = positions + (i - len(ages)/2 + 0.5) * bar_width

        bars = ax.bar(x, heights,
                      width=bar_width,
                      label=age,
                      color=colors[i % len(colors)],
                      edgecolor='black',
                      linewidth=0.5)

        # NEW: add the numeric labels
        ax.bar_label(bars, labels=[f"{h:.0f}" for h in heights],
                     padding=3, fontsize=8)

    # cosmetics
    ax.set_xlabel('Group')
    ax.set_ylabel('Number of Deaths')
    ax.set_title(title)
    ax.set_xticks(positions)
    ax.set_xticklabels(entities, rotation=45, ha='right')
    ax.grid(axis='y', linestyle='--', alpha=0.3)
    ax.legend(title='Age Group')
    plt.tight_layout()
    plt.show()

# ---------------------------------------------INPUT FUNCTIONS--------------------------------------------#
# ---------------------------------------------INPUT FUNCTIONS--------------------------------------------#
# ---------------------------------------------INPUT FUNCTIONS--------------------------------------------#
# ---------------------------------------------INPUT FUNCTIONS--------------------------------------------#
# ---------------------------------------------INPUT FUNCTIONS--------------------------------------------#


# ---------------------------------------------GRAPH FUNCTIONS--------------------------------------------#
# ---------------------------------------------GRAPH FUNCTIONS--------------------------------------------#
# ---------------------------------------------GRAPH FUNCTIONS--------------------------------------------#
# ---------------------------------------------GRAPH FUNCTIONS--------------------------------------------#
# ---------------------------------------------GRAPH FUNCTIONS--------------------------------------------#


def barGraph(statistical_data, x_axis_label, y_axis_label, title, error_data=None):
    # Accept either dict or Series
    if isinstance(statistical_data, pd.Series):
        statistical_data = statistical_data.to_dict()

    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    x_labels = list(statistical_data.keys())
    y_values = list(statistical_data.values())
    x_pos = np.arange(len(x_labels))

    if error_data:
        errors = [error_data.get(label, 0) for label in x_labels]
        ax.bar(x_pos, y_values, yerr=errors, capsize=5, color='skyblue')
    else:
        ax.bar(x_pos, y_values, color='skyblue')

    ax.set_xticks(x_pos)
    ax.set_xticklabels(x_labels)
    ax.set_xlabel(x_axis_label)
    ax.set_ylabel(y_axis_label)
    ax.set_title(title)

    sns.despine()
    plt.tight_layout()
    plt.show()


# NOT FINISHED YET
# This function will take at most 4 countries/regions/codes and will show the data with an optional trendline.
def lineGraph(statistical_data, index_array, x_axis, y_axis, title, error_data=None, show_trend=True):
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))

    for label in statistical_data:
        ax.plot(index_array, statistical_data[label], label=label, linewidth=2)

        # Add error bars if provided
        if error_data and label in error_data:
            upper = np.array(statistical_data[label]) + np.array(error_data[label])
            lower = np.array(statistical_data[label]) - np.array(error_data[label])
            ax.plot(index_array, upper, '-.', color='grey', linewidth=1, alpha=0.5)
            ax.plot(index_array, lower, '-.', color='grey', linewidth=1, alpha=0.5)
            ax.fill_between(index_array, lower, upper, color='grey', alpha=0.2)

        # Add trendline if requested
        if show_trend:
            try:
                x_numeric = np.arange(len(index_array))
                z = np.polyfit(x_numeric, statistical_data[label], 1)
                p = np.poly1d(z)
                ax.plot(index_array, p(x_numeric), linestyle='--', linewidth=1.5, alpha=0.6, label=f"{label} Trend")
            except Exception as e:
                print(f"Trendline error for {label}: {e}")

    ax.set_title(title)
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    ax.legend(frameon=False)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    sns.despine()
    plt.tight_layout()
    plt.show()


# ---------------------------------------------GRAPH FUNCTIONS--------------------------------------------#
# ---------------------------------------------GRAPH FUNCTIONS--------------------------------------------#
# ---------------------------------------------GRAPH FUNCTIONS--------------------------------------------#
# ---------------------------------------------GRAPH FUNCTIONS--------------------------------------------#
# ---------------------------------------------GRAPH FUNCTIONS--------------------------------------------#


# ---------------------------------------------HELPER FUNCTIONS--------------------------------------------#
# ---------------------------------------------HELPER FUNCTIONS--------------------------------------------#
# ---------------------------------------------HELPER FUNCTIONS--------------------------------------------#
# ---------------------------------------------HELPER FUNCTIONS--------------------------------------------#
# ---------------------------------------------HELPER FUNCTIONS--------------------------------------------#
# Removes the countries that are not in the dataframe that is given.


# Given the list of countries or regions in case it doesn't exist in the database that is searched
# it excludes them and returns a new array. Functions under that are its specified versions.
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


# This function returns the entries of a specific data provided with an array, indexTo search,
# and the column name to search
# The function will return a dictionary with the entry count for each item in the array
def entryCounter(df, arrayTouse, columnChecked, newColumnName):
    # ENSURING NO SHALLOW COPIES
    copyDataBase = deepcopy(df)
    validArray = database_validator(copyDataBase, arrayTouse, columnChecked)

    if validArray is None or len(validArray) == 0:
        return None

    # Filter the data
    df_filtered = copyDataBase[copyDataBase[columnChecked].isin(validArray)].copy()
    counts = df_filtered[columnChecked].value_counts()

    # Convert to DataFrame and rename
    result_df = pd.DataFrame({newColumnName: counts})
    result_df.index.name = columnChecked

    return result_df


def numberAuthorizationProduct(df, products):
    fixedDF = df.copy()
    validated_countries = database_validator(fixedDF, products, "PRODUCT_NAME")
    if validated_countries is None or len(validated_countries) == 0:
        return None

    df_countries = fixedDF[fixedDF['PRODUCT_NAME'].isin(validated_countries)].copy()
    result = df_countries.groupby("PRODUCT_NAME")["ISO3"].count()
    return result.rename("Number of Authorizations")



# Works for Global Daily data
# Given the ranges of two dates in case it is malicious data then it converts it.
def dateRangeValidator(df, start_date, end_date, columnName = "Date_reported"):
    #Ensuring no problems with data base.
    df = df.copy()
    df[columnName] = pd.to_datetime(df[columnName])

    if (end_date is None):
        end_date = df[columnName].max()
    if (start_date is None):
        start_date = df[columnName].min()

    try:
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
    except:
        print("Dates are invalid please check the format")
        return None

    min_date = df[columnName].min()
    max_date = df[columnName].max()

    if (start_date > end_date):
        start_date = df[columnName].min()
    if (start_date < min_date or start_date > max_date):
        start_date = df[columnName].min()
    if (end_date < min_date or end_date > max_date):
        end_date = df[columnName].max()

    #In case any missing data still handled with closest date possible in the system.
    end_date = getClosestDate(df, end_date, columnName)
    start_date = getClosestDate(df, start_date, columnName)

    print("─────────────────────────────────────────────────────────────")
    print(f" Date range apllied by the system : {start_date} – {end_date}")
    print("─────────────────────────────────────────────────────────────")
    return start_date, end_date

def getClosestDate(df, selectedDate, dateColumnName):
    selectedDate = pd.to_datetime(selectedDate)

    # goes trough every date possible and find the minimum difference and returns that date created the minimum date.
    closest = min(df[dateColumnName], key=lambda x: abs(x - selectedDate))
    return closest

# ---------------------------------------------HELPER FUNCTIONS--------------------------------------------#
# ---------------------------------------------HELPER FUNCTIONS--------------------------------------------#
# ---------------------------------------------HELPER FUNCTIONS--------------------------------------------#
# ---------------------------------------------HELPER FUNCTIONS--------------------------------------------#
# ---------------------------------------------HELPER FUNCTIONS--------------------------------------------#


# ---------------------------------------------CALCULATION FUNCTIONS--------------------------------------------#
# ---------------------------------------------CALCULATION FUNCTIONS--------------------------------------------#
# ---------------------------------------------CALCULATION FUNCTIONS--------------------------------------------#
# ---------------------------------------------CALCULATION FUNCTIONS--------------------------------------------#
# ---------------------------------------------CALCULATION FUNCTIONS--------------------------------------------#
# DEATH RATE CALCULATION FUNCTION COUNTRY CODE BASED
# Death rate = Deaths / Cases * 100
# This function will calculate the death rate for a given list of country codes (e.g., ['US', 'DE']). 2 letter code
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

    # Validate country codes
    #
    valid_codes = database_validator(df, country_codes, "Country_code")
    if valid_codes is None or len(valid_codes) == 0:
        return None
    df_countries = df[df['Country_code'].isin(valid_codes)].copy()

    df_latest = df_countries.sort_values('Date_reported').groupby('Country_code').last()

    df_latest["Death Rate"] = df_latest["Cumulative_deaths"] / df_latest["Cumulative_cases"] * 100

    return df_latest["Death Rate"]


# Gets average death rate for all countries existed in daily data
def averageDeathRate(df):
    df_countries = df.copy()
    df_latest_all_country_data = df_countries.sort_values('Date_reported').groupby('Country').last()
    df_latest_all_country_data["Death Rate"] = df_latest_all_country_data["Cumulative_deaths"] / \
                                               df_latest_all_country_data["Cumulative_cases"] * 100
    return df_latest_all_country_data


# DEATH RATE CALCULATION FUNCTION REGIONAL
# Death rate = Deaths / Cases * 100
# this function will calculate the death rate for a given region or regions as an array.
def deathRateRegion(df, regions):
    if (regions is None or len(regions) == 0):
        return None
    # Check if the all countries are in the dataframe
    validRegions = database_validator(df, regions, "WHO_region")


    if (validRegions is None or len(validRegions) == 0):
        return None

    df_regions = df[df['WHO_region'].isin(validRegions)].copy()

    df_regions["Date_reported"] = pd.to_datetime(df_regions["Date_reported"])

    df_latest_region_data = df_regions.sort_values('Date_reported').groupby('WHO_region').last()
    # df_latest_regional_data contains the latest data for each country that is considered to be valid. Moreover, the data has their latest cumulative deaths and cases

    df_latest_region_data["Death Rate"] = df_latest_region_data["Cumulative_deaths"] / df_latest_region_data[
        "Cumulative_cases"] * 100
    return df_latest_region_data["Death Rate"]


# Gets average death rate for all countries existed in daily data
def averageDeathRateRegion(df):
    df_countries = df.copy()
    df_latest_all_country_data = df_countries.sort_values('Date_reported').groupby('WHO_region').last()
    df_latest_all_country_data["Death Rate"] = df_latest_all_country_data["Cumulative_deaths"] / \
                                               df_latest_all_country_data["Cumulative_cases"] * 100
    return df_latest_all_country_data


# Death Rate Request Function
# Prints a text to user to better understanding
def DeathRateRequest(countries):
    result = deathRateCountry(GlobalDailyDF, countries)
    if result is not None:
        print("\nHere are the countries requested by the user with their death rates (%):")
        print(result["Death Rate"])
        print("Overall average death rate for the countries requested: ", result["Death Rate"].mean())
        print("All countries average death rate: ", averageDeathRate(GlobalDailyDF)["Death Rate"].mean())
    return


# Average cases daily for the countries list in a given time interval with date fixation
# End date is included but in case not given last date will be used
# Start date is included, but if start date > end date, it will be set to the first date in the dataframe
def averageDailyCases(df, country_codes, start_date, end_date=None):
    validated_codes = database_validator(df, country_codes, "Country_code")
    if validated_codes is None or len(validated_codes) == 0:
        return None
    df_countries = df[df['Country_code'].isin(validated_codes)].copy()
    #Changing the type so that we will ensure we can compare.
    df_countries["Date_reported"] = pd.to_datetime(df_countries["Date_reported"])
    df_countries = df_countries.sort_values("Date_reported")


    # Dates are validated trough this function
    start_date, end_date = dateRangeValidator(df_countries, start_date, end_date,"Date_reported")

    print(start_date, end_date)
    df_countries_filtered = df_countries[
        (df_countries["Date_reported"] >= start_date) & (df_countries["Date_reported"] <= end_date)]
    if df_countries_filtered.empty:
        print("Could not find any countries within the date range")
        return None

    df_countries_filtered.fillna(0, inplace=True)
    avg_cases = df_countries_filtered.groupby("Country_code")["New_cases"].mean()
    avg_cases = avg_cases.rename("Average")
    return avg_cases.round(2)


# Average cases daily for the countries list in a given time interval with date fixation
# End date is included but in case not given last date will be used
# Start date is included, but if start date > end date, it will be set to the first date in the dataframe
def averageDailyDeath(df, country_codes, start_date, end_date=None):
    validated_codes = database_validator(df, country_codes, "Country_code")

    if validated_codes is None or len(validated_codes) == 0:
        return None
    df_countries = df[df['Country_code'].isin(validated_codes)].copy()
    #Changing the type so that we will ensure we can compare.
    df_countries["Date_reported"] = pd.to_datetime(df_countries["Date_reported"])

    df_countries = df_countries.sort_values("Date_reported")

    # Dates are validated trough this function
    start_date, end_date = dateRangeValidator(df_countries, start_date, end_date,"Date_reported")

    df_countries_filtered = df_countries[
        (df_countries["Date_reported"] >= start_date) & (df_countries["Date_reported"] <= end_date)]
    if (df_countries_filtered.empty):
        print("Could not find any countries within the date range")
        return None
    df_countries_filtered.fillna(0, inplace=True)
    avg_cases = df_countries_filtered.groupby("Country_code")["New_deaths"].mean()
    avg_cases = avg_cases.rename("Average")
    return avg_cases.round(2)


# Average cases daily for the regions list in a given time interval with date fixation
# End date is included but in case not given last date will be used
# Start date is included, but if start date > end date, it will be set to the first date in the dataframe
def averageDailyRegionalCases(df, regions, start_date, end_date=None):
    validated_regions = database_validator(df, regions, "WHO_region")
    if validated_regions is None or len(validated_regions) == 0:
        return None
    df_regions = df[df['WHO_region'].isin(validated_regions)].copy()
    df_regions = df_regions.sort_values("Date_reported")

    # Dates are validated trough this function
    start_date, end_date = dateRangeValidator(df_regions, start_date, end_date)

    df_regions_filtered = df_regions[
        (df_regions["Date_reported"] >= start_date) & (df_regions["Date_reported"] <= end_date)]
    if (df_regions_filtered.empty):
        print("Could not find any countries within the date range")
        return None
    df_regions_filtered.fillna(0, inplace=True)
    avg_cases = df_regions_filtered.groupby("WHO_region")["New_cases"].mean()
    avg_cases = avg_cases.rename("Average")
    return avg_cases.round(2)


# Average deaths daily for the regions list in a given time interval with date fixation
# End date is included but in case not given last date will be used
# Start date is included, but if start date > end date, it will be set to the first date in the dataframe
def averageDailyRegionalDeath(df, regions, start_date, end_date=None):
    validated_regions = database_validator(df, regions, "WHO_region")
    if validated_regions is None or len(validated_regions) == 0:
        return None
    df_regions = df[df['WHO_region'].isin(validated_regions)].copy()
    df_regions = df_regions.sort_values("Date_reported")

    # Dates are validated trough this function
    start_date, end_date = dateRangeValidator(df_regions, start_date, end_date)

    df_regions_filtered = df_regions[
        (df_regions["Date_reported"] >= start_date) & (df_regions["Date_reported"] <= end_date)]
    if (df_regions_filtered.empty):
        print("Could not find any countries within the date range")
        return None
    df_regions_filtered.fillna(0, inplace=True)
    avg_cases = df_regions_filtered.groupby("WHO_region")["New_deaths"].mean()
    avg_cases = avg_cases.rename("Average")
    return avg_cases.round(2)


# Returns a DataFrame indexed by ISO3 country codes.
# Each row shows the percentage of the population vaccinated with at least one dose.
# This function aimes to calculate the vaccination coverage for a given country or countries
# Countries is an country array
def vaccinationCoverageISO3(df, ISO3_countries):
    if ISO3_countries is None or len(ISO3_countries) == 0:
        return None
    # Check if the all countries are in the dataframe
    fixedDF = df.copy()
    fixedDF = fixedDF.rename(columns={"COUNTRY": "Country"})
    validated_countries = database_validator(fixedDF, ISO3_countries, "ISO3")
    if validated_countries is None or len(validated_countries) == 0:
        return None

    df_countries = fixedDF[fixedDF['ISO3'].isin(validated_countries)].copy()

    df_countries_coverage = df_countries[["ISO3", "PERSONS_VACCINATED_1PLUS_DOSE_PER100"]]
    df_countries_coverage = df_countries_coverage.rename(columns={
        "COUNTRY": "Country",
        "PERSONS_VACCINATED_1PLUS_DOSE_PER100": "Vaccination Coverage (%)"
    })
    return df_countries_coverage.set_index("ISO3").round(2)


def totalVaccinationISO3(df, ISO3_countries):
    if ISO3_countries == None or len(ISO3_countries) == 0:
        return None
    # Check if the all countries are in the dataframe
    fixedDF = df.copy()
    fixedDF = fixedDF.rename(columns={"COUNTRY": "Country"})
    validated_countries = database_validator(fixedDF, ISO3_countries, "ISO3")
    if validated_countries == None or len(validated_countries) == 0:
        return None

    df_countries = fixedDF[fixedDF['ISO3'].isin(validated_countries)].copy()
    summary_df = df_countries[["Country", "ISO3", "TOTAL_VACCINATIONS", "PERSONS_LAST_DOSE"]]

    # Rename for clarity
    summary_df = summary_df.rename(columns={
        "TOTAL_VACCINATIONS": "Total Doses Administered",
        "PERSONS_LAST_DOSE": "People Fully Vaccinated"
    })

    return summary_df.set_index("ISO3").round(2)


# This function returns the percentage of population that received a booster dose for given ISO3 country codes
# Returns a DataFrame indexed by ISO3 with "Booster Dose Coverage (%)" as column
def boosterDoseRateISO3(df, ISO3_countries):
    if ISO3_countries is None or len(ISO3_countries) == 0:
        return None

    fixedDF = df.copy()
    fixedDF = fixedDF.rename(columns={"COUNTRY": "Country"})
    validated_countries = database_validator(fixedDF, ISO3_countries, "ISO3")
    if validated_countries is None or len(validated_countries) == 0:
        return None

    df_countries = fixedDF[fixedDF['ISO3'].isin(validated_countries)].copy()

    df_boosters = df_countries[["ISO3", "PERSONS_BOOSTER_ADD_DOSE_PER100"]]
    df_boosters = df_boosters.rename(columns={
        "PERSONS_BOOSTER_ADD_DOSE_PER100": "Booster Dose Coverage (%)"
    })
    return df_boosters.set_index("ISO3").round(2)


# This function returns total doses administered and people fully vaccinated for given ISO3 country codes
# Returns a DataFrame indexed by ISO3 with two columns: Total Doses, Fully Vaccinated
def totalVaccinationSummaryISO3(df, ISO3_countries):
    if ISO3_countries is None or len(ISO3_countries) == 0:
        return None

    fixedDF = df.copy()
    fixedDF = fixedDF.rename(columns={"COUNTRY": "Country"})
    validated_countries = database_validator(fixedDF, ISO3_countries, "ISO3")
    if validated_countries is None or len(validated_countries) == 0:
        return None

    df_countries = fixedDF[fixedDF['ISO3'].isin(validated_countries)].copy()

    summary_df = df_countries[["ISO3", "TOTAL_VACCINATIONS", "PERSONS_LAST_DOSE"]]
    summary_df = summary_df.rename(columns={
        "TOTAL_VACCINATIONS": "Total Doses Administered",
        "PERSONS_LAST_DOSE": "People Fully Vaccinated"
    })
    return summary_df.set_index("ISO3")


def numberAuthorizationISO3(df, ISO3_countries):
    if ISO3_countries is None or len(ISO3_countries) == 0:
        return None

    fixedDF = df.copy()
    validated_countries = database_validator(fixedDF, ISO3_countries, "ISO3")
    if validated_countries is None or len(validated_countries) == 0:
        return None

    df_countries = fixedDF[fixedDF['ISO3'].isin(validated_countries)].copy()

    df_countries = df_countries.rename(columns={"COUNTRY": "Country"})

    result = df_countries.groupby("ISO3")["PRODUCT_NAME"].count()

    return result.rename("Number of Authorizations")  # Count number of rows (authorizations) per country


# This function will take the ISO3 codes and two time intervals and will return the weekly average hospitalization in that time interval
# For example USA -> 785 etc.

# The time selections will be harder for this because there might not be data for those days so the time selection will be frst start date and end date will be assigned to their closest data entry.
# Then the normal time interval selection conditions will be applied.
def AverageHospitalizationWeeklyCountry(df, ISO3_countries, start_date, end_date):
    validated_countries = database_validator(df, ISO3_countries, "Country_code")
    if validated_countries is None or len(validated_countries) == 0:
        return None

    # Country code but the database contains ISO3
    df_countries = df[df['Country_code'].isin(validated_countries)].copy()
    df_countries = df_countries.sort_values("Date_reported")
    df_countries["Date_reported"] = pd.to_datetime(df_countries["Date_reported"])


    start_date, end_date = dateRangeValidator(df_countries, start_date, end_date, "Date_reported")

    df_adjusted = df_countries[
        (df_countries["Date_reported"] >= start_date) & (df_countries["Date_reported"] <= end_date)]

    if (df_adjusted.empty): return None

    avgWeekly = df_adjusted.groupby("Country_code")["New_hospitalizations_last_7days"].mean()
    return avgWeekly.rename("Avg Weekly Hospitalizations").round(2)


# This function will take the ISO3 codes and two time intervals and will return the monthly average hospitalization in that time interval
# For example USA -> 785 etc.

# The time selections will be harder for this because there might not be data for those days so the time selection will be frst start date and end date will be assigned to their closest data entry.
# Then the normal time interval selection conditions will be applied.
def AverageHospitalizationMonthlyCountry(df, ISO3_countries, start_date, end_date):
    validated_countries = database_validator(df, ISO3_countries, "Country_code")
    if validated_countries is None or len(validated_countries) == 0:
        return None

    # Country code but the database contains ISO3
    df_countries = df[df['Country_code'].isin(validated_countries)].copy()
    df_countries = df_countries.sort_values("Date_reported")
    df_countries["Date_reported"] = pd.to_datetime(df_countries["Date_reported"])


    start_date,end_date = dateRangeValidator(df_countries, start_date, end_date,"Date_reported")

    df_adjusted = df_countries[
        (df_countries["Date_reported"] >= start_date) & (df_countries["Date_reported"] <= end_date)]
    if (df_adjusted.empty): return None

    avgWeekly = df_adjusted.groupby("Country_code")["New_hospitalizations_last_28days"].mean()
    return avgWeekly.rename("Avg Monthly Hospitalizations").round(2)


def AverageHospitalizationMonthlyAll(df, start_date, end_date):
    if "New_hospitalizations_last_28days" not in df.columns:
        print("Missing expected column in dataset.")
        return None, None

    df_countries = df.copy()
    df_countries["Date_reported"] = pd.to_datetime(df_countries["Date_reported"])
    df_countries = df_countries.sort_values("Date_reported")

    start_date, end_date = dateRangeValidator(df_countries, start_date, end_date,"Date_reported")


    df_adjusted = df_countries[
        (df_countries["Date_reported"] >= start_date) &
        (df_countries["Date_reported"] <= end_date)
        ]

    if df_adjusted.empty:
        print("No data found in the selected date range.")
        return None, None
    df_adjusted = df_adjusted.dropna()
    avgMonthly = df_adjusted.groupby("Country_code")["New_hospitalizations_last_28days"].mean()
    overall_avg = avgMonthly.mean()

    avgMonthly = avgMonthly.rename("Avg Monthly Hospitalizations").round(2)
    overall_avg = round(overall_avg, 2)

    return avgMonthly, overall_avg


def AverageHospitalizationWeeklyAll(df, start_date, end_date):
    if "New_hospitalizations_last_7days" not in df.columns:
        print("Missing expected column in dataset.")
        return None, None

    df_countries = df.copy()
    df_countries["Date_reported"] = pd.to_datetime(df_countries["Date_reported"])
    df_countries = df_countries.sort_values("Date_reported")

    # Get closest dates from available data
    start_date,end_date = dateRangeValidator(df_countries, start_date, end_date,"Date_reported")


    df_adjusted = df_countries[
        (df_countries["Date_reported"] >= start_date) &
        (df_countries["Date_reported"] <= end_date)
        ]

    if df_adjusted.empty:
        print("No data found in the selected date range.")
        return None, None
    df_adjusted = df_adjusted.dropna()
    avgMonthly = df_adjusted.groupby("Country_code")["New_hospitalizations_last_7days"].mean()
    overall_avg = avgMonthly.mean()

    avgMonthly = avgMonthly.rename("Avg Monthly Hospitalizations").round(2)
    overall_avg = round(overall_avg, 2)

    return avgMonthly, overall_avg


def timeIntervalData(df, df_array, start_date, end_date, time_column_name, data_column_name, data_wanted):
    # Make a copy to work safely
    df_countries = df.copy()
    if data_wanted not in df.columns:
        print("Missing expected column in dataset.")
        return None

    df_array = database_validator(df, df_array, data_column_name)
    # Make sure the time column is in datetime format
    df_countries[time_column_name] = pd.to_datetime(df_countries[time_column_name])

    # Adjust start and end dates to closest available
    start_date,end_date = dateRangeValidator(df_countries, start_date, end_date,time_column_name)


    df_filtered_array = database_validator(df_countries, df_array, data_column_name)

    mask = (
            (df_countries[time_column_name] >= start_date) &
            (df_countries[time_column_name] <= end_date) &
            (df_countries[data_column_name].isin(df_filtered_array)))

    # Filtered data based on both time and array matching
    filtered_data = df_countries.loc[mask, [time_column_name, data_column_name, data_wanted]]

    return filtered_data


def deaths_by_age_group_country(df, ISO3_countries,
                                start_date=None, end_date=None):
    if not ISO3_countries:
        return None

    valid = database_validator(df, ISO3_countries, "Country_code")
    if not valid:
        return None

    d = df[df['Country_code'].isin(valid)].copy()
    d["Date_reported"] = pd.to_datetime(
        dict(year=d["Year"], month=d["Month"], day=1))

    start_date, end_date = dateRangeValidator(
        d, start_date, end_date, "Date_reported")

    d = d[(d["Date_reported"] >= start_date) & (d["Date_reported"] <= end_date)]

    # --- NEW: always return a tidy DF ---
    out = (d.groupby(["Country_code", "Agegroup"])["Deaths"]
             .sum()
             .reset_index()
             .rename(columns={"Country_code": "Group"}))   # unify column name
    return out


def deaths_by_income(df, income_groups,
                     start_date=None, end_date=None):
    if not income_groups:
        return None

    valid = database_validator(df, income_groups, "Wb_income")
    if not valid:
        return None

    dataincome = df[df['Wb_income'].isin(valid)].copy()
    dataincome["Date_reported"] = pd.to_datetime(
        dict(year=dataincome["Year"], month=dataincome["Month"], day=1))

    start_date, end_date = dateRangeValidator(
        dataincome, start_date, end_date, "Date_reported")

    dataincome = dataincome[(dataincome["Date_reported"] >= start_date) & (dataincome["Date_reported"] <= end_date)]

    out = (dataincome.groupby(["Wb_income", "Agegroup"])["Deaths"]
             .sum()
             .reset_index()
             .rename(columns={"Wb_income": "Group"}))
    return out


def deaths_by_age_group_region(df, who_regions,
                               start_date=None, end_date=None):
    if not who_regions:
        return None

    valid = database_validator(df, who_regions, "Who_region")
    if not valid:
        return None

    dataregion = df[df['Who_region'].isin(valid)].copy()
    dataregion["Date_reported"] = pd.to_datetime(
        dict(year=dataregion["Year"], month=dataregion["Month"], day=1))

    start_date, end_date = dateRangeValidator(
        dataregion, start_date, end_date, "Date_reported")

    dataregion = dataregion[(dataregion["Date_reported"] >= start_date) & (dataregion["Date_reported"] <= end_date)]

    out = (dataregion.groupby(["Who_region", "Agegroup"])["Deaths"]
             .sum()
             .reset_index()
             .rename(columns={"Who_region": "Group"}))
    return out


# ---------------------------------------------CALCULATION FUNCTIONS--------------------------------------------#
# ---------------------------------------------CALCULATION FUNCTIONS--------------------------------------------#
# ---------------------------------------------CALCULATION FUNCTIONS--------------------------------------------#
# ---------------------------------------------CALCULATION FUNCTIONS--------------------------------------------#
# ---------------------------------------------CALCULATION FUNCTIONS--------------------------------------------#
vaccinationmetaDF = pd.read_csv('/Users/ilbarskorkmaz/Downloads/database/vaccination-metadata.csv')
vaccinationDF = pd.read_csv('/Users/ilbarskorkmaz/Downloads/database/vaccination-data.csv')
GlobalDailyDF= pd.read_csv('/Users/ilbarskorkmaz/Downloads/database/WHO-COVID-19-global-daily-data.csv')
GlobalWeeklyDF= pd.read_csv('/Users/ilbarskorkmaz/Downloads/database/WHO-COVID-19-global-data.csv')
GlobalHospDF= pd.read_csv('/Users/ilbarskorkmaz/Downloads/database/WHO-COVID-19-global-hosp-icu-data.csv')
GlobalMontlyDeathDF= pd.read_csv('/Users/ilbarskorkmaz/Downloads/database/WHO-COVID-19-global-monthly-death-by-age-data.csv')
GlobalTableDF = pd.read_csv('/Users/ilbarskorkmaz/Downloads/database/WHO-COVID-19-global-table-data.csv')
ui = UserInput()
user_input = ui.prompt_user()


dfs = {
    "global_daily": GlobalDailyDF,  # WHO-COVID-19-global-daily-data.csv
    "global_hosp": GlobalHospDF,  # WHO-COVID-19-global-hosp-icu-data.csv
    "vaccination_data": vaccinationDF,  # vaccination-data.csv
    "vaccination_metadata": vaccinationmetaDF,  # vaccination-metadata.csv
    "table_data": GlobalTableDF,  # WHO-COVID-19-global-table-data.csv
    "monthly_death_age": GlobalMontlyDeathDF  # WHO-COVID-19-global-monthly-death-by-age-data.csv
}
result = dispatchUserQuery(user_input, dfs)
# If result is valid, show it and optionally plot it
# Dispatch and compute result
if result is not None:
    print("\nStatistical result:")
    print(result)
    print(f"\nType of result: {type(result)}")

    plot_choice = input("\nWould you like to visualize this data as a bar graph? (y/n): ").strip().lower()

    if plot_choice == 'y':
        plotResult(result, user_input)

