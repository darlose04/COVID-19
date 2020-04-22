import pandas as pd
import datetime

csv_path = '/home/zach/Storage/Projects/COVID-19/covidData/csse_covid_19_data/csse_covid_19_time_series/'

us_deaths = pd.read_csv(csv_path + 'time_series_covid19_deaths_US.csv')

yesterday = us_deaths["4/20/20"]
today = us_deaths["4/21/20"]
first_date = "1/22/20"

# print(datetime.datetime.now())

# print(today.sum() - yesterday.sum())

# for col in us_deaths:
#   print(col)

dates = us_deaths.columns[12:]


print(dates[-1])
print(us_deaths[dates[-1]].sum())