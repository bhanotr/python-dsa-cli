# Exercise 28: Maximum Subarray

## Meta Interview Pattern
This is a **frequently asked** question at Meta and all major tech companies.
- **Maximum Subarray** - LeetCode 53
- Dynamic programming/Kadane's algorithm problem
- Tests understanding of optimal substructure

## Task
Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

## What you'll learn
- Kadane's algorithm
- Dynamic programming intuition
- Local vs global maximum
- Single pass optimization

## Instructions
Complete the function in `main.py`:

**max_subarray(nums)** - Find maximum subarray sum
- Return sum of subarray with largest sum
- Use Kadane's algorithm
- Track local and global maxima

## Examples

```python
>>> max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
6  # Subarray [4, -1, 2, 1]

>>> max_subarray([1])
1

>>> max_subarray([5, 4, -1, 7, 8])
23  # Subarray [5, 4, -1, 7, 8]

>>> max_subarray([-1, -2, -3])
-1  # Single element -1 is best
```

## Testing
Run tests with:
```bash
cd exercises/general_dsa/maximum_subarray
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test maximum_subarray
```

## Hints
If you get stuck, run:
```bash
dsa hint maximum_subarray [1|2|3]
```

## Concepts

### Kadane's Algorithm
```python
current_sum = 0
best_sum = float('-inf')

for num in nums:
    # Either extend current subarray or start new
    current_sum = max(num, current_sum + num)
    # Update best sum seen so far
    best_sum = max(best_sum, current_sum)
```

### Local vs Global Maximum
```python
# current_sum = maximum sum of subarray ending at current position
# best_sum = maximum sum of any subarray seen so far
# At each step, decide: extend or restart?
```

### Key Insight
```python
# If current_sum is negative, starting fresh is better
# If current_sum is positive, extending might be better
# Example: [-2, 1, -3, 4]
# -2: current=-2, best=-2 (restart)
# 1: current=1, best=1 (restart because -2 < 0)
# -3: current=-2, best=1 (extend: 1 + (-3) = -2)
# 4: current=4, best=4 (restart because -2 < 0)
```

### All Negative Numbers
```python
# Algorithm still works!
# [-1, -2, -3]
# current will jump to -1, -2, -3
# best will be -1 (least negative)
```

## Time Complexity Analysis
- **Kadane's algorithm**: O(n) - Single pass through array

## Space Complexity
- **O(1)** - Constant extra space

## Why This Is Important
- Kadane's algorithm is classic
- Pattern for optimization problems
- Dynamic programming intuition
- Meta frequently asks this exact problem
- Foundation for maximum subarray variations
