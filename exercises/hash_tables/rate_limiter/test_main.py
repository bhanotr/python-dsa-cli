import pytest
import time
from main import RateLimiter


class TestRateLimiterInit:
    """Test suite for RateLimiter initialization."""
    
    def test_init(self):
        """Test rate limiter initialization."""
        limiter = RateLimiter(capacity=5, refill_rate=1)
        assert limiter.capacity == 5
        assert limiter.refill_rate == 1
    
    def test_init_different_values(self):
        """Test with different capacity and refill rate."""
        limiter = RateLimiter(capacity=10, refill_rate=2)
        assert limiter.capacity == 10
        assert limiter.refill_rate == 2


class TestAllowRequest:
    """Test suite for allow_request operation."""
    
    def test_initial_requests(self):
        """Test initial requests are allowed."""
        limiter = RateLimiter(capacity=5, refill_rate=1)
        for _ in range(5):
            assert limiter.allow_request("192.168.1.1") == True
    
    def test_requests_exceed_capacity(self):
        """Test requests beyond capacity are blocked."""
        limiter = RateLimiter(capacity=5, refill_rate=1)
        
        # First 5 allowed
        for _ in range(5):
            assert limiter.allow_request("192.168.1.1") == True
        
        # 6th blocked
        assert limiter.allow_request("192.168.1.1") == False
    
    def test_refill_after_time(self):
        """Test that tokens refill after time passes."""
        limiter = RateLimiter(capacity=5, refill_rate=1)
        ip = "192.168.1.1"
        
        # Use all tokens
        for _ in range(5):
            assert limiter.allow_request(ip) == True
        assert limiter.allow_request(ip) == False
        
        # Wait for refill
        time.sleep(2)
        
        # Should have 2 tokens refilled
        assert limiter.allow_request(ip) == True
        assert limiter.allow_request(ip) == True
        assert limiter.allow_request(ip) == False
    
    def test_different_ips_independent(self):
        """Test that different IPs have independent token buckets."""
        limiter = RateLimiter(capacity=2, refill_rate=1)
        
        # IP1 uses capacity
        assert limiter.allow_request("192.168.1.1") == True
        assert limiter.allow_request("192.168.1.1") == True
        assert limiter.allow_request("192.168.1.1") == False
        
        # IP2 should have full capacity
        assert limiter.allow_request("10.0.0.1") == True
        assert limiter.allow_request("10.0.0.1") == True


class TestGetTokenCount:
    """Test suite for get_token_count operation."""
    
    def test_token_count_decreases(self):
        """Test token count decreases with requests."""
        limiter = RateLimiter(capacity=5, refill_rate=1)
        ip = "192.168.1.1"
        
        assert limiter.get_token_count(ip) == 5
        limiter.allow_request(ip)
        assert limiter.get_token_count(ip) == 4
        limiter.allow_request(ip)
        assert limiter.get_token_count(ip) == 3
    
    def test_token_count_refills(self):
        """Test token count refills after time."""
        limiter = RateLimiter(capacity=5, refill_rate=2)
        ip = "192.168.1.1"
        
        # Use all tokens
        for _ in range(5):
            limiter.allow_request(ip)
        assert limiter.get_token_count(ip) == 0
        
        # Wait for refill
        time.sleep(1)
        
        # Should have 2 tokens refilled
        assert limiter.get_token_count(ip) == 2
    
    def test_token_count_new_ip(self):
        """Test token count for new IP."""
        limiter = RateLimiter(capacity=5, refill_rate=1)
        assert limiter.get_token_count("192.168.1.1") == 0


class TestTokenBucket:
    """Test suite for token bucket behavior."""
    
    def test_bucket_capped_at_capacity(self):
        """Test that tokens don't exceed capacity."""
        limiter = RateLimiter(capacity=5, refill_rate=10)
        ip = "192.168.1.1"
        
        # Use 1 token
        limiter.allow_request(ip)
        
        # Wait for refill (should add 10 tokens)
        time.sleep(1)
        
        # Should be capped at 5, not 14
        assert limiter.get_token_count(ip) == 5
    
    def test_refill_rate_zero(self):
        """Test that zero refill rate works."""
        limiter = RateLimiter(capacity=5, refill_rate=0)
        ip = "192.168.1.1"
        
        # Use all tokens
        for _ in range(5):
            limiter.allow_request(ip)
        
        # Wait - no refill
        time.sleep(2)
        
        assert limiter.get_token_count(ip) == 0
        assert limiter.allow_request(ip) == False


class TestIntegration:
    """Integration tests for rate limiter."""
    
    def test_burst_handling(self):
        """Test handling of request bursts."""
        limiter = RateLimiter(capacity=10, refill_rate=1)
        ip = "192.168.1.1"
        
        # Burst of 10 requests
        for _ in range(10):
            assert limiter.allow_request(ip) == True
        
        # 11th blocked
        assert limiter.allow_request(ip) == False
    
    def test_steady_requests(self):
        """Test steady request rate."""
        limiter = RateLimiter(capacity=5, refill_rate=2)
        ip = "192.168.1.1"
        
        # Make requests with delay
        for _ in range(3):
            assert limiter.allow_request(ip) == True
            time.sleep(0.5)  # Should add 1 token per iteration
        
        # Should still have tokens left
        assert limiter.get_token_count(ip) >= 2


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "Rate Limiter (Hash Tables) - DSA Exercises",
    ]
