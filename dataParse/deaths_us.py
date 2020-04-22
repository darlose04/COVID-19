import pandas

csv_path = '../covidData/csse_covid_19_data/csse_covid_19_time_series/'

df = pandas.read_csv(csv_path + 'time_series_covid19_deaths_US.csv')
print(df)