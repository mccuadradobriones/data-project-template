import pandas as pd
import numpy as np

# analysis functions
def analyze(df_wrang,country):
    a_df = df_wrang[['country', 'job_title', 'rural', 'person_id']]
    a_df= a_df.groupby(['country', 'job_title', 'rural'])['person_id'].count().reset_index()
    a_df.rename(columns={'person_id':'quantity'},inplace=True)
    a_df['percentage'] = (a_df['quantity'] / len(a_df)) * 100
    a_df = a_df[['country', 'job_title', 'rural', 'quantity', 'percentage']]
    dictionary = dict()
    for i in a_df['country']:
        a = dictionary.get(i, 0)
        b = a + 1
        dictionary[i] = b
    f = pd.DataFrame.from_dict(dictionary, orient='index', columns=['quantity_data_jobs_by_country'])
    f = f.reset_index()
    f = f.rename(columns={'index': 'country'})
    a_df = pd.merge(a_df, f, left_on='country', right_on='country')
    a_df['percentage_by_country'] = (a_df['quantity'] / a_df['quantity_data_jobs_by_country']) * 100
    a_df = a_df.drop(['quantity_data_jobs_by_country'], axis=1)
    country_list=[i for i in a_df['country'].unique()]
    a_df.to_csv(r'../data-project-template/data/results/analyzed_data.csv', index=False, sep=',')
    country_list = [i for i in a_df['country'].unique()]
    if country not in country_list:
        print(a_df)
    else:
        df = a_df[a_df['country' == country]]
        print(df)
    return a_df




