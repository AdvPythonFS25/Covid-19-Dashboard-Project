import streamlit as st

def layout(title, table, distribution_plots, timeseries_plot):
        # Layout
    st.subheader(title)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.dataframe(table)
    
    with col2:
        distribution_plots()
        
    timeseries_plot()
def layout_without_distribution(title, table, timeseries_plot):
        # Layout
    st.subheader(title)

    col1, col2 = st.columns(2)


    st.dataframe(table)
    timeseries_plot()

def summary_stat_checkbox(title, selected_column, summary_stat, key = None):

    if not st.sidebar.checkbox(title, key = key or title):
        return  # exit if the button is not clicked
    if not selected_column:  # dont use 'is none'
        return  # exit if no country or who region is selected
    
    summary_stat()

