import pandas as pd
from .countryOrRegionWrapper import country_or_region

class DeathRate:
    def __init__(self, filtered_df, region_or_country): # built for daily DF filtered by date and region
        self.filtered_df = filtered_df.copy()
        self.region_or_country = region_or_country

    def _get_death_rate_df(self):
        death_rate_df = self.filtered_df.copy()
        death_rate_df.fillna(0, inplace=True)
        death_rate_df = death_rate_df.sort_values('Date_reported')

        death_rate_df['death_rate']= death_rate_df.apply(lambda row: 
                                          ((row['Cumulative_deaths']/row['Cumulative_cases'])*100) 
                                          if row['Cumulative_cases'] > 0 else 0, axis= 1)
        return death_rate_df
    
    def avg_death_rate(self):
        death_rate_df = self._get_death_rate_df()
        averages = death_rate_df.groupby(self.region_or_country).agg(AverageDeathRate =('death_rate', 'mean')).reset_index()
        return averages
    
    def death_rate_lineplot(self):
        pass

    def death_rate_histogram(self):
        pass

def death_rate_country(df, country_names, start_date, end_date):
    """Calculate death rate by region

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

    #Calculate death rate as (n deaths / n cases) * 100 per row
    df_countries['death_rate'] = df_countries.apply(lambda row: ((row['Cumulative_deaths']/row['Cumulative_cases'])*100) if row['Cumulative_cases'] > 0 else 0, axis= 1)

    #filter by date range
    df_filtered = df_countries[(df_countries["Date_reported"] >= start_date) & (df_countries["Date_reported"] <= end_date)]

    #Return average Rt and last Rt in date range per country
    averages = df_filtered.groupby('Country').agg(AverageDeathRate =('death_rate', 'mean')).reset_index()

    return averages, df_filtered

def death_rate_region(df, who_regions, start_date, end_date):
    """Calculate death rate by region

    Args:
        df (Pandas dataframe)
        country_names (List)
        start_date (Datetime obj)
        end_date (Datetime obj)

    Returns:
        Value, Dataframe: 
    """

    #df with countries the user selected
    df_region = df[df['WHO_region'].isin(who_regions)].copy()

    #preprocess data
    df_region.fillna(0, inplace=True)
    df_region['Date_reported'] = pd.to_datetime(df_region['Date_reported'])
    df_region = df_region.sort_values('Date_reported')

    #Calculate death rate as (n deaths / n cases) * 100 per row
    df_region['death_rate'] = df_region.apply(lambda row: ((row['Cumulative_deaths']/row['Cumulative_cases'])*100) if row['Cumulative_cases'] > 0 else 0, axis= 1)

    #filter by date range
    df_filtered = df_region[(df_region["Date_reported"] >= start_date) & (df_region["Date_reported"] <= end_date)]

    #Return average Rt and last Rt in date range per country
    averages = df_filtered.groupby('WHO_region').agg(AverageDeathRate =('death_rate', 'mean')).reset_index()

    return averages, df_filtered

def death_rate(df, country_names, who_regions, start_date, end_date):
    """
    Calls the wrapper function to select region or country based of user input
    """
    return country_or_region(
        countries_function=death_rate_country,
        regions_function=death_rate_region,
        df=df,
        country_names=country_names,
        who_regions=who_regions,
        start_date=start_date,
        end_date=end_date)
