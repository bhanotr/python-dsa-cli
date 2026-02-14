# Python DSA Exercises

A comprehensive practice set of data structures and algorithms exercises for Meta Network Production Engineer interviews, inspired by LeetCode's Meta interview questions.

## Features

- **29 exercises** covering all major DSA topics (17 networking + 12 general DSA)
- **Meta-style interview questions** from actual Meta interview patterns
- **Progressive hints** (3 levels) for each exercise
- **Performance logging** - See your solution's time/space complexity in action
- **Topic-based organization** - Group by DSA concept with varying difficulty
- **CLI tool** - Manage exercises, get hints, run tests, view solutions

## Quick Start

```bash
# Clone the repository
git clone git@github.com:bhanotr/python-dsa-cli.git
cd python-dsa-cli

# Install dependencies
pip install -r requirements.txt

# Install the CLI tool
pip install -e exercise-cli/

# Or install from anywhere
pip install -e /path/to/python-dsa-cli/exercise-cli/

# Verify installation
dsa --help
```

## Usage

```bash
# List all exercises
dsa list

# Start working on an exercise
dsa start packet_parser

# Get hints (progressive levels 1-3)
dsa hint packet_parser 1
dsa hint packet_parser 2
dsa hint packet_parser 3

# Test your solution with performance logging
dsa test packet_parser

# Show reference solution
dsa solution packet_parser

# Reset an exercise to initial state
dsa reset packet_parser
```

## Exercise Progression

### Topic 1: Arrays & Strings
1. **packet_parser** (Easy) - Parse network packet headers
2. **url_encoder** (Medium) - URL encode/decode

### Topic 2: Linked Lists
3. **network_flow** (Medium) - Flow tracking using linked list
4. **lru_cache_ll** (Medium-Hard) - LRU cache using doubly linked list

### Topic 3: Stacks & Queues
5. **request_queue** (Easy-Medium) - Network request queuing
6. **bracket_validator** (Medium) - Validate nested network configs

### Topic 4: Hash Tables
7. **dns_cache** (Medium) - DNS caching with TTL
8. **ip_classifier** (Medium) - IP address classification
9. **rate_limiter** (Medium-Hard) - Token bucket rate limiter

### Topic 5: Trees
10. **network_topology** (Medium) - Tree-based network representation
11. **spanning_tree** (Hard) - Minimum spanning tree

### Topic 6: Graphs
12. **network_router** (Medium-Hard) - Shortest path routing
13. **network_flow_graph** (Hard) - Max flow problem

### Topic 7: Heaps
14. **packet_scheduler** (Medium) - Priority-based packet scheduling

### Topic 8: Recursion & DP
15. **path_finder** (Medium) - Network path backtracking
16. **network_optimization** (Hard) - DP for bandwidth allocation

### Topic 9: Sorting & Searching
17. **log_analyzer** (Medium) - Binary search in time-series logs

## Meta Interview Topics Covered

- **Arrays & Strings** - String manipulation, two pointers, sliding window
- **Linked Lists** - Two pointers, cycle detection, LRU cache
- **Stacks & Queues** - Valid parentheses, monotonic stacks
- **Hash Tables** - Grouping, caching, rate limiting
- **Trees** - Binary trees, BST traversal, tree problems
- **Graphs** - BFS, DFS, shortest paths, graph traversal
- **Heaps** - Priority queues, K elements problems
- **Recursion & DP** - Backtracking, memoization, dynamic programming
- **Sorting & Searching** - Binary search, sorting algorithms

## Testing

Tests include:
- **Correctness tests** - Verify algorithm correctness
- **Edge case tests** - Empty inputs, boundaries, corner cases
- **Performance logging** - Time and space usage for your solutions

```bash
# Run all tests
dsa test packet_parser

# Or use pytest directly
cd exercises/packet_parser
pytest test_main.py -v
```

## Performance Logs

When you run tests, you'll see performance information:
```
Test: test_parse_valid_packet
✓ PASSED (0.0012s, 42 operations)
Complexity: O(n) time, O(1) space
```

## Tips for Success

1. **Start with hints** - Don't struggle too long before using hints
2. **Understand, don't copy** - Read solutions only after trying
3. **Analyze complexity** - Note the time/space complexity of your solutions
4. **Practice systematically** - Complete each topic before moving to the next
5. **Focus on patterns** - Meta often asks about recurring patterns

## Concepts Covered

- Two pointers technique
- Sliding window
- Hash maps and sets
- Tree and graph traversal
- Dynamic programming
- Backtracking
- Binary search
- Sorting algorithms
- Greedy algorithms
- Recursion

## Project Structure

```
python-dsa-exercises/
├── exercise-cli/          # CLI tool for managing exercises
├── exercises/             # All exercise directories (organized by topic)
├── solutions/             # Reference implementations
├── hints/                 # Hint files for all exercises
├── README.md             # This file
├── QUICKSTART.md        # Quick start guide
└── requirements.txt    # Python dependencies
```

Each exercise contains:
- `README.md` - Exercise instructions and concepts
- `main.py` - Starter code with TODO comments
- `test_main.py` - Unit tests with performance logging
- `hints.txt` - Progressive hints (3 levels)

## Learning Path

1. **Phase 1: Fundamentals** - Arrays, Strings, Linked Lists
2. **Phase 2: Linear Structures** - Stacks, Queues, Hash Tables
3. **Phase 3: Hierarchical** - Trees, Graphs
4. **Phase 4: Advanced** - Heaps, Recursion, DP, Sorting

Each topic builds on the previous, so work systematically through them!

## Meta Interview Preparation

These exercises cover patterns commonly seen in Meta interviews:
- **Two Sum** variations
- **Valid Parentheses**
- **LRU Cache**
- **Group Anagrams**
- **Top K Frequent**
- **Valid Palindrome**
- **Merge Intervals**
- **Binary Search** patterns
- **Tree Traversals**
- **Graph BFS/DFS**
- **Coin Change** DP problem
- **Word Search** backtracking

Good luck with your Meta interview preparation!
