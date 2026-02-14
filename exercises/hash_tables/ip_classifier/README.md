# Exercise 8: IP Classifier

## Meta Interview Pattern
This exercise is based on the **Hash Map** pattern and **Group Similar Items** problems commonly asked at Meta. Similar to:
- **Group Anagrams** - LeetCode 49
- **Top K Frequent Elements** - LeetCode 347

## Task
Implement an IP address classifier that groups IPs by their subnet (network prefix). Count IPs in each network.

## What you'll learn
- Hash map for grouping data
- Parsing IP addresses
- Using hashable keys for grouping
- Aggregating data by category

## Instructions
Complete the functions in `main.py`:

1. **IPClassifier class** - Classify IPs by subnet
   - `__init__()` - Initialize classifier
   - `add_ip(ip)` - Add an IP address to its network group
   - `get_network_count(network)` - Get count of IPs in a network
   - `get_all_networks()` - Get all networks and their counts

## Examples

```python
classifier = IPClassifier()

classifier.add_ip("192.168.1.1")
classifier.add_ip("192.168.1.2")
classifier.add_ip("10.0.0.1")

assert classifier.get_network_count("192.168.1.0") == 2
assert classifier.get_network_count("10.0.0.0") == 1
```

## Testing
Run tests with:
```bash
cd exercises/hash_tables/ip_classifier
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test ip_classifier
```

## Hints
If you get stuck, run:
```bash
dsa hint ip_classifier [1|2|3]
```

## Concepts

### Subnet Mask
- IP: 192.168.1.100 with /24 mask
- Network prefix: 192.168.1.0
- Groups IPs by first 3 octets

### Hash Map Grouping
```python
groups = {
    "network_prefix": [ip1, ip2, ...]
}
```

### Extracting Network
```python
ip = "192.168.1.100"
parts = ip.split('.')
network = f"{parts[0]}.{parts[1]}.{parts[2]}.0"
```

## Time Complexity Analysis
- `add_ip`: O(1) - Hash map insert
- `get_network_count`: O(1) - Hash map lookup
- `get_all_networks`: O(n) - Iterate all keys

## Space Complexity
- O(n) - Stores n IPs
