#!/bin/bash

echo "Running Python scripts to update the database at $(date +%B%d,%T)" > /home/zach/Storage/Projects/COVID-19/pythonScripts.out

echo "Running recent_data.py to create and update the CSVs" >> /home/zach/Storage/Projects/COVID-19/pythonScripts.out
python3 /home/zach/Storage/Projects/COVID-19/dataParse/recent_data.py
echo "Done running recent_data.py" >> /home/zach/Storage/Projects/COVID-19/pythonScripts.out

echo "Running df_sql.py to push newly created CSVs into local MySQL database" >> /home/zach/Storage/Projects/COVID-19/pythonScripts.out
python3 /home/zach/Storage/Projects/COVID-19/dataParse/df_sql.py
echo "Done running df_sql.py" >> /home/zach/Storage/Projects/COVID-19/pythonScripts.out

echo "Running daily_report.py to add the daily report CSV to the database" >> /home/zach/Storage/Projects/COVID-19/pythonScripts.out
python3 /home/zach/Storage/Projects/COVID-19/dataParse/daily_report.py
echo "Done running daily_report.py" >> /home/zach/Storage/Projects/COVID-19/pythonScripts.out

echo "Python scripts finished" >> /home/zach/Storage/Projects/COVID-19/pythonScripts.out