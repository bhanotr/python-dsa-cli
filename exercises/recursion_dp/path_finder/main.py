from typing import Dict, List, Set


def find_all_paths(graph: Dict[int, List[int]], start: int, end: int) -> List[List[int]]:
    """
    Find all paths from start to end using DFS with backtracking.

    Args:
        graph: Adjacency list {node: [neighbors]}
        start: Starting node
        end: Target node

    Returns:
        List of all paths (each path is list of nodes)
    """
    # TODO: Implement DFS with backtracking
    # 1. Initialize result list
    # 2. Define recursive dfs function:
    #    - Parameters: current_node, current_path, visited
    #    - If current_node == end: add path to result
    #    - Otherwise: for each neighbor:
    #      - If not in visited:
    #        * Add to visited and path
    #        * Recurse
    #        * Backtrack: remove from visited and path
    # 3. Start DFS from start node
    # 4. Return result
    pass


def main():
    """Test the path finder with sample data."""
    print("Path Finder (Backtracking DFS)")
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
    
    # Find all paths
    tests = [(0, 4), (0, 3), (1, 4)]
    for start, end in tests:
        paths = find_all_paths(graph, start, end)
        print(f"\nAll paths from {start} to {end}:")
        for path in paths:
            print(f"  {' -> '.join(map(str, path))}")
        print(f"  Total: {len(paths)} path(s)")


if __name__ == "__main__":
    main()
