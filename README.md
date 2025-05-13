# 🦠 Covid-19 Dashboard 

An interactive dashboard providing insights to the global COVID-19 pandemic, developed for the *Programming for Data Science* course at the Univeristy of Bern. 

## 🌍 Project Overview 

This project aims to create a reporting tool for the Covid-19 outbreak that allows users to explore cases and deaths across countries/regions at specific time spans using data from the [WHO’s Global Health Observatory](https://www.who.int/data/gho).

## 🛠️ Installation Guide 


To run the dashboard, download the file and run in terminal: (1st way) 

Requirement : DOCKER Installed, no other things are necessary, streamlit, python etc. docker image does the job for you :)
```bash
cd Covid-19-Dashboard-Project 
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
- seabord

## Features 
📊 **Basic statistics and visualisations**  

| Statistic | Description |
| :------ | :---- |
| Death Rate (CFR) | (Cumulative deaths / Cumulative cases) * 100|
| Rt (Reproduction Number)| Indicator of how contagious a disease is. Average number of new cases that arise from an infected individual at a given time|
| Daily Cases | Number of daily cases |
| Daily Deaths | Number of daily deaths |
| Vaccination Coverage | Number of people vaccinated |
| Booster Dose Rate | Number of people successful administered with booster dose |
| Vaccine Authorisations | Type of vaccines authourised by country |
| Hospitalisations | Number of weekly or monthly hospitalisations |
| Monthly Deaths by Age Group (countries, region, income) | to be added |

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

