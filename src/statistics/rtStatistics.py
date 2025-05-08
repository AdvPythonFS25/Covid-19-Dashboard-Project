import pandas as pd 
import numpy as np
from .countryOrRegionWrapper import country_or_region


def rt_country(df, country_names, start_date, end_date):
    """Rt (reproductive time) calculation per country

    Args:
        df (Pandas dataframe)
        country_names (List)
        start_date (Datetime obj)
        end_date (Datetime obj)

    Returns:
        Value, Dataframe:
    """

    #df with countries the user selected
    df_countries = df[df['Country'].isin(country_names)].copy()

    #preprocess data
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    df_countries.fillna(0, inplace=True)
    df_countries['Date_reported'] = pd.to_datetime(df_countries['Date_reported'])
    df_countries = df_countries.sort_values('Date_reported')

    #Calculate Rt
    df_countries['Rt'] = df_countries.groupby('Country')['New_cases'].transform(lambda x: x / x.shift(1))
    df_countries['Rt'].replace([np.inf, -np.inf], np.nan, inplace=True) #replace inf values with NaN
    df_countries['Rt'].fillna(0, inplace=True) #replace all NaN with 0 

    #filter by date range
    df_filtered = df_countries[(df_countries["Date_reported"] >= start_date) & (df_countries["Date_reported"] <= end_date)]

    #Return average Rt and last Rt in date range per country
    averages = df_filtered.groupby('Country').agg(AverageRt=('Rt', 'mean')).reset_index()

    return averages, df_filtered


def rt_region (df, who_regions, start_date, end_date):
    """Rt (reproductive time) calculation per region

    Args:
        df (Pandas dataframe)
        country_names (List)
        start_date (Datetime obj)
        end_date (Datetime obj)

    Returns:
        Value, Dataframe:
    """

    #df with WHO regions the user selected
    df_regions = df[df['WHO_region'].isin(who_regions)].copy()
    
    #preprocess data
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    df_regions.fillna(0, inplace=True)
    df_regions["Date_reported"] = pd.to_datetime(df_regions["Date_reported"])
    df_regions = df_regions.sort_values('Date_reported')

    #calculate Rt
    df_regions['Rt'] = df_regions.groupby('WHO_region')['New_cases'].transform(lambda x: x / x.shift(1))
    df_regions['Rt'].replace([np.inf, -np.inf], np.nan, inplace=True) #replace inf values with NaN
    df_regions['Rt'].fillna(0, inplace=True) #replace all NaN with 0 

    #filter by date range
    df_filtered = df_regions[(df_regions["Date_reported"] >= start_date) & (df_regions["Date_reported"] <= end_date)]
    
    #Return average Rt and last Rt in date range per country
    averages = df_filtered.groupby('WHO_region').agg(AverageRt=('Rt', 'mean')).reset_index()

    return averages, df_filtered

def rt(df, country_names, who_regions, start_date, end_date):
    """
    Calls the wrapper function to select region or country based of user input
    """
    return country_or_region(
        countries_function= rt_country,
        regions_function=rt_region,
        df=df,
        country_names=country_names,
        who_regions=who_regions,
        start_date=start_date,
        end_date=end_date)
