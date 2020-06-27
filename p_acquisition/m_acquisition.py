import pandas as pd
import requests

#acquisition functions

def setup.quandl(api_key:str):
    print("setting quandl API key")
    quandl.ApiConfig.api_key=api_key

def get_db(path:str):
    jobs=pd.read_csv(path)
    ticker_list=companies['Ticker'].to_list()
    print(f'retrieved{len(ticker_list)}companies...')
    return ticker_list

def get_prices(ticker):
    print(f'getting historical stock prices for company: {ticker}')
    prices_full=quandl.get(f'WIKI/{ticker}')
    prices_full.to_csv(f'./data/raw/{ticker}.csv')
    prices=prices_full[['Adj. Close']].reset_index()
    prices['Ticker']=ticker
    prices_full.to_csv(f'./data/raw/{ticker}.csv', index=false)
    return prices

def acquire():
    data=pd.read_csv('./data/raw/companies.csv')

