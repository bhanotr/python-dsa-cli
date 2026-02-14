from typing import Dict, List, Set


def find_all_paths(graph: Dict[int, List[int]], start: int, end: int) -> List[List[int]]:
    result = []
    
    def dfs(current: int, path: List[int], visited: Set[int]):
        path.append(current)
        visited.add(current)
        
        if current == end:
            result.append(path.copy())
        else:
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    dfs(neighbor, path, visited)
        
        path.pop()
        visited.remove(current)
    
    dfs(start, [], set())
    return result


def main():
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
    
    tests = [(0, 4), (0, 3), (1, 4)]
    for start, end in tests:
        paths = find_all_paths(graph, start, end)
        print(f"\nAll paths from {start} to {end}:")
        for path in paths:
            print(f"  {' -> '.join(map(str, path))}")
        print(f"  Total: {len(paths)} path(s)")


if __name__ == "__main__":
    main()
