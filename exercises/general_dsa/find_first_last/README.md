# Exercise 26: Find First and Last Position

## Meta Interview Pattern
This is a **frequently asked** question at Meta and all major tech companies.
- **Find First and Last Position** - LeetCode 34
- Binary search problem
- Tests understanding of binary search variations

## Task
Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If target is not found in the array, return `[-1, -1]`.

You must write an algorithm with O(log n) runtime complexity.

## What you'll learn
- Binary search for boundaries
- Finding first/last occurrence
- Modifying standard binary search
- Handling edge cases

## Instructions
Complete the function in `main.py`:

**find_first_last(nums, target)** - Find first and last position
- Return [first_index, last_index]
- Use binary search for O(log n) time
- Binary search twice: find first, then find last

## Examples

```python
>>> find_first_last([5, 7, 7, 8, 8, 10], 8)
[3, 4]

>>> find_first_last([5, 7, 7, 8, 8, 10], 6)
[-1, -1]

>>> find_first_last([], 0)
[-1, -1]

>>> find_first_last([2, 2], 2)
[0, 1]
```

## Testing
Run tests with:
```bash
cd exercises/general_dsa/find_first_last
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test find_first_last
```

## Hints
If you get stuck, run:
```bash
dsa hint find_first_last [1|2|3]
```

## Concepts

### Binary Search for First Position
```python
def find_first(nums, target):
    left, right = 0, len(nums) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid
            right = mid - 1  # Keep searching left
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result
```

### Binary Search for Last Position
```python
def find_last(nums, target):
    left, right = 0, len(nums) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid
            left = mid + 1  # Keep searching right
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result
```

### Key Insight
```python
# When we find target, don't stop!
# - For first: keep searching left (right = mid - 1)
# - For last: keep searching right (left = mid + 1)
```

## Time Complexity Analysis
- **Two binary searches**: O(log n) + O(log n) = O(log n)

## Space Complexity
- **O(1)** - Constant extra space

## Why This Is Important
- Pattern for boundary search
- Binary search modifications
- Meta frequently asks binary search variations
- Understanding how to adapt standard algorithms
