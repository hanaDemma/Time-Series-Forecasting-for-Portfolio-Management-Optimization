import pandas as pd  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import seaborn as sns  # type: ignore

def closePriceOverTime(stockData, tickers):
    """
    Plots Adjusted Close Price trends for each stock in a separate figure.
    
    Parameters:
        stockData (list of DataFrames): List of stock price DataFrames (each with 'Date' and 'Adj Close' columns).
        tickers (list of str): Corresponding stock ticker symbols.
    """
    sns.set_style("whitegrid")

    for data, ticker in zip(stockData, tickers):
        plt.figure(figsize=(12, 6))
        plt.plot(data['Date'], data['Adj Close'], label=ticker, linewidth=2)
        plt.title(f"Adjusted Close Prices for {ticker}", fontsize=14)
        plt.xlabel("Date", fontsize=12)
        plt.ylabel("Close Price", fontsize=12)
        plt.legend(title="Ticker")
        plt.xticks(rotation=45)
        plt.show()
