import pytest
from main import LRUCache, DLinkedNode


class TestDLinkedNode:
    """Test suite for DLinkedNode class."""
    
    def test_node_creation(self):
        """Test creating a node."""
        node = DLinkedNode(1, "10.0.0.1")
        assert node.key == 1
        assert node.value == "10.0.0.1"
        assert node.prev is None
        assert node.next is None
    
    def test_node_creation_default(self):
        """Test creating node with default values."""
        node = DLinkedNode()
        assert node.key == 0
        assert node.value == ""
        assert node.prev is None
        assert node.next is None


class TestLRUCacheInit:
    """Test suite for LRUCache initialization."""
    
    def test_init_capacity(self):
        """Test initializing with capacity."""
        cache = LRUCache(2)
        assert cache.capacity == 2
    
    def test_init_cache_dict(self):
        """Test that cache dict is initialized."""
        cache = LRUCache(2)
        assert len(cache.cache) == 0
    
    def test_init_head_tail(self):
        """Test that dummy head and tail are initialized."""
        cache = LRUCache(2)
        assert cache.head is not None
        assert cache.tail is not None
        assert cache.head.next == cache.tail
        assert cache.tail.prev == cache.head


class TestLRUCacheGet:
    """Test suite for get operation."""
    
    def test_get_empty_cache(self):
        """Test getting from empty cache."""
        cache = LRUCache(2)
        assert cache.get(1) is None
    
    def test_get_existing_key(self):
        """Test getting existing key."""
        cache = LRUCache(2)
        cache.put(1, "10.0.0.1")
        assert cache.get(1) == "10.0.0.1"
    
    def test_get_nonexistent_key(self):
        """Test getting nonexistent key."""
        cache = LRUCache(2)
        cache.put(1, "10.0.0.1")
        assert cache.get(2) is None
    
    def test_get_moves_to_head(self):
        """Test that get moves item to most recent."""
        cache = LRUCache(2)
        cache.put(1, "10.0.0.1")
        cache.put(2, "10.0.0.2")
        
        # Get key 1, should move it to head
        cache.get(1)
        
        # Add key 3, should evict key 2 (not key 1)
        cache.put(3, "10.0.0.3")
        
        assert cache.get(1) == "10.0.0.1"
        assert cache.get(2) is None
        assert cache.get(3) == "10.0.0.3"


class TestLRUCachePut:
    """Test suite for put operation."""
    
    def test_put_new_key(self):
        """Test putting new key."""
        cache = LRUCache(2)
        cache.put(1, "10.0.0.1")
        assert cache.get(1) == "10.0.0.1"
    
    def test_put_update_existing_key(self):
        """Test updating existing key."""
        cache = LRUCache(2)
        cache.put(1, "10.0.0.1")
        cache.put(1, "192.168.1.1")
        assert cache.get(1) == "192.168.1.1"
    
    def test_put_evicts_lru(self):
        """Test that put evicts least recently used item."""
        cache = LRUCache(2)
        cache.put(1, "10.0.0.1")
        cache.put(2, "10.0.0.2")
        
        # This should evict key 1
        cache.put(3, "10.0.0.3")
        
        assert cache.get(1) is None
        assert cache.get(2) == "10.0.0.2"
        assert cache.get(3) == "10.0.0.3"
    
    def test_put_update_makes_recent(self):
        """Test that updating existing key makes it most recent."""
        cache = LRUCache(2)
        cache.put(1, "10.0.0.1")
        cache.put(2, "10.0.0.2")
        
        # Update key 1, should make it most recent
        cache.put(1, "192.168.1.1")
        
        # Add key 3, should evict key 2 (not key 1)
        cache.put(3, "10.0.0.3")
        
        assert cache.get(1) == "192.168.1.1"
        assert cache.get(2) is None
        assert cache.get(3) == "10.0.0.3"


class TestLRUCacheCapacity:
    """Test suite for capacity handling."""
    
    def test_capacity_one(self):
        """Test cache with capacity 1."""
        cache = LRUCache(1)
        cache.put(1, "10.0.0.1")
        cache.put(2, "10.0.0.2")
        
        assert cache.get(1) is None
        assert cache.get(2) == "10.0.0.2"
    
    def test_capacity_multiple(self):
        """Test cache with larger capacity."""
        cache = LRUCache(5)
        
        for i in range(5):
            cache.put(i, f"10.0.0.{i}")
        
        for i in range(5):
            assert cache.get(i) == f"10.0.0.{i}"
        
        # Add one more, should evict key 0
        cache.put(5, "10.0.0.5")
        
        assert cache.get(0) is None
        assert cache.get(1) == "10.0.0.1"
        assert cache.get(5) == "10.0.0.5"
    
    def test_eviction_order(self):
        """Test that items are evicted in correct order."""
        cache = LRUCache(3)
        
        cache.put(1, "10.0.0.1")
        cache.put(2, "10.0.0.2")
        cache.put(3, "10.0.0.3")
        
        # Access key 1 to make it most recent
        cache.get(1)
        
        # Add key 4, should evict key 2 (least recent)
        cache.put(4, "10.0.0.4")
        
        assert cache.get(1) == "10.0.0.1"
        assert cache.get(2) is None
        assert cache.get(3) == "10.0.0.3"
        assert cache.get(4) == "10.0.0.4"


class TestLRUCacheIntegration:
    """Integration tests for LRU cache."""
    
    def test_full_workflow(self):
        """Test complete workflow of operations."""
        cache = LRUCache(3)
        
        # Initial puts
        cache.put(1, "A")
        cache.put(2, "B")
        cache.put(3, "C")
        
        # Get key 2 (makes it recent)
        assert cache.get(2) == "B"
        
        # Add key 4 (evicts key 1)
        cache.put(4, "D")
        assert cache.get(1) is None
        
        # Update key 3 (makes it recent)
        cache.put(3, "C2")
        assert cache.get(3) == "C2"
        
        # Add key 5 (evicts key 2)
        cache.put(5, "E")
        assert cache.get(2) is None
        
        # Verify remaining
        assert cache.get(3) == "C2"
        assert cache.get(4) == "D"
        assert cache.get(5) == "E"
    
    def test_repeated_gets(self):
        """Test that repeated gets work correctly."""
        cache = LRUCache(2)
        cache.put(1, "A")
        cache.put(2, "B")
        
        # Get key 1 multiple times
        assert cache.get(1) == "A"
        assert cache.get(1) == "A"
        assert cache.get(1) == "A"
        
        # Key 2 should still be evicted when we add key 3
        cache.put(3, "C")
        assert cache.get(2) is None
        assert cache.get(1) == "A"
        assert cache.get(3) == "C"


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "LRU Cache (Linked List) - DSA Exercises",
    ]
