import os
import sys
import streamlit as st
import pandas as pd

# import 
from importData import DataImporter
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
    URL = 'https://srhdpeuwpubsa.blob.core.windows.net/whdh/COVID/WHO-COVID-19-global-daily-data.csv'
    GLOBAL_DAILY_DATA_FILE = "WHO-COVID-19-global-daily-data.csv"


    # create Dataimporter instance and load data
    global_daily_data_object = DataImporter(url=URL, filename=GLOBAL_DAILY_DATA_FILE, data_dir=DATA_DIR)
    daily_df = global_daily_data_object.load_data()

    # maybe change this to a seperate processing class (not sure yet)
    daily_df = global_daily_data_object.set_datetime(daily_df) 
    

    # Set page config
    st.set_page_config(page_title="COVID-19 Evolution Dashboard", layout="wide")

    start_date, end_date = sidebar_date_selector(df=daily_df)
    countries, who_regions = sidebar_location_selector(df=daily_df)

    daily_statistics = [AverageDailyCases, DeathRate, AverageDailyDeaths, ReproductiveNumber]
    
    for daily_stat in daily_statistics:
        
        daily_stats_checkbox(df=daily_df, 
                            stat_object=daily_stat, 
                            countries=countries, 
                            who_regions=who_regions, 
                            start_date=start_date, 
                            end_date=end_date)
    
    

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


#def rt_number_sidebar_button(df, countries, who_regions, start_date, end_date):
    if not st.sidebar.checkbox("rt_number"):
        return # exit if check isnt checked
    
    # Filtered instance and get date time filtered df
    filtered_obj = DateAndLocationFilter(
        df=df, 
        countries=countries, 
        regions=who_regions, 
        start_date=start_date, 
        end_date=end_date)
    
    filtered_df = filtered_obj.get_filtered_df()
    selected_column = filtered_obj.choose_country_or_who_region()

    if not selected_column: # dont use 'is none'
        return  # exit if no country or who region is selected
    
    daily_cases_obj = ReproductiveNumber(
        filtered_df=filtered_df, 
        region_or_country=selected_column
        )
    
    st.subheader("Average Reproductive Number")
    
    col1, col2 = st.columns(2)

    with col1:
        avg_df = daily_cases_obj.avg_rt_number()
        st.dataframe(avg_df) 

    with col2:
        # to be preplace with some graph
        st.text('some graph showing variation : boxplot/violin plot or overlayed histograms')

    # To be replaced with some other graph
    avg_df = daily_cases_obj.avg_rt_number()
    st.dataframe(avg_df)

    st.text('some graph over time : lineplot. fix bug when plotting by region to many things  ')

def daily_stats_checkbox(df, stat_object, countries, who_regions, start_date, end_date):
        filtered_obj = DateAndLocationFilter(
            df=df, 
            countries=countries, regions=who_regions, 
            start_date=start_date, end_date=end_date)
        
        filtered_df = filtered_obj.get_filtered_df()
        selected_column = filtered_obj.choose_country_or_who_region()

        stat_obj = stat_object(filtered_df=filtered_df, region_or_country=selected_column)
        stat_obj.get_checkbox()



if __name__ == "__main__":
    main()
