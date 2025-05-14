import os
import sys
from zipfile import error

import streamlit as st
import pandas as pd

# import 
from importData import DataImporter
from statistiques.vaccinationStats import VaccinationStats
from statistiques.deathByAgeIncome import AverageDeathsByAgeIncome
from statistiques.averageHospitalizations import AverageHospitalizations
from statistiques.countryOrRegionWrapper import DateAndLocationFilter
from statistiques.rtStatistics import ReproductiveNumber
from statistiques.deathRate import DeathRate
from statistiques.averageDailyCases import AverageDailyCases
from statistiques.averageDailyDeaths import AverageDailyDeaths



def main():
    # Get Paths
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    ROOT_DIR = os.path.dirname(SCRIPT_DIR)
    DATA_DIR = os.path.join(ROOT_DIR, 'data')

    # Constant urls and Filenames
    URL_global_daily = 'https://raw.githubusercontent.com/omerkaraca-fire/data/main/WHO-COVID-19-global-daily-data.csv'
    URL_global_data  = 'https://raw.githubusercontent.com/omerkaraca-fire/data/main/WHO-COVID-19-global-data.csv'
    URL_global_hosp = 'https://raw.githubusercontent.com/omerkaraca-fire/data/main/WHO-COVID-19-global-hosp-icu-data.csv'
    URL_global_monthly_death = 'https://raw.githubusercontent.com/omerkaraca-fire/data/main/WHO-COVID-19-global-monthly-death-by-age-data.csv'
    URL_global_vaccination = "https://raw.githubusercontent.com/omerkaraca-fire/data/main/vaccination-data.csv"
    URL_global_meta = "https://raw.githubusercontent.com/omerkaraca-fire/data/main/vaccination-metadata.csv"

    GLOBAL_DAILY_DATA_FILE = "WHO-COVID-19-global-daily-data.csv"
    GLOBAL_DATA_FILE = "WHO-COVID-19-global-data.csv"
    GLOBAL_HOSP_DATA_FILE = "WHO-COVID-19-global-hosp-icu-data.csv"
    GLOBAL_MONTHLY_DEATH_DATA_FILE = "WHO-COVID-19-global-monthly-death-by-age-data.csv"
    GLOBAL_VACCINATION_DATA_FILE = "vaccination-data.csv"
    GLOBAL_META_DATA_FILE ="vaccination-metadata.csv"

    DATA_FILE_ARR = [GLOBAL_DAILY_DATA_FILE,
                     GLOBAL_DATA_FILE,
                     GLOBAL_HOSP_DATA_FILE,
                     GLOBAL_MONTHLY_DEATH_DATA_FILE,
                     GLOBAL_VACCINATION_DATA_FILE,
                     GLOBAL_META_DATA_FILE]
    URL_ARR = [URL_global_daily,
                URL_global_data,
                URL_global_hosp,
                URL_global_monthly_death,
                URL_global_vaccination,
                URL_global_meta]

    importer_objects = []
    dataframes = []

    for url, filename in zip(URL_ARR, DATA_FILE_ARR):
        importer = DataImporter(url=url, filename=filename, data_dir=DATA_DIR)
        df = importer.load_data()

        importer_objects.append(importer)
        dataframes.append(df)
    daily_df = importer_objects[0].set_date_time(dataframes[0])
    global_df = dataframes[1]
    hosp_df = importer_objects[2].set_date_time(dataframes[2])

    #montly death df doesn not have date column it needs to be created manually and this is done in the
    # deathbyage.py file

    monthly_death_df = importer_objects[3].fix_monthly_death(dataframes[3])
    monthly_death_df.rename(columns={"Who_region": "WHO_region"},inplace=True)

    vaccination_df = dataframes[4]
    vaccination_df.rename(columns={"DATE_UPDATED": "Date_reported", "COUNTRY": "Country", "WHO_REGION" : "WHO_region"},inplace=True)

    vaccination_df = importer_objects[4].set_date_time(dataframes[4])
    vaccination_df["WHO_region"] = vaccination_df["WHO_region"].str.replace(r"O$", "", regex=True)
    meta_df = dataframes[5]



    # Set page config
    st.set_page_config(page_title="COVID-19 Evolution Dashboard", layout="wide")

    start_date, end_date = sidebar_date_selector(df=daily_df)
    countries, who_regions = sidebar_location_selector(df=daily_df)


    # there is a case for unexpected arguments, thus used kwargs to handle them
    daily_statistics = [
        (AverageDailyCases, {}, daily_df),
        (DeathRate, {}, daily_df),
        (AverageDailyDeaths, {}, daily_df),
        (ReproductiveNumber, {}, daily_df),
        (AverageHospitalizations,
         {"label": "New Hospitalizations"},
         hosp_df),

        (AverageHospitalizations,
         {"label": "New ICU Admissions"},
         hosp_df),

         (VaccinationStats,
          {"value_col": "TOTAL_VACCINATIONS",
           "name_given": "Total Doses",
           "label": "Total Doses"},
          vaccination_df),

         (VaccinationStats,
          {"value_col": "PERSONS_VACCINATED_1PLUS_DOSE_PER100",
           "name_given": "% Population ≥ 1 Dose",
           "label": "% ≥ 1 Dose"},
          vaccination_df),

         (VaccinationStats,
          {"value_col": "PERSONS_BOOSTER_ADD_DOSE_PER100",
           "name_given": "Booster Coverage (%)",
           "label": "Booster Coverage %"},
          vaccination_df),
    ]

    for daily_stat, extra, source_df in daily_statistics:
            daily_stats_checkbox(df=source_df.copy(),
                                 stat_object=daily_stat,
                                 extra_kwargs=extra,
                                 countries=countries,
                                 who_regions=who_regions,
                                 start_date=start_date,
                                 end_date=end_date)

    # Age and Income part had to do it separately, because of issues that couldn't be solvesd
    if st.sidebar.checkbox("Deaths by Age and Income"):
        # user pick age group and income group
        ages = sorted(monthly_death_df["Agegroup"].astype(str).unique())
        incomes = sorted(monthly_death_df["Wb_income"].astype(str).unique())
        sel_ages = st.sidebar.multiselect(
            "Age group", ages, default=ages, key="age_sel_deaths")
        sel_inc = st.sidebar.multiselect(
            "WB income level", incomes, default=incomes, key="inc_sel_deaths")

        #filtering acording to chosen groups
        df_ai = monthly_death_df[
            monthly_death_df["Agegroup"].isin(sel_ages) &
            monthly_death_df["Wb_income"].isin(sel_inc)
            ]
        if not countries and not who_regions:
            st.info("Select at least one **Country** or **WHO Region** to display results.")
            st.stop()
        #Had to implement a daily static in here, because of the way the data is structured and the mechanism work
        # If it works without problem, please feel welcome to remove it
        filt_obj = DateAndLocationFilter(
            df=df_ai,
            countries=countries,
            regions=who_regions,
            start_date=start_date,
            end_date=end_date,
        )
        df_ai_filt = filt_obj.get_filtered_df()
        geo_col = filt_obj.choose_country_or_who_region()

        # 4) build the metric and render it *without* its own checkbox
        metric = AverageDeathsByAgeIncome(
            filtered_df=df_ai_filt,
            region_or_country=geo_col,
        )
        if df_ai_filt.empty:
            st.warning("No data for the chosen Age/Income + Country/Region combination.")
            st.stop()
        if countries or who_regions is not None :
            metric.summary_stat()
