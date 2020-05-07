import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csv_path = '/home/zach/Storage/Projects/COVID-19/covidData/csse_covid_19_data/csse_covid_19_time_series/'

us_deaths = pd.read_csv(csv_path + 'time_series_covid19_deaths_US.csv')
us_confirmed = pd.read_csv(csv_path + 'time_series_covid19_confirmed_US.csv')

death_dates = us_deaths.columns[12:]
confirmed_dates = us_confirmed.columns[11:]

total_deaths = []
total_cases = []

for column in death_dates:
  total_deaths.append(us_deaths[column].sum())

for column in confirmed_dates:
  total_cases.append(us_confirmed[column].sum())

# print(total_deaths)
# print(total_cases)

plt.plot(death_dates, total_deaths)
plt.xlabel("Dates")
plt.ylabel("Deaths")
plt.title("COVID-19 Deaths U.S.")
plt.show()