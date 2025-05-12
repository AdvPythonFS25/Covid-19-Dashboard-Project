import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

class HospitalizationStats :
    _COL_WEEK  = "New_hospitalizations_last_7days"
    _COL_MONTH = "New_hospitalizations_last_28days"
    def __init__(self, filtered_df: pd.DataFrame, region_or_country: str):
        self.df = filtered_df.copy()
        self.key = region_or_country  # "Country" or "WHO_region"
        self.df["Date_reported"] = pd.to_datetime(self.df["Date_reported"])

    def avg_hosp(self, freq: str = "W") -> pd.DataFrame:
        if freq not in ("D", "W", "M"):
            st.error("freq must be 'D', 'W' or 'M'")
            return pd.DataFrame()

        if freq == "W":
            col = self._COL_WEEK
            tbl = (
                self.df.groupby(self.key)[col]
                .mean()
                .round(2)
                .rename("Mean_weekly_hosp")
                .reset_index()
            )
        elif freq == "M":
            col = self._COL_MONTH
            tbl = (
                self.df.groupby(self.key)[col]
                .mean()
                .round(2)
                .rename("Mean_monthly_hosp")
                .reset_index()
            )
        else:  # Daily: derive per-day admissions first
            df = self.df.copy()
            df["Daily_from_week"] = df[self._COL_WEEK] / 7
            df["Daily_from_month"] = df[self._COL_MONTH] / 28
            # choose whichever period is available on each row
            df["Daily_hosp"] = df[["Daily_from_week", "Daily_from_month"]].bfill(axis=1).iloc[:, 0]

            tbl = (
                df.groupby(self.key)["Daily_hosp"]
                .mean()
                .round(2)
                .rename("Mean_daily_hosp")
                .reset_index()
            )
        return tbl

    def daily_hospitalization_lineplot(self, freq: str = "W"):
        """
        Draws the rolling-sum curve (weekly or monthly).  Daily curves are not
        available in the source data, so 'D' falls back to weekly.
        """
        if freq not in ("W", "M", "D"):
            st.error("freq must be 'D', 'W' or 'M'")
            return

        freq = "W" if freq == "D" else freq  # fallback

        col = self._COL_WEEK if freq == "W" else self._COL_MONTH
        label = "Weekly (7-day sum)" if freq == "W" else "Monthly (28-day sum)"

        fig, ax = plt.subplots(figsize=(8, 4))
        many = self.df[self.key].nunique() > 15

        for loc, g in self.df.groupby(self.key):
            ax.plot(g["Date_reported"], g[col],
                    linewidth=1.5 if many else 2.0,
                    label=None if many else loc)

        ax.set(
            title=f"Hospitalisations – {label}",
            xlabel="Date", ylabel="Admissions"
        )
        if not many:
            ax.legend(fontsize=8, title=self.key)
        ax.tick_params(axis="x", rotation=45)
        st.pyplot(fig, use_container_width=True)