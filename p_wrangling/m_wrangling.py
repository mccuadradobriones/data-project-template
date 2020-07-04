import pandas as pd

# wrangling functions
def wrangle(df_acq):
    "Standardizing rural!"
    df = df_acq.replace(
        {'countryside': 'rural', 'city': 'Non-rural', 'urban': 'Non-rural', 'Country': 'rural', 'Rural': 'rural',
         'Non-Rural': 'Non-rural'})
    df=df.rename(columns={'normalized_job_title': 'job_title'})
    return df