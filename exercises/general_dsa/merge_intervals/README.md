# Exercise 23: Merge Intervals

## Meta Interview Pattern
This is a **frequently asked** question at Meta and all major tech companies.
- **Merge Intervals** - LeetCode 56
- Sorting + greedy problem
- Tests understanding of interval manipulation

## Task
Given an array of intervals `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

## What you'll learn
- Interval manipulation
- Sorting for greedy algorithms
- Two pointer/iteration pattern
- Overlap detection

## Instructions
Complete the function in `main.py`:

**merge(intervals)** - Merge overlapping intervals
- Return merged intervals
- Sort intervals by start time
- Merge overlapping intervals iteratively

## Examples

```python
>>> merge([[1, 3], [2, 6], [8, 10], [15, 18]])
[[1, 6], [8, 10], [15, 18]]

>>> merge([[1, 4], [4, 5]])
[[1, 5]]

>>> merge([[1, 4], [0, 4]])
[[0, 4]]

>>> merge([])
[]
```

## Testing
Run tests with:
```bash
cd exercises/general_dsa/merge_intervals
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test merge_intervals
```

## Hints
If you get stuck, run:
```bash
dsa hint merge_intervals [1|2|3]
```

## Concepts

### Sorting by Start Time
```python
# Sort intervals by start time
intervals.sort(key=lambda x: x[0])
```

### Overlap Detection
```python
# Check if current interval overlaps with last merged
# Overlap if: current[0] <= last_merged[1]
# Merge: last_merged[1] = max(last_merged[1], current[1])
```

### Iterative Merging
```python
merged = []
for interval in intervals:
    if not merged or interval[0] > merged[-1][1]:
        # No overlap, add new interval
        merged.append(interval)
    else:
        # Overlap, merge with last interval
        merged[-1][1] = max(merged[-1][1], interval[1])
```

## Time Complexity Analysis
- **Sorting**: O(n log n)
- **Merging**: O(n)
- **Total**: O(n log n)

## Space Complexity
- **O(n)** - Store merged intervals (worst case no merging)

## Why This Is Important
- Pattern for interval problems
- Sorting + greedy algorithm
- Meta frequently asks interval scheduling problems
- Foundation for calendar, scheduling applications
