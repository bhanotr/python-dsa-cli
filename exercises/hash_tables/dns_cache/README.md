# Exercise 7: DNS Cache

## Meta Interview Pattern
This exercise is based on the **Hash Map + TTL** pattern and **Cache Design** problems commonly asked at Meta. Similar to:
- **LRU Cache** - LeetCode 146
- **Design Twitter** - LeetCode 355

## Task
Implement a DNS cache with time-to-live (TTL) expiration. Cached entries expire after their TTL and should not be returned.

## What you'll learn
- Hash map for O(1) lookups
- Time-based cache expiration
- Tracking entry timestamps
- Cleanup of expired entries

## Instructions
Complete the functions in `main.py`:

1. **DNSCache class** - DNS caching with TTL
   - `__init__()` - Initialize empty cache
   - `get(hostname)` - Get IP if not expired, else None
   - `put(hostname, ip, ttl)` - Store IP with expiration time
   - `cleanup()` - Remove all expired entries

## Examples

```python
cache = DNSCache()

cache.put("example.com", "93.184.216.34", 60)
cache.put("google.com", "142.250.81.46", 30)

assert cache.get("example.com") == "93.184.216.34"
# After 30 seconds, google.com expires
# After 60 seconds, example.com expires
```

## Testing
Run tests with:
```bash
cd exercises/hash_tables/dns_cache
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test dns_cache
```

## Hints
If you get stuck, run:
```bash
dsa hint dns_cache [1|2|3]
```

## Concepts

### TTL (Time To Live)
- Each entry has an expiration time
- Entry expires after TTL seconds
- Expired entries should not be returned

### Hash Map Structure
```python
cache = {
    "hostname": {
        "ip": "192.168.1.1",
        "expires_at": timestamp
    }
}
```

### Time Comparison
```python
import time
current_time = time.time()
if entry["expires_at"] < current_time:
    # Entry expired
```

## Time Complexity Analysis
- `get`: O(1) - Hash map lookup
- `put`: O(1) - Hash map insert
- `cleanup`: O(n) - Iterate through all entries

## Space Complexity
- O(n) - Stores n DNS entries
