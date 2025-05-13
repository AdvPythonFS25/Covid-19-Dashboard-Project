import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from .layout import layout, summary_stat_checkbox
from .plots import plot_distribution, plot_streamlit_time_series_weekly


def get_mode(series):
    mode_series = series.mode()
    if not mode_series.empty:
        return mode_series.iloc[0]
    return None


class AverageHospitalizations:

    def __init__(self, filtered_df, region_or_country, value_col="New_hospitalizations_last_7days"):  # built for daily DF filtered by date and region
        self.value_col = value_col
        self.filtered_df = filtered_df.copy()
        self.region_or_country = region_or_country

    #if not said the choice considered to be New_hospitalizations_last_7days
    def avg_hosp_icu_weekly_montly(self):
        self.filtered_df.fillna(0, inplace=True)
        # if no values are selected for country and region
        if self.region_or_country not in ["Country", "WHO_region"]:
            st.error("Invalid selection for country or region.")
            return None
        #Column name could be New_hospitalizations_last_7days, New_hospitalizations_last_28days, New_icu_admissions_last_7days, New_icu_admissions_last_28days
        #ICU admissions are for the severe cases
        summary_hospitalizations_icu = self.filtered_df.groupby(self.region_or_country)[self.value_col].agg(['mean','median','min','max', 'count','std']).reset_index()
        summary_hospitalizations_icu.columns = [self.region_or_country, 'Mean', 'Median','Min', 'Max', 'Count','Std']

        # Round the results to 2 decimal places
        return summary_hospitalizations_icu.round(2)

    def distribution_plots(self):
        return plot_distribution(
            df=self.filtered_df,
            value_column=self.value_col,
            group_column=self.region_or_country,
            title_prefix='Hospitalizations or ICU admissions distribution plots',)

    def time_series(self):
        return plot_streamlit_time_series_weekly(
            df=self.filtered_df,
            region_or_country=self.region_or_country,
            date_col='Date_reported',
            value_col=self.value_col,
            y_label="Daily Hospitalizations or ICU admissions time series",)

    def _summary_stat(self):
        return layout(title="Average Daily Hospitalizations or ICU admissions summary statistics",
                      table=self.avg_hosp_icu_weekly_montly(),
                      distribution_plots=self.distribution_plots,
                      timeseries_plot=self.time_series)

    def get_checkbox(self):
        visible_title = "Hospital / ICU admissions"
        unique_key = f"{visible_title}_{self.value_col}"

        return summary_stat_checkbox(title=self.value_col,
                                     selected_column=self.region_or_country,
                                     summary_stat=self._summary_stat,
                                     key=unique_key)