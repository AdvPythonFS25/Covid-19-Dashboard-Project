import pandas as pd 
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

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

        summary_deaths = self.filtered_df.groupby(self.region_or_country)["New_deaths"].agg(['mean','median','min','max', 'count','std']).reset_index()
        summary_deaths.columns = [self.region_or_country, 'Mean', 'Median','Min', 'Max', 'Count','Std']
        return summary_deaths.round(2)
    

    def daily_deaths_histogram(self): # locations are either regions or countries

        unique_entries = self.filtered_df[self.region_or_country].nunique()

        if unique_entries == 1:
            fig, ax = plt.subplots(1, 1, figsize=(19, 6))
            ax.hist(self.filtered_df["New_deaths"], colour= 'skyblue')

            return st.pyplot(fig)
        elif unique_entries > 1 and unique_entries <= 15:

            fig, ax = plt.subplots(1, 1, figsize=(19, 6))

            # make hist for every selected entry
            for location in unique_entries:
                location_df = self.filtered_df[self.filteed_df[self.region_or_country] == location]
                ax.hist(location_df["New_deaths"], 
                        bins=30, alpha=0.5, label=location, stacked=True, edgecolor='black')
                
            return st.pyplot(fig) 
        elif unique_entries > 15: # NEED TO FIX
            fig, ax = plt.subplots(1, 1, figsize=(19, 6))
            ax.hist(self.filtered_df["New_deaths"], colour= 'skyblue')
    def daily_deaths_barchart(self):
        """
        Weekly-aggregated bars.
        • 1–15 locations → one colour per location
        • >15 locations  → everything merged
        """
        df = self.filtered_df.copy()
        df["Date_reported"] = pd.to_datetime(df["Date_reported"])
        df = df.sort_values("Date_reported")

        fig, ax = plt.subplots(figsize=(8, 4))

        locations = df[self.region_or_country].unique()

        if len(locations) > 15:           # too many → aggregate
            week_df = (
                df.set_index("Date_reported")
                  .resample("W")["New_deaths"]
                  .sum()
                  .reset_index()
            )
            ax.bar(week_df["Date_reported"], week_df["New_deaths"],
                   color='salmon', edgecolor='black')
            ax.set_title("Weekly Deaths (all selected)")
        else:                             # separate bar series
            for loc in locations:
                loc_df = df[df[self.region_or_country] == loc]
                week_df = (
                    loc_df.set_index("Date_reported")
                          .resample("W")["New_deaths"]
                          .sum()
                          .reset_index()
                )
                ax.bar(week_df["Date_reported"], week_df["New_deaths"],
                       alpha=0.7, label=loc, edgecolor='black')
            ax.set_title(f"Weekly Deaths by {self.region_or_country}")
            ax.legend(fontsize=8, title=self.region_or_country)

        ax.set_xlabel("Week")
        ax.set_ylabel("Deaths")
        ax.tick_params(axis='x', rotation=45)
        st.pyplot(fig, use_container_width=True)


    def daily_deaths_lineplot(self,freq: str = "W"):
        """
        Weekly-aggregated line plot.
        Same logic as above.
        """
        freq_map = {"D": "Daily", "W": "Weekly", "M": "Monthly"}
        if freq not in freq_map:
            st.error("freq must be 'D', 'W', or 'M'")
            return

        df = self.filtered_df.copy()
        df["Date_reported"] = pd.to_datetime(df["Date_reported"])
        df.sort_values("Date_reported", inplace=True)

        def _agg(series):
            if freq == "D":
                return series  # no resample
            return series.resample(freq).sum()

        fig, ax = plt.subplots(figsize=(8, 4))
        locations = df[self.region_or_country].unique()

        if len(locations) > 15:
            series = (
                df.set_index("Date_reported")["New_deaths"]
                .pipe(_agg)
                .reset_index(drop=False)
            )
            ax.plot(series["Date_reported"], series["New_deaths"], linewidth=2)
            title_tail = "(all selected)"
        else:
            for loc in locations:
                loc_df = df[df[self.region_or_country] == loc]
                series = (
                    loc_df.set_index("Date_reported")["New_deaths"]
                    .pipe(_agg)
                    .reset_index(drop=False)
                )
                ax.plot(series["Date_reported"], series["New_deaths"],
                        linewidth=2, label=loc)
            title_tail = f"by {self.region_or_country}"
            ax.legend(fontsize=8, title=self.region_or_country)

        ax.set_title(f"{freq_map[freq]} Deaths {title_tail}")
        ax.set_xlabel(freq_map[freq][:-2])  # Day / Week / Month
        ax.set_ylabel("Deaths")
        ax.tick_params(axis="x", rotation=45)
        st.pyplot(fig, use_container_width=True)


        
