import pandas as pd

# wrangling functions
def wrangle(df_acq):
    "Cleaning Educational Level data!"
    for i in df_acq['ed_level']:
        for x in df_acq['suggestion']:
            if i== 'no' and

    df[filtro]['suggestion'].unique()
    df=df(replace({'no':'high'}))
    "Standardizing rural!"
    df = df_acq.replace(
        {'countryside': 'rural', 'city': 'Non-rural', 'urban': 'Non-rural', 'Country': 'rural', 'Rural': 'rural',
         'Non-Rural': 'Non-rural'})
    return df