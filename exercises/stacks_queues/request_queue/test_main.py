import pytest
from main import RequestQueue


class TestRequestQueueInit:
    """Test suite for RequestQueue initialization."""
    
    def test_init_empty(self):
        """Test that new queue is empty."""
        queue = RequestQueue()
        assert queue.is_empty()
        assert queue.size() == 0


class TestEnqueue:
    """Test suite for enqueue operation."""
    
    def test_enqueue_single(self):
        """Test enqueuing a single request."""
        queue = RequestQueue()
        queue.enqueue("GET /api/users")
        assert queue.size() == 1
        assert not queue.is_empty()
    
    def test_enqueue_multiple(self):
        """Test enqueuing multiple requests."""
        queue = RequestQueue()
        requests = ["GET /api/users", "POST /api/data", "DELETE /api/item"]
        
        for req in requests:
            queue.enqueue(req)
        
        assert queue.size() == 3
    
    def test_enqueue_empty_string(self):
        """Test enqueuing empty string."""
        queue = RequestQueue()
        queue.enqueue("")
        assert queue.size() == 1


class TestDequeue:
    """Test suite for dequeue operation."""
    
    def test_dequeue_single(self):
        """Test dequeuing a single request."""
        queue = RequestQueue()
        queue.enqueue("GET /api/users")
        
        req = queue.dequeue()
        assert req == "GET /api/users"
        assert queue.is_empty()
    
    def test_dequeue_multiple(self):
        """Test dequeuing multiple requests in FIFO order."""
        queue = RequestQueue()
        requests = ["GET /api/users", "POST /api/data", "DELETE /api/item"]
        
        for req in requests:
            queue.enqueue(req)
        
        for expected_req in requests:
            assert queue.dequeue() == expected_req
        
        assert queue.is_empty()
    
    def test_dequeue_empty(self):
        """Test dequeuing from empty queue."""
        queue = RequestQueue()
        assert queue.dequeue() is None


class TestPeek:
    """Test suite for peek operation."""
    
    def test_peek_single(self):
        """Test peeking at single request."""
        queue = RequestQueue()
        queue.enqueue("GET /api/users")
        
        assert queue.peek() == "GET /api/users"
        assert queue.size() == 1  # Should not remove
    
    def test_peek_multiple(self):
        """Test peeking at front of multiple requests."""
        queue = RequestQueue()
        requests = ["GET /api/users", "POST /api/data", "DELETE /api/item"]
        
        for req in requests:
            queue.enqueue(req)
        
        assert queue.peek() == requests[0]
        assert queue.size() == 3
    
    def test_peek_empty(self):
        """Test peeking at empty queue."""
        queue = RequestQueue()
        assert queue.peek() is None
    
    def test_peek_after_dequeue(self):
        """Test peeking after dequeuing."""
        queue = RequestQueue()
        queue.enqueue("GET /api/users")
        queue.enqueue("POST /api/data")
        
        queue.dequeue()
        assert queue.peek() == "POST /api/data"


class TestIsEmpty:
    """Test suite for is_empty operation."""
    
    def test_is_empty_new_queue(self):
        """Test new queue is empty."""
        queue = RequestQueue()
        assert queue.is_empty()
    
    def test_is_empty_after_enqueue(self):
        """Test queue is not empty after enqueue."""
        queue = RequestQueue()
        queue.enqueue("GET /api/users")
        assert not queue.is_empty()
    
    def test_is_empty_after_dequeue_all(self):
        """Test queue is empty after dequeuing all."""
        queue = RequestQueue()
        queue.enqueue("GET /api/users")
        queue.enqueue("POST /api/data")
        
        queue.dequeue()
        queue.dequeue()
        assert queue.is_empty()


class TestSize:
    """Test suite for size operation."""
    
    def test_size_empty(self):
        """Test size of empty queue."""
        queue = RequestQueue()
        assert queue.size() == 0
    
    def test_size_after_enqueue(self):
        """Test size after enqueuing."""
        queue = RequestQueue()
        
        for i in range(5):
            queue.enqueue(f"request_{i}")
            assert queue.size() == i + 1
    
    def test_size_after_dequeue(self):
        """Test size after dequeuing."""
        queue = RequestQueue()
        
        for i in range(5):
            queue.enqueue(f"request_{i}")
        
        for i in range(5):
            queue.dequeue()
            assert queue.size() == 4 - i


class TestRequestQueueIntegration:
    """Integration tests for RequestQueue."""
    
    def test_fifo_order(self):
        """Test that queue maintains FIFO order."""
        queue = RequestQueue()
        items = ["first", "second", "third"]
        
        for item in items:
            queue.enqueue(item)
        
        for item in items:
            assert queue.dequeue() == item
    
    def test_mixed_operations(self):
        """Test mixing enqueue and dequeue operations."""
        queue = RequestQueue()
        
        queue.enqueue("A")
        queue.enqueue("B")
        assert queue.dequeue() == "A"
        
        queue.enqueue("C")
        assert queue.peek() == "B"
        
        assert queue.dequeue() == "B"
        assert queue.dequeue() == "C"
        assert queue.is_empty()
    
    def test_large_queue(self):
        """Test queue with many items."""
        queue = RequestQueue()
        n = 1000
        
        for i in range(n):
            queue.enqueue(f"request_{i}")
        
        assert queue.size() == n
        
        for i in range(n):
            assert queue.dequeue() == f"request_{i}"


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "Request Queue - DSA Exercises",
    ]
