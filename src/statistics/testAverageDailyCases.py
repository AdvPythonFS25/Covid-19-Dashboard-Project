import pandas as pd
import numpy as np
from averageDailyCases import *

df = pd.read_csv('./data/WHO-COVID-19-global-daily-data.csv')
start_date='19/08/2021'
end_date='23/07/2023'
cases = AverageDailyCases(df=df,start_date=start_date, end_date=end_date)
print (cases.country_avg_daily_cases(['Yemen','Zimbabwe','Andorra']))