# run webapp with streamlit run /Users/lysander/Documents/CovidProject/streamlitApp.py
    
def sidebar_date_selector(df):
    st.sidebar.subheader("Select Start and End Dates")

    # Select start and end time for calculation defaults to
    #   first day of pandemic and WHO official end day
    start_date = st.sidebar.date_input("Pick Start Date", value=df['Date_reported'].min())
    end_date = st.sidebar.date_input("Pick End Date", value=df['Date_reported'].max()) # change to official pandemic end date
    
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    return start_date, end_date


def sidebar_daily_weekly_monthly_selector():
    return st.sidebar.radio(
        "Granularity", ["Daily", "Weekly", "Monthly"],
        index=0
    )

def sidebar_location_selector(df):
    st.sidebar.subheader("Select Country or  WHO Region")

    # All Unique Countries
    countries = df["Country"].unique()
    countries.sort()

    # All Unique Who Regions
    who_regions = df['WHO_region'].unique()
    who_regions.sort()

    selected_who_regions = st.sidebar.multiselect("Choose at least one region", who_regions)

    if selected_who_regions :
        available_countries = df[df['WHO_region'].isin(selected_who_regions)]['Country'].unique().tolist()
    else:
        available_countries = countries 

    selected_countries = st.sidebar.multiselect("Choose at least one country", available_countries)

    if selected_countries:
        selected_who_regions = []

    return selected_countries, selected_who_regions

def daily_stats_checkbox(df, stat_object, countries, who_regions, start_date, end_date, extra_kwargs=None):
        extra_kwargs = extra_kwargs or {}
        filtered_obj = DateAndLocationFilter(
            df=df.copy(),
            countries=countries, regions=who_regions, 
            start_date=start_date, end_date=end_date)
        filtered_df = filtered_obj.get_filtered_df()
        selected_column = filtered_obj.choose_country_or_who_region()

        stat_obj = stat_object(
            filtered_df=filtered_df,
            region_or_country=selected_column,
            **{k: v for k, v in extra_kwargs.items() if k != "label"}
        )

        label = extra_kwargs.get("label")
        if label is not None:
            stat_obj.get_checkbox(label=label)
        else:
            stat_obj.get_checkbox()



if __name__ == "__main__":
    main()
