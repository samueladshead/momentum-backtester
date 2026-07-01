# =============================================================================
# Momentum Month-end Backtester - Trading Personal Project
# =============================================================================
#
# Author: Samuel Adshead
# Date:   N/A
#
# -----------------------------------------------------------------------------
# Project Description
# -----------------------------------------------------------------------------
# IDK
# -----------------------------------------------------------------------------

import pandas as pd
import numpy as np
import yfinance as yf
from datetime import date
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt

def create_dataframe(data, backtest_length):
    '''
    Creates a dataframe of historical financial data as defined by the user. The dataframe is 
    hardcoded to start at the last day of the last full year.

    The created dataframe is 12 months longer than whatever the user inputs, in order to enable
    the 12-1 month momentum calculation method.

    Args:
    data(list): A list of all tickers that the user wants to get information on.
    backtest_length(int): Length of the test (months).

    Returns:
    DataFrame[int]: A Pandas dataframe containing financial data for the chosen companies
    '''
    end = date(date.today().year-1, 12, 31) #Last day of the last full year
    start = end - relativedelta(months=backtest_length + 13)#Exactly x months before the final date + 12 months of data for the momentum calc
    value = pd.DataFrame(yf.download(data, start=start, end=end)["Close"])
    return value

def calc_momentum(data):
    '''
    Creates a monthly dataframe of the momentum of stocks using the 12-1 method. 

    Returns:
    DataFrame[int]: A Pandas dataframe containing the value of the stock at every month-end.
    ''' 
    df = pd.DataFrame(data)
    df = df.resample('ME').last()
    df = df.shift(1).pct_change(periods=12).dropna()
    return df

def rank_stocks(data, n):
    '''
    Ranks the top n stock momentums over the given period as defined by the other functions.

    Arguments:
    data(pd.DataFrame): Values of all tickers' momentums sampled monthly.
    n(int): Number of momentums to be shown at the top.

    Returns:
    pd.DataFrame[pd.Timestamp, (pd.Ticker, pd.Series)]: A Pandas Dataframe mapping
    the top n tickers onto the last day of the month.
    '''
    rankings = {}
    biden = {}
    df = pd.DataFrame(data)
    for index, row in df.iterrows():
        rankings[index] = row.nlargest(n)

    for x,y in rankings.items(): #Per day basis
        y = pd.Series(y)
        huge = []
        for index, value in y.items(): #Dive into each day and disect a day
            joe = (index, round(value,3))
            huge.append(joe)
        biden[x] = huge
    
    kamala = []
    harris = np.arange(1,n+1,1)
    for x in harris:
        f = f'Rank {x}'
        kamala.append(f)

    biden = pd.DataFrame(biden, index = kamala).T
    return biden

companies = ['NVDA', 'GOOGL', 'AAPL', 'MSFT', 'AMZN', 'TSM', 'AVGO', 'META', 'TSLA', 'JPM']

df = create_dataframe(companies, 12) #Create a dataframe for the last 12 months
print(df)
#df.plot()
#plt.show()

momentum = calc_momentum(df)
#print(momentum)

rankedtickers = rank_stocks(momentum, 3)
print(rankedtickers)

def simulate_portfolio(prices,momentum,rankings,money):
    prices = pd.DataFrame(prices)
    momentum = pd.DataFrame(momentum)
    rankings = pd.DataFrame(rankings)
    #Extract the top 3 tickers from each month from rankings
    #Find their prices on the last trading day of the month
    #Buy them at that price on 