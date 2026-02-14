import pytest
from main import PacketScheduler


class TestPacketScheduler:
    """Test suite for PacketScheduler."""
    
    def test_enqueue_single(self):
        """Test enqueuing a single packet."""
        scheduler = PacketScheduler()
        scheduler.enqueue("packet1", 1)
        assert scheduler.size() == 1
    
    def test_enqueue_multiple(self):
        """Test enqueuing multiple packets."""
        scheduler = PacketScheduler()
        scheduler.enqueue("packet1", 1)
        scheduler.enqueue("packet2", 2)
        scheduler.enqueue("packet3", 3)
        assert scheduler.size() == 3
    
    def test_dequeue_single(self):
        """Test dequeuing a single packet."""
        scheduler = PacketScheduler()
        scheduler.enqueue("packet1", 1)
        assert scheduler.dequeue() == "packet1"
        assert scheduler.is_empty()
    
    def test_dequeue_priority_order(self):
        """Test that higher priority packets are dequeued first."""
        scheduler = PacketScheduler()
        scheduler.enqueue("low", 1)
        scheduler.enqueue("high", 3)
        scheduler.enqueue("medium", 2)
        
        assert scheduler.dequeue() == "high"
        assert scheduler.dequeue() == "medium"
        assert scheduler.dequeue() == "low"
    
    def test_dequeue_empty(self):
        """Test dequeuing from empty scheduler."""
        scheduler = PacketScheduler()
        assert scheduler.dequeue() is None
    
    def test_peek(self):
        """Test peeking at highest priority packet."""
        scheduler = PacketScheduler()
        scheduler.enqueue("low", 1)
        scheduler.enqueue("high", 3)
        assert scheduler.peek() == "high"
        assert scheduler.size() == 2
    
    def test_peek_empty(self):
        """Test peeking at empty scheduler."""
        scheduler = PacketScheduler()
        assert scheduler.peek() is None
    
    def test_is_empty(self):
        """Test is_empty check."""
        scheduler = PacketScheduler()
        assert scheduler.is_empty()
        scheduler.enqueue("packet1", 1)
        assert not scheduler.is_empty()
    
    def test_size(self):
        """Test size tracking."""
        scheduler = PacketScheduler()
        assert scheduler.size() == 0
        scheduler.enqueue("packet1", 1)
        assert scheduler.size() == 1
        scheduler.enqueue("packet2", 2)
        assert scheduler.size() == 2
        scheduler.dequeue()
        assert scheduler.size() == 1
    
    def test_same_priority_fifo(self):
        """Test that same priority uses FIFO order."""
        scheduler = PacketScheduler()
        scheduler.enqueue("first", 1)
        scheduler.enqueue("second", 1)
        scheduler.enqueue("third", 1)
        
        assert scheduler.dequeue() == "first"
        assert scheduler.dequeue() == "second"
        assert scheduler.dequeue() == "third"


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "Packet Scheduler (Heaps) - DSA Exercises",
    ]
