import pandas as pd 
import numpy as np

class AverageDailyCases:

    def __init__(self, filtered_df): # built for daily DF filtered by date and region
        self.filtered_df = filtered_df.copy()

    def avg_daily_cases(self):
        self.df.fillna(0, inplace=True)
        avg_cases = self.df.groupby("Country")["New_cases"].mean()
        avg_cases = avg_cases.rename("Average")
        return avg_cases.round(2)

    def avg_daily_cases_plot(self):
        
        
