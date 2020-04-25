import pandas as pd
import mysql.connector
import os

csv_path = '/home/zach/Storage/Projects/COVID-19/covidData/csse_covid_19_data/csse_covid_19_time_series/'

us_deaths = pd.read_csv(csv_path + 'time_series_covid19_deaths_US.csv')

uid = us_deaths.columns[0]
dates = us_deaths.columns[12:]

# want to grab every item in uid column except for last row since last row is NaN
uid_vals = us_deaths[uid][:-1]

# Create database connection
mydb = mysql.connector.connect(
  host='localhost',
  user='zach',
  passwd=os.environ['DBPASSWD'],
  database='covid19'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE deaths (UID INT PRIMARY KEY)")

