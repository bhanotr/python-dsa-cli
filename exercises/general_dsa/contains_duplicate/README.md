# Exercise 22: Contains Duplicate

## Meta Interview Pattern
This is a **frequently asked** warm-up question at Meta and all major tech companies.
- **Contains Duplicate** - LeetCode 217
- Hash set problem
- Tests understanding of sets and time complexity

## Task
Given an integer array `nums`, return `True` if any value appears at least twice in the array, and return `False` if every element is distinct.

## What you'll learn
- Hash set for O(1) lookups
- Understanding set vs list performance
- Early termination optimization
- Edge case handling

## Instructions
Complete the function in `main.py`:

**contains_duplicate(nums)** - Check for duplicates
- Return True/False
- Use hash set for efficiency
- Return as soon as duplicate found

## Examples

```python
>>> contains_duplicate([1, 2, 3, 1])
True

>>> contains_duplicate([1, 2, 3, 4])
False

>>> contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
True

>>> contains_duplicate([])
False
```

## Testing
Run tests with:
```bash
cd exercises/general_dsa/contains_duplicate
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test contains_duplicate
```

## Hints
If you get stuck, run:
```bash
dsa hint contains_duplicate [1|2|3]
```

## Concepts

### Hash Set Approach
```python
seen = set()
for num in nums:
    if num in seen:  # O(1) lookup
        return True
    seen.add(num)
return False
```

### Set Comparison
```python
# Alternative: Compare length
return len(nums) != len(set(nums))
```

### Sorting Approach (Slower)
```python
nums.sort()
for i in range(len(nums) - 1):
    if nums[i] == nums[i + 1]:
        return True
return False
```

## Time Complexity Analysis
- **Hash set**: O(n) average, O(n²) worst (rare)
- **Set comparison**: O(n) average
- **Sorting**: O(n log n)

## Space Complexity
- **Hash set**: O(n) - Store up to n elements
- **Set comparison**: O(n) - Create set
- **Sorting**: O(1) or O(n) depending on sort implementation

## Why This Is Important
- Foundation for many hash set problems
- Understanding when to use sets vs lists
- Early termination pattern
- Often used as a warm-up or building block
