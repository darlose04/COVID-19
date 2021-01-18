import pandas as pd
import mysql.connector
import os

csv_path = '/home/zach/Storage/Projects/COVID-19/covidData/csse_covid_19_data/csse_covid_19_time_series/'

global_cases = pd.read_csv(
    csv_path + 'time_series_covid19_confirmed_global.csv')

mydb = mysql.connector.connect(
    host=os.environ['DBIP'],
    user='zach',
    passwd=os.environ['DBPASSWD'],
    database='covid19'
)

# Make variables for each column from the csv that I want to push into SQL
province = global_cases.columns[0]
country = global_cases.columns[1]
# latitude = global_cases.columns[2]
# longitude = global_cases.columns[3]

province_vals = global_cases[province]
country_vals = global_cases[country]
# latitude_vals = global_cases[latitude]
# longitude_vals = global_cases[longitude]

province_arr = []

for item in province_vals:
    if item != item:
        province_arr.append(None)
    else:
        province_arr.append(item)

# create db table
mycursor = mydb.cursor()
mycursor.execute(
    "CREATE TABLE global (ID INT AUTO_INCREMENT PRIMARY KEY, Province VARCHAR(255), Country VARCHAR(255))")

# inserting values into the table
sql = "INSERT INTO global (Province, Country) VALUES (%s, %s)"

data_arr = list(zip(province_arr, country_vals))

mycursor.executemany(sql, data_arr)
mydb.commit()
