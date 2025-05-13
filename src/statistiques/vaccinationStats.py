import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from .layout import layout, summary_stat_checkbox, layout_without_distribution
from .plots import plot_distribution, plot_streamlit_time_series_weekly, plot_streamlit_time_series_monthly, \
    plot_streamlit_barchart, basic_table


class VaccinationStats:

    def __init__(self, filtered_df, region_or_country, name_given,value_col= "TOTAL_VACCINATIONS"):  # built for daily DF filtered by date and region
        self.filtered_df = filtered_df.copy()
        # Convert the 'Date_reported' column to datetime format
        self.region_or_country = region_or_country
        self.col = value_col
        self.name = name_given

    #if not said the choice considered to be Agegroup
    def _summary_table(self):

        self.filtered_df.fillna(0, inplace=True)
        # if no values are selected for country and region
        if self.region_or_country not in ["Country", "WHO_region"]:
            st.error("Invalid selection for country or region.")
            return None
        #Column name could be

        summary_vaccination = self.filtered_df.groupby(self.region_or_country)[self.col].agg(['mean', 'median', 'min', 'max', 'count', 'std']).reset_index()
        summary_vaccination.columns = [self.region_or_country, 'Mean', 'Median','Min', 'Max', 'Count','Std']

        # Round the results to 2 decimal places
        return summary_vaccination.round(2)

    def _render(self):
        return basic_table(self.filtered_df, self.region_or_country, self.col, self.name)


    def _country_region_plot(self):
        return plot_streamlit_barchart(
            df=self.filtered_df,
            region_or_country=self.region_or_country,
            value_col=self.col,
            y_label=self.col,)

    def _summary_stat(self) -> None:
        return layout_without_distribution(title=self.name,
                      table=self._summary_table(),
                      timeseries_plot=self._country_region_plot,)


    def get_checkbox(self, label = "None", key_suffix = ""):
        visible_title = label or f"Show {self.col}"
        key = f"vax_{self.col}_{key_suffix}"  # <── stays the same each rerun
        return summary_stat_checkbox(
            title=label,  # empty label ⇒ invisible
            selected_column=self.region_or_country,
            summary_stat=self._summary_stat,
            key= key,
        )