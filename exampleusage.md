EXAMPLE USAGE


Select statistic to compute:
  1  – Death Rate (CFR)
  2  – Rt (Effective Reproduction Number)
  3  – Average Daily Cases
  4  – Average Daily Deaths
  5  – Regional Death Rate
  6  – Vaccination Coverage  (ISO3)
  7  – Booster Dose Rate     (ISO3)
  8  – Total Vaccination Summary (ISO3)
  9  – # Vaccine Authorisations by ISO3
 10  – # Vaccine Authorisations by Product
 11  – Average Weekly Hospitalisations (ISO3)
 12  – Average Monthly Hospitalisations (ISO3)
 13  – Daily Time-Series
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

Start date (YYYY-MM-DD): 2022-01-01
End date   (YYYY-MM-DD): 2022-04-30

─────────────────────────────────────────────────────────────
 Statistic   : Average Daily Cases
 IDs type    : Country code (2-letter)
 IDs         : TR, US, FR
 Date range  : 2022-01-01 – 2022-04-30 (auto-fixed if invalid)
─────────────────────────────────────────────────────────────

Statistical result:
Country_code
FR    155467.97
TR     46571.31
US    225092.51
Name: Average, dtype: float64





Select statistic to compute:
  1  – Death Rate (CFR)
  2  – Rt (Effective Reproduction Number)
  3  – Average Daily Cases
  4  – Average Daily Deaths
  5  – Regional Death Rate
  6  – Vaccination Coverage  (ISO3)
  7  – Booster Dose Rate     (ISO3)
  8  – Total Vaccination Summary (ISO3)
  9  – # Vaccine Authorisations by ISO3
 10  – # Vaccine Authorisations by Product
 11  – Average Weekly Hospitalisations (ISO3)
 12  – Average Monthly Hospitalisations (ISO3)
 13  – Daily Time-Series
 14  – Monthly Deaths by Age Group (countries)
 15  – Monthly Deaths by Age Group (income groups)
 16  – Monthly Deaths by Age Group (WHO regions)
Enter the number of your choice: 13

Choose identifier type:
 1 – ISO3 code
 2 – Country code
 3 – WHO region
 4 – Vaccine product name
 5 – World-Bank income group
Enter input type number: 2

Enter values (comma-separated): TR,US

Start date (YYYY-MM-DD): 2022-01-01
End date   (YYYY-MM-DD): 2023-01-01

Which column? e.g. New_cases, New_deaths, Cumulative_cases, Cumulative_deaths → New_deaths

─────────────────────────────────────────────────────────────
 Statistic   : Daily Time-Series
 IDs type    : Country code (2-letter)
 IDs         : TR, US
 Date range  : 2022-01-01 – 2023-01-01 (auto-fixed if invalid)
 Column      : New_deaths
─────────────────────────────────────────────────────────────
If there is nan data it is replaced with overall average for that country.

Statistical result:
Country_code           TR           US
Date_reported                         
2022-01-01     139.000000  1334.000000
2022-01-02     163.000000  1344.000000
2022-01-03     145.000000   430.000000
2022-01-04     129.000000   374.000000
2022-01-05     160.000000  1672.000000
...                   ...          ...
2022-12-28     111.647399   866.450658
2022-12-29     111.647399   866.450658
2022-12-30     111.647399  2480.000000
2022-12-31     111.647399   866.450658
2023-01-01     111.647399   866.450658

[366 rows x 2 columns]

Type of result: <class 'pandas.core.frame.DataFrame'>

Would you like to visualize this data as a bar graph? (y/n): y

#GRAPH IS NOT PASTED IN HERE IT CAN BE SEEN IN WHEN THE CODE IS RUN



Select statistic to compute:
  1  – Death Rate (CFR)
  2  – Rt (Effective Reproduction Number)
  3  – Average Daily Cases
  4  – Average Daily Deaths
  5  – Regional Death Rate
  6  – Vaccination Coverage  (ISO3)
  7  – Booster Dose Rate     (ISO3)
  8  – Total Vaccination Summary (ISO3)
  9  – # Vaccine Authorisations by ISO3
 10  – # Vaccine Authorisations by Product
 11  – Average Weekly Hospitalisations (ISO3)
 12  – Average Monthly Hospitalisations (ISO3)
 13  – Daily Time-Series
 14  – Monthly Deaths by Age Group (countries)
 15  – Monthly Deaths by Age Group (income groups)
 16  – Monthly Deaths by Age Group (WHO regions)
Enter the number of your choice: 1

Choose identifier type:
 1 – ISO3 code
 2 – Country code
 3 – WHO region
 4 – Vaccine product name
 5 – World-Bank income group
Enter input type number: 2

Enter values (comma-separated): TR,US,FR

─────────────────────────────────────────────────────────────
 Statistic   : Death Rate (CFR)
 IDs type    : Country code (2-letter)
 IDs         : TR, US, FR
─────────────────────────────────────────────────────────────

Statistical result:
Country_code
FR    0.430775
TR    0.596417
US    1.180865
Name: Death Rate, dtype: float64

Type of result: <class 'pandas.core.series.Series'>

Would you like to visualize this data as a bar graph? (y/n): y
#GRAPH IS NOT PASTED IN HERE IT CAN BE SEEN IN WHEN THE CODE IS RUN




