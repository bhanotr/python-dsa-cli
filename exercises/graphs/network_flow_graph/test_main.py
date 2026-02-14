import pytest
from main import max_flow_edmonds_karp


class TestMaxFlow:
    """Test suite for max flow algorithm."""
    
    def test_simple_graph(self):
        """Test max flow on simple graph."""
        graph = [
            [0, 10, 0],
            [0, 0, 10],
            [0, 0, 0]
        ]
        assert max_flow_edmonds_karp(graph, 0, 2) == 10
    
    def test_parallel_paths(self):
        """Test graph with parallel paths."""
        graph = [
            [0, 5, 5, 0],
            [0, 0, 0, 5],
            [0, 0, 0, 5],
            [0, 0, 0, 0]
        ]
        # Two paths: 0->1->3 (5) and 0->2->3 (5)
        assert max_flow_edmonds_karp(graph, 0, 3) == 10
    
    def test_sample_graph(self):
        """Test on sample graph."""
        graph = [
            [0, 16, 13, 0, 0, 0],
            [0, 0, 10, 12, 0, 0],
            [0, 4, 0, 0, 14, 0],
            [0, 0, 9, 0, 0, 20],
            [0, 0, 0, 7, 0, 4],
            [0, 0, 0, 0, 0, 0]
        ]
        assert max_flow_edmonds_karp(graph, 0, 5) == 23
    
    def test_no_path(self):
        """Test when no path exists."""
        graph = [
            [0, 10, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        assert max_flow_edmonds_karp(graph, 0, 2) == 0
    
    def test_source_equals_sink(self):
        """Test when source equals sink."""
        graph = [
            [0, 10],
            [0, 0]
        ]
        assert max_flow_edmonds_karp(graph, 0, 0) == 0
    
    def test_bottleneck_edge(self):
        """Test graph with bottleneck edge."""
        graph = [
            [0, 10, 10, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 1],
            [0, 0, 0, 0]
        ]
        # Bottleneck is 1 on edges to sink
        assert max_flow_edmonds_karp(graph, 0, 3) == 2


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "Network Flow Graph (Graphs) - DSA Exercises",
    ]
