import pandas as pd 
import numpy as np
from .countryOrRegionWrapper import country_or_region

class ReproductiveNumber:
    def __init__(self, filtered_df, region_or_country): # built for daily DF filtered by date and region
        self.filtered_df = filtered_df.copy()
        self.region_or_country = region_or_country

    def _get_rt_df(self):
        rt_df = self.filtered_df.copy()
        rt_df['Rt'] = self.filtered_df.groupby(self.region_or_country)['New_cases'].transform(lambda x: x / x.shift(1))
        rt_df['Rt'].replace([np.inf, -np.inf], np.nan, inplace=True) #replace inf values with NaN
        rt_df['Rt'].fillna(0, inplace=True) #replace all NaN with 0
        return rt_df
    
    def avg_rt_number(self): 
        rt_df = self._get_rt_df()
        averages = rt_df.groupby(self.region_or_country).agg(AverageRt=('Rt', 'mean')).reset_index()
        return averages
    
    def rt_histogram(self):
        pass # use  _get_rt_df to make a histogram or maybe seaborn violine plot?
    
    def rt_line_plot(self):
        #    st.line_chart(data=rt_df, x = 'Date_reported', y='Rt', color=colouring, x_label='Date', y_label='Rt')
        pass # use  _get_rt_df to make a lineplot



def rt_country(df, country_names, start_date, end_date):

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
