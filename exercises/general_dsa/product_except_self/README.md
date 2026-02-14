# Exercise 24: Product of Array Except Self

## Meta Interview Pattern
This is a **frequently asked** question at Meta and all major tech companies.
- **Product of Array Except Self** - LeetCode 238
- Prefix/suffix product problem
- Tests understanding of prefix products and space optimization

## Task
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

## What you'll learn
- Prefix and suffix products
- Space optimization
- Two-pass algorithms
- In-place computation

## Instructions
Complete the function in `main.py`:

**product_except_self(nums)** - Calculate product except self
- Return array where each element is product of all others
- O(n) time complexity
- O(1) extra space (excluding output array)

## Examples

```python
>>> product_except_self([1, 2, 3, 4])
[24, 12, 8, 6]
# [2*3*4, 1*3*4, 1*2*4, 1*2*3]

>>> product_except_self([-1, 1, 0, -3, 3])
[0, 0, 9, 0, 0]

>>> product_except_self([1, 2])
[2, 1]
```

## Testing
Run tests with:
```bash
cd exercises/general_dsa/product_except_self
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test product_except_self
```

## Hints
If you get stuck, run:
```bash
dsa hint product_except_self [1|2|3]
```

## Concepts

### Prefix and Suffix Products
```python
# For nums = [1, 2, 3, 4]
# Prefix: [1, 1, 2, 6]    (product of all elements before)
# Suffix: [24, 12, 4, 1]  (product of all elements after)
# Answer: [24, 12, 8, 6]   (prefix[i] * suffix[i])
```

### Two-Pass Approach (O(n) space)
```python
# Pass 1: Calculate prefix products
# Pass 2: Multiply by suffix products
```

### Space-Optimized (O(1) extra space)
```python
# Pass 1: Store prefix in answer array
# Pass 2: Use running suffix product
suffix = 1
for i in range(n-1, -1, -1):
    answer[i] *= suffix
    suffix *= nums[i]
```

### Why No Division?
```python
# Division fails with zeros
# nums = [1, 2, 3, 0]
# What's answer[3]? 1*2*3 = 6
# Can't divide 0 by 0
```

## Time Complexity Analysis
- **Both approaches**: O(n) - Two passes through array

## Space Complexity
- **Two-pass with suffix array**: O(n)
- **Space-optimized**: O(1) extra (excluding output)

## Why This Is Important
- Prefix/suffix pattern is common
- Space optimization skills
- Meta frequently asks this exact problem
- Understanding in-place computation
