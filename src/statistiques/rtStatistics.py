import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from .countryOrRegionWrapper import country_or_region
from .layout import layout, summary_stat_checkbox
from .plots import plot_distribution, plot_streamlit_time_series, hist_plot


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
    
    def distribution_plots(self):
        rt_df = self._get_rt_df()

        return plot_distribution(
            df=rt_df, 
            value_column='Rt', 
            group_column=self.region_or_country, 
            title_prefix='Rt')
     
    def time_series(self):
        rt_df = rt_df = self._get_rt_df()
        return plot_streamlit_time_series(
            df=rt_df,
            region_or_country=self.region_or_country,
            date_col='Date_reported',
            value_col='Rt',
            y_label='Rt')
 
    def _summary_stat(self):
        return layout(title="Rt Number", 
               table=self.avg_rt_number(), 
               distribution_plots=self.distribution_plots, 
               timeseries_plot=self.time_series)
         
    def get_checkbox(self):
        return summary_stat_checkbox(title = 'Rt Number', 
                                     selected_column=self.region_or_country, 
                                     summary_stat=self._summary_stat)
    


