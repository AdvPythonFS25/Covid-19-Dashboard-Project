import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st
import numpy as np


def plot_distribution(df, value_column, group_column, title_prefix):



    if not group_column:
         st.error('No Country and region selected')
         
    unique_entries = df[group_column].nunique()

    if unique_entries <= 15:
        log_value_column = f"log_{value_column}"
        df[log_value_column] = np.log1p(df[value_column])

        # Boxplot/ violin plot Graph
        fig, ax = plt.subplots(2, 1, figsize=(12, 12))
        sns.boxenplot(df, 
                    x=group_column, y=log_value_column, 
                    hue=group_column, 
                    ax=ax[0],
 #                   showfliers=False,
 #                   log_scale=True,
                    palette=sns.color_palette("coolwarm", n_colors=8)) 
        
        ax[0].set_title(f"{title_prefix} Boxplot", fontsize=30)
        ax[0].set_xlabel(None)
        ax[0].set_ylabel(value_column, fontsize=20)
        ax[0].set_xticklabels(ax[0].get_xticklabels(), rotation=85, fontsize=20)
        ax[0].set_yticklabels(ax[0].get_yticklabels(), fontsize=20)
        
        # Log of all selected areas histogram
        ax[1].hist(df[value_column], log=True)
        ax[1].set_title(f"Histogram of {title_prefix}", fontsize=30)
        ax[1].set_xlabel(f"Log {value_column}", fontsize=20)
        ax[1].set_ylabel(None)
        ax[1].set_xticklabels(ax[1].get_xticklabels(), fontsize=20)
        ax[1].set_yticklabels(ax[1].get_yticklabels(), fontsize=20)

        fig.subplots_adjust(hspace=1.5)
        return st.pyplot(fig)

    else:
        # only histogram
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.hist(df[value_column], log=True)
        ax.set_title(f"Histogram of {title_prefix}", fontsize=30)
        ax.set_xlabel(f'Log {value_column}', fontsize=20)
        ax.set_ylabel(None)
        ax.set_xticklabels(ax.get_xticklabels(), fontsize=20)
        ax.set_yticklabels(ax.get_yticklabels(), fontsize=20)

        return st.pyplot(fig)
    
def plot_streamlit_time_series_weekly(df, region_or_country, date_col, value_col, y_label):
    if region_or_country == "Country":
        grouped_df = df.groupby([region_or_country, pd.Grouper(key=date_col, freq='W')])[value_col].mean().reset_index()

        st.text("Timeseries by Country")
        return st.line_chart(grouped_df, 
                             y_label=y_label,
                             x_label='Date Reported',
                             color=region_or_country,
                             x=date_col, 
                             y=value_col)

    elif region_or_country == "WHO_region":
        st.text("Timeseries by WHO Region")

        # Group by Who_region and date
        grouped_df = df.groupby([region_or_country, pd.Grouper(key=date_col, freq='W')])[value_col].sum().reset_index()
        return st.line_chart(grouped_df, 
                             y_label=y_label,
                             x_label='Date Reported',
                             color=region_or_country,
                             x=date_col, 
                             y=value_col)
    
def plot_streamlit_time_series_monthly(df, region_or_country, date_col, value_col, y_label):
    if df is None or df.empty:
        return
    grouped_df = (df.groupby([region_or_country,pd.Grouper(key=date_col, freq='M')])[value_col].sum().reset_index())
    st.text("Timeseries by " + ("Country" if region_or_country == "Country" else "WHO Region"))
    return st.line_chart(
        grouped_df,
        y_label=y_label,
        x_label='Date Reported',
        color=region_or_country,
        x=date_col,
        y=value_col,)

def plot_streamlit_barchart(df,region_or_country, value_col, y_label):
    if df is None or df.empty:
        return
    grouped_df = (df.groupby([region_or_country])[value_col].sum().reset_index())
    st.text("Barchart by " + ("Country" if region_or_country == "Country" else "WHO Region"))
    return st.bar_chart(
        grouped_df,
        y_label=y_label,
        x_label="Country/Region",
        x=region_or_country,
        y=value_col,)

def hist_plot(df, value_column, title_prefix):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.hist(df[value_column], log=True)
        ax.set_title(f"Histogram of {title_prefix}", fontsize=30)
        ax.set_xlabel(f'Log {value_column}', fontsize=20)
        ax.set_ylabel(None)
        ax.set_xticklabels(ax.get_xticklabels(), fontsize=20)
        ax.set_yticklabels(ax.get_yticklabels(), fontsize=20)

        return st.pyplot(fig)

#One line table showing the chosen column
def basic_table(df, geo_col, value_col, title):
    tbl = (df[[geo_col, value_col]]
           .sort_values(value_col, ascending=False)
           .reset_index(drop=True)
           .rename(columns={geo_col: geo_col.title(),
                            value_col: title}))
    st.dataframe(tbl)