# Python DSA Exercises - Project Summary

## ✅ Project Created Successfully!

A complete set of Data Structures and Algorithms practice exercises for Meta Network Production Engineer interviews has been created.

## 📊 Project Statistics

- **Total Exercises**: 17
- **Topics Covered**: 9 major DSA topics
- **Difficulty Levels**: Easy to Hard
- **Total Files Created**: 68+ files

## 📁 Project Structure

```
python-dsa-exercises/
├── exercise-cli/              # CLI tool for managing exercises
│   ├── dsa/__init__.py      # Main CLI implementation
│   ├── pyproject.toml        # CLI package config
│   └── setup.py            # Setup script
│
├── exercises/                 # All exercise directories (by topic)
│   ├── arrays_strings/       # 2 exercises
│   ├── linked_lists/         # 2 exercises
│   ├── stacks_queues/        # 2 exercises
│   ├── hash_tables/          # 3 exercises
│   ├── trees/               # 2 exercises
│   ├── graphs/              # 2 exercises
│   ├── heaps/               # 1 exercise
│   ├── recursion_dp/         # 2 exercises
│   └── sorting_searching/    # 1 exercise
│
├── solutions/                 # 16 reference solutions
├── hints/                    # 16 hint files (3 levels each)
├── README.md                # Main documentation
├── QUICKSTART.md           # Quick start guide
└── requirements.txt        # Python dependencies
```

## 📚 Exercises Created

### Topic 1: Arrays & Strings (2 exercises)
1. **packet_parser** (Easy) - Parse network packet headers
2. **url_encoder** (Medium) - URL encode/decode strings

### Topic 2: Linked Lists (2 exercises)
3. **network_flow** (Medium) - Flow tracking using linked list
4. **lru_cache_ll** (Medium-Hard) - LRU cache using doubly linked list

### Topic 3: Stacks & Queues (2 exercises)
5. **request_queue** (Easy-Medium) - Network request queuing
6. **bracket_validator** (Medium) - Validate nested network configs

### Topic 4: Hash Tables (3 exercises)
7. **dns_cache** (Medium) - DNS caching with TTL
8. **ip_classifier** (Medium) - IP address classification
9. **rate_limiter** (Medium-Hard) - Token bucket rate limiter

### Topic 5: Trees (2 exercises)
10. **network_topology** (Medium) - Tree-based network representation
11. **spanning_tree** (Hard) - Minimum spanning tree

### Topic 6: Graphs (2 exercises)
12. **network_router** (Medium-Hard) - Shortest path routing
13. **network_flow_graph** (Hard) - Max flow problem

### Topic 7: Heaps (1 exercise)
14. **packet_scheduler** (Medium) - Priority-based packet scheduling

### Topic 8: Recursion & DP (2 exercises)
15. **path_finder** (Medium) - Network path backtracking
16. **network_optimization** (Hard) - DP for bandwidth allocation

### Topic 9: Sorting & Searching (1 exercise)
17. **log_analyzer** (Medium) - Binary search in time-series logs

## 🎯 Meta Interview Patterns Covered

- **Two Pointers** - String manipulation, array traversal
- **Linked List Operations** - Reversal, insertion, deletion
- **Stack Applications** - Valid parentheses, monotonic stacks
- **Hash Map Patterns** - Grouping, caching, rate limiting
- **Tree Traversals** - In-order, pre-order, post-order
- **Graph Algorithms** - BFS, DFS, shortest paths
- **Heap Operations** - Priority queues, top-K elements
- **Recursion & Backtracking** - Path finding, permutations
- **Dynamic Programming** - Optimization, memoization
- **Binary Search** - Searching in sorted data
- **LRU Cache Design** - Classic Meta problem
- **Graph Algorithms** - MST, max flow

## 🚀 Quick Start

### 1. List all exercises
```bash
dsa list
```

### 2. Start an exercise
```bash
dsa start bracket_validator
```

### 3. Get hints (3 levels)
```bash
dsa hint bracket_validator --level 1
dsa hint bracket_validator --level 2
dsa hint bracket_validator --level 3
```

