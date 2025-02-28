import pandas as pd  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import seaborn as sns  # type: ignore
import matplotlib.pyplot as plt
from scipy.stats import zscore
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



def rollingAvgAndStd(stockData,tickers):
    # Calculate rolling averages and standard deviations
    for data, ticker in zip(stockData,tickers):
        data['Rolling_Mean'] = data['Close'].rolling(window=30).mean()
        data['Rolling_Std'] = data['Close'].rolling(window=30).std()
        data['Rolling_Mean'].fillna(0, inplace=True) 
        data['Rolling_Std'].fillna(0, inplace=True)
        
        # Plot rolling mean and std
        plt.figure(figsize=(12, 6))
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Rolling_Mean'], label='30-Day Rolling Mean')
        plt.plot(data['Date'], data['Rolling_Std'], label='30-Day Rolling Std', linestyle='--')
        plt.title(f'{ticker} Volatility with Rolling Mean & Standard Deviation')
        plt.xlabel('Date')
        plt.ylabel('Price / Volatility')
        plt.legend()
        plt.xlim(pd.Timestamp("2015-01-01"), pd.Timestamp("2025-01-31"))
        plt.show()


def detect_outliers(stockData, tickers):
    """
    Detects and plots outliers in Adjusted Close Price for each stock using Z-score.

    Parameters:
        stockData (list of DataFrames): List of stock price DataFrames (each with 'Date' and 'Adj Close' columns).
        tickers (list of str): Corresponding stock ticker symbols.
    """
    for data, ticker in zip(stockData, tickers):
        data = data.copy()  # Avoid modifying the original DataFrame
        
        # Ensure Date column exists and is set as index
        if 'Date' in data.columns:
            data['Date'] = pd.to_datetime(data['Date'])  # Convert to datetime if not already
            data = data.set_index('Date')

        # Compute Z-score
        data['Z-Score'] = (data['Adj Close'] - data['Adj Close'].mean()) / data['Adj Close'].std()
        outliers = data[data['Z-Score'].abs() > 3]  # Outliers: Z-score > 3 or < -3

        # Plot Adjusted Close Price with outliers
        plt.figure(figsize=(12, 6))
        plt.plot(data.index, data['Adj Close'], label=f'{ticker} Adjusted Close Price', color='blue', linewidth=1.5)
        plt.scatter(outliers.index, outliers['Adj Close'], color='red', label='Outliers', zorder=5)
        plt.title(f'{ticker} Outliers in Adjusted Close Price', fontsize=14)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Adjusted Close Price', fontsize=12)
        plt.legend()
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()

        # Print Outliers DataFrame in requested format
        print(f"\nOutliers for {ticker}:")
        if outliers.empty:
            print("Empty DataFrame\nColumns: [Price, Adj Close, Z-Score]\nIndex: []")
        else:
            formatted_outliers = outliers[['Adj Close', 'Z-Score']].copy()
            formatted_outliers.index.name = "Date"
            formatted_outliers.columns = ["Price", "Z-Score"]
            formatted_outliers["Ticker"] = ticker
            print(formatted_outliers)



import numpy as np
import pandas as pd

def remove_outliers(stockData, tickers, threshold=3):
    """
    Detects and removes outliers in Adjusted Close Price using Z-score.

    Parameters:
        stockData (list of DataFrames): List of stock price DataFrames (each with 'Date' and 'Adj Close' columns).
        tickers (list of str): Corresponding stock ticker symbols.
        threshold (float): Z-score threshold for defining outliers (default is 3).

    Returns:
        list of DataFrames: Cleaned DataFrames with outliers removed.
    """
    cleaned_data = []

    for data, ticker in zip(stockData, tickers):
        data = data.copy()  # Avoid modifying the original DataFrame
        
        # Ensure 'Date' is set as index
        if 'Date' in data.columns:
            data['Date'] = pd.to_datetime(data['Date'])
            data = data.set_index('Date')

        # Compute Z-score
        data['Z-Score'] = (data['Adj Close'] - data['Adj Close'].mean()) / data['Adj Close'].std()

        # Identify outliers
        outliers = data[np.abs(data['Z-Score']) > threshold]

        # Remove outliers
        data_cleaned = data[np.abs(data['Z-Score']) <= threshold].drop(columns=['Z-Score'])

        # Store cleaned data
        cleaned_data.append(data_cleaned)

        # Print removed outliers
        print(f"\nRemoved Outliers for {ticker}:")
        if outliers.empty:
            print("No outliers found.")
        else:
            print(outliers[['Adj Close', 'Z-Score']])

    return cleaned_data



def calc_daily_return(stockData,tickers):
    for data, ticker in zip(stockData, tickers):
        data['Daily Return'] = data['Adj Close'].pct_change() * 100 
        data.dropna(inplace=True)

def plot_daily_percentage(stockData, tickers):
    for data, ticker in zip(stockData, tickers):
        plt.figure(figsize=(10, 6))
        plt.plot(data.index, data['Daily Return'], label=f'{ticker} Daily Returns')
        
        plt.title(f'{ticker} Daily Percentage Change')
        plt.xlabel('Date')
        plt.ylabel('Daily Return (%)')
        plt.legend()
        plt.grid(True)

        # Format the x-axis to show readable dates
        plt.xticks(rotation=45)  # Rotate labels for better readability
        plt.show()


def plot_significant_anomalies(stockData,tickers):
    threshold = 5  # 5% threshold for high/low returns

    for data, ticker in zip(stockData, tickers):
        high_returns = data[data['Daily Return'] > threshold]
        low_returns = data[data['Daily Return'] < -threshold]

        # Plot high and low returns
        plt.figure(figsize=(10, 6))
        plt.plot(data['Daily Return'],  label=f'{ticker} Daily Returns')
        plt.scatter(high_returns.index, high_returns['Daily Return'], color='green', label='High Returns', zorder=5)
        plt.scatter(low_returns.index, low_returns['Daily Return'], color='red', label='Low Returns', zorder=5)
        plt.title(f'{ticker}Days with Unusually High/Low Returns')
        plt.xlabel('Date')
        plt.ylabel('Daily Return (%)')
        plt.legend()
        plt.grid(True)
        plt.show()

        print(f"{ticker}High Returns for:")
        print(high_returns[['Daily Return']])
        print("\n")
        
        print(f"{ticker}Low Returns for:")
        print(low_returns[['Daily Return']])
        print("\n")