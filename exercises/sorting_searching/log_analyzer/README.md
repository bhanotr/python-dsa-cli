# Exercise 16: Log Analyzer (Binary Search)

## Meta Interview Pattern
This exercise is based on the **Binary Search** pattern and **Search in Sorted Array** problems commonly asked at Meta. Similar to:
- **Find First and Last Position** - LeetCode 34
- **Search in Rotated Sorted Array** - LeetCode 33

## Task
Implement binary search to find first/last log entry matching criteria in timestamped logs.

## What you'll learn
- Binary search algorithm
- Finding first/last occurrence
- Searching sorted data
- Edge case handling

## Instructions
Complete the functions in `main.py`:

1. **find_first_log(logs, timestamp)** - Find first log with given timestamp
2. **find_last_log(logs, timestamp)** - Find last log with given timestamp
3. **find_log_range(logs, start_ts, end_ts)** - Find logs in timestamp range

Logs format: List of (timestamp, message) tuples, sorted by timestamp.

## Examples

```python
logs = [
    (100, "log1"),
    (100, "log2"),
    (200, "log3"),
    (300, "log4")
]

assert find_first_log(logs, 100) == 0  # Index of first log with ts 100
assert find_last_log(logs, 100) == 1   # Index of last log with ts 100
```

## Testing
Run tests with:
```bash
cd exercises/sorting_searching/log_analyzer
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test log_analyzer
```

## Hints
If you get stuck, run:
```bash
dsa hint log_analyzer [1|2|3]
```

## Concepts

### Binary Search
- Repeatedly divide search space in half
- O(log n) time complexity
- Works on sorted data

### Finding First/Last
- For first: keep moving left when match found
- For last: keep moving right when match found
- Similar to finding boundaries

## Time Complexity Analysis
- All operations: O(log n)

## Space Complexity
- O(1) - No extra space needed
