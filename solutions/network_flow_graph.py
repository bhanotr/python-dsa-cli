from collections import deque
from typing import List


def bfs_find_path(graph: List[List[int]], parent: List[int], source: int, sink: int) -> bool:
    n = len(graph)
    visited = [False] * n
    queue = deque()
    queue.append(source)
    visited[source] = True
    parent[source] = -1
    
    while queue:
        u = queue.popleft()
        for v in range(n):
            if not visited[v] and graph[u][v] > 0:
                visited[v] = True
                parent[v] = u
                queue.append(v)
                if v == sink:
                    return True
    return False


def max_flow_edmonds_karp(graph: List[List[int]], source: int, sink: int) -> int:
    n = len(graph)
    residual = [row[:] for row in graph]
    parent = [-1] * n
    max_flow = 0
    
    while bfs_find_path(residual, parent, source, sink):
        path_flow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual[u][v])
            v = u
        
        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][u] += path_flow
            v = u
        
        max_flow += path_flow
    
    return max_flow


def main():
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
