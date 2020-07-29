import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
import os
from datetime import datetime

csv_path = "/home/zach/Storage/Projects/COVID-19/covidData/csse_covid_19_data/csse_covid_19_daily_reports/"
