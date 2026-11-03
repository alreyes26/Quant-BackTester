import pytest 
from quant_backtester.metrics.return_calculator import calculate_return


def test_positive_return():
    current_price = 105.0
    previous_price = 100.0
    expected_return = 0.05 # (105 - 100) / 100
    assert calculate_return(current_price, previous_price) == expected_return

def test_negative_return():
    current_price = 90.0
    previous_price = 100.0
    expected_return = -0.10 # (90 - 100) / 100
    assert calculate_return(current_price, previous_price) == expected_return

def test_zero_return():
    current_price = 100.0
    previous_price = 100.0
    expected_return = 0.0 # (100 - 100) / 100
    assert calculate_return(current_price, previous_price) == expected_return

    