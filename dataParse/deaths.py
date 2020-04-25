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

# mycursor.execute("CREATE TABLE deaths (UID INT AUTO_INCREMENT PRIMARY KEY)")

# mycursor.execute(f"ALTER TABLE deaths ADD COLUMN FIRST INT AFTER UID")

for item in dates:
  date_split = item.split("/")
  month = date_split[0]
  day = date_split[1]
  year = date_split[2]

  if month == "1":
    month = "Jan"
  elif month == "2":
    month = "Feb"
  elif month == "3":
    month = "Mar"
  elif month == "4":
    month = "Apr"
  elif month == "5":
    month = "May"
  elif month == "6":
    month = "Jun"
  elif month == "7":
    month = "Jul"
  elif month == "8":
    month = "Aug"
  elif month == "9":
    month = "Sep"
  elif month == "10":
    month = "Oct"
  elif month == "11":
    month = "Nov"
  elif month == "12":
    month = "Dec"

  date = month + day + year
  print(date)