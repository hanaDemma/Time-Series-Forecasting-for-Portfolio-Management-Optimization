import pandas as pd  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import seaborn as sns  # type: ignore

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def closePriceOverTime(stockData, tickers):
    """
    Plots Adjusted Close Price trends for each stock in a separate figure, ensuring x-axis covers 2015-2025.
    
    Parameters:
        stockData (list of DataFrames): List of stock price DataFrames (each with 'Date' and 'Adj Close' columns).
        tickers (list of str): Corresponding stock ticker symbols.
    """
    sns.set_style("whitegrid")

    for data, ticker in zip(stockData, tickers):
        plt.figure(figsize=(12, 6))

        # Ensure Date is a column, not an index
        if isinstance(data.index, pd.DatetimeIndex):
            data = data.reset_index()

        plt.plot(data['Date'], data['Adj Close'], label=ticker, linewidth=2)

        plt.title(f"Adjusted Close Prices for {ticker}", fontsize=14)
        plt.xlabel("Date", fontsize=12)
        plt.ylabel("Adjusted Close Price", fontsize=12)
        plt.legend(title="Ticker")
        plt.xticks(rotation=45)

        # Force x-axis range from 2015 to 2025
        plt.xlim(pd.Timestamp("2015-01-01"), pd.Timestamp("2025-01-31"))

        plt.show()



def dailyReturn(stockData,tickers):
    # Calculate daily percentage change for volatility analysis
    for data, ticker in zip(stockData, tickers):
        data['Daily_Return'] = data['Close'].pct_change()
        data['Daily_Return'].fillna(0, inplace=True)
        
        # Plot daily returns
        plt.figure(figsize=(12, 6))
        plt.plot(data['Date'], data['Daily_Return'], label=f'{ticker} Daily Returns')
        plt.title(f'{ticker} Daily Returns Over Time')
        plt.xlabel('Date')
        plt.ylabel('Daily Return')
        plt.legend()
        plt.xlim(pd.Timestamp("2015-01-01"), pd.Timestamp("2025-01-31"))
        plt.show()