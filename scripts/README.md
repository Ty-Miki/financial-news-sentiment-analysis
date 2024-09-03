# Utilties used in the project

## 1. `utils.py`

### 1.1 Stock sentiment analysis

- Since there are many stocks in the dataset using a generalized function makes sense to perform the analysis
- The function is `stock_sentiment_analysis(sentiment_data:pd.DataFrame, stock_name:str)`
  - It expects two arguments:
    - ` sentiment_data` - This must pandas dataframe object where the sentiment analysis will be performed.
    - `stock_name` - This must be a string with the stock name that is going to be evaluated
  - The code captures the data where the stock_name is found in the stock column and displays the catagorized sentiment score.

### 1.2 Sentiment date analysis

- This is much similar to the first function except it prints the latest and earliest sentiment dates to evaluate the range covered by the dataset.

## 2. `financial_analyzer.py`

- Includes a class named `FinancialAnalyzer` which is designed for comprehensive financial analysis.
- The class integrates various financial data processing and analysis techniques, including loading stock data, calculating technical indicators, visualizing financial metrics, and performing portfolio optimization.

### Features

The `FinancialAnalyzer` class offers the following functionalities:

1. **Load Stock Data** : Import historical stock data from CSV files.
2. **Technical Indicators** : Calculate key technical indicators such as Simple Moving Average (SMA), Relative Strength Index (RSI), Exponential Moving Average (EMA), and Moving Average Convergence Divergence (MACD).
3. **Data Visualization** : Plot stock prices and technical indicators using interactive charts.
4. **Portfolio Optimization** : Calculate optimal portfolio weights and evaluate portfolio performance using the Sharpe ratio.

### Usage

To use the `FinancialAnalyzer` class:

1. Import the class and necessary libraries.
2. Create an instance of the `FinancialAnalyzer` class.
3. Use the provided methods to load data, calculate technical indicators, visualize data, and optimize portfolios.

### Requirements

* Python 3.x
* Pandas
* yFinance
* TA-Lib
* Plotly
* PyPortfolioOpt
