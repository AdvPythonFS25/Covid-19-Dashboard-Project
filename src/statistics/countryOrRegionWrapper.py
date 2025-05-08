import streamlit as st

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
