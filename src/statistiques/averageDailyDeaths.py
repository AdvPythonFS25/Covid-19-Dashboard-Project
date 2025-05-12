import pandas as pd 
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from .layout import layout, summary_stat_checkbox
from .plots import plot_distribution, plot_streamlit_time_series

def get_mode(series):
    mode_series = series.mode() 
    if not mode_series.empty:  
        return mode_series.iloc[0]  
    return None

class AverageDailyDeaths:

    def __init__(self, filtered_df, region_or_country): # built for daily DF filtered by date and region
        self.filtered_df = filtered_df.copy()
        self.region_or_country = region_or_country

    def avg_daily_deaths(self):
        self.filtered_df.fillna(0, inplace=True)
        # if no values are selected for country and region
        if self.region_or_country not in ["Country", "WHO_region"]:
            st.error("Invalid selection for country or region.")
            return None
        

        summary_deaths = self.filtered_df.groupby(self.region_or_country)["New_deaths"].agg(
            mean='mean', 
            median='median', 
            mode=get_mode,  
            std='std'  
        ).reset_index()
        
        # Round the results to 2 decimal places
        return summary_deaths.round(2)
    

    def distribution_plots(self):
        return plot_distribution(
            df=self.filtered_df,
            value_column="New_deaths",
            group_column=self.region_or_country,
            title_prefix='Daily Deaths')
        
    def time_series(self):
        return plot_streamlit_time_series(
            df=self.filtered_df,
            region_or_country=self.region_or_country,
            date_col='Date_reported',
            value_col='New_deaths',
            y_label="Daily Deaths")
    
    def _summary_stat(self):
        return layout(title="Average Daily Deaths", 
               table=self.avg_daily_deaths(), 
               distribution_plots=self.distribution_plots, 
               timeseries_plot=self.time_series)
        
    def get_checkbox(self):
        return summary_stat_checkbox(title = 'Daily Deaths', 
                                     selected_column=self.region_or_country, 
                                     summary_stat=self._summary_stat)