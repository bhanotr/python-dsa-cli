# New General DSA Exercises - Summary

## ✅ Successfully Added 12 New Exercises!

All exercises are **LeetCode-style algorithmic problems** (not networking-specific) commonly asked at Meta and other top tech companies.

## 📊 Project Statistics

**Total Exercises**: 29
- **17 Networking DSA exercises** (original)
- **12 General DSA exercises** (newly added)
- **Difficulty**: Easy & Medium
- **Topics**: Arrays & Strings, Hash Maps & Sets, Sorting & Searching

## 📁 New Exercises Created

### Arrays & Strings (3 exercises)
18. **valid_palindrome** (Easy) - LeetCode 125
   - Check if string is palindrome
   - Two pointer technique
   - Ignore non-alphanumeric, case-insensitive

19. **best_time_buy_sell** (Easy) - LeetCode 121
   - Best time to buy and sell stock
   - Single transaction
   - Find maximum profit

20. **remove_duplicates** (Easy) - LeetCode 26
   - Remove duplicates from sorted array
   - In-place removal
   - Two pointer technique

### Hash Maps & Sets (5 exercises)
21. **two_sum** (Easy) - LeetCode 1
   - Find two numbers that sum to target
   - Hash map for O(n) solution
   - Complement pattern

22. **contains_duplicate** (Easy) - LeetCode 217
   - Check if array contains duplicates
   - Hash set for O(n) solution
   - Return True/False

23. **group_anagrams** (Medium) - LeetCode 49
   - Group strings that are anagrams
   - Hash map with sorted string as key
   - List of groups

24. **top_k_frequent** (Medium) - LeetCode 347
   - Find k most frequent elements
   - Hash map for counting
   - Return top k elements

25. **longest_consecutive** (Medium) - LeetCode 128
   - Find longest consecutive sequence
   - Hash set for O(n) solution
   - Return length

### Sorting & Searching (4 exercises)
26. **find_first_last** (Medium) - LeetCode 34
   - Find first and last position in sorted array
   - Binary search twice
   - Return [first, last]

27. **merge_intervals** (Medium) - LeetCode 56
   - Merge overlapping intervals
   - Sort then merge
   - Return merged intervals

28. **product_except_self** (Medium) - LeetCode 238
   - Product of array except self
   - Cannot use division
   - O(n) time, O(1) space

29. **maximum_subarray** (Medium) - LeetCode 53
   - Maximum subarray sum
   - Kadane's algorithm
   - O(n) solution

## 🎯 Complete Exercise List (29 Total)

### Phase 1: Networking DSA (1-17)
1. packet_parser - Arrays & Strings (Easy)
2. url_encoder - Arrays & Strings (Medium)
3. network_flow - Linked Lists (Medium)
4. lru_cache_ll - Linked Lists (Medium-Hard)
5. request_queue - Stacks & Queues (Easy-Medium)
6. bracket_validator - Stacks & Queues (Medium)
7. dns_cache - Hash Tables (Medium)
8. ip_classifier - Hash Tables (Medium)
9. rate_limiter - Hash Tables (Medium-Hard)
10. network_topology - Trees (Medium)
11. spanning_tree - Trees (Hard)
12. network_router - Graphs (Medium-Hard)
13. network_flow_graph - Graphs (Hard)
14. packet_scheduler - Heaps (Medium)
15. path_finder - Recursion & DP (Medium)
16. network_optimization - Recursion & DP (Hard)
17. log_analyzer - Sorting & Searching (Medium)

### Phase 2: General DSA (18-29)
18. valid_palindrome - Arrays & Strings (Easy)
19. best_time_buy_sell - Arrays & Strings (Easy)
20. remove_duplicates - Arrays & Strings (Easy)
21. two_sum - Hash Maps & Sets (Easy)
22. contains_duplicate - Hash Maps & Sets (Easy)
23. group_anagrams - Hash Maps & Sets (Medium)
24. top_k_frequent - Hash Maps & Sets (Medium)
25. longest_consecutive - Hash Maps & Sets (Medium)
26. find_first_last - Sorting & Searching (Medium)
27. merge_intervals - Sorting & Searching (Medium)
28. product_except_self - Sorting & Searching (Medium)
29. maximum_subarray - Sorting & Searching (Medium)

## 🎓 Meta Interview Patterns Covered

