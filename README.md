# 🦠 Covid-19 Dashboard 

An interactive dashboard providing insights to the global COVID-19 pandemic, developed for the *Programming for Data Science* course at the Univeristy of Bern. 

## 🌍 Project Overview 
The current project is going on in one of the branches that is called lysandersbranch. It will be made main as soon as possible.
This project aims to create a reporting tool for the Covid-19 outbreak that allows users to explore cases and deaths across countries/regions at specific time spans using data from the [WHO’s Global Health Observatory](https://www.who.int/data/gho).
## 🛠️ Installation Guide - WINDOWS Commands

**Important note**
The file sizes are now too big because of the cache's etc. it will be resolved as soon as possible. After the file has been downloaded and used, it can be deleted. 

```bash
mkdir foldernewlycreated
cd foldernewlycreated
```
You can directly download the code from GitHub as well, if you want to copy the repository you may use the code below, but it requires git to be installed in the PC
```bash
git clone --branch lysanders-branch https://github.com/AdvPythonFS25/Covid-19-Dashboard-Project.git
cd Covid-19-Dashboard-Project
```
If the GitHub repository already has a venv folder, delete it:
```bash
rmdir /s /q venv
```
```bash
python -m venv venv
```
```bash
venv\Scripts\activate
```
```bash
pip install streamlit pandas numpy matplotlib seaborn requests
```
```bash
streamlit run src/streamlitApp.py
```
To run the dashboard, download the file and run in terminal: (2nd way UNDER DEVELOPMENT MAY NOT WORK):

Requirement : DOCKER Installed, no other things are necessary, streamlit, python etc. docker image does the job for you :)

```bash
mkdir foldernewlycreated
cd foldernewlycreated
```
You can directly download the code from GitHub as well, if you want to copy the repository you may use the code below, but it requires git to be installed in the PC
```bash
git clone --branch lysanders-branch https://github.com/AdvPythonFS25/Covid-19-Dashboard-Project.git
cd Covid-19-Dashboard-Project
```

```bash
cd Covid-19-Dashboard-Project
```

```bash
docker run -p 8501:8501 covid-dashboard-lani
```
## 🛠️ Installation Guide - MAC Commands

## 2 WAYS

To run the dashboard, download the file and run in terminal: (1st way) 

```bash
mkdir foldernewlycreated
cd foldernewlycreated
```
You can directly download the code from GitHub as well, if you want to copy the repository you may use the code below, but it requires git to be installed in the PC

```bash
git clone --branch lysanders-branch https://github.com/AdvPythonFS25/Covid-19-Dashboard-Project.git
cd Covid-19-Dashboard-Project
```
If the Github repository already has the venv we need to delete it.
```bash
rm -rf venv
```

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

```bash
pip install streamlit pandas numpy matplotlib seaborn requests
```

```bash
streamlit run /src/streamlitApp.py
```

To run the dashboard, download the file and run in terminal: (2nd way UNDER DEVELOPMENT MAY NOT WORK):

Requirement : DOCKER Installed, no other things are necessary, streamlit, python etc. docker image does the job for you :)

```bash
mkdir foldernewlycreated
```

```bash
cd ~/Desktop/foldernewlycreated
```
You can directly download the code from GitHub as well, if you want to copy the repository you may use the code below, but it requires git to be installed in the PC
```bash
git clone --branch lysanders-branch https://github.com/AdvPythonFS25/Covid-19-Dashboard-Project.git
```

```bash
cd Covid-19-Dashboard-Project
```

```bash
docker run -p 8501:8501 covid-dashboard-lani
```


**Dependencies/packages used**
- python
- streamlit
- pandas
- numpy
- seaborn

## Features 
📊 **Statistics calculations and visualisations**  


## DELIVARABLE 3, AND PROCESS OVER THE TIME:
**PROCESS (PHASE 1 & 2)**
Phase 1 - 2
Process of creating the project :

