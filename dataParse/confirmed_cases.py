import pandas as pd
import mysql.connector
import os

csv_path = '/home/zach/Storage/Projects/COVID-19/covidData/csse_covid_19_data/csse_covid_19_time_series/'

us_confirmed = pd.read_csv(csv_path + 'time_series_covid19_confirmed_US.csv')

dates = us_confirmed.columns[11:]
# for item in dates:
#   print(item)

# Create database connection
mydb = mysql.connector.connect(
  host='localhost',
  user='zach',
  passwd=os.environ['DBPASSWD'],
  database='covid19'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS confirmed (UID INT AUTO_INCREMENT PRIMARY KEY)")


# reverse array in order to add items in sql table in proper order
for item in reversed(dates):
  mycursor.execute(f"ALTER TABLE confirmed ADD COLUMN `{item}` INT AFTER UID")