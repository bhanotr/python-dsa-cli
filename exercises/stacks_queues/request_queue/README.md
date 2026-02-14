# Exercise 5: Request Queue

## Meta Interview Pattern
This exercise is based on the **Queue** pattern and **Deque** data structures commonly asked at Meta. Similar to:
- **Implement Stack using Queues** - LeetCode 225
- **Implement Queue using Stacks** - LeetCode 232

## Task
Implement a request queue using Python's `deque` to track network requests in order they arrive. This is a simple FIFO (First In, First Out) data structure.

## What you'll learn
- Queue data structure (FIFO)
- Python's `collections.deque`
- Basic queue operations: enqueue, dequeue, peek, is_empty
- Tracking ordered data

## Instructions
Complete the functions in `main.py`:

1. **RequestQueue class** - Queue for network requests
   - `__init__()` - Initialize empty queue
   - `enqueue(request)` - Add request to back of queue
   - `dequeue()` - Remove and return request from front
   - `peek()` - Return front request without removing
   - `is_empty()` - Check if queue is empty
   - `size()` - Return number of requests in queue

## Examples

```python
queue = RequestQueue()

queue.enqueue("GET /api/users")
queue.enqueue("POST /api/data")
queue.enqueue("DELETE /api/item/1")

assert queue.peek() == "GET /api/users"
assert queue.size() == 3

request = queue.dequeue()
assert request == "GET /api/users"
assert queue.size() == 2
```

## Testing
Run tests with:
```bash
cd exercises/stacks_queues/request_queue
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test request_queue
```

## Hints
If you get stuck, run:
```bash
dsa hint request_queue [1|2|3]
```

## Concepts

### Queue (FIFO)
- First In, First Out
- Elements added at back, removed from front
- Maintains insertion order

### Python Deque
```python
from collections import deque

queue = deque()
queue.append(item)      # Add to back
queue.popleft()          # Remove from front
queue[0]                 # Peek at front
len(queue)               # Get size
bool(queue)              # Check if empty
```

### Queue Operations
- **enqueue**: Add to back - O(1)
- **dequeue**: Remove from front - O(1)
- **peek**: Look at front - O(1)
- **is_empty**: Check if empty - O(1)

## Time Complexity Analysis
- `enqueue`: O(1) - amortized for deque
- `dequeue`: O(1) - amortized for deque
- `peek`: O(1)
- `is_empty`: O(1)
- `size`: O(1)

## Space Complexity
- O(n) - Stores n requests
