from collections import deque
from typing import Dict, List


def bfs_shortest_path(graph: Dict[int, List[int]], start: int, end: int) -> List[int]:
    if start == end:
        return [start]
    
    visited = set([start])
    queue = deque([start])
    parent = {}
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
                
                if neighbor == end:
                    path = [end]
                    node = end
                    while node != start:
                        node = parent[node]
                        path.append(node)
                    return path[::-1]
    
    return []


def main():
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
