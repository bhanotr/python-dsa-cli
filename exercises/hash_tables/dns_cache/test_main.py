import pytest
import time
from main import DNSCache


class TestDNSCacheInit:
    """Test suite for DNSCache initialization."""
    
    def test_init_empty(self):
        """Test that new cache is empty."""
        cache = DNSCache()
        assert cache.size() == 0


class TestPut:
    """Test suite for put operation."""
    
    def test_put_single(self):
        """Test putting a single DNS entry."""
        cache = DNSCache()
        cache.put("example.com", "93.184.216.34", 60)
        assert cache.size() == 1
    
    def test_put_multiple(self):
        """Test putting multiple DNS entries."""
        cache = DNSCache()
        cache.put("example.com", "93.184.216.34", 60)
        cache.put("google.com", "142.250.81.46", 30)
        assert cache.size() == 2
    
    def test_put_overwrite(self):
        """Test overwriting an existing entry."""
        cache = DNSCache()
        cache.put("example.com", "93.184.216.34", 60)
        cache.put("example.com", "93.184.216.35", 30)
        assert cache.size() == 1


class TestGet:
    """Test suite for get operation."""
    
    def test_get_existing(self):
        """Test getting existing entry."""
        cache = DNSCache()
        cache.put("example.com", "93.184.216.34", 60)
        assert cache.get("example.com") == "93.184.216.34"
    
    def test_get_nonexistent(self):
        """Test getting non-existent entry."""
        cache = DNSCache()
        cache.put("example.com", "93.184.216.34", 60)
        assert cache.get("google.com") is None
    
    def test_get_expired(self):
        """Test getting expired entry."""
        cache = DNSCache()
        cache.put("example.com", "93.184.216.34", 1)
        time.sleep(1.5)
        assert cache.get("example.com") is None
    
    def test_get_not_expired(self):
        """Test getting not expired entry."""
        cache = DNSCache()
        cache.put("example.com", "93.184.216.34", 10)
        time.sleep(0.5)
        assert cache.get("example.com") == "93.184.216.34"
    
    def test_get_from_empty_cache(self):
        """Test getting from empty cache."""
        cache = DNSCache()
        assert cache.get("example.com") is None


class TestCleanup:
    """Test suite for cleanup operation."""
    
    def test_cleanup_empty(self):
        """Test cleaning up empty cache."""
        cache = DNSCache()
        removed = cache.cleanup()
        assert removed == 0
    
    def test_cleanup_no_expired(self):
        """Test cleaning up when no entries are expired."""
        cache = DNSCache()
        cache.put("example.com", "93.184.216.34", 60)
        removed = cache.cleanup()
        assert removed == 0
        assert cache.size() == 1
    
    def test_cleanup_some_expired(self):
        """Test cleaning up when some entries are expired."""
        cache = DNSCache()
        cache.put("example.com", "93.184.216.34", 10)
        cache.put("google.com", "142.250.81.46", 1)
        time.sleep(1.5)
        removed = cache.cleanup()
        assert removed == 1
        assert cache.size() == 1
    
    def test_cleanup_all_expired(self):
        """Test cleaning up when all entries are expired."""
        cache = DNSCache()
        cache.put("example.com", "93.184.216.34", 1)
        cache.put("google.com", "142.250.81.46", 1)
        time.sleep(1.5)
        removed = cache.cleanup()
        assert removed == 2
        assert cache.size() == 0


class TestSize:
    """Test suite for size operation."""
    
    def test_size_empty(self):
        """Test size of empty cache."""
        cache = DNSCache()
        assert cache.size() == 0
    
    def test_size_after_put(self):
        """Test size after putting entries."""
        cache = DNSCache()
        for i in range(5):
            cache.put(f"host{i}.com", f"192.168.1.{i}", 60)
            assert cache.size() == i + 1
    
    def test_size_after_cleanup(self):
        """Test size after cleanup."""
        cache = DNSCache()
        cache.put("example.com", "93.184.216.34", 1)
        cache.put("google.com", "142.250.81.46", 60)
        time.sleep(1.5)
        cache.cleanup()
        assert cache.size() == 1


class TestIntegration:
    """Integration tests for DNS cache."""
    
    def test_full_workflow(self):
        """Test complete workflow of DNS cache."""
        cache = DNSCache()
        
        # Add entries
        cache.put("example.com", "93.184.216.34", 60)
        cache.put("google.com", "142.250.81.46", 30)
        cache.put("github.com", "140.82.112.3", 10)
        
        # Verify size
        assert cache.size() == 3
        
        # Verify all are accessible
        assert cache.get("example.com") == "93.184.216.34"
        assert cache.get("google.com") == "142.250.81.46"
        assert cache.get("github.com") == "140.82.112.3"
        
        # Wait for github.com to expire
        time.sleep(1)
        assert cache.get("github.com") is None
        
        # Cleanup
        removed = cache.cleanup()
        assert removed >= 1
        assert cache.get("github.com") is None
        assert cache.get("example.com") is not None
    
    def test_overwrite_updates_ttl(self):
        """Test that overwriting updates TTL."""
        cache = DNSCache()
        cache.put("example.com", "93.184.216.34", 1)
        time.sleep(0.5)
        cache.put("example.com", "93.184.216.35", 60)
        time.sleep(1)
        # Should still be accessible due to new TTL
        assert cache.get("example.com") == "93.184.216.35"


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "DNS Cache (Hash Tables) - DSA Exercises",
    ]
