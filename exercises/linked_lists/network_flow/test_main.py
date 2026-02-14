import pytest
from main import FlowNode, append_flow, find_flow, remove_flow, get_total_bandwidth, reverse_flows


class TestFlowNode:
    """Test suite for FlowNode class."""
    
    def test_node_creation(self):
        """Test creating a node."""
        node = FlowNode("10.0.0.1", 100)
        assert node.destination == "10.0.0.1"
        assert node.bandwidth == 100
        assert node.next is None


class TestAppendFlow:
    """Test suite for append_flow function."""
    
    def test_append_to_empty_list(self):
        """Test appending to empty list."""
        head = append_flow(None, "10.0.0.1", 100)
        assert head is not None
        assert head.destination == "10.0.0.1"
        assert head.bandwidth == 100
        assert head.next is None
    
    def test_append_to_nonempty_list(self):
        """Test appending to non-empty list."""
        head = append_flow(None, "10.0.0.1", 100)
        head = append_flow(head, "10.0.0.2", 200)
        
        assert head.destination == "10.0.0.1"
        assert head.bandwidth == 100
        assert head.next is not None
        assert head.next.destination == "10.0.0.2"
        assert head.next.bandwidth == 200
        assert head.next.next is None
    
    def test_append_multiple(self):
        """Test appending multiple nodes."""
        head = None
        destinations = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]
        
        for dest in destinations:
            head = append_flow(head, dest, 100)
        
        current = head
        for dest in destinations:
            assert current is not None
            assert current.destination == dest
            current = current.next


class TestFindFlow:
    """Test suite for find_flow function."""
    
    def test_find_in_empty_list(self):
        """Test finding in empty list."""
        result = find_flow(None, "10.0.0.1")
        assert result is None
    
    def test_find_existing_flow(self):
        """Test finding an existing flow."""
        head = append_flow(None, "10.0.0.1", 100)
        head = append_flow(head, "10.0.0.2", 200)
        
        node = find_flow(head, "10.0.0.2")
        assert node is not None
        assert node.destination == "10.0.0.2"
        assert node.bandwidth == 200
    
    def test_find_nonexistent_flow(self):
        """Test finding a non-existent flow."""
        head = append_flow(None, "10.0.0.1", 100)
        head = append_flow(head, "10.0.0.2", 200)
        
        node = find_flow(head, "10.0.0.3")
        assert node is None


class TestRemoveFlow:
    """Test suite for remove_flow function."""
    
    def test_remove_from_empty_list(self):
        """Test removing from empty list."""
        result = remove_flow(None, "10.0.0.1")
        assert result is None
    
    def test_remove_head(self):
        """Test removing head of list."""
        head = append_flow(None, "10.0.0.1", 100)
        head = append_flow(head, "10.0.0.2", 200)
        
        head = remove_flow(head, "10.0.0.1")
        
        assert head is not None
        assert head.destination == "10.0.0.2"
        assert head.next is None
    
    def test_remove_middle(self):
        """Test removing middle node."""
        head = append_flow(None, "10.0.0.1", 100)
        head = append_flow(head, "10.0.0.2", 200)
        head = append_flow(head, "10.0.0.3", 300)
        
        head = remove_flow(head, "10.0.0.2")
        
        assert head.destination == "10.0.0.1"
        assert head.next.destination == "10.0.0.3"
        assert head.next.next is None
    
    def test_remove_nonexistent(self):
        """Test removing non-existent node."""
        head = append_flow(None, "10.0.0.1", 100)
        head = append_flow(head, "10.0.0.2", 200)
        
        result = remove_flow(head, "10.0.0.3")
        
        assert result is not None
        assert result.destination == "10.0.0.1"


class TestGetTotalBandwidth:
    """Test suite for get_total_bandwidth function."""
    
    def test_empty_list(self):
        """Test getting total bandwidth of empty list."""
        total = get_total_bandwidth(None)
        assert total == 0
    
    def test_single_node(self):
        """Test getting total bandwidth of single node."""
        head = append_flow(None, "10.0.0.1", 100)
        total = get_total_bandwidth(head)
        assert total == 100
    
    def test_multiple_nodes(self):
        """Test getting total bandwidth of multiple nodes."""
        head = None
        bandwidths = [100, 200, 150, 300]
        
        for bw in bandwidths:
            head = append_flow(head, "10.0.0.x", bw)
        
        total = get_total_bandwidth(head)
        assert total == sum(bandwidths)


class TestReverseFlows:
    """Test suite for reverse_flows function."""
    
    def test_reverse_empty_list(self):
        """Test reversing empty list."""
        result = reverse_flows(None)
        assert result is None
    
    def test_reverse_single_node(self):
        """Test reversing single node list."""
        head = append_flow(None, "10.0.0.1", 100)
        reversed_head = reverse_flows(head)
        
        assert reversed_head is not None
        assert reversed_head.destination == "10.0.0.1"
        assert reversed_head.next is None
    
    def test_reverse_multiple_nodes(self):
        """Test reversing multiple nodes."""
        head = None
        destinations = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]
        
        for dest in destinations:
            head = append_flow(head, dest, 100)
        
        reversed_head = reverse_flows(head)
        
        current = reversed_head
        reversed_destinations = destinations[::-1]
        for dest in reversed_destinations:
            assert current is not None
            assert current.destination == dest
            current = current.next


class TestIntegration:
    """Integration tests."""
    
    def test_full_workflow(self):
        """Test complete workflow of operations."""
        head = None
        
        # Create list
        head = append_flow(head, "10.0.0.1", 100)
        head = append_flow(head, "10.0.0.2", 200)
        head = append_flow(head, "10.0.0.3", 150)
        
        # Verify total
        assert get_total_bandwidth(head) == 450
        
        # Find and verify
        node = find_flow(head, "10.0.0.2")
        assert node.bandwidth == 200
        
        # Remove
        head = remove_flow(head, "10.0.0.2")
        assert get_total_bandwidth(head) == 250
        
        # Reverse
        head = reverse_flows(head)
        assert head.destination == "10.0.0.3"
        assert head.next.destination == "10.0.0.1"


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "Network Flow (Linked List) - DSA Exercises",
    ]
