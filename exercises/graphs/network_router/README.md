# Exercise 12: Network Router (BFS Shortest Path)

## Meta Interview Pattern
This exercise is based on the **BFS** pattern and **Shortest Path** problems commonly asked at Meta. Similar to:
- **Shortest Path in Binary Matrix** - LeetCode 1091
- **Rotting Oranges** - LeetCode 994

## Task
Implement BFS to find the shortest path between two nodes in an unweighted graph. Return the path as a list of nodes.

## What you'll learn
- BFS algorithm for shortest path
- Queue-based traversal
- Path reconstruction
- Graph representation

## Instructions
Complete the functions in `main.py`:

1. **bfs_shortest_path(graph, start, end)** - Find shortest path
   - Graph is adjacency list: {node: [neighbor1, neighbor2, ...]}
   - Return list of nodes from start to end (inclusive)
   - Return empty list if no path exists

## Examples

```python
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2, 4],
    4: [3]
}
path = bfs_shortest_path(graph, 0, 4)
assert path == [0, 1, 3, 4]  # or [0, 2, 3, 4]
```

## Testing
Run tests with:
```bash
cd exercises/graphs/network_router
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test network_router
```

## Hints
If you get stuck, run:
```bash
dsa hint network_router [1|2|3]
```

## Concepts

### BFS for Shortest Path
- BFS explores level by level
- First time we reach target is shortest path
- Use queue to process nodes in order
- Track parent pointers for path reconstruction

### Path Reconstruction
- Store parent for each visited node
- Backtrack from end to start using parents
- Reverse to get path from start to end

## Time Complexity Analysis
- O(V + E) - Visit all vertices and edges in worst case

## Space Complexity
- O(V) for visited set and queue
