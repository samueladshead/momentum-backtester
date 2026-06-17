import pandas as pd
import yfinance as yf
from datetime import date
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt

companies = ['NVDA', 'GOOGL', 'AAPL', 'MSFT', 'AMZN', 'TSM', 'AVGO', 'META', 'TSLA', 'JPM']
end = date.today() - relativedelta(months=1)
start = end - relativedelta(months=12)

def create_dataframe(idk):
    data = pd.DataFrame(yf.download(idk, start=start, end=end)["Close"])
    return data

dataframe = create_dataframe(companies)
#dataframe.plot()
#plt.show()
print(dataframe)

def calc_momentum(data):
    data = pd.DataFrame(data)
    data.iloc[0] / data.iloc[-1]
    something = 0
    output = pd.DataFrame(something)
    return output

momentum = calc_momentum(dataframe)
print(momentum)