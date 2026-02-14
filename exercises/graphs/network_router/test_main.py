import pytest
from main import bfs_shortest_path


class TestBFSShortestPath:
    """Test suite for BFS shortest path."""
    
    def test_direct_path(self):
        """Test direct edge between nodes."""
        graph = {0: [1], 1: [0]}
        assert bfs_shortest_path(graph, 0, 1) == [0, 1]
    
    def test_shortest_path_multiple(self):
        """Test shortest path when multiple paths exist."""
        graph = {
            0: [1, 2],
            1: [0, 3],
            2: [0, 3],
            3: [1, 2]
        }
        path = bfs_shortest_path(graph, 0, 3)
        # Should be [0, 1, 3] or [0, 2, 3]
        assert len(path) == 3
        assert path[0] == 0
        assert path[-1] == 3
    
    def test_no_path(self):
        """Test when no path exists."""
        graph = {
            0: [1],
            1: [0],
            2: [3],
            3: [2]
        }
        assert bfs_shortest_path(graph, 0, 2) == []
    
    def test_start_equals_end(self):
        """Test when start equals end."""
        graph = {0: [1], 1: [0]}
        assert bfs_shortest_path(graph, 0, 0) == [0]
    
    def test_single_node(self):
        """Test single node graph."""
        graph = {0: []}
        assert bfs_shortest_path(graph, 0, 0) == [0]
    
    def test_longer_path(self):
        """Test longer shortest path."""
        graph = {
            0: [1],
            1: [0, 2],
            2: [1, 3],
            3: [2, 4],
            4: [3]
        }
        path = bfs_shortest_path(graph, 0, 4)
        assert path == [0, 1, 2, 3, 4]
    
    def test_linear_graph(self):
        """Test linear graph."""
        graph = {
            0: [1],
            1: [0, 2],
            2: [1, 3],
            3: [2]
        }
        path = bfs_shortest_path(graph, 0, 3)
        assert path == [0, 1, 2, 3]


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "Network Router (Graphs) - DSA Exercises",
    ]
