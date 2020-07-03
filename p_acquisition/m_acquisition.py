import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from sqlalchemy import inspect, create_engine
import sqlsoup


#acquisition functions
#Acquiring data from database
def get_db(path):
    print('Getting database')
    engine = create_engine(f'sqlite:////{path}')
    table_names = inspect(engine).get_table_names()
    for i in table_names:
        print(f'Loading table {i}')
        if i == table_names[0]:
            print(f'Transforming {i} to dataframe')
            df = pd.read_sql_query(f'SELECT * FROM {i}', engine)
        else:
            print(f'Merging dataframe with {i}')
            db_df = pd.read_sql_query(f'SELECT * FROM {i}', engine)
            df = pd.merge(df, db_df, left_on="uuid", right_on="uuid")
    db_df = df.rename(columns={'uuid': 'person_id','normalized_job_code': 'uuid','dem_education_level': 'ed_level',
                            'dem_full_time_job': 'job_type',
                            'question_bbi_2016wave4_basicincome_awareness': 'bi_awareness',
                            'question_bbi_2016wave4_basicincome_vote': 'bi_vote',
                            'question_bbi_2016wave4_basicincome_effect': 'bi_effect',
                            'question_bbi_2016wave4_basicincome_argumentsfor': 'bi_argsfor',
                            'question_bbi_2016wave4_basicincome_argumentsagainst': 'bi_argsagsagainst'})
    print('Cleaning out null values from uuid')
    filtered = db_df.uuid.notnull()
    jobs_db = db_df[filtered]
    return db_df

#Acquiring data from API
def get_jobsid(url):
    print('Calling api!')
    response = requests.get(url)
    json_data=response.json()
    print('Transforming api data into dataframe')
    api_df = pd.DataFrame(json_data)
    api_df.rename(columns={'suggestion': 'job_title'})
    return api_df

#Acquiring data from Web Scrapping
def get_web(url):
    print('Starting to web scrap!')
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'lxml')
    countries = soup.find_all('td')
    print('Cleaning retrived data')
    lista = []
    lista = [i.text for i in countries]
    cleaned = [i.strip() for i in lista if len(i) > 3]
    split = 2
    country_codes = [cleaned[i:i + split] for i in range(0, len(cleaned), split)]
    print('Transforming web scrapping data into dataframe')
    country_codes = pd.DataFrame(country_codes)
    country_codes = country_codes.rename(columns={0: 'country', 1: 'country_code'})
    country_codes['country_code'] = country_codes['country_code'].str.replace(')', '')
    country_codes['country_code'] = country_codes['country_code'].str.replace('(', '')
    return country_codes


def data_df():
    db_df = get_db(path='home/carmencuadrado/Ironhack/Project-1/data-project-template/data/raw/raw_data_project_m1.db')
    api_df = get_jobsid(url=f'http://api.dataatwork.org/v1/jobs/autocomplete?contains=data')
    web_df = get_web(url = 'https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes')
    print('Merging all retrieved data')
    df_1= pd.merge(db_df, web_df, left_on='country_code', right_on='country_code', how='inner')
    df = pd.merge(df_1, api_df, left_on='uuid', right_on='uuid')
    return df


