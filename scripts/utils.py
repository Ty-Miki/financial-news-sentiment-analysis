"""Utilities used for the data analysis"""
import pandas as pd

def stock_sentiment_analysis(sentiment_data:pd.DataFrame, stock_name:str) -> None:
    """
    - Count the number of headline that fall into each sentiment category
    - Expects the sentiment data to have a stock and sentiment_category columns
    """
    stock_data = sentiment_data[sentiment_data['stock'] == stock_name]
    print(stock_data['sentiment_category'].value_counts())

def inspect_sentiment_dates(sentiment_data: pd.DataFrame, stock_name:str) -> None:
    """
    - prints the latest and earlies dates of the sentiment data
    """
    stock_data = sentiment_data[sentiment_data['stock'] == stock_name]
    print(f'Earliest Date: {stock_data['date'].min()}')
    print(f'Latest Date: {stock_data['date'].max()}')