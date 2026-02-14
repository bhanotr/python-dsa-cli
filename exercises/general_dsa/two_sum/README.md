# Exercise 18: Two Sum

## Meta Interview Pattern
This is one of the **most frequently asked** questions at Meta and all major tech companies.
- **Two Sum** - LeetCode 1
- Classic hash map problem
- Tests understanding of hash tables and time complexity

## Task
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

## What you'll learn
- Hash map for O(1) lookups
- Trade-offs between time and space complexity
- Complement value pattern
- Handling edge cases

## Instructions
Complete the function in `main.py`:

**two_sum(nums, target)** - Find two numbers that add to target
- Return list of two indices
- Use hash map for O(n) time complexity
- Exactly one valid solution exists

## Examples

```python
>>> two_sum([2, 7, 11, 15], 9)
[0, 1]  # Because nums[0] + nums[1] = 2 + 7 = 9

>>> two_sum([3, 2, 4], 6)
[1, 2]  # Because nums[1] + nums[2] = 2 + 4 = 6

>>> two_sum([3, 3], 6)
[0, 1]  # Two separate indices
```

## Testing
Run tests with:
```bash
cd exercises/general_dsa/two_sum
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test two_sum
```

## Hints
If you get stuck, run:
```bash
dsa hint two_sum [1|2|3]
```

## Concepts

### Hash Map Approach
```python
# For each number, check if (target - number) exists in hash map
# Store {number: index} in hash map as we iterate
# O(n) time, O(n) space
```

### Complement Pattern
```python
# For each number num, we need:
# complement = target - num
# If complement is in our hash map, we found the pair!
```

### Brute Force (O(n²))
```python
# Two nested loops to check every pair
# Simple but slow - what's the better approach?
```

## Time Complexity Analysis
- **Brute Force**: O(n²) - Check all pairs
- **Hash Map**: O(n) - Single pass with O(1) lookups

## Space Complexity
- **Brute Force**: O(1) - No extra space
- **Hash Map**: O(n) - Store up to n elements

## Learning Resources

Study these before attempting to solve:
- **LeetCode 1 (Two Sum)** - Read problem and discussion: https://leetcode.com/problems/two-sum/
- **NeetCode Video** - Excellent explanation: https://www.youtube.com/watch?v=KLlX8kIbM0
- **Hash Tables Guide** - Understand when and why to use: https://leetcode.com/discuss/study-guide/5/
- **Complement Pattern** - Key algorithmic insight: Search "two sum complement pattern"

### Concept Questions to Consider
- **Why O(n²) is bad**: What happens if input size is very large?
- **What makes O(n) possible**: How can we remember what we've seen?
- **The "aha!" moment**: If we need X to reach target T, we're also looking for (T - X)
- **Hash map trade-off**: We're using extra memory - is it worth it?

## Why This Is Important
- Foundation for many hash map problems
- Understanding complement pattern
- Choosing optimal data structures
- Meta frequently asks variations of this pattern
