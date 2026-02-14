# Exercise 14: Packet Scheduler (Priority Queue)

## Meta Interview Pattern
This exercise is based on the **Heap/Priority Queue** pattern and **Top K Elements** problems commonly asked at Meta. Similar to:
- **Kth Largest Element** - LeetCode 215
- **Merge K Sorted Lists** - LeetCode 23

## Task
Implement a packet scheduler using priority queue (heapq) to process packets by priority. Higher priority packets are processed first.

## What you'll learn
- Priority queue using heapq
- Min-heap vs max-heap
- Priority-based scheduling
- Heap operations

## Instructions
Complete the functions in `main.py`:

1. **PacketScheduler class** - Priority-based packet scheduler
   - `__init__()` - Initialize scheduler
   - `enqueue(packet, priority)` - Add packet with priority
   - `dequeue()` - Remove and return highest priority packet
   - `peek()` - Return highest priority without removing
   - `is_empty()` - Check if scheduler is empty
   - `size()` - Return number of packets

## Examples

```python
scheduler = PacketScheduler()
scheduler.enqueue("packet1", 1)
scheduler.enqueue("packet2", 3)
scheduler.enqueue("packet3", 2)

assert scheduler.dequeue() == "packet2"  # Highest priority (3)
assert scheduler.dequeue() == "packet3"  # Next (2)
```

## Testing
Run tests with:
```bash
cd exercises/heaps/packet_scheduler
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test packet_scheduler
```

## Hints
If you get stuck, run:
```bash
dsa hint packet_scheduler [1|2|3]
```

## Concepts

### Priority Queue (Min-Heap)
- heapq implements min-heap by default
- For max-heap, negate priority
- Operations: push, pop, peek (index 0)

### Heap Operations
```python
import heapq
heapq.heappush(heap, item)
item = heapq.heappop(heap)
min_item = heap[0]
```

## Time Complexity Analysis
- `enqueue`: O(log n)
- `dequeue`: O(log n)
- `peek`: O(1)
- `is_empty`: O(1)
- `size`: O(1)

## Space Complexity
- O(n) - Stores n packets
