# Financial Analysis Notebook

## Overview

This Jupyter Notebook provides a comprehensive financial analysis using the  `FinancialAnalyzer` class.

The notebook covers key financial metrics, technical indicators, and portfolio optimization techniques. The analysis is structured as follows:

1. **Data Loading and Understanding**
2. **Technical Indicator Calculations**
3. **Data Visualization**
4. **Portfolio Optimization**

## 1. Data Loading and Understanding

### 1.1 Loading Stock Data

* **Objective:** Load historical stock data for analysis.
* **Steps:**
  * Use the `load_stock_data(ticker)` method from the `FinancialAnalyzer` class to load historical stock data from a CSV file.

### 1.2 Data Inspection**Objective:** Understand the structure of the loaded data.

* **Steps:**
  * Inspect the first few rows and summarize the dataset to identify key features such as 'Open', 'Close', 'Volume', etc.

## 2. Technical Indicator Calculations

### 2.1 Simple Moving Average (SMA)

* **Objective:** Calculate the Simple Moving Average (SMA) to smooth out price data.
* **Steps:**
  * Use the `calculate_moving_average(data, window_size)` method to calculate the SMA.

### 2.2 Additional Technical Indicators

* **Objective:** Calculate various technical indicators to analyze stock performance.
* **Steps:**
  * Use the `calculate_technical_indicators(data)` method to calculate indicators such as SMA, RSI, EMA, and MACD.

## 3. Data Visualization

### 3.1 Plotting Stock Data with SMA

* **Objective:** Visualize stock prices alongside the Simple Moving Average.
* **Steps:**
  * Use the `plot_stock_data(data)` method to create an interactive line plot.

### 3.2 Plotting RSI, EMA, and MACD

* **Objective:** Visualize additional technical indicators.
* **Steps:**
  * Use the `plot_rsi(data)`, `plot_ema(data)`, and `plot_macd(data)` methods to create interactive plots.

## 4. Portfolio Optimization

### 4.1 Calculating Optimal Portfolio Weights

* **Objective:** Determine the optimal asset allocation for a portfolio.
* **Steps:**
  * Use the `calculate_portfolio_weights(tickers, start_date, end_date)` method to calculate the weights that maximize the Sharpe ratio.

### 4.2 Portfolio Performance Analysis

* **Objective:** Evaluate the performance of the optimized portfolio.
* **Steps:**
  * Use the `calculate_portfolio_performance(tickers, start_date, end_date)` method to calculate the portfolio's return, volatility, and Sharpe ratio.

## Requirements

* Python 3.x
* Jupyter Notebook
* Pandas
* yFinance
* TA-Lib
* Plotly
* PyPortfolioOpt

## How to Run the Notebook

1. Ensure all required libraries are installed. Use `pip install -r requirements.txt` if a `requirements.txt` file is provided.
2. Open the Jupyter Notebook.
3. Run each cell sequentially to perform the analysis.
