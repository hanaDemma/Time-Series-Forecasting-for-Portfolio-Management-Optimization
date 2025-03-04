# Time-Series-Forecasting-for-Portfolio-Management-Optimization

## Project Overview

This project leverages time series forecasting to enhance portfolio management strategies for Guide Me in Finance (GMF) Investments. By predicting future market trends, we aim to optimize asset allocation, balancing risk and returns effectively.

## Business Objective

GMF Investments is a financial advisory firm specializing in personalized portfolio management through advanced time series forecasting models. By accurately predicting market trends, GMF aims to:

- Optimize asset allocation for better returns.
- Minimize risk exposure by balancing volatile and stable assets.
- Maximize portfolio performance through data-driven investment decisions.
 
GMF’s financial analysts use real-time market data and predictive insights to make informed recommendations, with a focus on high-growth stocks, bonds for stability, and diversified index funds.

## Folder Structure 
TIME-SERIES-FORECASTING-FOR-PORTFOLIO-MANAGEMENT-OPTIMIZATION/

│── .github/

│── week11/

│── notebooks/

│   │── portfolioManagement.ipynb

│   └── README.md

│── scripts/

│   │── data_cleaning.py

│   │── data_loader.py

│   │── plots.py

│   │── features.py

│── src/

│── tests/

│── .gitignore

│── README.md

└── requirements.txt

## Features

✅  **Data Extraction**: Fetching historical financial data using the YFinance.
📊  **Exploratory Data Analysis (EDA)**: Analyzing trends, seasonality, volatility, and other key indicators.
📆  **Time Series Forecasting Models**: Implementing ARIMA, SARIMA, and LSTM models to predict market trends.
📈  **Portfolio Optimization**: Using forecasted data to rebalance asset allocations and maximize returns.

## Data

Historical data was collected for three primary assets:
1. **Tesla, Inc. (TSLA)** - High-growth stock with potential for high returns but significant volatility.
2. **Vanguard Total Bond Market ETF (BND)** - A bond ETF providing stability and income.
3. **S&P 500 ETF (SPY)** - An index fund representing the U.S. market for diversification.

## Technologies Used

The project uses Python Libraries
yfinance

- numpy

- pandas

- statsmodels

- pmdarima

- matplotlib

- seaborn

- scikit-learn


## Installation


1️⃣ Clone the repository
To set up the project on your local machine, follow these steps:


1. Clone the repository:
   ```bash
   https://github.com/hanaDemma/Time-Series-Forecasting-for-Portfolio-Management-Optimization
2. Navigate into the project directory:
   ```bash
   cd Change_point_analysis_and_statistical_modelling

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt


## Contributing

We welcome contributions to enhance the project. To contribute, please follow these steps:

1. **Fork the repository**: Create a personal copy of the repository on GitHub.

2. **Create a new branch**: Develop your feature or fix in a separate branch.

3. **Commit your changes**: Ensure your commits are clear and descriptive.

4. **Push to your fork**: Upload your changes to your GitHub repository.

5. **Create a Pull Request**: Submit a PR to the main repository for review.