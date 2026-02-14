import pytest
from main import NetworkTopology, TreeNode


class TestTreeNode:
    """Test suite for TreeNode class."""
    
    def test_node_creation(self):
        """Test creating a tree node."""
        node = TreeNode(1, "10.0.0.1")
        assert node.device_id == 1
        assert node.ip == "10.0.0.1"
        assert node.left is None
        assert node.right is None


class TestInsert:
    """Test suite for insert operation."""
    
    def test_insert_root(self):
        """Test inserting root node."""
        tree = NetworkTopology()
        tree.insert(1, "10.0.0.1")
        assert tree.root is not None
        assert tree.root.device_id == 1
    
    def test_insert_left(self):
        """Test inserting left child."""
        tree = NetworkTopology()
        tree.insert(10, "10.0.0.10")
        tree.insert(5, "10.0.0.5")
        assert tree.root.left is not None
        assert tree.root.left.device_id == 5
    
    def test_insert_right(self):
        """Test inserting right child."""
        tree = NetworkTopology()
        tree.insert(10, "10.0.0.10")
        tree.insert(15, "10.0.0.15")
        assert tree.root.right is not None
        assert tree.root.right.device_id == 15
    
    def test_insert_multiple(self):
        """Test inserting multiple nodes."""
        tree = NetworkTopology()
        for i in [50, 30, 70, 20, 40, 60, 80]:
            tree.insert(i, f"10.0.0.{i}")
        assert tree.get_depth() >= 3


class TestFind:
    """Test suite for find operation."""
    
    def test_find_root(self):
        """Test finding root."""
        tree = NetworkTopology()
        tree.insert(1, "10.0.0.1")
        node = tree.find(1)
        assert node is not None
        assert node.device_id == 1
    
    def test_find_left_child(self):
        """Test finding left child."""
        tree = NetworkTopology()
        tree.insert(10, "10.0.0.10")
        tree.insert(5, "10.0.0.5")
        node = tree.find(5)
        assert node is not None
        assert node.ip == "10.0.0.5"
    
    def test_find_nonexistent(self):
        """Test finding non-existent node."""
        tree = NetworkTopology()
        tree.insert(1, "10.0.0.1")
        node = tree.find(99)
        assert node is None
    
    def test_find_empty_tree(self):
        """Test finding in empty tree."""
        tree = NetworkTopology()
        node = tree.find(1)
        assert node is None


class TestInorderTraversal:
    """Test suite for in-order traversal."""
    
    def test_inorder_single_node(self):
        """Test in-order traversal with single node."""
        tree = NetworkTopology()
        tree.insert(1, "10.0.0.1")
        result = tree.inorder_traversal()
        assert result == [(1, "10.0.0.1")]
    
    def test_inorder_sorted(self):
        """Test that in-order gives sorted order."""
        tree = NetworkTopology()
        for i in [50, 30, 70, 20, 40]:
            tree.insert(i, f"10.0.0.{i}")
        result = tree.inorder_traversal()
        device_ids = [d[0] for d in result]
        assert device_ids == [20, 30, 40, 50, 70]
    
    def test_inorder_empty(self):
        """Test in-order traversal of empty tree."""
        tree = NetworkTopology()
        assert tree.inorder_traversal() == []


class TestPreorderTraversal:
    """Test suite for pre-order traversal."""
    
    def test_preorder_single_node(self):
        """Test pre-order traversal with single node."""
        tree = NetworkTopology()
        tree.insert(1, "10.0.0.1")
        result = tree.preorder_traversal()
        assert result == [(1, "10.0.0.1")]
    
    def test_preorder_structure(self):
        """Test pre-order traversal order."""
        tree = NetworkTopology()
        for i in [50, 30, 70]:
            tree.insert(i, f"10.0.0.{i}")
        result = tree.preorder_traversal()
        device_ids = [d[0] for d in result]
        assert device_ids[0] == 50


class TestPostorderTraversal:
    """Test suite for post-order traversal."""
    
    def test_postorder_single_node(self):
        """Test post-order traversal with single node."""
        tree = NetworkTopology()
        tree.insert(1, "10.0.0.1")
        result = tree.postorder_traversal()
        assert result == [(1, "10.0.0.1")]
    
    def test_postorder_structure(self):
        """Test post-order traversal order."""
        tree = NetworkTopology()
        for i in [50, 30, 70]:
            tree.insert(i, f"10.0.0.{i}")
        result = tree.postorder_traversal()
        device_ids = [d[0] for d in result]
        assert device_ids[-1] == 50


class TestGetDepth:
    """Test suite for get_depth operation."""
    
    def test_depth_empty(self):
        """Test depth of empty tree."""
        tree = NetworkTopology()
        assert tree.get_depth() == 0
    
    def test_depth_single(self):
        """Test depth of single node."""
        tree = NetworkTopology()
        tree.insert(1, "10.0.0.1")
        assert tree.get_depth() == 1
    
    def test_depth_balanced(self):
        """Test depth of balanced tree."""
        tree = NetworkTopology()
        for i in [50, 30, 70, 20, 40, 60, 80]:
            tree.insert(i, f"10.0.0.{i}")
        assert tree.get_depth() == 3


class TestIntegration:
    """Integration tests for network topology."""
    
    def test_full_workflow(self):
        """Test complete workflow of tree operations."""
        tree = NetworkTopology()
        
        devices = [(50, "10.0.0.50"), (30, "10.0.0.30"), (70, "10.0.0.70")]
        for device_id, ip in devices:
            tree.insert(device_id, ip)
        
        node = tree.find(30)
        assert node is not None
        assert node.ip == "10.0.0.30"
        
        inorder = tree.inorder_traversal()
        preorder = tree.preorder_traversal()
        postorder = tree.postorder_traversal()
        
        assert len(inorder) == 3
        assert len(preorder) == 3
        assert len(postorder) == 3


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "Network Topology (Trees) - DSA Exercises",
    ]
