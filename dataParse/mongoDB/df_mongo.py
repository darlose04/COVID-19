import pandas as pd
import os
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

csv_path = "/home/zach/Storage/Projects/COVID-19/covidData/csse_covid_19_data/csse_covid_19_time_series/"

us_confirmed = pd.read_csv(csv_path + "time_series_covid19_confirmed_US.csv")
us_deaths = pd.read_csv(csv_path + "time_series_covid19_deaths_US.csv")

db = client.covid19
collection = db.usa

states = list(set(us_confirmed["Province_State"]))
states.sort()
# print(states)

counties = us_confirmed["Admin2"]

# print(us_confirmed.iloc[0, 0:len(us_confirmed)])

one_row = us_confirmed.iloc[0, 0:len(us_confirmed)]
print(one_row[:20])


usa_data = [
    {
        'state_name': '',
        'counties': [
            {
                'county_name': '',
                'cases': {
                    '1/1/20': 0,
                    '1/2/20': 43,
                },
                'deaths': {
                    '1/1/20': 0,
                    '1/2/20': 4,
                }
            }
        ]
    }
]

# print(us_data['states'][0]['state_name'])
