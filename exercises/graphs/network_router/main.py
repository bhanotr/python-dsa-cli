from collections import deque
from typing import Dict, List, Set, Optional


def bfs_shortest_path(graph: Dict[int, List[int]], start: int, end: int) -> List[int]:
    """
    Find the shortest path between start and end using BFS.

    Args:
        graph: Adjacency list {node: [neighbors]}
        start: Starting node
        end: Target node

    Returns:
        List of nodes representing the shortest path, empty if no path
    """
    # TODO: Implement BFS shortest path
    # 1. Check if start equals end
    # 2. Use deque for queue
    # 3. Track visited set
    # 4. Track parent dict: {child: parent}
    # 5. BFS loop:
    #    - Pop from queue
    #    - For each neighbor:
    #      - If not visited, mark visited, set parent, add to queue
    #      - If neighbor is end, break
    # 6. Reconstruct path by backtracking from end using parents
    # 7. Reverse path and return
    pass


def main():
    """Test the network router with sample data."""
    print("Network Router (BFS Shortest Path)")
    print("=" * 60)
    
    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2, 4],
        4: [3]
    }
    
    print("\nGraph:")
    for node, neighbors in graph.items():
        print(f"  {node} -> {neighbors}")
    
    # Find paths
    tests = [(0, 4), (0, 2), (1, 4), (4, 0)]
    for start, end in tests:
        path = bfs_shortest_path(graph, start, end)
        print(f"\nShortest path from {start} to {end}:")
        if path:
            print(f"  Path: {' -> '.join(map(str, path))}")
            print(f"  Length: {len(path) - 1}")
        else:
            print("  No path found")


if __name__ == "__main__":
    main()
