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

# for item in dates:
#   mycursor.execute(f"ALTER TABLE deaths ADD COLUMN `{item}` INT FIRST")

# reverse array in order to add items in sql table in proper order
for item in reversed(dates):
  mycursor.execute(f"ALTER TABLE deaths ADD COLUMN `{item}` INT AFTER UID")

# for item in dates:
#   for num in us_deaths[item]:
#     print(item, num)

# deaths_arr = []


# for item in dates:
  # sql = f"INSERT INTO deaths (`{item}`) VALUES (%s)"
  # data_arr = list(zip(us_deaths[item][:-1]))
  # deaths_arr.append(data_arr)

# mycursor.executemany(sql, deaths_arr)
# print(deaths_arr[-1])

# mydb.commit()