### 4. Run tests
```bash
dsa test bracket_validator
```

### 5. View solution
```bash
dsa solution bracket_validator
```

## 📝 Exercise Structure

Each exercise includes:
- **README.md** - Instructions, concepts, Meta pattern reference
- **main.py** - Starter code with TODO comments
- **test_main.py** - Comprehensive pytest tests
- **hints.txt** - 3 progressive hint levels (General → Detailed)

## 🧪 Testing

Tests include:
- **Correctness tests** - Verify algorithm correctness
- **Edge case tests** - Empty inputs, boundaries, corner cases
- **Integration tests** - Test combined operations

Run tests individually:
```bash
cd exercises/{topic}/{exercise}
pytest test_main.py -v
```

## 💡 Features

- ✅ **17 complete exercises** covering all major DSA topics
- ✅ **Meta-specific patterns** - Based on actual interview questions
- ✅ **Progressive hints** - 3 levels for each exercise
- ✅ **Comprehensive tests** - Edge cases and integration tests
- ✅ **CLI tool** - Easy management of exercises
- ✅ **Reference solutions** - Working implementations for learning
- ✅ **Topic-based organization** - Grouped by DSA concept
- ✅ **Difficulty progression** - Easy → Medium → Hard

## 🎓 Recommended Learning Path

### Phase 1: Fundamentals (Exercises 1-4)
Start with basic data structures and algorithms:
1. packet_parser - Arrays & parsing
2. url_encoder - String manipulation
3. network_flow - Linked list basics
4. lru_cache_ll - Complex linked lists

### Phase 2: Linear Structures (Exercises 5-9)
Master stacks, queues, and hash tables:
5. request_queue - Queue operations
6. bracket_validator - Stack pattern
7. dns_cache - Hash table caching
8. ip_classifier - Hash table grouping
9. rate_limiter - Advanced hash tables

### Phase 3: Hierarchical Structures (Exercises 10-13)
Trees and graphs:
10. network_topology - Tree basics
11. spanning_tree - Tree algorithms
12. network_router - Graph traversal
13. network_flow_graph - Advanced graphs

### Phase 4: Advanced (Exercises 14-17)
Advanced algorithms:
14. packet_scheduler - Heaps & priority queues
15. path_finder - Recursion & backtracking
16. network_optimization - Dynamic programming
17. log_analyzer - Binary search

## 📚 Key Concepts to Master

### Must Know
- Arrays & Strings manipulation
- Hash tables and hash maps
- Linked list operations
- Stack and queue operations
- Tree traversals (BFS, DFS)

### Should Know
- Binary search patterns
- Heaps and priority queues
- Graph algorithms (shortest path, MST)
- Dynamic programming basics
- Recursion and backtracking

### Nice to Have
- Advanced graph algorithms (max flow)
- Complex DP patterns
- Advanced tree operations

## 🔧 Troubleshooting

**CLI not found?**
```bash
pip install -e /home/ritwik/python-dsa-exercises/exercise-cli/
```

**Tests failing?**
- Read test output carefully
- Check TODO comments in main.py
- Use hints progressively
- Look at edge cases

**Import errors?**
```bash
pip install -r /home/ritwik/python-dsa-exercises/requirements.txt
```

## 📖 Additional Resources

- **README.md** - Full documentation
- **QUICKSTART.md** - Quick start guide
- **LeetCode** - Practice additional problems
- **Meta Interview Guide** - Interview preparation tips

## 🎯 Success Tips

1. **Work systematically** - Complete each topic before moving on
2. **Use hints wisely** - Don't struggle too long before using hints
3. **Understand patterns** - Focus on recurring patterns, not just solutions
4. **Analyze complexity** - Note time/space complexity of your solutions
5. **Practice regularly** - Consistent practice is key to mastery

## 📊 Progress Tracking

The CLI tracks your progress automatically:
- `dsa list` shows completion status (✓ or ○)
- Completed exercises show ✓ mark
- In-progress exercises show ○ mark

---

**Good luck with your Meta interview preparation! 🚀**
