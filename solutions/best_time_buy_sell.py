from typing import List


def max_profit(prices: List[int]) -> int:
    """
    Find the maximum profit from buying and selling stock once.

    Args:
        prices: List of stock prices

    Returns:
        Maximum profit achievable (0 if no profit possible)
    """
    if len(prices) < 2:
        return 0
    
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit


def main():
    """Test the max_profit function."""
    test_cases = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],
        [1, 2],
        [2, 4, 1],
        [1, 2, 3, 4, 5],
        [5, 5, 5, 5],
    ]

    print("Best Time to Buy and Sell Stock Tests:")
    print("=" * 60)
    
    for prices in test_cases:
        result = max_profit(prices)
        print(f"\nPrices: {prices}")
        print(f"Max profit: {result}")


if __name__ == "__main__":
    main()
