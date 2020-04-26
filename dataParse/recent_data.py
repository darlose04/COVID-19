import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
import os

csv_path = '/home/zach/Storage/Projects/COVID-19/covidData/csse_covid_19_data/csse_covid_19_time_series/'

us_deaths = pd.read_csv(csv_path + 'time_series_covid19_deaths_US.csv')
us_confirmed = pd.read_csv(csv_path + 'time_series_covid19_confirmed_US.csv')

# Create database connection
engine = create_engine(f"mysql+mysqlconnector://zach:{os.environ['DBPASSWD']}@127.0.0.1:3306/covid19")

# print(engine)

# print(us_deaths)

uid_arr = []
increment = 1

# create ids for new csv
while increment < 3262:
  uid_arr.append(increment)
  increment += 1

dates = us_deaths.columns[12:]
# print(dates)

# print(uid_arr)

columns = ['UID']

for header in dates:
  columns.append(header)

data_input = []

for header in dates:
  data_input.append(us_deaths[header])

last_column = []

for item in data_input[-1]:
  last_column.append(item)


zipcol = list(zip(uid_arr, last_column))
print(zipcol)



coviddeaths = pd.DataFrame(zipcol, columns=['UID', '4/25/20'],)
coviddeaths.to_csv('deaths.csv')
