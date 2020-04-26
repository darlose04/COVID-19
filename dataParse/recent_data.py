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

for header in dates:
  for item in us_deaths[header]:
    print(item)


# coviddeaths = pd.DataFrame([uid_arr, ], columns=columns)
# coviddeaths.to_csv('deaths.csv')
