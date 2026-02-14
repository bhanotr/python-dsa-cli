import pytest
from main import mst_prim, build_sample_graph


class TestMSTPrim:
    """Test suite for MST Prim's algorithm."""
    
    def test_simple_graph(self):
        """Test MST on simple graph."""
        graph = {
            0: [(1, 10)],
            1: [(0, 10)]
        }
        assert mst_prim(graph, 0) == 10
    
    def test_triangle_graph(self):
        """Test MST on triangle graph."""
        graph = {
            0: [(1, 1), (2, 2)],
            1: [(0, 1), (2, 1)],
            2: [(0, 2), (1, 1)]
        }
        # MST should pick edges with weights 1 and 1
        assert mst_prim(graph, 0) == 2
    
    def test_sample_graph(self):
        """Test MST on sample graph."""
        graph = build_sample_graph()
        # MST: 0-2 (1), 2-1 (2), 1-3 (1) = total 4
        # Or: 0-2 (1), 2-1 (2), 1-3 (1)
        weight = mst_prim(graph, 0)
        assert weight == 4
    
    def test_disconnected_graph(self):
        """Test that algorithm handles disconnected components."""
        graph = {
            0: [(1, 1)],
            1: [(0, 1)],
            2: [(3, 1)],
            3: [(2, 1)]
        }
        # Should only connect the component with start node
        weight = mst_prim(graph, 0)
        assert weight == 1
    
    def test_empty_graph(self):
        """Test MST on empty graph."""
        graph = {}
        assert mst_prim(graph, 0) == 0
    
    def test_single_node(self):
        """Test MST on single node."""
        graph = {0: []}
        assert mst_prim(graph, 0) == 0
    
    def test_different_start_nodes(self):
        """Test that different start nodes give same weight."""
        graph = {
            0: [(1, 1), (2, 2)],
            1: [(0, 1), (2, 1)],
            2: [(0, 2), (1, 1)]
        }
        weight_0 = mst_prim(graph, 0)
        weight_1 = mst_prim(graph, 1)
        weight_2 = mst_prim(graph, 2)
        assert weight_0 == weight_1 == weight_2 == 2


class TestGraphStructure:
    """Test suite for graph structure."""
    
    def test_build_sample_graph(self):
        """Test sample graph structure."""
        graph = build_sample_graph()
        assert 0 in graph
        assert 1 in graph
        assert 2 in graph
        assert 3 in graph
        assert len(graph) == 4


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "Spanning Tree (Trees) - DSA Exercises",
    ]
