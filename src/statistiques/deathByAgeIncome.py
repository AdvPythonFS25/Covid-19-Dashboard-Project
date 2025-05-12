import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from .layout import layout, summary_stat_checkbox
from .plots import plot_distribution, plot_streamlit_time_series, plot_streamlit_time_series_monthly


def get_mode(series):
    mode_series = series.mode()
    if not mode_series.empty:
        return mode_series.iloc[0]
    return None



# The original data doesn't have a column for Date_reported it justs has the month and year; thus there should it will be taken as the first day of the month
# Also need to create a new column for the Date_reported using that information.
class AverageDeathsByAgeIncome:

    def __init__(self, filtered_df, region_or_country):  # built for daily DF filtered by date and region
        self.filtered_df = filtered_df.copy()
        if "Date_reported" not in self.filtered_df.columns:
            self.filtered_df["Date_reported"] = pd.to_datetime(
                dict(year=self.filtered_df["Year"], month=self.filtered_df["Month"], day=1)
            )
        # Convert the 'Date_reported' column to datetime format
        self.region_or_country = region_or_country
        self.key = region_or_country

    #if not said the choice considered to be Agegroup
    def avg_deaths_age_income(self):

        self.filtered_df.fillna(0, inplace=True)
        # if no values are selected for country and region
        if self.region_or_country not in ["Country", "WHO_region"]:
            st.error("Invalid selection for country or region.")
            return None
        #Column name could be
        summary_deaths = self.filtered_df.groupby(self.region_or_country)["Deaths"].agg(['mean','median','min','max', 'count','std']).reset_index()
        summary_deaths.columns = [self.region_or_country, 'Mean', 'Median','Min', 'Max', 'Count','Std']

        # Round the results to 2 decimal places
        return summary_deaths.round(2)

    def distribution_plots(self):
        return plot_distribution(
            df=self.filtered_df,
            value_column="Deaths",
            group_column=self.region_or_country,
            title_prefix='Deaths',)

    def time_series(self):
        return plot_streamlit_time_series_monthly(
            df=self.filtered_df,
            region_or_country=self.region_or_country,
            date_col='Date_reported',
            value_col="Deaths",
            y_label="Deaths",)

    def summary_stat(self) -> None:
        return layout(title="Deaths by Age and Income",
                      table=self.avg_deaths_age_income(),
                      distribution_plots=self.distribution_plots,
                      timeseries_plot=self.time_series)


    def get_checkbox(self):
        visible_title = "Deaths by Age and Income"
        key = "deaths_age_income_checkbox"  # <── stays the same each rerun
        return summary_stat_checkbox(
            title="SHOW THE SELECTION DATA",  # empty label ⇒ invisible
            selected_column=self.region_or_country,
            summary_stat=self.summary_stat,
            key="key",
        )