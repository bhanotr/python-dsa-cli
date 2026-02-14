# Exercise 2: URL Encoder

## Meta Interview Pattern
This exercise is based on the **String Manipulation** pattern and **URL Encoding** problems commonly asked at Meta. Similar to:
- **URL LCCI** - LeetCode面试题 01.09
- **Encode and Decode Strings** - LeetCode 271
- **String compression** variations

## Task
Implement URL encoding and decoding functions. URL encoding converts special characters to their percent-encoded representation (%XX where XX is the hexadecimal value).

## URL Encoding Rules
- Alphanumeric characters (a-z, A-Z, 0-9) remain unchanged
- The following characters remain unchanged: `-`, `_`, `.`, `~`
- All other characters are encoded as `%XX` where XX is 2-digit hexadecimal
- Spaces are encoded as `%20` or `+`

## What you'll learn
- Character iteration and mapping
- Hexadecimal conversion
- String building techniques
- Encoding/decoding patterns

## Instructions
Complete the functions in `main.py`:

1. **url_encode(url)** - Encode a URL string
   - Replace special characters with %XX format
   - Convert spaces to %20

2. **url_decode(encoded_url)** - Decode an encoded URL
   - Convert %XX back to characters
   - Convert %20 back to space

3. **is_valid_encoded(encoded_url)** - Validate encoded URL format
   - Check that % is followed by 2 hex digits
   - Return True if valid, False otherwise

## Examples

```python
>>> url_encode("hello world")
"hello%20world"

>>> url_encode("hello@world!")
"hello%40world%21"

>>> url_decode("hello%20world")
"hello world"

>>> url_decode("hello%40world%21")
"hello@world!"

>>> is_valid_encoded("hello%20world")
True

>>> is_valid_encoded("hello%2gworld")
False
```

## Testing
Run tests with:
```bash
cd exercises/arrays_strings/url_encoder
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test url_encoder
```

## Hints
If you get stuck, run:
```bash
dsa hint url_encoder [1|2|3]
```

## Concepts

### Character Iteration
```python
for char in s:
    # Process each character
    if should_encode(char):
        encoded += encode_char(char)
```

### Hexadecimal Encoding
```python
# Convert character to hex
hex_val = hex(ord(char))[2:].upper()
# Ensure 2 digits
hex_val = hex_val.zfill(2)
encoded = '%' + hex_val
```

### Character Sets
```python
# Characters that don't need encoding
SAFE_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.~"
```

## Time Complexity Analysis
- `url_encode`: O(n) - Single pass through string
- `url_decode`: O(n) - Single pass with lookahead
- `is_valid_encoded`: O(n) - Single pass validation

## Space Complexity
- O(n) - New string of similar size
