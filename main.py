from src import streamlitApp
import os
from src import *

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)

def main():

    start_date, end_date = sidebar_date_selector()
    country_names, who_regions = sidebar_location_selector()
    rt_number_sidebar_button()
    death_rate_sidebar_button()

if __name__ == "__main__":
    main()