import pytest
import pandas as pd
from scripts import utils

# Sample data for testing
@pytest.fixture
def sentiment_data():
    data = {
        'stock': ['AAPL', 'AAPL', 'GOOG', 'AAPL', 'GOOG'],
        'sentiment_category': ['positive', 'negative', 'positive', 'neutral', 'neutral'],
        'date': ['2023-09-01', '2023-09-02', '2023-09-01', '2023-09-03', '2023-09-02']
    }
    return pd.DataFrame(data)


def test_inspect_sentiment_dates(sentiment_data, mocker):
    mock_print = mocker.patch("builtins.print")

    utils.inspect_sentiment_dates(sentiment_data, 'AAPL')
    
    # Expected output (print calls)
    expected_calls = [
        mocker.call('Earliest Date: 2023-09-01'),
        mocker.call('Latest Date: 2023-09-03')
    ]
    
    mock_print.assert_has_calls(expected_calls)
