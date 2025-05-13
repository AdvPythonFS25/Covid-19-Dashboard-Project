import pandas as pd
from .countryOrRegionWrapper import country_or_region
import streamlit as st
from .plots import plot_distribution, plot_streamlit_time_series_weekly
from .layout import layout, summary_stat_checkbox

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
    
    def distribution_plots(self):
        death_rate_df = self._get_death_rate_df()
        return plot_distribution(
            df=death_rate_df,
            value_column="death_rate",
            group_column=self.region_or_country,
            title_prefix='Death Rate (%)')
        
    def time_series(self):
        death_rate_df = self._get_death_rate_df()
        return plot_streamlit_time_series_weekly(
            df=death_rate_df,
            region_or_country=self.region_or_country,
            date_col='Date_reported',
            value_col="death_rate",
            y_label="death_rate")
    
    def _summary_stat(self):
                layout(title="Death Rate", 
               table=self.avg_death_rate(), 
               distribution_plots=self.distribution_plots, 
               timeseries_plot=self.time_series)
                
    def get_checkbox(self):
            return summary_stat_checkbox(title = 'Death Rate', 
                                     selected_column=self.region_or_country, 
                                     summary_stat=self._summary_stat)

    

