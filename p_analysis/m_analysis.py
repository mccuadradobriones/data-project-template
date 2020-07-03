import pandas as pd

# analysis functions

def analyze(df_wrang):
    datasubset = df_wrang[['country', 'job_title', 'rural', 'person_id']]
    datasubset['quantity'] = 1
    datasubset = datasubset.groupby(['country', 'job_title', 'rural'])['quantity'].count().reset_index()
    datasubset['percentage'] = (datasubset['quantity'] / len(datasubset)) * 100
    datasubset['country_percetange']=
    table=datasubset.sort_values('country',ascending=False)
    return table

def filter_by_country(table,country):
    table['country']==country:
        return table[table['country']==country]
    else:
        return table

