# Exercise 20: Top K Frequent Elements

## Meta Interview Pattern
This is a **frequently asked** question at Meta and all major tech companies.
- **Top K Frequent Elements** - LeetCode 347
- Hash map + sorting/heap problem
- Tests understanding of counting and ranking

## Task
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

## What you'll learn
- Hash map for counting
- Sorting by frequency
- Priority queue/heap concepts
- Time-space trade-offs

## Instructions
Complete the function in `main.py`:

**top_k_frequent(nums, k)** - Find k most frequent elements
- Return list of k most frequent elements
- Use hash map for counting
- Sort or use heap to get top k

## Examples

```python
>>> top_k_frequent([1, 1, 1, 2, 2, 3], 2)
[1, 2]  # 1 appears 3 times, 2 appears 2 times

>>> top_k_frequent([1], 1)
[1]

>>> top_k_frequent([4, 1, -1, 2, -1, 2, 3], 2)
[-1, 2]  # Both appear twice
```

## Testing
Run tests with:
```bash
cd exercises/general_dsa/top_k_frequent
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test top_k_frequent
```

## Hints
If you get stuck, run:
```bash
dsa hint top_k_frequent [1|2|3]
```

## Concepts

### Count Frequencies
```python
# Use hash map to count occurrences
# nums = [1, 1, 1, 2, 2, 3]
# count = {1: 3, 2: 2, 3: 1}
```

### Get Top K
```python
# Approach 1: Sort by frequency
# sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)

# Approach 2: Use min-heap of size k
# More efficient when k << n
```

### Heap Approach (Advanced)
```python
import heapq
# Maintain heap of size k with most frequent elements
# O(n log k) time instead of O(n log n)
```

## Time Complexity Analysis
- **Hash map count**: O(n)
- **Sorting approach**: O(n log n) total
- **Heap approach**: O(n log k) total (better when k is small)

## Space Complexity
- **Both approaches**: O(n) - Hash map stores all unique elements

## Why This Is Important
- Pattern for ranking/frequency problems
- Understanding heap data structure
- Trade-offs between different approaches
- Meta frequently asks variations (top K anything)
