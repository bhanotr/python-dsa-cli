# Exercise 13: Network Flow Graph (Max Flow)

## Meta Interview Pattern
This exercise is based on the **Max Flow** pattern and **Ford-Fulkerson/Edmonds-Karp** algorithms commonly asked at Meta. Similar to:
- **Network flow problems**
- **Max matching problems**

## Task
Implement Edmonds-Karp algorithm to find the maximum flow from source to sink in a weighted graph.

## What you'll learn
- Edmonds-Karp algorithm (BFS-based Ford-Fulkerson)
- Residual graphs
- Finding augmenting paths
- Network flow concepts

## Instructions
Complete the functions in `main.py`:

1. **max_flow_edmonds_karp(graph, source, sink)** - Find max flow
   - Graph is adjacency matrix: [[capacity], ...]
   - Return maximum flow from source to sink

## Examples

```python
graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]
flow = max_flow_edmonds_karp(graph, 0, 5)
assert flow == 23
```

## Testing
Run tests with:
```bash
cd exercises/graphs/network_flow_graph
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test network_flow_graph
```

## Hints
If you get stuck, run:
```bash
dsa hint network_flow_graph [1|2|3]
```

## Concepts

### Edmonds-Karp Algorithm
- BFS-based Ford-Fulkerson
- Find augmenting paths in residual graph
- Update capacities along path
- Sum of all augmenting path flows = max flow

### Residual Graph
- Tracks remaining capacity on each edge
- Also tracks reverse edges for flow cancellation
- Initially same as original graph

## Time Complexity Analysis
- O(V * E^2) - Each BFS is O(E),最多O(VE) augmentations

## Space Complexity
- O(V^2) for adjacency matrix
