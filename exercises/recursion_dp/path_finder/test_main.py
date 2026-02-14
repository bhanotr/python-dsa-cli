import pytest
from main import find_all_paths


class TestFindAllPaths:
    """Test suite for find_all_paths."""
    
    def test_direct_path(self):
        """Test direct edge between nodes."""
        graph = {0: [1], 1: [0]}
        paths = find_all_paths(graph, 0, 1)
        assert len(paths) == 1
        assert paths[0] == [0, 1]
    
    def test_multiple_paths(self):
        """Test multiple paths between nodes."""
        graph = {
            0: [1, 2],
            1: [3],
            2: [3],
            3: []
        }
        paths = find_all_paths(graph, 0, 3)
        assert len(paths) == 2
        assert [0, 1, 3] in paths
        assert [0, 2, 3] in paths
    
    def test_no_path(self):
        """Test when no path exists."""
        graph = {
            0: [1],
            1: [0],
            2: [3],
            3: [2]
        }
        paths = find_all_paths(graph, 0, 2)
        assert len(paths) == 0
    
    def test_start_equals_end(self):
        """Test when start equals end."""
        graph = {0: [1], 1: [0]}
        paths = find_all_paths(graph, 0, 0)
        assert paths == [[0]]
    
    def test_acyclic_graph(self):
        """Test acyclic graph."""
        graph = {
            0: [1],
            1: [2],
            2: [3],
            3: []
        }
        paths = find_all_paths(graph, 0, 3)
        assert len(paths) == 1
        assert paths[0] == [0, 1, 2, 3]
    
    def test_graph_with_cycles(self):
        """Test graph with cycles (should avoid revisiting)."""
        graph = {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1, 3],
            3: [2]
        }
        paths = find_all_paths(graph, 0, 3)
        # Should find paths without cycles
        for path in paths:
            assert path[0] == 0
            assert path[-1] == 3
            assert len(path) == len(set(path))  # No duplicates


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "Path Finder (Recursion/DP) - DSA Exercises",
    ]
