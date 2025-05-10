import os
import sys
import streamlit as st
import pandas as pd

# import 
from importData import DataImporter
from statistics.countryOrRegionWrapper import DateAndLocationFilter
from statistics.rtStatistics import rt
from statistics.deathRate import death_rate
from statistics.averageDailyCases import AverageDailyCases


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
    country_names, who_regions = sidebar_location_selector(df=daily_df)

    rt_number_sidebar_button(df=daily_df, 
                             country_names=country_names,
                             who_regions=who_regions, 
                             start_date=start_date, 
                             end_date=end_date)

    death_rate_sidebar_button(df=daily_df, 
                              country_names=country_names,
                              who_regions=who_regions, 
                              start_date=start_date, 
                              end_date=end_date)
        
    daily_cases_sidebar_button(df=daily_df, 
                              countries=country_names,
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

def rt_number_sidebar_button(df, country_names, who_regions, start_date, end_date):
    if st.sidebar.checkbox("rt number"):
        rt_value, rt_df = rt(df=df, 
                                      country_names=country_names,
                                      who_regions=who_regions,
                                      start_date = start_date,
                                      end_date=end_date)
        
        st.subheader("The Rt number over time") 
        st.dataframe(rt_value)

        if len(country_names) > 0:
            colouring = 'Country'
        elif len(who_regions) > 0:
            colouring = 'WHO_region'
        else:
            st.error("No country or region selected.")
            return

        st.line_chart(data=rt_df, x = 'Date_reported', y='Rt', color=colouring, x_label='Date', y_label='Rt')


def death_rate_sidebar_button(df, country_names, who_regions, start_date, end_date):
    if st.sidebar.checkbox("Death Rate"):

        death_rate_value, death_rate_df = death_rate(df=df, 
                                      country_names=country_names,
                                      who_regions=who_regions,
                                      start_date = start_date,
                                      end_date=end_date)
        
        st.subheader("The Death Rate Over Time") 
        st.dataframe(death_rate_value)

        if len(country_names) > 0:
            colouring = 'Country'
        elif len(who_regions) > 0:
            colouring = 'WHO_region'
        else:
            st.error("No country or region selected.")
            return

        st.line_chart(data=death_rate_df, x = 'Date_reported', y='death_rate', color=colouring, x_label='Date', y_label='Death Rate')

def daily_cases_sidebar_button(df, countries, who_regions, start_date, end_date):
    if st.sidebar.checkbox("Daily Cases"):
        # Filtered instance and get date time filtered df
        filtered_df_obj = DateAndLocationFilter(df=df, countries=countries, regions=who_regions, start_date=start_date, end_date=end_date)
        filtered_df = filtered_df_obj.date_location_filter()
        region_or_country = filtered_df_obj.choose_country_or_who_region()

       # daily cases obj 
        daily_cases_obj = AverageDailyCases(filtered_df=filtered_df, 
                                            region_or_country=region_or_country)
        st.dataframe(daily_cases_obj.avg_daily_cases())
        







if __name__ == "__main__":
    main()