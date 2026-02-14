# Quick Start Guide

## Installation

1. **Create and enter the project directory** (if not already there):
```bash
cd /home/ritwik/python-dsa-exercises
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Install the CLI tool**:
```bash
pip install -e exercise-cli/
```

4. **Verify installation**:
```bash
dsa list
```

You should see all 17 exercises listed with completion status (✓ or ○).

## Getting Started

### View All Exercises
```bash
dsa list
```

You'll see all exercises organized by topic with their completion status.

### Start an Exercise
```bash
dsa start packet_parser
```

This will display the exercise instructions and tell you where the exercise files are.

### Work on an Exercise
```bash
cd exercises/packet_parser
# Edit main.py to implement the solution
```

### Get Help (Hints)

Hints are progressive - use them as you need:

```bash
# Level 1 hint (general direction)
dsa hint packet_parser 1

# Level 2 hint (more specific approach)
dsa hint packet_parser 2

# Level 3 hint (detailed explanation)
dsa hint packet_parser 3
```

### Test Your Solution

Run tests with performance logging:

```bash
# From anywhere
dsa test packet_parser

# Or from exercise directory
cd exercises/packet_parser
pytest test_main.py -v
```

Tests will show:
- ✓ or ✗ for pass/fail
- Execution time
- Number of operations
- Estimated complexity

### View Solution (if stuck)

```bash
dsa solution packet_parser
```

Try to solve it yourself first! Use solutions as a learning tool.

### Reset an Exercise

```bash
dsa reset packet_parser
```

This restores the exercise to its initial state.

## Recommended Learning Path

### Phase 1: Fundamentals (Exercises 1-4)
1. `packet_parser` - Arrays & parsing
2. `url_encoder` - String manipulation
3. `network_flow` - Linked lists
4. `lru_cache_ll` - LRU cache pattern

### Phase 2: Linear Structures (Exercises 5-9)
5. `request_queue` - Queue basics
6. `bracket_validator` - Stack pattern
7. `dns_cache` - Hash tables & caching
8. `ip_classifier` - Hashing & classification
9. `rate_limiter` - Advanced hash tables

### Phase 3: Hierarchical Structures (Exercises 10-13)
10. `network_topology` - Tree basics
11. `spanning_tree` - Tree algorithms
12. `network_router` - Graph BFS/DFS
13. `network_flow_graph` - Advanced graphs

### Phase 4: Advanced (Exercises 14-17)
14. `packet_scheduler` - Heaps & priority queues
15. `path_finder` - Recursion & backtracking
16. `network_optimization` - Dynamic programming
17. `log_analyzer` - Binary search

## Tips for Success

1. **Read the README** - Each exercise has detailed instructions
2. **Start with level 1 hints** - Don't waste time getting stuck
3. **Understand the problem** - Before coding, think through the approach
4. **Check edge cases** - Empty inputs, single elements, boundaries
5. **Analyze complexity** - Note your time and space complexity
6. **Compare with solution** - Learn different approaches

## Example Workflow

```bash
# 1. List exercises
dsa list

# 2. Start an exercise
dsa start url_encoder

# 3. Read the instructions
cat exercises/url_encoder/README.md

# 4. Work on the solution
cd exercises/url_encoder
# Edit main.py in your editor

# 5. Run tests
pytest test_main.py -v

# 6. If stuck, get hints
cd ../..
dsa hint url_encoder 1
# Continue working...

# 7. Check solution if needed
dsa solution url_encoder

# 8. Reset to try again
dsa reset url_encoder
```

## Understanding Test Output

```
test_url_encode_simple PASSED (0.0008s, 156 ops)
test_url_encode_special_chars PASSED (0.0012s, 234 ops)
test_url_decode PASSED (0.0009s, 189 ops)
test_round_trip PASSED (0.0015s, 312 ops)

Performance Summary:
- Average time: 0.0011s
- Total operations: 891
- Estimated complexity: O(n) time, O(n) space
```

## Common Patterns

### Two Pointers
```python
# Often used in arrays/strings
left, right = 0, len(nums) - 1
while left < right:
    # Process
    left += 1
    right -= 1
```

### Hash Map
```python
# Counting, grouping, caching
count = {}
for item in items:
    count[item] = count.get(item, 0) + 1
```

### BFS
```python
# Trees, graphs, shortest path
from collections import deque
queue = deque([start])
while queue:
    node = queue.popleft()
    # Process neighbors
    queue.extend(neighbors)
```

### DFS
```python
# Trees, graphs, backtracking
def dfs(node):
    if not node:
        return
    # Process
    dfs(node.left)
    dfs(node.right)
```

## Troubleshooting

**CLI not found?**
```bash
pip install -e exercise-cli/
```

**Tests failing?**
- Read test output carefully
- Check TODO comments in main.py
- Use hints progressively
- Look at edge cases

**Performance concerns?**
- Check time complexity of your approach
- Look for O(n²) that could be O(n)
- Consider using hash tables for lookups
- Check for unnecessary data copies

**Import errors?**
```bash
pip install -r requirements.txt
```

## Project Structure Reminder

```
python-dsa-exercises/
├── exercise-cli/          # CLI tool
│   └── dsa                # Main CLI module
├── exercises/             # All exercises (by topic)
│   ├── arrays_strings/
│   ├── linked_lists/
│   ├── stacks_queues/
│   ├── hash_tables/
│   ├── trees/
│   ├── graphs/
│   ├── heaps/
│   ├── recursion_dp/
│   └── sorting_searching/
├── solutions/             # Reference solutions
├── hints/                 # Hint files
├── README.md
├── QUICKSTART.md         # This file
└── requirements.txt
```

Each exercise has:
- `README.md` - Instructions
- `main.py` - Starter code (TODOs)
- `test_main.py` - Tests
- `hints.txt` - Progressive hints

Ready to start? Run `dsa list` and pick your first exercise!
