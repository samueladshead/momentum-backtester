<a id="readme-top"></a>
# Momentum Backtester

![Python](https://img.shields.io/badge/python->3.14-blue)
![numpy](https://img.shields.io/badge/numpy-2.5.2-green)
![pandas](https://img.shields.io/badge/pandas-3.05-green)
![yfinance](https://img.shields.io/badge/yfinance-1.4.1-green)
![dateutil](https://img.shields.io/badge/dateutil-2.9.0-green)
![Matplotlib](https://img.shields.io/badge/matplotlib-3.11.1-green)

In this project, I used Python to use historical data from Yahoo Finance to simulate a stock portfolio over a user-defined period.

## Overview
This project is a momemntum backtester built from scratch, which analyses
data outputted from Yahoo Finance, ranks the top n stocks over a period of time
and simulates a real portfolio over a given period. The code is the able to
compare the perfomance of the model against the SPY reference stock.

## Prerequisites
- Python (3.14 or higher)
- Required packages: `numpy`, `pandas`, `yfinance`, `matplotlib`, `dateutil`

## Main features
- Show **historic data** for user-defined stocks
- **Simulate** the portfolio using the top 3 stocks with the highest momentum for each month with a user-defined portfolio starting value
- Calculate various parameters of the simulation, including **Annual Return**, **Monthly Returns**, **Sharpe Ratio** and the **Maximum Drawdown**

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/momentum-backtester.git
   cd momentum-backtester
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
```bash
pip install -r requirements.txt
python main.py
```
*Note: To access various feaurues of the code, uncomment individual sections at the end of the code.
