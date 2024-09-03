"""Utilities used for the data analysis"""
import pandas as pd

def stock_sentiment_analysis(sentiment_data:pd.DataFrame, stock_name:str) -> None:
    """
    - Count the number of headline that fall into each sentiment category
    - Expects the sentiment data to have a stock and sentiment_category columns
    """
    stock_data = sentiment_data[sentiment_data['stock'] == stock_name]

    if not stock_data.empty:  # Check if the stock_data DataFrame is not empty
        print(stock_data['sentiment_category'].value_counts())
    else:
        print(f"No sentiment data found for stock: {stock_name}")

def inspect_sentiment_dates(sentiment_data: pd.DataFrame, stock_name:str) -> None:
    """
    - prints the latest and earlies dates of the sentiment data
    """
    stock_data = sentiment_data[sentiment_data['stock'] == stock_name]
    
    if not stock_data.empty:  # Check if the stock_data DataFrame is not empty
        print(f'Earliest Date: {stock_data["date"].min()}')
        print(f'Latest Date: {stock_data["date"].max()}')
    else:
        print(f"No sentiment data found for stock: {stock_name}")