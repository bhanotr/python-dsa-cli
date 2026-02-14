# Exercise 15: Path Finder (Backtracking)

## Meta Interview Pattern
This exercise is based on the **Backtracking** pattern and **DFS** problems commonly asked at Meta. Similar to:
- **All Paths From Source to Target** - LeetCode 797
- **Combination Sum** - LeetCode 39

## Task
Implement DFS with backtracking to find all paths between two nodes in a graph. Avoid cycles.

## What you'll learn
- Backtracking algorithm
- Depth-first search (DFS)
- Finding all paths in graph
- Cycle detection and avoidance

## Instructions
Complete the functions in `main.py`:

1. **find_all_paths(graph, start, end)** - Find all paths
   - Graph is adjacency list: {node: [neighbor1, neighbor2, ...]}
   - Return list of all paths (each path is list of nodes)
   - Avoid revisiting nodes in current path

## Examples

```python
graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}
paths = find_all_paths(graph, 0, 3)
# paths = [[0, 1, 3], [0, 2, 3]]
```

## Testing
Run tests with:
```bash
cd exercises/recursion_dp/path_finder
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test path_finder
```

## Hints
If you get stuck, run:
```bash
dsa hint path_finder [1|2|3]
```

## Concepts

### Backtracking
- Build solution incrementally
- Explore all possibilities
- Backtrack when can't continue
- Track current path state

### DFS for Paths
- Start from source
- Recursively explore neighbors
- Track visited nodes (in current path)
- When reaching target, record path
- Backtrack by removing node from path

## Time Complexity Analysis
- O((V+E) * P) where P is number of paths

## Space Complexity
- O(V) for recursion depth and path storage
