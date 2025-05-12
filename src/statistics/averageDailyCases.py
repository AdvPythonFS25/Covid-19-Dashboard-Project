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
        summary_cases = self.filtered_df.groupby(self.region_or_country)["New_cases"].agg(['mean','median','min','max', 'count','std']).reset_index()
        summary_cases.columns = [self.region_or_country, 'Mean', 'Median','Min', 'Max', 'Count','Std']
        return summary_cases.round(2)

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
        elif unique_entries > 15: # NEED TO FIX
            fig, ax = plt.subplots(1, 1, figsize=(19, 6))
            ax.hist(self.filtered_df["New_cases"], colour= 'skyblue')
    #NEWLY ADDED
    def daily_cases_lineplot(self, freq: str = "W"):
        freq_map = {"D": "Daily", "W": "Weekly", "M": "Monthly"}
        if freq not in freq_map:
            st.error("freq must be 'D', 'W', or 'M'")
            return

        df = self.filtered_df.copy()
        df["Date_reported"] = pd.to_datetime(df["Date_reported"])
        df.sort_values("Date_reported", inplace=True)

        # -------- resample helper --------
        def _agg(series):
            if freq == "D":
                return series  # no resample
            return series.resample(freq).sum()

        fig, ax = plt.subplots(figsize=(8, 4))
        locations = df[self.region_or_country].unique()

        if len(locations) > 15:
            series = (
                df.set_index("Date_reported")["New_cases"]
                .pipe(_agg)
                .reset_index(drop=False)
            )
            ax.plot(series["Date_reported"], series["New_cases"], linewidth=2)
            title_tail = "(all selected)"
        else:
            for loc in locations:
                loc_df = df[df[self.region_or_country] == loc]
                series = (
                    loc_df.set_index("Date_reported")["New_cases"]
                    .pipe(_agg)
                    .reset_index(drop=False)
                )
                ax.plot(series["Date_reported"], series["New_cases"],
                        linewidth=2, label=loc)
            title_tail = f"by {self.region_or_country}"
            ax.legend(fontsize=8, title=self.region_or_country)

        ax.set_title(f"{freq_map[freq]} Cases {title_tail}")
        ax.set_xlabel(freq_map[freq][:-2])  # Day / Week / Month
        ax.set_ylabel("Cases")
        ax.tick_params(axis="x", rotation=45)
        st.pyplot(fig, use_container_width=True)


        