At first, we focused on identifying which statistics we could calculate, since we had seven different databases to work with and limited time.
Therefore, we gradually built some functions to process the data, along with general utility functions to simplify our work—such as data filters and validation helpers. We then built the rest of our code on top of this foundation. At that time, these were the core functions we developed:


	1.	DataBaseValidator
	2.	entryCounter
	3.	numberAuthorizationProduct
	4.	CountryValidator
	5.	WHO_regionValidator
	6.	ISO3Validator
	7.	Country_codeValidator
	8.	Product_validator
	9.	deathRateCountry
	10.	averageDeathRate
	11.	deathRateRegion
	12.	averageDeathRateRegion
	13.	DeathRateRequest
	…
 
In the early stages of the second deliverable, we focused on building out the core functionality of the code as much as possible—especially by creating generalized graph functions and similar utilities. This work was mainly completed during the first half of Deliverable 2.

Later, we decided to use Streamlit for better visualizations and shifted our focus to integrating Streamlit during the second half of the deliverable. By the deadline, we ended up with two versions of the code: one that was about 80% complete in a single Python file, and another that was around 30% implemented using Streamlit.

At the end of that phase, the following were the potential next steps we could take with the old code (note: for some functions, the visualizations were unfinished, but most of the other parts were completed):


When that phase ended possible things to do with our old code were these(for some functions graphics wasn’t finished but the others were mostly finished ); 

Example Usage
```bash
——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
Select statistic to compute: example usage ISO3: TUR,USA,FRA   Country code : TR,US,FR    Who region : AMR,EUR    Income group: LIC,UMC
  1  – Death Rate (CFR) (country code)
  2  – Rt (Effective Reproduction Number)
  3  – Average Daily Cases (country code)
  4  – Average Daily Deaths (country code)
  5  – Regional Death Rate (country code)
  6  – Vaccination Coverage  (ISO3)
  7  – Booster Dose Rate     (ISO3)
  8  – Total Vaccination Summary (ISO3)
  9  – # Vaccine Authorisations by ISO3
 10  – # Vaccine Authorisations by Product
 11  – Average Weekly Hospitalisations (ISO3)
 12  – Average Monthly Hospitalisations (ISO3)
 13  – Daily Time-Series (country code)
 14  – Monthly Deaths by Age Group (countries)
 15  – Monthly Deaths by Age Group (income groups)
 16  – Monthly Deaths by Age Group (WHO regions)
Enter the number of your choice: 3

Choose identifier type:
 1 – ISO3 code
 2 – Country code
 3 – WHO region
 4 – Vaccine product name
 5 – World-Bank income group
Enter input type number: 2

Enter values (comma-separated): TR,US,FR

Start date (YYYY-MM-DD): 2021-01-01
End date   (YYYY-MM-DD): 2022-02-02

─────────────────────────────────────────────────────────────
 Statistic   : Average Daily Cases
 IDs type    : Country code (2-letter)
 IDs         : TR, US, FR
 Date range  : 2021-01-01 – 2022-02-02 (auto-fixed if invalid)
─────────────────────────────────────────────────────────────
─────────────────────────────────────────────────────────────
 Date range apllied by the system : 2021-01-01 00:00:00 – 2022-02-02 00:00:00
─────────────────────────────────────────────────────────────
2021-01-01 00:00:00 2022-02-02 00:00:00

Statistical result:
Country_code
FR     40067.68
TR     23940.23
US    138533.17
Name: Average, dtype: float64
￼
——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
```


-photo from old graphs-

**Phase 2 Deliverable**

The Streamlit implementation was unfinished at the time because two versions of the code were being developed simultaneously, as mentioned previously.

In that phase, we attempted to do the following (taken and paraphrased from the second deliverable’s changes):
	•	We changed the architecture of our code to integrate the use of the Streamlit UI.
	•	We updated our functions for death rate and Rt to reflect the new structure and added visualizations (both Streamlit and the original Python code).
	•	Pylint formatting changes were implemented for the earlier Python code; these changes can be found under formatter.md.
	•	Abstraction and decomposition: From the beginning of the project, we aimed to design our code with abstraction and decomposition in mind. Additionally, by using the Streamlit UI, users can simply run the app without needing to interact with the source code. Decomposition was achieved by modularizing our code—each statistic calculation, data processing step, and plotting logic has its own function.


