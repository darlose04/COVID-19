import pandas as pd
import mysql.connector
import os

csv_path = '/home/zach/Storage/Projects/COVID-19/covidData/csse_covid_19_data/csse_covid_19_time_series/'

us_deaths = pd.read_csv(csv_path + 'time_series_covid19_deaths_US.csv')

mydb = mysql.connector.connect(
  host='localhost',
  user='zach',
  passwd=os.environ['DBPASSWD'],
  database='covid19'
)

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
#dates = us_deaths.columns[12:] # ints

# want to grab every item in columns except for last row since last row is NaN
# Last row also doesn't have useful info
uid_vals = us_deaths[uid][:-1]
# convert floats in uid column to ints for db
int_uid = []
for item in uid_vals:
  int_uid.append(int(item))

city_vals = us_deaths[city][:-1]
province_state_vals = us_deaths[province_state][:-1]
latitude_vals = us_deaths[latitude][:-1]
longitude_vals = us_deaths[longitude][:-1]
population_vals = us_deaths[population][:-1]

mycursor = mydb.cursor()




# create db table
# mycursor.execute("CREATE TABLE usa (UID INT PRIMARY KEY, City VARCHAR(100), Province_State VARCHAR(100), Latitude FLOAT(10, 8), Longitude FLOAT(11,8), Population INT)")

# inserting values into table
# sql = "INSERT INTO usa (UID) VALUES (%s)"
# uid_arr = []

# for num in uid_vals:
#   uid_arr.append((num,))

# mycursor.executemany(sql, uid_arr)
# mydb.commit()

def insert_data(col, data):
  sql = f'INSERT INTO usa ({col}) VALUES (%s)'
  data_arr = []
  # account for NaN values in csv
  nan_rows = data.isnull()

  for item in data:
    if item != item:
      data_arr.append(("",))
    else:
      data_arr.append((item,))

  mycursor.executemany(sql, data_arr)
  mydb.commit()

# insert_data("UID", uid_vals)
# insert_data("City", city_vals)
# insert_data("Province_State", province_state_vals)
# insert_data("Latitude", latitude_vals)
# insert_data("Longitude", longitude_vals)
# insert_data("Population", population_vals)

# nan_rows = city_vals.isnull()
# print(nan_rows)

# print(city_vals)

# for item in city_vals:
#   if item != item:
#     print("NaN")
#   else:
#     print(item)

# for item in nan_rows:
  # print(item)
