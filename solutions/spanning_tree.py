import heapq
from typing import Dict, List, Tuple


def mst_prim(graph: Dict[int, List[Tuple[int, int]]], start: int) -> int:
    if not graph:
        return 0
    
    visited = set()
    total_weight = 0
    heap = []
    
    for neighbor, weight in graph.get(start, []):
        heapq.heappush(heap, (weight, start, neighbor))
    
    visited.add(start)
    
    while heap and len(visited) < len(graph):
        weight, from_node, to_node = heapq.heappop(heap)
        
        if to_node not in visited:
            visited.add(to_node)
            total_weight += weight
            
            for neighbor, edge_weight in graph.get(to_node, []):
                if neighbor not in visited:
                    heapq.heappush(heap, (edge_weight, to_node, neighbor))
    
    return total_weight


def build_sample_graph() -> Dict[int, List[Tuple[int, int]]]:
    return {
        0: [(1, 4), (2, 1)],
        1: [(0, 4), (2, 2), (3, 1)],
        2: [(0, 1), (1, 2), (3, 5)],
        3: [(1, 1), (2, 5)]
    }


def main():
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
