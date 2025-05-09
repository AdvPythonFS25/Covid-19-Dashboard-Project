# this should be a code that downloads data from online if its not already present
import os
import pandas as pd 
import requests

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

    def download_data(self):
        if not self.check_for_data():
            print('Data is not present. Downloading to data directory.')
            data = requests.get(self.url)
            with open (self.filepath, 'wb') as file: # must use write binary or gets a weird error
                file.write(data.content)
        else:
            print('Data is already present. Not dowloading.')  

    def load_data(self):
        self.download_data()
        return pd.read_csv(self.filepath) 


URL = 'https://srhdpeuwpubsa.blob.core.windows.net/whdh/COVID/WHO-COVID-19-global-daily-data.csv'
FILENAME = "WHO-COVID-19-global-daily-data.csv"

cwd = os.getcwd()
print(cwd)

#global_daily_data_object = DataImporter(url=URL, filename=FILENAME)
#df = global_daily_data_object.load_data()
