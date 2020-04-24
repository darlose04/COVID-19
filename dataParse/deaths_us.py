import pandas as pd
import datetime

csv_path = '/home/zach/Storage/Projects/COVID-19/covidData/csse_covid_19_data/csse_covid_19_time_series/'

us_deaths = pd.read_csv(csv_path + 'time_series_covid19_deaths_US.csv')

# yesterday = us_deaths["4/20/20"]
# today = us_deaths["4/21/20"]
# first_date = "1/22/20"

dates = us_deaths.columns[12:]

for item in dates:
  print(item, us_deaths[item].sum())

uid = us_deaths.columns[0]

print(us_deaths[uid])