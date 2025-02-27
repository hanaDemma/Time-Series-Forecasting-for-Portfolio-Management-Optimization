import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
import numpy as np # type: ignore
import yfinance as yf # type: ignore
from statsmodels.tsa.seasonal import seasonal_decompose # type: ignore
import math
from matplotlib.dates import DateFormatter
import scipy.optimize as sco
from scipy.stats import norm

def loadData():
    tickers = ["TSLA", "BND", "SPY"]
    start_date = "2015-01-01"
    end_date = "2025-01-31"
    data_frames = {}

    for ticker in tickers:
        data = yf.download(ticker, start=start_date, end=end_date)

        # If 'Adj Close' is missing, assume it's the same as 'Close'
        if 'Adj Close' not in data.columns:
            data['Adj Close'] = data['Close']

        # Ensure column order
        data = data[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
        
        data_frames[ticker] = data

    return data_frames["TSLA"], data_frames["BND"], data_frames["SPY"]

