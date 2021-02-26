import pandas as pd
import numpy as np

dates = pd.date_range('20190101',periods=366)

year = pd.DataFrame({'date': dates,
                    'Vacation': 0,
                    'Sick': 0,
                    'Absence': 0,
                    'Remote' : 0,
                    'Overtime': 0
              })

def processLeave(leave):
    if(not pd.isnull(leave.type)):
        year.loc[(year['date'] >= leave.start)&(year['date'] <= leave.end), leave.type] +=1
    pass

vacations = pd.read_csv('data-2019.csv', index_col=0, parse_dates=["start","end"])

for row in vacations.itertuples():
    processLeave(row)

year.to_csv('out.csv')