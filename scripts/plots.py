import pandas as pd  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import seaborn as sns  # type: ignore
import matplotlib.pyplot as plt
from scipy.stats import zscore
import seaborn as sns
import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose # type: ignore


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


    
def timeSeriesDecomposition(stockData,tickers):
    # Time Series Decomposition
    for data, ticker in zip(stockData,tickers):
        decomposition = seasonal_decompose(data['Close'], model='additive', period=252)
        plt.figure(figsize=(12,6))
        decomposition.plot()
        plt.suptitle(f'{ticker} Time Series Decomposition')
        plt.xlim(pd.Timestamp("2015-01-01"), pd.Timestamp("2025-01-31"))
        plt.show()



def volatility_rolling(window_size,stockData,tickers):
    # Analyze volatility for each asset
    for data, ticker in zip(stockData,tickers):
        # Calculate the rolling mean and standard deviation for the adjusted close price
        rolling_mean = data['Adj Close'].rolling(window=window_size).mean()
        rolling_std = data['Adj Close'].rolling(window=window_size).std()

        # Plot the adjusted close price along with rolling mean and rolling standard deviation
        plt.figure(figsize=(12, 8))

        # Plot the adjusted close price
        plt.subplot(311)
        plt.plot(data['Adj Close'], label=f'{ticker} Adjusted Close', color='black')
        plt.title(f'{ticker} - Adjusted Close Price')
        plt.legend()

        # Plot the rolling mean
        plt.subplot(312)
        plt.plot(rolling_mean, label=f'{ticker} {window_size}-Day Rolling Mean', color='blue')
        plt.title(f'{ticker} - {window_size}-Day Rolling Mean')
        plt.legend()

        # Plot the rolling standard deviation
        plt.subplot(313)
        plt.plot(rolling_std, label=f'{ticker} {window_size}-Day Rolling Std Dev', color='red')
        plt.title(f'{ticker} - {window_size}-Day Rolling Std Dev (Volatility)')
        plt.legend()

        plt.tight_layout()
        plt.show()



def varAndSharpeRatio(stockData, tickers):
    VaRs = {}  # Store VaR values
    Sharpe_ratios = {}  # Store Sharpe Ratios

    for data, ticker in zip(stockData, tickers):
        if 'Daily_Return' not in data.columns:
            print(f"Skipping {ticker}: 'Daily_Return' column not found.")
            continue
        
        # ✅ Calculate VaR (5th percentile)
        VaR = data['Daily_Return'].quantile(0.05)
        VaRs[ticker] = VaR
        
        # ✅ Calculate Sharpe Ratio
        mean_return = data['Daily_Return'].mean()
        std_dev_return = data['Daily_Return'].std()
        sharpe_ratio = mean_return / std_dev_return * np.sqrt(252)  # 252 trading days
        Sharpe_ratios[ticker] = sharpe_ratio

    # ✅ Create VaR Bar Chart
    plt.figure(figsize=(8, 6))
    plt.bar(VaRs.keys(), VaRs.values(), color='red')
    plt.xlabel('Ticker')
    plt.ylabel('VaR (Lower is Riskier)')
    plt.title('Value at Risk (VaR) at 5% Confidence Level')
    plt.grid(axis='y')
    plt.show()

    # ✅ Create Sharpe Ratio Bar Chart
    plt.figure(figsize=(8, 6))
    plt.bar(Sharpe_ratios.keys(), Sharpe_ratios.values(), color='purple')
    plt.xlabel('Ticker')
    plt.ylabel('Sharpe Ratio (Higher is Better)')
    plt.title('Sharpe Ratios of Stocks')
    plt.grid(axis='y')
    plt.show()

    # ✅ Print Values
    print("\nValue at Risk (VaR) at 5% Confidence Level:")
    for ticker, value in VaRs.items():
        print(f"{ticker}: {value:.4f}")
    
    print("\nSharpe Ratios:")
    for ticker, value in Sharpe_ratios.items():
        print(f"{ticker}: {value:.4f}")
