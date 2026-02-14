# Exercise 4: LRU Cache (Linked List)

## Meta Interview Pattern
This exercise is based on the **LRU Cache** pattern and **Doubly Linked List + Hash Map** combination commonly asked at Meta. Similar to:
- **LRU Cache** - LeetCode 146
- **Design HashMap** - LeetCode 706

## Task
Implement an LRU (Least Recently Used) Cache using a doubly linked list and hash map. The cache has a fixed capacity and evicts the least recently used item when it becomes full.

## What you'll learn
- Doubly linked list implementation
- Hash map for O(1) lookups
- LRU cache design pattern
- Moving nodes within a linked list
- Edge cases for capacity limits

## Instructions
Complete the functions in `main.py`:

1. **DLinkedNode class** - Node for doubly linked list
   - Attributes: `key`, `value`, `prev`, `next`

2. **LRUCache class** - LRU Cache implementation
   - `__init__(capacity)` - Initialize with capacity
   - `get(key)` - Get value and move to most recent
   - `put(key, value)` - Add/update value, evict LRU if needed

## Examples

```python
cache = LRUCache(2)

cache.put(1, "10.0.0.1")
cache.put(2, "10.0.0.2")

assert cache.get(1) == "10.0.0.1"  # Now key 1 is most recent
cache.put(3, "10.0.0.3")  # Evicts key 2 (least recent)

assert cache.get(2) is None  # Key 2 was evicted
assert cache.get(3) == "10.0.0.3"
```

## Testing
Run tests with:
```bash
cd exercises/linked_lists/lru_cache_ll
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test lru_cache_ll
```

## Hints
If you get stuck, run:
```bash
dsa hint lru_cache_ll [1|2|3]
```

## Concepts

### Doubly Linked List Node
```python
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
```

### LRU Cache Operations
- **get(key)**: Return value if exists, move node to head (most recent)
- **put(key, value)**: Update existing or add new, evict tail if over capacity

### Hash Map + Doubly Linked List
- Hash map provides O(1) node access
- Doubly linked list maintains usage order
- Head = most recently used
- Tail = least recently used

## Time Complexity Analysis
- `get`: O(1) - Hash map lookup + O(1) node move
- `put`: O(1) - Hash map insert/delete + O(1) node operations

## Space Complexity
- O(capacity) - Stores at most `capacity` items
