import os
import streamlit as st
import pandas as pd
from rtStatistics import *
from deathRate import *
from importData import *


# MUST FIX PATH SO CONSISTENT ACROSS PLATFORMS
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)

df = get_data("global_daily")
# run webapp with streamlit run /Users/lysander/Documents/CovidProject/streamlitApp.py
    
def sidebar_date_selector():
    st.sidebar.subheader("Select Start and End Dates")

    # Select start and end time for calculation defaults to
    #   first day of pandemic and WHO official end day
    start_date = st.sidebar.date_input("Pick Start Date", value=df['Date_reported'].min())
    end_date = st.sidebar.date_input("Pick End Date", value=df['Date_reported'].max()) # change to official pandemic end date
    
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    return start_date, end_date

def sidebar_location_selector():
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

def rt_number_sidebar_button():
    if st.sidebar.checkbox("rt number"):
        reproduction_number = rt(df=df, 
                                      country_names=country_names,
                                      who_regions=who_regions,
                                      start_date = start_date,
                                      end_date=end_date)
        rt_value = reproduction_number[0]
        rt_df = reproduction_number[1]
        st.text("The Rt number over time") 
        st.dataframe(rt_value)

        if len(country_names) > 0:
            colouring = 'Country'
        elif len(who_regions) > 0:
            colouring = 'WHO_region'
        else:
            st.error("No country or region selected.")
            return

        st.line_chart(data=rt_df, x = 'Date_reported', y='Rt', color=colouring, x_label='Date', y_label='Rt')


def death_rate_sidebar_button():
    if st.sidebar.checkbox("Death Rate"):

        death_rate_value = death_rate(df=df, 
                                      country_names=country_names,
                                      who_regions=who_regions,
                                      start_date = start_date,
                                      end_date=end_date)[0]
        death_rate_df = death_rate(df, country_names, who_regions, start_date, end_date)[1]
        st.text("The Death Rate Over Time") 
        st.dataframe(death_rate_value)

        if len(country_names) > 0:
            colouring = 'Country'
        elif len(who_regions) > 0:
            colouring = 'WHO_region'
        else:
            st.error("No country or region selected.")
            return

        st.bar_chart(data=death_rate_df, x = colouring, y='death_rate', color=colouring, x_label=colouring, y_label='Death Rate')

        


start_date, end_date = sidebar_date_selector()
country_names, who_regions = sidebar_location_selector()
rt_number_sidebar_button()
death_rate_sidebar_button()
