# importData.py  – identical class, plus a tiny registry section

import os
import pandas as pd
import requests

class DataImporterGithub:
    """
    Downloads a single CSV from `url` into `data_dir/filename`
    if not already present, then returns it as a DataFrame.
    """
    def __init__(self, url, filename, data_dir='./data'):
        self.url = url
        self.filename = filename
        self.data_dir = data_dir
        self.filepath = os.path.join(self.data_dir, self.filename)

    def check_for_data_github(self):
        return os.path.exists(self.filepath)

    def download_data_github(self):
        if not self.check_for_data_github():
            print(f'Downloading {self.filename} …')
            self._ensure_dir_github()
            data = requests.get(self.url)
            with open(self.filepath, 'wb') as f:
                f.write(data.content)

    def _ensure_dir_github(self):
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir, exist_ok=True)

    def load_data_github(self):
        self.download_data_github()
        return pd.read_csv(self.filepath)


SOURCES = {
    "global_daily": (
        "https://raw.githubusercontent.com/omerkaraca-fire/data/main/WHO-COVID-19-global-daily-data.csv",
        "WHO-COVID-19-global-daily-data.csv"
    ),
    "global_data": (
        "https://raw.githubusercontent.com/omerkaraca-fire/data/main/WHO-COVID-19-global-data.csv",
        "WHO-COVID-19-global-data.csv"
    ),
    "global_hosp": (
        "https://raw.githubusercontent.com/omerkaraca-fire/data/main/WHO-COVID-19-global-hosp-icu-data.csv",
        "WHO-COVID-19-global-hosp-icu-data.csv"
    ),
    "global_monthly_death": (
        "https://raw.githubusercontent.com/omerkaraca-fire/data/main/WHO-COVID-19-global-monthly-death-by-age-data.csv",
        "WHO-COVID-19-global-monthly-death-by-age-data.csv"
    ),
    "global_table": (
        "https://raw.githubusercontent.com/omerkaraca-fire/data/main/WHO-COVID-19-global-table-data.csv",
        "WHO-COVID-19-global-table-data.csv"
    ),
    "vaccination_data": (
        "https://raw.githubusercontent.com/omerkaraca-fire/data/main/vaccination-data.csv",
        "vaccination-data.csv"
    ),
    "vaccination_meta": (
        "https://raw.githubusercontent.com/omerkaraca-fire/data/main/vaccination-metadata.csv",
        "vaccination-metadata.csv"
    ),
}

# helper so the rest of your code can do:
#   from importData import get_data
#   df_daily = get_data("global_daily")
_importers = {
    key: DataImporterGithub(url, filename)
    for key, (url, filename) in SOURCES.items()
}

def get_data_github(name):
    """
    name must be one of: global_daily, global_hosp,
    vaccination_data, vaccination_meta
    """
    return _importers[name].load_data_github()