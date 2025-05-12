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

def layout2(title, table, distribution_plots, timeseries_plot):
        # Layout
    st.subheader(title)
    
    st.dataframe(
        data=table,
        column_config={
            "graphs": st.column_config.Column(distribution_plots)
            
        }, 
        hide_index=True)
    
    timeseries_plot()

def summary_stat_checkbox(title, selected_column, summary_stat):
    if not st.sidebar.checkbox(title):
        return  # exit if the button is not clicked
    if not selected_column:  # dont use 'is none'
        return  # exit if no country or who region is selected
    
    summary_stat()

