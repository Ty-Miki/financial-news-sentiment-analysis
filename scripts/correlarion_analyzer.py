import pandas as pd
from textblob import TextBlob

class CorrelationAnalyzer():

    def __init__(self) -> None:
        pass

    def load_headline_data(self, parent_dir: str, ticker: str) -> pd.DataFrame:
        """Load the headline data and filter for a specific ticker"""

        file_path = f'{parent_dir}/notebooks/data/raw_analyst_ratings.csv'
        df = pd.read_csv(file_path)

        headline_data = df[['date', 'headline']][df['stock'] == ticker]

        return headline_data

    def add_sentiment_score(self, headline_data: pd.DataFrame) -> pd.DataFrame:
        """Add sentiment scores for a headline data"""
        
        headline_data['sentiment'] = headline_data['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)

        return headline_data
    
    def load_stock_data(self, parent_directory: str, ticker: str) -> pd.DataFrame:
        """Load the stock data and filter the Close column"""
        
        file_path = f'{parent_directory}/notebooks/data/yfinance_data/{ticker}_historical_data.csv'
        df = pd.read_csv(file_path)

        stock_data = df.rename(columns={'Date': 'date'})[['date', 'Close']]
        
        return stock_data
    
    def add_daily_returns(self, stock_data:pd.DataFrame) -> pd.DataFrame:
        """Add daily returns based on stock data close prices"""

        stock_data['Daily Returns'] = stock_data['Close'].pct_change()

        return stock_data

    def merge_stock_data(self, headline_data: pd.DataFrame, stock_data: pd.DataFrame) -> pd.DataFrame:
        """Merge the headline data and stock data based on date"""

        merged_data = pd.merge(headline_data, stock_data, on='date', how='inner')
        return merged_data
    
    def calc_correlation(self, merged_data: pd.DataFrame, col1: str, col2: str) -> float | None:
        """Calculate correlation of two columns"""
        if not merged_data.empty: 
            correlation = merged_data[col1].corr(merged_data[col2])
            return correlation
        print("No correlation can be calculated between these two datasets")
        return None
    
