import os
from statistics.rtStatistics import *
from statistics.deathRate import *


#GlobalDailyDF = pd.read_csv('./CovidProject/data/WHO-COVID-19-global-daily-data.csv')

# country_names = []
# who_regions = ['EUR']

# start_date = '2020-05-06'
# end_date = '2024-04-06'

# #rt_country(GlobalDailyDF, country_names=['Albania'], start_date=start_date, end_date=end_date)
# avg_reg = rt_region(GlobalDailyDF, who_regions=['EUR'], start_date=start_date, end_date=end_date)
# #print(avg_reg)
# country_names = ['France']

# dr = death_rate(df=GlobalDailyDF, country_names=country_names, 
#                 who_regions=who_regions, 
#                 start_date=start_date, 
#                 end_date=end_date)
# #print(dr[0])

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
print(ROOT_DIR)