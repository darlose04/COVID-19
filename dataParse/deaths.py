import pandas as pd
import mysql.connector
import os

csv_path = '/home/zach/Storage/Projects/COVID-19/covidData/csse_covid_19_data/csse_covid_19_time_series/'

us_deaths = pd.read_csv(csv_path + 'time_series_covid19_deaths_US.csv')

dates = us_deaths.columns[12:]

# Create database connection
mydb = mysql.connector.connect(
  host='localhost',
  user='zach',
  passwd=os.environ['DBPASSWD'],
  database='covid19'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS deaths (UID INT AUTO_INCREMENT PRIMARY KEY)")

# reverse array in order to add items in sql table in proper order
for item in reversed(dates):
  mycursor.execute(f"ALTER TABLE deaths ADD COLUMN `{item}` INT AFTER UID")

