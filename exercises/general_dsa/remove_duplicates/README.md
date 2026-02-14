# Exercise 29: Remove Duplicates from Sorted Array

## Meta Interview Pattern
This is a **frequently asked** question at Meta and all major tech companies.
- **Remove Duplicates from Sorted Array** - LeetCode 26
- Two pointer problem
- Tests understanding of in-place operations

## Task
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Return the number of unique elements `k`.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

## What you'll learn
- Two pointer technique
- In-place array modification
- Working with sorted arrays
- Efficient space usage

## Instructions
Complete the function in `main.py`:

**remove_duplicates(nums)** - Remove duplicates in-place
- Return number of unique elements
- Modify nums in-place
- Use two pointer technique

## Examples

```python
>>> nums = [1, 1, 2]
>>> k = remove_duplicates(nums)
>>> k
2
>>> nums[:k]
[1, 2]

>>> nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
>>> k = remove_duplicates(nums)
>>> k
5
>>> nums[:k]
[0, 1, 2, 3, 4]

>>> nums = [1]
>>> k = remove_duplicates(nums)
>>> k
1
>>> nums[:k]
[1]
```

## Testing
Run tests with:
```bash
cd exercises/general_dsa/remove_duplicates
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test remove_duplicates
```

## Hints
If you get stuck, run:
```bash
dsa hint remove_duplicates [1|2|3]
```

## Concepts

### Two Pointer Technique
```python
# Slow pointer: position for next unique element
# Fast pointer: scans through array
slow = 0

for fast in range(1, len(nums)):
    if nums[fast] != nums[slow]:
        slow += 1
        nums[slow] = nums[fast]

return slow + 1
```

### Why Two Pointers?
```python
# Since array is sorted, duplicates are adjacent
# We only need to compare with the last unique element
# [1, 1, 2, 2, 3]
#      ^  ^
#    slow fast
# nums[fast] != nums[slow], so we found a new unique!
```

### Key Insight
```python
# slow tracks where to place the next unique element
# fast scans to find unique elements
# When nums[fast] != nums[slow], it's a new unique
# Place it at slow + 1
```

### What About Rest of Array?
```python
# Problem doesn't care about elements after index k
# Only first k elements need to be correct
# [1, 1, 2, 2, 3] -> [1, 2, 2, 2, 3] (k=2)
#                       ^^^^
#                   first 2 correct, rest doesn't matter
```

## Time Complexity Analysis
- **Two pointer**: O(n) - Single pass through array

## Space Complexity
- **O(1)** - Constant extra space (in-place)

## Why This Is Important
- Two pointer pattern is fundamental
- In-place operations are common
- Meta frequently asks this exact problem
- Foundation for many array modification problems
