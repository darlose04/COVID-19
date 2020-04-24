import pandas as pd
import datetime

csv_path = '/home/zach/Storage/Projects/COVID-19/covidData/csse_covid_19_data/csse_covid_19_time_series/'

us_deaths = pd.read_csv(csv_path + 'time_series_covid19_deaths_US.csv')

# yesterday = us_deaths["4/20/20"]
# today = us_deaths["4/21/20"]
# first_date = "1/22/20"

# Make variables for each column from the csv that I want to push into SQL

uid = us_deaths.columns[0] # int or float
city = us_deaths.columns[5]  # string. will need to account for null values
province_state = us_deaths.columns[6] # string
latitude = us_deaths.columns[8] # float
longitude = us_deaths.columns[9] # float
population = us_deaths.columns[11] # int
dates = us_deaths.columns[12:] # ints

# for item in dates:
#   print(item, us_deaths[item].sum())

# print(type(us_deaths[latitude]))

for item in us_deaths[dates[-1]]:
  print(type(item))