### New Patterns (Exercises 18-29)
- **Two Pointers** - Valid palindrome, Remove duplicates
- **Hash Map/Complement** - Two Sum
- **Hash Set** - Contains duplicate, Longest consecutive
- **Hash Map Grouping** - Group anagrams, Top K frequent
- **Binary Search** - Find first/last position
- **Sorting + Merging** - Merge intervals
- **Prefix/Postfix Products** - Product except self
- **Kadane's Algorithm** - Maximum subarray
- **Greedy** - Best time to buy/sell stock

### Existing Patterns (Exercises 1-17)
- All previous patterns from networking exercises

## 📝 Each Exercise Includes

✅ `README.md` - Instructions, Meta pattern reference, concepts
✅ `main.py` - Starter code with TODO comments
✅ `test_main.py` - Comprehensive pytest tests
✅ `hints/{exercise}.txt` - 3 progressive hint levels
✅ `solutions/{exercise}.py` - Complete reference solution

## 🚀 Usage

```bash
# List all 29 exercises
dsa list

# Start a general DSA exercise
dsa start two_sum

# Get hints
dsa hint two_sum --level 1
dsa hint two_sum --level 2
dsa hint two_sum --level 3

# Run tests
dsa test two_sum

# View solution
dsa solution two_sum
```

## 🎯 Focus Areas

### Easy Exercises (8)
- Arrays: valid_palindrome, best_time_buy_sell, remove_duplicates
- Hash Maps: two_sum, contains_duplicate

### Medium Exercises (7)
- Hash Maps: group_anagrams, top_k_frequent, longest_consecutive
- Sorting/Searching: find_first_last, merge_intervals, product_except_self, maximum_subarray

### Key Techniques Covered

#### Arrays & Strings
- Two pointers
- In-place modifications
- String manipulation
- Character validation

#### Hash Maps & Sets
- Complement pattern
- Frequency counting
- Grouping patterns
- O(1) lookups

#### Sorting & Searching
- Binary search
- Sorting algorithms
- Interval merging
- Dynamic programming (Kadane's)

## 💡 Why These Exercises?

1. **Most Frequently Asked** - All are from LeetCode's Meta interview question bank
2. **Foundational Patterns** - Teach core DSA concepts
3. **Progressive Difficulty** - Build from Easy to Medium
4. **Real Applications** - Problems you'll actually see in interviews
5. **Multiple Approaches** - Understand trade-offs (brute force vs optimized)

## 📚 Recommended Learning Path

### Quick Start (Exercises 18-20)
Start with Easy exercises:
18. valid_palindrome - Warm up two pointers
19. best_time_buy_sell - Simple greedy
20. remove_duplicates - Two pointers in arrays

### Hash Map Mastery (Exercises 21-25)
Master hash map/set patterns:
21. two_sum - Complement pattern (THE classic!)
22. contains_duplicate - Set usage
23. group_anagrams - Hash map grouping
24. top_k_frequent - Frequency counting
25. longest_consecutive - Set operations

### Advanced Arrays (Exercises 26-29)
More complex array operations:
26. find_first_last - Binary search
27. merge_intervals - Sorting + merging
28. product_except_self - Prefix/postfix pattern
29. maximum_subarray - Kadane's algorithm

## 🎓 Success Metrics

After completing all 29 exercises, you'll have mastered:
- ✅ **29 different algorithms** and patterns
- ✅ **All major DSA topics** (Arrays, Lists, Stacks, Queues, Hash Tables, Trees, Graphs, Heaps, DP, Sorting, Searching)
- ✅ **Meta-specific questions** - Most frequently asked at Meta
- ✅ **Performance analysis** - Understanding time/space complexity
- ✅ **Problem-solving skills** - Multiple approaches and trade-offs

## 🔧 Complete File Structure

```
python-dsa-exercises/
├── exercise-cli/           # CLI tool
├── exercises/
│   ├── arrays_strings/     # 5 exercises (2 networking + 3 general)
│   ├── linked_lists/       # 2 exercises (networking)
│   ├── stacks_queues/      # 2 exercises (networking)
│   ├── hash_tables/        # 5 exercises (3 networking + 2 general)
│   ├── trees/             # 2 exercises (networking)
│   ├── graphs/            # 2 exercises (networking)
│   ├── heaps/             # 1 exercise (networking)
│   ├── recursion_dp/       # 2 exercises (networking)
│   ├── sorting_searching/  # 1 exercise (networking)
│   └── general_dsa/       # 12 NEW exercises (general DSA)
├── hints/                  # 29 hint files
├── solutions/               # 29 solution files
├── README.md
├── QUICKSTART.md
└── SUMMARY.md
```

---

**Total: 29 DSA exercises ready for your Meta interview preparation! 🚀**

Good luck with your studies!
