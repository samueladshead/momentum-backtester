import pandas as pd
import yfinance as yf
from datetime import date
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt

companies = ['NVDA', 'GOOGL', 'AAPL', 'MSFT', 'AMZN', 'TSM', 'AVGO', 'META', 'TSLA', 'JPM']

def create_dataframe(idk, backtest_length):
    year = date.today().year
    end = date(year-1, 12, 31) #Last day of the last full year
    start = end - relativedelta(months=backtest_length + 12) #Exactly x months before the final date + 12 months of data for the momentum calc
    data = pd.DataFrame(yf.download(idk, start=start, end=end)["Close"])
    return data

dataframe = create_dataframe(companies, 12)
#dataframe.plot()
#plt.show()
print(dataframe)

def calc_momentum(data): 
    data = pd.DataFrame(data)
    data.iloc[0] / data.iloc[-1]
    something = 0
    output = pd.DataFrame(something)
    return output

#momentum = calc_momentum(dataframe)
#print(momentum)