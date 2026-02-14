from collections import deque
from typing import List


def bfs_find_path(graph: List[List[int]], parent: List[int], source: int, sink: int) -> bool:
    """
    Find a path from source to sink using BFS in residual graph.

    Args:
        graph: Residual graph (adjacency matrix)
        parent: Array to store parent of each node
        source: Source node
        sink: Sink node

    Returns:
        True if path exists, False otherwise
    """
    # TODO: Implement BFS to find path
    # 1. Initialize visited set
    # 2. Use queue for BFS
    # 3. For each node, find neighbors with capacity > 0
    # 4. Track parent to reconstruct path
    # 5. Return True if sink reached, False otherwise
    pass


def max_flow_edmonds_karp(graph: List[List[int]], source: int, sink: int) -> int:
    """
    Find the maximum flow from source to sink using Edmonds-Karp.

    Args:
        graph: Adjacency matrix of capacities
        source: Source node
        sink: Sink node

    Returns:
        Maximum flow value
    """
    # TODO: Implement Edmonds-Karp algorithm
    # 1. Create residual graph as copy of original
    # 2. Initialize max_flow = 0
    # 3. While BFS finds path from source to sink:
    #    a. Find minimum capacity along path (bottleneck)
    #    b. Update residual capacities along path
    #    c. Update reverse edges
    #    d. Add bottleneck to max_flow
    # 4. Return max_flow
    pass


def main():
    """Test the max flow algorithm with sample data."""
    print("Network Flow Graph (Max Flow)")
    print("=" * 60)
    
    graph = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ]
    
    print("\nGraph capacities:")
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] > 0:
                print(f"  {i} -> {j} (capacity: {graph[i][j]})")
    
    source, sink = 0, 5
    flow = max_flow_edmonds_karp(graph, source, sink)
    
    print(f"\nMax flow from {source} to {sink}: {flow}")


if __name__ == "__main__":
    main()
