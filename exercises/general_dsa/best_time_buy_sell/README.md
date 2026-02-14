# Exercise 27: Best Time to Buy and Sell Stock

## Meta Interview Pattern
This is a **frequently asked** question at Meta and all major tech companies.
- **Best Time to Buy and Sell Stock** - LeetCode 121
- Single pass problem
- Tests understanding of greedy approach and tracking minimum

## Task
You are given an array `prices` where `prices[i]` is the price of a given stock on the i-th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

## What you'll learn
- Single pass optimization
- Tracking minimum while iterating
- Greedy approach
- Understanding profit calculation

## Instructions
Complete the function in `main.py`:

**max_profit(prices)** - Find maximum profit
- Return maximum profit from single buy-sell
- Track minimum price seen so far
- Calculate potential profit each day

## Examples

```python
>>> max_profit([7, 1, 5, 3, 6, 4])
5  # Buy at 1, sell at 6

>>> max_profit([7, 6, 4, 3, 1])
0  # Prices only go down

>>> max_profit([1, 2])
1  # Buy at 1, sell at 2

>>> max_profit([2, 4, 1])
2  # Buy at 2, sell at 4 (better than buying at 1)
```

## Testing
Run tests with:
```bash
cd exercises/general_dsa/best_time_buy_sell
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test best_time_buy_sell
```

## Hints
If you get stuck, run:
```bash
dsa hint best_time_buy_sell [1|2|3]
```

## Concepts

### Single Pass Approach
```python
min_price = float('inf')
max_profit = 0

for price in prices:
    # Update minimum price seen
    min_price = min(min_price, price)
    # Calculate profit if we sold today
    profit = price - min_price
    # Update maximum profit
    max_profit = max(max_profit, profit)
```

### Key Insight
```python
# For each day, the best profit is:
# (today's price) - (minimum price before today)
# We track the minimum price and calculate profit
```

### Why This Works
```python
# We don't need to know when to buy
# We just need the minimum price seen so far
# Profit = price - min_price_so_far
# Update max_profit at each step
```

### Brute Force (O(n²))
```python
# Check every pair of buy/sell days
# Too slow for large inputs
```

## Time Complexity Analysis
- **Single pass**: O(n) - One iteration through array
- **Brute force**: O(n²) - Check all pairs

## Space Complexity
- **O(1)** - Constant extra space

## Why This Is Important
- Pattern for optimization problems
- Greedy single-pass approach
- Meta frequently asks this exact problem
- Foundation for multi-transaction variations
