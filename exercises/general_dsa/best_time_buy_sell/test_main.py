import pytest
from main import max_profit


class TestMaxProfit:
    """Test suite for max_profit function."""
    
    def test_basic_example(self):
        """Test basic example from LeetCode."""
        assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    
    def test_no_profit_possible(self):
        """Test when prices only go down."""
        assert max_profit([7, 6, 4, 3, 1]) == 0
    
    def test_two_elements(self):
        """Test with two elements."""
        assert max_profit([1, 2]) == 1
    
    def test_buy_low_sell_high(self):
        """Test obvious buy low sell high."""
        assert max_profit([2, 4, 1]) == 2
    
    def test_increasing_prices(self):
        """Test with increasing prices."""
        assert max_profit([1, 2, 3, 4, 5]) == 4
    
    def test_constant_prices(self):
        """Test with constant prices."""
        assert max_profit([5, 5, 5, 5]) == 0
    
    def test_single_day(self):
        """Test with single price."""
        assert max_profit([5]) == 0
    
    def test_large_profit(self):
        """Test with large profit."""
        assert max_profit([1, 100, 50, 100]) == 99
    
    def test_multiple_dips(self):
        """Test with multiple dips."""
        assert max_profit([3, 2, 6, 5, 0, 3]) == 4
    
    def test_negative_prices(self):
        """Test with negative prices (edge case)."""
        assert max_profit([-5, -3, -1]) == 4


class TestMaxProfitVerification:
    """Tests that verify the solution is correct."""
    
    def test_verification_buy_before_sell(self):
        """Verify that buy day is before sell day."""
        test_cases = [
            [7, 1, 5, 3, 6, 4],
            [2, 4, 1],
            [1, 2, 3, 4, 5],
        ]
        
        for prices in test_cases:
            profit = max_profit(prices)
            
            if profit > 0:
                found = False
                for buy in range(len(prices) - 1):
                    for sell in range(buy + 1, len(prices)):
                        if prices[sell] - prices[buy] == profit:
                            found = True
                            break
                    if found:
                        break
                assert found, f"Could not find buy/sell pair for profit {profit}"
    
    def test_verification_maximum(self):
        """Verify that result is indeed maximum profit."""
        test_cases = [
            [7, 1, 5, 3, 6, 4],
            [3, 2, 6, 5, 0, 3],
            [1, 2, 3, 4, 5],
        ]
        
        for prices in test_cases:
            result = max_profit(prices)
            max_possible = 0
            for buy in range(len(prices) - 1):
                for sell in range(buy + 1, len(prices)):
                    max_possible = max(max_possible, prices[sell] - prices[buy])
            assert result == max_possible


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "Best Time to Buy and Sell Stock - DSA Exercises",
    ]
