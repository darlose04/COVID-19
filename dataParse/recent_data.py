import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
import os

"""
This script pulls the date columns out of the two time series CSVs from the Johns Hopkins Github repository.
The columns are then used to create another CSV file along with a column for IDs, called UIDs.
I am doing it this way since I want to be able to store the date columns in a SQL database, but 
I don't want all the columns that are in the original time series CSVs.
"""

csv_path = '/home/zach/Storage/Projects/COVID-19/covidData/csse_covid_19_data/csse_covid_19_time_series/'

us_deaths = pd.read_csv(csv_path + 'time_series_covid19_deaths_US.csv')
us_confirmed = pd.read_csv(csv_path + 'time_series_covid19_confirmed_US.csv')

# Create database connection
# engine = create_engine(f"mysql+mysqlconnector://zach:{os.environ['DBPASSWD']}@127.0.0.1:3306/covid19")

# print(engine)



death_dates = us_deaths.columns[12:]
confirmed_dates = us_confirmed.columns[11:]

def create_csv(data, dates, csv_name):
  columns = ['UID']

  for header in dates:
    columns.append(header)

  uid_arr = []
  increment = 1

  # create ids for new csv
  while increment < 3262:
    uid_arr.append(increment)
    increment += 1

  count = 1
  col_arr = []

  while count < 3262:
    sub_arr = []

    sub_arr.append(uid_arr.pop(0))

    for header in dates:
      sub_arr.append(data[header][:-1].pop(count-1))


    col_arr.append(sub_arr)

    count += 1
  
  csv = csv_name + '.csv'

  csv_name = pd.DataFrame(col_arr, columns=columns,)
  csv_name.to_csv(csv)


create_csv(us_deaths, death_dates, 'deaths')
create_csv(us_confirmed, confirmed_dates, 'cases')

