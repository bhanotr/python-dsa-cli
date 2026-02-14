# Exercise 6: Bracket Validator

## Meta Interview Pattern
This exercise is based on the **Stack** pattern commonly asked at Meta. Similar to:
- **Valid Parentheses** - LeetCode 20
- **Min Stack** - LeetCode 155

## Task
Implement a bracket validator using a stack to check if nested configurations are valid. Supports brackets: `{}`, `[]`, `()`.

## What you'll learn
- Stack data structure (LIFO)
- Using stack for matching pairs
- Validating nested structures
- Early termination on errors

## Instructions
Complete the functions in `main.py`:

1. **is_valid_config(config)** - Validate bracket configuration
   - Return True if all brackets are properly nested and closed
   - Return False if any bracket is unmatched or mismatched
   - Handle empty string (should return True)

## Examples

```python
assert is_valid_config("()") == True
assert is_valid_config("()[]{}") == True
assert is_valid_config("(]") == False
assert is_valid_config("([)]") == False
assert is_valid_config("{[]}") == True
assert is_valid_config("") == True
```

## Testing
Run tests with:
```bash
cd exercises/stacks_queues/bracket_validator
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test bracket_validator
```

## Hints
If you get stuck, run:
```bash
dsa hint bracket_validator [1|2|3]
```

## Concepts

### Stack (LIFO)
- Last In, First Out
- Use `append()` to push, `pop()` to pop
- Perfect for matching nested structures

### Matching Brackets
```python
pairs = {
    ')': '(',
    '}': '{',
    ']': '['
}
```

### Algorithm
1. Iterate through each character
2. If opening bracket, push to stack
3. If closing bracket, check if stack top matches
4. At end, stack should be empty

## Time Complexity Analysis
- `is_valid_config`: O(n) - Single pass through string

## Space Complexity
- O(n) - Worst case all opening brackets
