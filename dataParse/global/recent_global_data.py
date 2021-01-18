import pandas as pd

"""
This script pulls the date columns out of the two time series CSVs for global cases and deaths
"""

csv_path = '/home/zach/Storage/Projects/COVID-19/covidData/csse_covid_19_data/csse_covid_19_time_series/'

global_cases = pd.read_csv(
    csv_path + 'time_series_covid19_confirmed_global.csv')
global_deaths = pd.read_csv(csv_path + 'time_series_covid19_deaths_global.csv')

confirmed_dates = global_cases.columns[4:]
death_dates = global_deaths.columns[4:]


def create_csv(data, dates, csv_name):
    columns = ['ID']

    for header in dates:
        columns.append(header)

    id_arr = []
    increment = 1

    # create ids for new csv
    while increment < 272:
        id_arr.append(increment)
        increment += 1

    count = 1
    col_arr = []

    while count < 272:
        sub_arr = []

        sub_arr.append(id_arr.pop(0))

        for header in dates:
            sub_arr.append(data[header].pop(count - 1))

        col_arr.append(sub_arr)

        count += 1

    csv = csv_name + '.csv'
    csv_name = pd.DataFrame(col_arr, columns=columns,)
    csv_name.to_csv(csv)


create_csv(global_cases, confirmed_dates, 'global_cases')
create_csv(global_deaths, death_dates, 'global_deaths')
