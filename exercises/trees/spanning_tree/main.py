import heapq
from typing import Dict, List, Tuple, Set


def mst_prim(graph: Dict[int, List[Tuple[int, int]]], start: int) -> int:
    """
    Find the minimum spanning tree using Prim's algorithm.

    Args:
        graph: Adjacency list {node: [(neighbor, weight), ...]}
        start: Starting node for MST

    Returns:
        Total weight of the MST
    """
    # TODO: Implement Prim's algorithm
    # 1. Initialize visited set
    # 2. Use priority queue to track edges (weight, from, to)
    # 3. Add all edges from start to queue
    # 4. While queue not empty:
    #    - Pop min weight edge
    #    - If to_node not visited:
    #      - Mark visited
    #      - Add weight to total
    #      - Add all edges from to_node to queue
    # 5. Return total weight
    pass


def build_sample_graph() -> Dict[int, List[Tuple[int, int]]]:
    """
    Build a sample graph for testing.

    Returns:
        Adjacency list representation of graph
    """
    return {
        0: [(1, 4), (2, 1)],
        1: [(0, 4), (2, 2), (3, 1)],
        2: [(0, 1), (1, 2), (3, 5)],
        3: [(1, 1), (2, 5)]
    }


def main():
    """Test the MST algorithm with sample data."""
    print("Minimum Spanning Tree (Prim's Algorithm)")
    print("=" * 60)
    
    graph = build_sample_graph()
    
    print("\nGraph:")
    for node, edges in graph.items():
        for neighbor, weight in edges:
            print(f"  {node} --({weight})-- {neighbor}")
    
    start_node = 0
    mst_weight = mst_prim(graph, start_node)
    
    print(f"\nStarting from node {start_node}")
    print(f"MST Total Weight: {mst_weight}")


if __name__ == "__main__":
    main()
