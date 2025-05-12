import streamlit as st
import pandas as pd

def country_or_region(countries_function, regions_function,
                       df, country_names, who_regions, start_date, end_date):
    """ Chooses country or region columns depending on user input """

    if len(country_names) > 0:
        return countries_function(df=df, country_names=country_names,
                         start_date=start_date, end_date=end_date)

    elif len(who_regions) > 0:
        return regions_function(df=df, who_regions=who_regions,
                         start_date=start_date, end_date=end_date)
    else:
        st.error("No country or region selected.")


class DateAndLocationFilter:

    def __init__(self, df, start_date, end_date, countries, regions):
        self.df = df
        self.start_date = start_date
        self.end_date = end_date
        self.countries = countries 
        self.regions = regions


    def choose_country_or_who_region(self):
        """ Chooses country or region columns depending on user input """

        if len(self.countries) > 0:
            return "Country"
        
        elif len(self.regions) > 0:
            return "WHO_region"
        
        else:
            st.error("No country or region selected.")

    #Legacy code if needed can be used
    def getClosestDate(self, selectedDate):
        selectedDate = pd.to_datetime(selectedDate)
        # goes trough every date possible and find the minimum difference and returns that date created the minimum date.
        closest = min(self.df["Date_reported"], key=lambda x: abs(x - selectedDate))

    def get_filtered_df(self):

        filtered_df = self.df[
            (self.df["Date_reported"] >= pd.to_datetime(self.start_date)) &
            (self.df["Date_reported"] <= pd.to_datetime(self.end_date))
        ]

        if len(self.countries) > 0:
            filtered_df = filtered_df[filtered_df['Country'].isin(self.countries)]
        elif len(self.regions) > 0:
            filtered_df = filtered_df[filtered_df['WHO_region'].isin(self.regions)]

        return filtered_df
    


        

        