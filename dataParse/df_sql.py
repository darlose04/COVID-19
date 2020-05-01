import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
import os

csv_path = "/home/zach/Storage/Projects/COVID-19/"

deaths = pd.read_csv(csv_path + 'deaths.csv')
cases = pd.read_csv(csv_path + 'cases.csv')

# delete first column that was created automatically when csv was created
del deaths['Unnamed: 0']
del cases['Unnamed: 0']

engine = create_engine(f"mysql+mysqlconnector://zach:{os.environ['DBPASSWD']}@127.0.0.1:3306/covid19")

deaths.to_sql('deaths', engine, if_exists='replace', index=True, index_label=None, method=None)
cases.to_sql('cases', engine, if_exists='replace', index=True, index_label=None, method=None)