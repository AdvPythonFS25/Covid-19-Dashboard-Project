# this should be a code that downloads data from online if its not already present
import os
import pandas as pd 
import requests
import socket

class DataImporter:
    """
    This class dowloads files from URL to the data directory 
    if not already present.
    """
    def __init__(self, url, filename, data_dir):
        self.url = url
        self.filename = filename
        self.data_dir = data_dir
        # make path to that file with data directory
        self.filepath = os.path.join(self.data_dir, self.filename)


    def check_for_data(self):
        return os.path.exists(self.filepath)
    
    def check_internet_connection(self):
        try:
            socket.setdefaulttimeout(3)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
            return True
        except socket.error:
            return False
        
    def download_data(self):
        if not self.check_internet_connection() and not self.check_for_data():
          print('You are not connected to the interweb.\
                 Please connect once to have the data downloaded.')  
        elif not self.check_for_data():
            print('Data is not present. Downloading to data directory.')
            data = requests.get(self.url)
            with open (self.filepath, 'wb') as file: # must use write binary or gets a weird error
                file.write(data.content)
        else:
            print('Data is already present. Not dowloading.')  

    def load_data(self):
        self.download_data()
        return pd.read_csv(self.filepath) 
    
    def set_date_time(self, df):
        """Fixes the datetime columns in the dataframe."""
        # Convert 'Date_reported' column to datetime
        df['Date_reported'] = pd.to_datetime(df['Date_reported'], errors='coerce')
        return df
    
    def fix_monthly_death(self, df):
        df["Date_reported"] = pd.to_datetime(
            dict(year=df["Year"], month=df["Month"], day=1))
        return df

URL = 'https://srhdpeuwpubsa.blob.core.windows.net/whdh/COVID/WHO-COVID-19-global-daily-data.csv'
FILENAME = "WHO-COVID-19-global-daily-data.csv"
data_dir = './data'
cwd = os.getcwd()
print(cwd)

global_daily_data_object = DataImporter(url=URL, filename=FILENAME, data_dir=data_dir)
df = global_daily_data_object.load_data()
