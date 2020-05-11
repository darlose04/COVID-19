import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
import os
from datetime import datetime

csv_path = "/home/zach/Storage/Projects/COVID-19/covidData/csse_covid_19_data/csse_covid_19_daily_reports_us"

# check if the date is January 1st and adjust day, month, and year accordingly
if datetime.now().day == 1 and datetime.now().month == 1:
  month = 12
  day == 31
  year = datetime.now().year - 1

# check if it's March 1st in order to set the necessary to Feb 28th. Not going to bother with checking for leap years, won't be needed for 4 years and hopefully COVID won't be a thing by then
if datetime.now().day == 1 and datetime.now().month == 3:
  month = datetime.now().month - 1
  day = 28

# check if it's the first day of the month
if datetime.now().day == 1:
  if datetime.now().month == 2 or datetime.now().month == 4 or datetime.now().month == 6 or datetime.now().month == 8 or datetime.now().month == 9 or datetime.now().month == 11:
    day = 31
    month = datetime.now().month - 1
  elif datetime.now().month == 5 or datetime.now().month == 7 or datetime.now().month == 10 or datetime.now().month == 12:
    month = datetime.now().month - 1
    day = 30
else:
  month = datetime.now().month
  day = datetime.now().day - 1
  year = datetime.now().year

# create yesterday's date as a string since that will be the most recent csv in the daily reports


# daily_report = pd.read_csv(csv_path + )