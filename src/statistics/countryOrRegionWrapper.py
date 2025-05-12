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
        if self.countries:
            # • ISO-3 codes are 3 upper-case letters (e.g. "USA")
            if all(len(c) == 3 and c.isupper() for c in self.countries):
                return "Country_code"
            return "Country"
        if self.regions:
            return "WHO_region"
        st.error("No country or region selected.")
        return None

    def get_filtered_df(self) -> pd.DataFrame:
        df = self.df.copy()
        df["Date_reported"] = pd.to_datetime(df["Date_reported"])

        # date slice first
        df = df.query("@self.start_date <= Date_reported <= @self.end_date")

        if self.countries:
            key = self.choose_country_or_who_region()
            df = df[df[key].isin(self.countries)]
        elif self.regions:
            df = df[df["WHO_region"].isin(self.regions)]

        return df
    


        

        