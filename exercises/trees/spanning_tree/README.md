# Exercise 11: Spanning Tree (MST)

## Meta Interview Pattern
This exercise is based on the **Minimum Spanning Tree** pattern and **Graph Algorithms** commonly asked at Meta. Similar to:
- **Minimum Spanning Tree** - LeetCode (Premium)
- **Network connectivity problems**

## Task
Implement Prim's algorithm to find the Minimum Spanning Tree (MST) of a weighted graph. Return the total weight of the MST.

## What you'll learn
- Prim's algorithm for MST
- Priority queue for greedy selection
- Graph representation
- Minimum cut concepts

## Instructions
Complete the functions in `main.py`:

1. **mst_prim(graph, start)** - Find MST using Prim's
   - Return total weight of MST
   - Graph is adjacency list: {node: [(neighbor, weight), ...]}

## Examples

```python
graph = {
    0: [(1, 10), (2, 6)],
    1: [(0, 10), (2, 5)],
    2: [(0, 6), (1, 5)]
}
mst_weight = mst_prim(graph, 0)
# MST would have edges with weights 6 and 5, total = 11
```

## Testing
Run tests with:
```bash
cd exercises/trees/spanning_tree
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test spanning_tree
```

## Hints
If you get stuck, run:
```bash
dsa hint spanning_tree [1|2|3]
```

## Concepts

### Prim's Algorithm
1. Start from arbitrary node
2. Add all edges from current node to priority queue
3. Pick minimum weight edge to unvisited node
4. Add to MST, mark visited
5. Repeat until all nodes visited

### Priority Queue
- Use heapq for efficient min extraction
- Store (weight, current_node, next_node)

## Time Complexity Analysis
- Prim's with heap: O(E log V) where E = edges, V = vertices

## Space Complexity
- O(V + E) for graph and visited set