**Phase 3 Deliverable**

Afterward, we attempted to import our code into Streamlit using a different approach, but it was inconsistent and not well-structured. Therefore, in Phase 3, we redefined our structure with the following updates:
	•	We separated all statistics into different classes, with each database having its own class. Public and private functions are named accordingly; if a function name starts with an underscore _, it is intended to be used only within that class.
	•	DataFrames are filtered using a class defined in a file called country_region_wrapper. This modular approach allows for easy extension, as proper filtering is crucial for topics like these.
	•	All plots and data outputs are shown on the main page. To support this, we created a reusable layout file shared across the different classes.
	•	Unit testing is currently unfinished.

Below is our current UI when the app is running. The code can be run using Docker. We chose Docker to manage containers and dependencies, as this project is still in the development stage. Docker makes it easy to test and explore the project. If desired, the Dockerization setup using Poetry is also provided below.

-photo-

|Sidebar element / Section | What it means & how it works in our dashboard|
| :------ | :---- |
Pick Start Date / Pick End Date | Lets the user trim **all** datasets to a custom period. Every metric we calculate—from daily cases to vaccinations—reads the start/end dates you choose here.
Select Country or WHO Region  • Choose at least one region  • Choose at least one country | Geographic filter. • If you pick **one or more WHO regions** we ignore the country picker. • If you pick **one or more countries** we ignore the region picker. All subsequent statistics are grouped by the field that remains active (**Country** or **WHO_region**).
Granularity (Daily / Weekly / Monthly) | Global time-resolution selector for line-charts that support resampling. Hospital-related metrics ignore **Daily** and always resample to **Last 7 days** or **Last 28 days** using their own radio.
Daily Cases | Shows: • mean / median daily cases table • distribution plots • time-series resampled to the granularity radio.
Death Rate | Case-fatality rate (CFR) — computed each day as *(Cumulative deaths / Cumulative cases) × 100* and then averaged over the selected period.
Daily Deaths | Same layout as *Daily Cases* but for new deaths.
Rt Number | Instant reproduction number (new cases ÷ previous-day cases) averaged for each country/region, with distribution and time-series.
New Hospitalizations | Tick-box reveals its own **Last 7 days / Last 28 days** radio. The chosen window decides which column (*…_last_7days* or *…_last_28days*) is analysed. Daily granularity is not offered here.
New ICU Admissions | Same behaviour as *New Hospitalizations* but uses ICU columns.
Total Doses | Vaccination snapshot – table & bar-chart of *TOTAL_VACCINATIONS* summed over the period.
% ≥ 1 Dose | Percentage of population with at least one dose (*PERSONS_VACCINATED_1PLUS_DOSE_PER100*).
Booster Coverage % | Booster-dose coverage (*PERSONS_BOOSTER_ADD_DOSE_PER100*).
Deaths by Age and Income | Tick-box adds two multiselects: **Age group** & **WB income level**. Metric then shows deaths aggregated by the age/income slices plus your country/region/date filters.
Choose window (inside Hospital/ICU sections) | Quick look-back switch: **7-day** versus **28-day** totals. Updates the plots instantly.

## 👨‍💻 Contributors 
- Ankitha Kumble
- Lysander Tucker
- Nihat Ömer Karaca
- İlbars Efe Korkmaz

# Links 
- Project Overview: [Link Text](#Project-Overview/)
- Features: [Link Text](#Features)
- Installation guide: [Link Text](#Installation-Guide).

![Covid meme](https://www.graphicdesignforum.com/uploads/default/original/2X/b/bfda98588e18bedca5818e31c486b76349a3a926.jpeg)

