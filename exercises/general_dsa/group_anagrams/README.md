# Exercise 19: Group Anagrams

## Meta Interview Pattern
This is a **frequently asked** question at Meta and all major tech companies.
- **Group Anagrams** - LeetCode 49
- Classic hash map problem
- Tests understanding of string manipulation and hash tables

## Task
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## What you'll learn
- Hash map for grouping
- String sorting and manipulation
- Using sorted strings as keys
- Handling edge cases

## Instructions
Complete the function in `main.py`:

**group_anagrams(strs)** - Group anagrams together
- Return list of groups (each group is a list of anagrams)
- Use hash map with sorted string as key
- O(n * k log k) time where k is max string length

## Examples

```python
>>> group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

>>> group_anagrams([""])
[[""]]

>>> group_anagrams(["a"])
[["a"]]
```

## Testing
Run tests with:
```bash
cd exercises/general_dsa/group_anagrams
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test group_anagrams
```

## Hints
If you get stuck, run:
```bash
dsa hint group_anagrams [1|2|3]
```

## Concepts

### Hash Map with Sorted Key
```python
# Key insight: All anagrams have the same sorted string
# "eat" -> "aet", "tea" -> "aet", "ate" -> "aet"
# Use sorted string as hash map key
# { "aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"] }
```

### String Sorting
```python
sorted_str = ''.join(sorted("eat"))  # "aet"
```

### Alternative: Character Count
```python
# Instead of sorting, count characters
# "eat" -> {a:1, e:1, t:1} -> "1#0#0#1#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#1"
# Better for long strings with limited alphabet
```

## Time Complexity Analysis
- **Sorting approach**: O(n * k log k) where n is number of strings, k is max length
- **Character count approach**: O(n * k) where n is number of strings, k is max length

## Space Complexity
- **Both approaches**: O(n * k) - Store all strings in hash map

## Why This Is Important
- Pattern for grouping similar items
- Hash map with composite keys
- String manipulation skills
- Meta frequently asks grouping and categorization problems
