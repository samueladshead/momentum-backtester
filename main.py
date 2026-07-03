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

def simulate_portfolio(prices,momentum,rankings,money):
    prices = pd.DataFrame(prices)
    rankings = pd.DataFrame(rankings)
    rankings2 = {}
    portfolio_value = money
    
    for index, row in rankings.iterrows(): #Extract the top 3 tickers from each month from rankings
        balls = []
        rfk = []
        noofshares = []
        rfk2 = []
        nextindex = index + pd.offsets.MonthEnd(1)
        for index1,value in row.items():
                ticker = value[0]
                balls.append(ticker)#Find their prices on the last trading day of the month 
                rfk.append(round(prices[ticker].asof(index),3))#Or as close as possible with the .asof function 
                rfk2.append(round(prices[ticker].asof(nextindex),3))#rfk2 defintion here(next value)
                cost = portfolio_value / len(row)
                shares = round(cost / rfk[-1],3)
                noofshares.append(shares)
        rankings2[index] = [balls, rfk, noofshares, portfolio_value]
        portfolio_value = round(sum(noofshares[i] * rfk2[i] for i in range(len(noofshares))), 3)
    rankings2 = pd.DataFrame(rankings2, index = ["Tickers", "Prices (Close)", "No. of shares"
                                                 ,"Portfolio Value"]).T
    return rankings2

def parameter_calculation(simulationresult):
    simres = pd.DataFrame(simulationresult)
    dates = list(simres.index)
    nmonthreturn = np.subtract(simres.loc[dates[-1], "Portfolio Value"] / simres.loc[dates[0], "Portfolio Value"], 1)
    annualreturn = (1 + nmonthreturn) ** (12 / len(dates)) - 1

    equitycurve = simres.get("Portfolio Value")
    monthlyreturns = equitycurve.pct_change().dropna()

    sharpe = (monthlyreturns.mean() / monthlyreturns.std()) * np.sqrt(12)

    maximumvalue = equitycurve.cummax()
    temp = (equitycurve - maximumvalue) / maximumvalue
    maxdrawdown = f"{round(temp.min(),3) * 100} %"

    print("Please type the number(s) of the parameter(s) you wish to calculate")
    print("Key:")
    print("1 - Annual Return")
    print("2 - Monthly returns")
    print("3 - Sharpe ratio")
    print("4 - Maximum Drawdown (MDD)")

    options = {
    "1": ("Annual Return", annualreturn),
    "2": ("Monthly Returns", monthlyreturns),
    "3": ("Sharpe Ratio", sharpe),
    "4": ("Maximum Drawdown (MDD)", maxdrawdown)
    }

    userinput = input("Enter option(s) e.g. 13 for options 1 and 3: ")

    for char in userinput:
        if char in options:
            label, value = options[char]
            print(f"{label}: {value}")
        else:
            print(f"'{char}' is not a valid option")

def plotequitycurve(simulation):
    simres = pd.DataFrame(simulation)
    equitycurve = simres.get("Portfolio Value")

    dates = list(simres.index)
    spy = pd.DataFrame(yf.download("SPY", start=dates[0], end=dates[-1])["Close"])
    spy_normalised = spy / spy.iloc[0] * 10000



    plt.plot(equitycurve, label='Momentum Strategy')
    plt.plot(spy_normalised, label='SPY Benchmark')
    plt.title('Momentum strategy vs SPY Benchmark')
    plt.xlabel('Days (yyyy-mm-dd)')
    plt.ylabel('Portfolio Value')
    plt.legend()
    plt.grid(True)
    plt.show()


# =============================================================================
# TESTING THE FUNCTIONS AND THE SOLUTIONS
# =============================================================================

companies = ['NVDA', 'GOOGL', 'AAPL', 'MSFT', 'AMZN', 'TSM', 'AVGO', 'META', 'TSLA', 'JPM']

df = create_dataframe(companies, 12) #Create a dataframe for the last 12 months
#print(df)
#df.plot()
#plt.show()

momentum = calc_momentum(df)
#print(momentum)

rankedtickers = rank_stocks(momentum, 3)
#print(rankedtickers)

simulation = simulate_portfolio(df,momentum,rankedtickers,10000)
#print(simulation)

#parameter_calculation(simulation)

plotequitycurve(simulation)