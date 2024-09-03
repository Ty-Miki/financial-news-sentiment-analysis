import pytest
import pandas as pd
from scripts.financial_analyzer import FinancialAnalyzer  # Ensure this import points to the correct location of your class

# Sample data for testing
@pytest.fixture
def sample_data():
    data = {
        'Date': pd.date_range(start='2023-01-01', periods=5, freq='D'),
        'Close': [150, 152, 154, 153, 155],
        'Open': [148, 151, 153, 152, 154],
        'Volume': [1000, 1100, 1050, 1020, 1080],
    }
    return pd.DataFrame(data)

# Test for loading stock data
def test_load_stock_data(mocker, sample_data):
    mocker.patch('pandas.read_csv', return_value=sample_data)
    analyzer = FinancialAnalyzer()
    data = analyzer.load_stock_data('AAPL')
    assert isinstance(data, pd.DataFrame)
    assert not data.empty

# Test for calculating moving average
def test_calculate_moving_average(sample_data):
    analyzer = FinancialAnalyzer()
    sma = analyzer.calculate_moving_average(sample_data['Close'], 3)
    assert isinstance(sma, pd.Series)
    assert len(sma) == len(sample_data)

# Test for calculating technical indicators
def test_calculate_technical_indicators(sample_data):
    analyzer = FinancialAnalyzer()
    data_with_indicators = analyzer.calculate_technical_indicators(sample_data)
    assert 'SMA' in data_with_indicators.columns
    assert 'RSI' in data_with_indicators.columns
    assert 'EMA' in data_with_indicators.columns
    assert 'MACD' in data_with_indicators.columns
    assert 'MACD_Signal' in data_with_indicators.columns
