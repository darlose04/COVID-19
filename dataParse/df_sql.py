import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
import os

csv_path = "/home/zach/Storage/Projects/COVID-19/"

deaths = pd.read_csv(csv_path + 'deaths.csv')
cases = pd.read_csv(csv_path + 'cases.csv')
global_cases = pd.read_csv(csv_path + 'dataParse/global/global_cases.csv')
global_deaths = pd.read_csv(csv_path + 'dataParse/global/global_deaths.csv')

# delete first column that was created automatically when csv was created
del deaths['Unnamed: 0']
del cases['Unnamed: 0']
del global_cases['Unnamed: 0']
del global_deaths['Unnamed: 0']

engine = create_engine(
    f"mysql+mysqlconnector://zach:{os.environ['DBPASSWD']}@localhost:3306/covid19")

deaths.to_sql('deaths', engine, if_exists='replace',
              index=True, index_label=None, method=None)
cases.to_sql('cases', engine, if_exists='replace',
             index=True, index_label=None, method=None)
global_cases.to_sql('global_cases', engine, if_exists='replace',
                    index=True, index_label=None, method=None)
global_deaths.to_sql('global_deaths', engine, if_exists='replace',
                     index=True, index_label=None, method=None)
