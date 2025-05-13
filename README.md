# 🦠 Covid-19 Dashboard 

An interactive dashboard providing insights to the global COVID-19 pandemic, developed for the *Programming for Data Science* course at the Univeristy of Bern. 

## 🌍 Project Overview 

This project aims to create a reporting tool for the Covid-19 outbreak that allows users to explore cases and deaths across countries/regions at specific time spans using data from the [WHO’s Global Health Observatory](https://www.who.int/data/gho).
## 🛠️ Installation Guide - WINDOWS Commands

```bash
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

