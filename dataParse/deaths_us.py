import pandas as pd

csv_path = '/home/zach/Storage/Projects/COVID-19/covidData/csse_covid_19_data/csse_covid_19_time_series/'

us_deaths = pd.read_csv(csv_path + 'time_series_covid19_deaths_US.csv')

today = us_deaths["4/21/20"]

print(today)