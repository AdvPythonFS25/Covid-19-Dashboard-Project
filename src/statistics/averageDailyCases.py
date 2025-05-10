import pandas as pd 
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

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
        
        avg_cases = self.filtered_df.groupby(self.region_or_country)["New_cases"].mean()
        avg_cases = avg_cases.rename("Average")
        return avg_cases.round(2)

    def daily_cases_histogram(self): # locations are either regions or countries

        unique_entries = self.filtered_df[self.region_or_country].nunique()

        if unique_entries == 1:
            fig, ax = plt.subplots(1, 1, figsize=(19, 6))
            ax.hist(self.filtered_df["New_cases"], colour= 'skyblue')

            return st.pyplot(fig)
        elif unique_entries > 1 and unique_entries <= 15:

            fig, ax = plt.subplots(1, 1, figsize=(19, 6))

            # make hist for every selected entry
            for location in unique_entries:
                location_df = self.filtered_df[self.filteed_df[self.region_or_country] == location]
                ax.hist(location_df["New_cases"], 
                        bins=30, alpha=0.5, label=location, stacked=True, edgecolor='black')
                
            return st.pyplot(fig) 
        elif unique_entries > 15:
            fig, ax = plt.subplots(1, 1, figsize=(19, 6))
            ax.hist(self.filtered_df["New_cases"], colour= 'skyblue')



        
