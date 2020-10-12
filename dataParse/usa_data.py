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

# Make variables for each column from the csv that I want to push into SQL

uid = us_deaths.columns[0]  # int or float
county = us_deaths.columns[5]  # string. will need to account for null values
province_state = us_deaths.columns[6]  # string
latitude = us_deaths.columns[8]  # float
longitude = us_deaths.columns[9]  # float
population = us_deaths.columns[11]  # int

# want to grab every item in columns except for last row since last row is NaN
# Last row also doesn't have useful info
county_vals = us_deaths[county][:-1]
province_state_vals = us_deaths[province_state][:-1]
latitude_vals = us_deaths[latitude][:-1]
longitude_vals = us_deaths[longitude][:-1]
population_vals = us_deaths[population][:-1]

mycursor = mydb.cursor()

# create db table
mycursor.execute("CREATE TABLE usa (UID INT AUTO_INCREMENT PRIMARY KEY, County VARCHAR(255), State VARCHAR(255), Latitude FLOAT(10, 8), Longitude FLOAT(11,8), Population INT)")

# inserting values into table
sql = "INSERT INTO usa (County, State, Latitude, Longitude, Population) VALUES (%s, %s, %s, %s, %s)"

city_arr = []

for item in county_vals:
    if item != item:
        city_arr.append(None)
    else:
        city_arr.append(item)

data_arr = list(zip(city_arr, province_state_vals,
                    latitude_vals, longitude_vals, population_vals))

mycursor.executemany(sql, data_arr)
mydb.commit()
