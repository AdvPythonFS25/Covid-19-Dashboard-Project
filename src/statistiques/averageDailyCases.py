import pandas as pd 
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from .layout import layout, summary_stat_checkbox
from . plots import plot_distribution, plot_streamlit_time_series

class AverageDailyCases:

    def __init__(self, filtered_df, region_or_country): # built for daily DF filtered by date and region
        self.filtered_df = filtered_df.copy()
        self.region_or_country = region_or_country

    def avg_daily_cases(self):
        self.filtered_df.fillna(0, inplace=True)
        # if no values are selected for country and region
        if self.region_or_country not in ["Country", "WHO_region"]:
            st.error("Invalid selection for country or region.")
            return None
        
        summary_cases = self.filtered_df.groupby(self.region_or_country)["New_cases"].agg(['mean', 'median']).reset_index()
        summary_cases.columns = [self.region_or_country, 'Mean', 'Median']
        return summary_cases.round(2)

    def distribution_plots(self):
        return plot_distribution(
            df=self.filtered_df,
            value_column="New_cases",
            group_column=self.region_or_country,
            title_prefix='Daily New Cases')
        
    def time_series(self):
        return plot_streamlit_time_series(
            df=self.filtered_df,
            region_or_country=self.region_or_country,
            date_col='Date_reported',
            value_col='New_cases',
            y_label="Daily New Cases")
    
    def _summary_stat(self):
        return layout(title="Average New Cases", 
               table=self.avg_daily_cases(), 
               distribution_plots=self.distribution_plots, 
               timeseries_plot=self.time_series)
        
    def get_checkbox(self):
        return summary_stat_checkbox(title = 'Daily Cases', 
                                     selected_column=self.region_or_country, 
                                     summary_stat=self._summary_stat)