# Exercise 9: Rate Limiter

## Meta Interview Pattern
This exercise is based on the **Rate Limiting** pattern and **Token Bucket Algorithm** commonly asked at Meta. Similar to:
- **Design Hit Counter** - LeetCode 362
- **Logger Rate Limiter** - LeetCode 359

## Task
Implement a token bucket rate limiter to control request rates per IP address. Allow or block requests based on available tokens.

## What you'll learn
- Token bucket algorithm
- Per-client rate limiting
- Time-based token refill
- Hash map for tracking clients

## Instructions
Complete the functions in `main.py`:

1. **RateLimiter class** - Token bucket rate limiter
   - `__init__(capacity, refill_rate)` - Initialize with capacity and refill rate
   - `allow_request(ip)` - Check if request should be allowed
   - Consume token if available, refill based on time elapsed

## Examples

```python
limiter = RateLimiter(capacity=5, refill_rate=1)

assert limiter.allow_request("192.168.1.1") == True  # 4 tokens left
assert limiter.allow_request("192.168.1.1") == True  # 3 tokens left

# After 2 seconds, 2 tokens refilled
# Now 5 tokens (capped at capacity)
```

## Testing
Run tests with:
```bash
cd exercises/hash_tables/rate_limiter
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test rate_limiter
```

## Hints
If you get stuck, run:
```bash
dsa hint rate_limiter [1|2|3]
```

## Concepts

### Token Bucket
- Bucket has max capacity of tokens
- Tokens refill at constant rate
- Each request consumes 1 token
- Request allowed if tokens >= 1

### Per-Client Tracking
```python
clients = {
    "ip": {
        "tokens": 5,
        "last_refill_time": timestamp
    }
}
```

### Refill Calculation
```python
time_elapsed = current_time - last_refill_time
tokens_to_add = time_elapsed * refill_rate
```

## Time Complexity Analysis
- `allow_request`: O(1) - Hash map lookup + arithmetic

## Space Complexity
- O(n) - Stores state for n unique IPs
