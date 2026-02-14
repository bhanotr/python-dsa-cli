# Exercise 21: Valid Palindrome

## Meta Interview Pattern
This is a **frequently asked** question at Meta and all major tech companies.
- **Valid Palindrome** - LeetCode 125
- Two pointer problem
- Tests understanding of string manipulation and pointers

## Task
Given a string `s`, return `True` if it is a palindrome, or `False` otherwise.

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

## What you'll learn
- Two pointer technique
- String manipulation
- Character validation
- Case insensitivity handling

## Instructions
Complete the function in `main.py`:

**is_palindrome(s)** - Check if string is palindrome
- Return True/False
- Ignore non-alphanumeric characters
- Case-insensitive comparison
- Use two pointer approach

## Examples

```python
>>> is_palindrome("A man, a plan, a canal: Panama")
True  # "amanaplanacanalpanama"

>>> is_palindrome("race a car")
False

>>> is_palindrome(" ")
True

>>> is_palindrome("0P")
False
```

## Testing
Run tests with:
```bash
cd exercises/general_dsa/valid_palindrome
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test valid_palindrome
```

## Hints
If you get stuck, run:
```bash
dsa hint valid_palindrome [1|2|3]
```

## Concepts

### Two Pointer Approach
```python
left = 0
right = len(s) - 1

while left < right:
    # Skip non-alphanumeric
    # Compare characters
    # Move pointers
```

### Character Validation
```python
# Check if character is alphanumeric
c.isalnum()  # Returns True for letters and numbers

# Convert to lowercase
c.lower()
```

### Alternative: Clean and Compare
```python
# Create cleaned string first
cleaned = ''.join(c.lower() for c in s if c.isalnum())
return cleaned == cleaned[::-1]
```

## Time Complexity Analysis
- **Two pointer**: O(n) - Single pass
- **Clean and compare**: O(n) - Build string + reverse

## Space Complexity
- **Two pointer**: O(1) - No extra space
- **Clean and compare**: O(n) - Store cleaned string

## Why This Is Important
- Two pointer pattern is fundamental
- String manipulation skills
- Efficient space usage
- Meta frequently asks two pointer variations
