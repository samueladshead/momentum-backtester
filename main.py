import pandas as pd
import yfinance as yf
import numpy as np
from datetime import date
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt

companies = ['NVDA', 'GOOGL', 'AAPL', 'MSFT', 'AMZN', 'TSM', 'AVGO', 'META', 'TSLA', 'JPM']

def createdataframe(idk):
    end = date.today() - relativedelta(months=1)
    start = end - relativedelta(months=12)
    data = pd.DataFrame(yf.download(idk, start=start, end=end)["Close"])
    return data

dataframe = createdataframe(companies)
dataframe.plot()
plt.show()
print(dataframe)
print("Wow!")