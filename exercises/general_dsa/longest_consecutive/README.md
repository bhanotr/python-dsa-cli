# Exercise 25: Longest Consecutive Sequence

## Meta Interview Pattern
This is a **frequently asked** question at Meta and all major tech companies.
- **Longest Consecutive Sequence** - LeetCode 128
- Hash set problem
- Tests understanding of set operations and efficient algorithms

## Task
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

## What you'll learn
- Hash set for O(1) lookups
- Efficient sequence detection
- Avoiding redundant work
- O(n) vs O(n log n) trade-offs

## Instructions
Complete the function in `main.py`:

**longest_consecutive(nums)** - Find longest consecutive sequence
- Return length of longest consecutive sequence
- Use hash set for O(n) time
- Only start counting from sequence beginnings

## Examples

```python
>>> longest_consecutive([100, 4, 200, 1, 3, 2])
4  # [1, 2, 3, 4]

>>> longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
9  # [0, 1, 2, 3, 4, 5, 6, 7, 8]

>>> longest_consecutive([])
0

>>> longest_consecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6])
7  # [-1, 0, 1, 2, 3, 4, 5, 6]
```

## Testing
Run tests with:
```bash
cd exercises/general_dsa/longest_consecutive
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test longest_consecutive
```

## Hints
If you get stuck, run:
```bash
dsa hint longest_consecutive [1|2|3]
```

## Concepts

### Hash Set Approach
```python
num_set = set(nums)  # O(n) to create set

for num in num_set:
    # Only start counting if num is the start of a sequence
    if num - 1 not in num_set:
        # Count consecutive numbers
        current_num = num
        current_streak = 1
        while current_num + 1 in num_set:
            current_num += 1
            current_streak += 1
        longest = max(longest, current_streak)
```

### Why Check `num - 1`?
```python
# This ensures we only count each sequence once
# [1, 2, 3, 4] - only start from 1
# If num = 2, num - 1 = 1 IS in set, so skip
# If num = 1, num - 1 = 0 NOT in set, so start counting
```

### Sorting Approach (Slower)
```python
nums.sort()
# Then count consecutive in sorted array
# O(n log n) time, not acceptable for this problem
```

## Time Complexity Analysis
- **Hash set**: O(n) - Each number visited at most twice
- **Sorting**: O(n log n) - Not acceptable

## Space Complexity
- **Hash set**: O(n) - Store all numbers in set

## Why This Is Important
- Pattern for sequence problems
- Understanding O(n) vs O(n log n)
- Meta frequently asks this exact problem
- Hash set optimization techniques
