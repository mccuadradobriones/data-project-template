import pandas as pd
import numpy as np
from IPython.core.display import display, HTML

# analysis functions
def analyze(df_wrang, country):
    a_df = df_wrang[['country_name', 'job_title', 'rural', 'person_id']]
    a_df= a_df.groupby(['country_name', 'job_title', 'rural'])['person_id'].count().reset_index()
    a_df.rename(columns={'person_id':'quantity'},inplace=True)
    a_df['percentage'] = (a_df['quantity'] / len(a_df)) * 100
    a_df = a_df[['country_name', 'job_title', 'rural', 'quantity', 'percentage']]
    dictionary = dict()
    for i in a_df['country_name']:
        a = dictionary.get(i, 0)
        b = a + 1
        dictionary[i] = b
    f = pd.DataFrame.from_dict(dictionary, orient='index', columns=['quantity_data_jobs_by_country'])
    f = f.reset_index()
    f = f.rename(columns={'index': 'country_name'})
    a_df = pd.merge(a_df, f, left_on='country_name', right_on='country_name')
    a_df['percentage_by_country'] = (a_df['quantity'] / a_df['quantity_data_jobs_by_country']) * 100
    a_df = a_df.drop(['quantity_data_jobs_by_country'], axis=1)
    country_list=[i for i in a_df['country_name'].unique()]
    a_df.to_csv(r'../data-project-template/data/results/analyzed_data.csv', index=False, sep=',')
    country_list = [i for i in a_df['country_name'].unique()]
    a_df['percentage'] = a_df['percentage'].apply(lambda x: "{0:.2f}%".format(x * 1))
    a_df['percentage_by_country'] = a_df['percentage_by_country'].apply(lambda x: "{0:.2f}%".format(x * 1))
    df = a_df[a_df['country_name'] == country]
    print(df)
    return df


