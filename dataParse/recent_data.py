import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
import os

csv_path = '/home/zach/Storage/Projects/COVID-19/covidData/csse_covid_19_data/csse_covid_19_time_series/'

us_deaths = pd.read_csv(csv_path + 'time_series_covid19_deaths_US.csv')
us_confirmed = pd.read_csv(csv_path + 'time_series_covid19_confirmed_US.csv')

# Create database connection
# engine = create_engine(f"mysql+mysqlconnector://zach:{os.environ['DBPASSWD']}@127.0.0.1:3306/covid19")

# print(engine)

uid_arr = []
increment = 1

# create ids for new csv
while increment < 3262:
  uid_arr.append(increment)
  increment += 1

dates = us_deaths.columns[12:]

columns = ['UID']
# print(len(uid_arr))

for header in dates:
  columns.append(header)

data_input = []
# data_input.append(uid_arr)

# for header in dates:
#   firstItem = us_deaths[header].pop(0)
#   data_input.append(firstItem)

# print(data_input)
count = 1
col_arr = []

while count < 3262:
  sub_arr = []

  sub_arr.append(uid_arr.pop(0))

  for header in dates:
    sub_arr.append(us_deaths[header][:-1].pop(0))


  col_arr.append(sub_arr)
  # print(sub_arr)
  count += 1


# print(col_arr)


coviddeaths = pd.DataFrame(col_arr, columns=columns,)
coviddeaths.to_csv('deaths.csv')
