# Exercise 1: Packet Parser

## Meta Interview Pattern
This exercise is based on the **Two Pointers** pattern and **String Parsing** problems commonly asked at Meta. Similar to:
- **Valid Palindrome** - LeetCode 125
- **String to Integer (atoi)** - LeetCode 8
- **Parse packets** variations in Meta's networking interviews

## Task
Implement a network packet parser that extracts different fields from a simplified packet format. Packets are encoded as strings with specific delimiters.

## Packet Format
```
SOURCE:DESTINATION|TYPE:PAYLOAD
```

Example: `"192.168.1.1:10.0.0.1|HTTP:GET /index.html"`

## What you'll learn
- Two pointers technique
- String parsing and manipulation
- Splitting and extracting data
- Handling edge cases (empty packets, missing fields)

## Instructions
Complete the functions in `main.py`:

1. **parse_packet(packet)** - Parse a packet string into its components
   - Return a dict with: `source`, `destination`, `packet_type`, `payload`
   - Handle malformed packets (return None)

2. **is_valid_ip(ip)** - Validate IP address format
   - Should be in format: `X.X.X.X` where each X is 0-255

3. **get_packet_size(packet)** - Calculate packet size (length of payload)
   - Return 0 for invalid packets

## Examples

```python
>>> parse_packet("192.168.1.1:10.0.0.1|HTTP:GET /index.html")
{
    'source': '192.168.1.1',
    'destination': '10.0.0.1',
    'packet_type': 'HTTP',
    'payload': 'GET /index.html'
}

>>> is_valid_ip("192.168.1.1")
True
>>> is_valid_ip("256.1.1.1")
False

>>> get_packet_size("192.168.1.1:10.0.0.1|HTTP:GET /index.html")
16  # Length of "GET /index.html"
```

## Testing
Run tests with:
```bash
cd exercises/arrays_strings/packet_parser
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test packet_parser
```

## Hints
If you get stuck, run:
```bash
dsa hint packet_parser [1|2|3]
```

## Concepts

### Two Pointers
- Use two indices to track positions in the string
- One pointer for start, one for end of a field
- Move pointers forward as you parse

### String Parsing
```python
# Split on delimiter
parts = packet.split('|')

# Parse nested fields
source_dest = parts[0].split(':')
```

### Edge Cases to Consider
- Empty packet string
- Missing delimiters
- Missing fields
- Invalid IP format
- Empty payload

## Time Complexity Analysis
- `parse_packet`: O(n) - Single pass through the string
- `is_valid_ip`: O(1) - Constant time (IPs have fixed length)
- `get_packet_size`: O(n) - Parse and count

## Space Complexity
- O(n) - Create new strings/objects during parsing
