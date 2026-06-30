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
import yfinance as yf
from datetime import date
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt

companies = ['NVDA', 'GOOGL', 'AAPL', 'MSFT', 'AMZN', 'TSM', 'AVGO', 'META', 'TSLA', 'JPM']

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
    start = end - relativedelta(months=backtest_length + 12) #Exactly x months before the final date + 12 months of data for the momentum calc
    value = pd.DataFrame(yf.download(data, start=start, end=end)["Close"])
    return value

df = create_dataframe(companies, 12) #Create a dataframe for the last 12 months
#df.plot()
#plt.show()

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

momentum = calc_momentum(df)
#print(momentum)

def rank_stocks(data, n):
    '''
    Identifies the top N stocks by momentum for each date in the dataset.

    For every row (date) in the input DataFrame, ranks all tickers by their
    momentum value and selects the top N performers.

    Args:
    data (DataFrame): Momentum values indexed by date, with one column
    per ticker (output of calc_momentum).
    n (int): Number of top-ranked tickers to select per date.

    Returns:
    dict[pd.Timestamp, pd.Series]: A dictionary mapping each date to a
    Series of the top N tickers and their momentum values, sorted
    in descending order.
    '''
    rankings = {}
    tickers = []
    df = pd.DataFrame(data)
    for index, row in df.iterrows():
        rankings[index] = row.nlargest(n)
    print(tickers)
    
    return rankings

rankedtickers = rank_stocks(momentum, 3)
print(rankedtickers)
