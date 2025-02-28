# Time-Series-Forecasting-for-Portfolio-Management-Optimization

## Project Overview

This project is part of a challenge for 10 Academy's Artificial Intelligence Mastery program aimed at optimizing portfolio management strategies for Guide Me in Finance (GMF) Investments. The objective is to extract, clean, and analyze historical financial data to improve investment decision-making. By leveraging time series forecasting techniques, GMF seeks to enhance portfolio performance, reduce risk, and identify market opportunities.

## Business Objective

GMF Investments is a financial advisory firm specializing in personalized portfolio management through data-driven insights. By accurately analyzing market trends, GMF aims to:

- Optimize asset allocation

- Minimize risk exposure

- Maximize portfolio returns for its clients

Financial analysts at GMF utilize historical and real-time data to extract valuable insights on high-risk stocks, stable bonds, and diversified index funds.


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

│── src/

│── tests/

│── .gitignore

│── README.md

└── requirements.txt

## Features
✅ Data Extraction: Pulling historical financial data using the yFinance Python library for:

- TSLA: High volatility and potential high returns

- BND: Stability and low risk

- SPY: Diversified, moderate-risk market exposure

🔍 Data Cleaning & Understanding:

- Checking basic statistics to understand data distribution

- Ensuring appropriate data types and handling missing values (filling, interpolating, or removing)

- Normalizing or scaling data if required

📊 Exploratory Data Analysis (EDA):

- Visualizing closing prices over time to identify trends

- Calculating and plotting daily percentage changes to observe volatility

- Analyzing short-term trends and fluctuations using rolling means and standard deviations

- Detecting outliers and identifying anomalies in returns

📆 Seasonality & Trends Analysis:

- Decomposing the time series into trend, seasonal, and residual components using statistical models

- Assessing fluctuations in daily returns and their impact

- Measuring risk-adjusted returns using VaR (Value at Risk) and the Sharpe Ratio


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

To improve tracking of changes, ensure commits are frequent and meaningful. Each commit should include a clear message describing what was changed and why.

We welcome contributions to enhance the project. To contribute, please follow these steps:

1. Fork the repository: Create a personal copy of the repository on GitHub.

2. Create a new branch: Develop your feature or fix in a separate branch.

3. Commit your changes: Ensure your commits are clear and descriptive.

4. Push to your fork: Upload your changes to your GitHub repository.

5. Create a Pull Request: Submit a PR to the main repository for review.