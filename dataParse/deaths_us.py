import pandas as pd

csv_path = '/home/zach/Storage/Projects/COVID-19/covidData/csse_covid_19_data/csse_covid_19_time_series/'

df = pd.read_csv(csv_path + 'time_series_covid19_deaths_US.csv')
print(df.head(20))