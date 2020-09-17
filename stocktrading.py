import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials


yahoo_financials = YahooFinancials('TSLA')

data = yahoo_financials.get_historical_price_data(start_date='2019-01-01', 
                                                  end_date='2019-12-31', 
                                                  time_interval='daily')



tsla_df = pd.DataFrame(data['TSLA']['prices'])
tsla_df = tsla_df.drop('date', axis=1).set_index('formatted_date')
tsla_df.head()

data1  = yf.download("G" , period = "6mo")  


import datetime as dt
import yfinance as yf
import pandas as pd

stocks = ["AMZN","MSFT","INTC","GOOG","INFY.NS","3988.HK"]
start = dt.datetime.today()-dt.timedelta(360)
end = dt.datetime.today()
cl_price = pd.DataFrame() # empty dataframe which will be filled with closing prices of each stock
ohlcv_data = {} # empty dictionary which will be filled with ohlcv dataframe for each ticker

# looping over tickers and creating a dataframe with close prices
for ticker in stocks:
    cl_price[ticker] = yf.download(ticker,start,end)["Adj Close"]
    

# looping over tickers and storing OHLCV dataframe in dictionary
for ticker in stocks:
    ohlcv_data[ticker] = yf.download(ticker,start,end)

# filling NaN values
cl_price.fillna(method='bfill',axis=0,inplace=True)

#dropping NaN values
cl_price.dropna(axis=0,how='any')
cl_price.mean(axis=0)

cl_price.median(axis=0)

cl_price.std(axis=0)



daily_return=cl_price.pct_change(axis=0)

cl_price/cl_price.shift(1)


daily_return.rolling(window=20).mean()

daily_return.ewm(span=20 , min_periods).mean()


















#extracting fundamental data

import requests
from bs4 import BeautifulSoup
import pandas as pd

tickers = ["AAPL","MSFT"] #list of tickers whose financial data needs to be extracted
financial_dir = {}


for ticker in tickers:
    #getting balance sheet data from yahoo finance for the given ticker
    temp_dir = {}
    url = 'https://in.finance.yahoo.com/quote/'+ticker+'/balance-sheet?p='+ticker
    page = requests.get(url)
    page_content = page.content
    soup = BeautifulSoup(page_content,'html.parser')
    tabl = soup.find_all("div", {"class" : "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
    for t in tabl:
        rows = t.find_all("div", {"class" : "rw-expnded"})
        for row in rows:
            temp_dir[row.get_text(separator='|').split("|")[0]]=row.get_text(separator='|').split("|")[1]
    
    #getting income statement data from yahoo finance for the given ticker
    url = 'https://in.finance.yahoo.com/quote/'+ticker+'/financials?p='+ticker
    page = requests.get(url)
    page_content = page.content
    soup = BeautifulSoup(page_content,'html.parser')
    tabl = soup.find_all("div", {"class" : "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
    for t in tabl:
        rows = t.find_all("div", {"class" : "rw-expnded"})
        for row in rows:
            temp_dir[row.get_text(separator='|').split("|")[0]]=row.get_text(separator='|').split("|")[1]
    
    #getting cashflow statement data from yahoo finance for the given ticker
    url = 'https://in.finance.yahoo.com/quote/'+ticker+'/cash-flow?p='+ticker
    page = requests.get(url)
    page_content = page.content
    soup = BeautifulSoup(page_content,'html.parser')
    tabl = soup.find_all("div", {"class" : "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
    for t in tabl:
        rows = t.find_all("div", {"class" : "rw-expnded"})
        for row in rows:
            temp_dir[row.get_text(separator='|').split("|")[0]]=row.get_text(separator='|').split("|")[1]
    
    #getting key statistics data from yahoo finance for the given ticker
    url = 'https://in.finance.yahoo.com/quote/'+ticker+'/key-statistics?p='+ticker
    page = requests.get(url)
    page_content = page.content
    soup = BeautifulSoup(page_content,'html.parser')
    tabl = soup.findAll("table", {"class": "W(100%) Bdcl(c) "})
    for t in tabl:
        rows = t.find_all("tr")
        for row in rows:
            if len(row.get_text(separator='|').split("|")[0:2])>0:
                temp_dir[row.get_text(separator='|').split("|")[0]]=row.get_text(separator='|').split("|")[-1]    
    
    #combining all extracted information with the corresponding ticker
    financial_dir[ticker] = temp_dir


#storing information in pandas dataframe
combined_financials = pd.DataFrame(financial_dir)
tickers = combined_financials.columns
for ticker in tickers:
    combined_financials = combined_financials[~combined_financials[ticker].str.contains("[a-z]").fillna(False)]


















    