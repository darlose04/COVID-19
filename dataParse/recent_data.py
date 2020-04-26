import pandas as pd
import mysql.connector
import os
import datetime

csv_path = '/home/zach/Storage/Projects/COVID-19/covidData/csse_covid_19_data/csse_covid_19_time_series/'

us_deaths = pd.read_csv(csv_path + 'time_series_covid19_deaths_US.csv')
us_confirmed = pd.read_csv(csv_path + 'time_series_covid19_confirmed_US.csv')

# Create database connection
mydb = mysql.connector.connect(
  host='localhost',
  user='zach',
  passwd=os.environ['DBPASSWD'],
  database='covid19'
)

mycursor = mydb.cursor()

recent_column = us_deaths.columns[-1]

# for item in us_deaths[recent_column][:-1]:
  # print(item)

todays_date = datetime.date.today()
# print(todays_date.year)
current_year = todays_date.year
current_month = todays_date.month
current_day =  todays_date.day

yesterday = str(current_month) + "/" + str(current_day - 1) + "/" + str(current_year)
two_days_prior = str(current_month) + "/" + str(current_day - 2) + "/" + str(current_year)
print(yesterday)
print(two_days_prior)

# def get_recent_data(recent_column_date, yesterday, data):
