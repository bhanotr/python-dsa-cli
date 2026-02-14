import pytest
from main import find_first_log, find_last_log, find_log_range


class TestFindFirstLog:
    """Test suite for find_first_log."""
    
    def test_find_first_exists(self):
        """Test finding first occurrence when exists."""
        logs = [(100, "a"), (100, "b"), (200, "c")]
        assert find_first_log(logs, 100) == 0
    
    def test_find_first_single(self):
        """Test finding single occurrence."""
        logs = [(100, "a"), (200, "b")]
        assert find_first_log(logs, 100) == 0
    
    def test_find_first_not_exists(self):
        """Test when timestamp doesn't exist."""
        logs = [(100, "a"), (200, "b")]
        assert find_first_log(logs, 150) is None
    
    def test_find_first_empty(self):
        """Test on empty logs."""
        assert find_first_log([], 100) is None
    
    def test_find_first_all_same(self):
        """Test when all logs have same timestamp."""
        logs = [(100, "a"), (100, "b"), (100, "c")]
        assert find_first_log(logs, 100) == 0


class TestFindLastLog:
    """Test suite for find_last_log."""
    
    def test_find_last_exists(self):
        """Test finding last occurrence when exists."""
        logs = [(100, "a"), (100, "b"), (200, "c")]
        assert find_last_log(logs, 100) == 1
    
    def test_find_last_single(self):
        """Test finding single occurrence."""
        logs = [(100, "a"), (200, "b")]
        assert find_last_log(logs, 100) == 0
    
    def test_find_last_not_exists(self):
        """Test when timestamp doesn't exist."""
        logs = [(100, "a"), (200, "b")]
        assert find_last_log(logs, 150) is None
    
    def test_find_last_empty(self):
        """Test on empty logs."""
        assert find_last_log([], 100) is None
    
    def test_find_last_all_same(self):
        """Test when all logs have same timestamp."""
        logs = [(100, "a"), (100, "b"), (100, "c")]
        assert find_last_log(logs, 100) == 2


class TestFindLogRange:
    """Test suite for find_log_range."""
    
    def test_find_range_basic(self):
        """Test finding logs in range."""
        logs = [(100, "a"), (150, "b"), (200, "c"), (250, "d")]
        result = find_log_range(logs, 150, 200)
        assert len(result) == 2
        assert result[0][0] == 150
        assert result[1][0] == 200
    
    def test_find_range_no_match(self):
        """Test when no logs in range."""
        logs = [(100, "a"), (200, "b")]
        result = find_log_range(logs, 150, 180)
        assert len(result) == 0
    
    def test_find_range_empty(self):
        """Test on empty logs."""
        assert find_log_range([], 100, 200) == []
    
    def test_find_range_all_logs(self):
        """Test when all logs in range."""
        logs = [(100, "a"), (150, "b"), (200, "c")]
        result = find_log_range(logs, 100, 200)
        assert len(result) == 3
    
    def test_find_range_same_timestamp(self):
        """Test range with same start and end."""
        logs = [(100, "a"), (100, "b"), (200, "c")]
        result = find_log_range(logs, 100, 100)
        assert len(result) == 2


class TestIntegration:
    """Integration tests for log analyzer."""
    
    def test_first_and_last(self):
        """Test first and last on same data."""
        logs = [(100, "a"), (100, "b"), (100, "c")]
        assert find_first_log(logs, 100) == 0
        assert find_last_log(logs, 100) == 2
    
    def test_range_edges(self):
        """Test range at edges of logs."""
        logs = [(100, "a"), (150, "b"), (200, "c"), (250, "d")]
        result = find_log_range(logs, 100, 250)
        assert len(result) == 4


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "Log Analyzer (Sorting/Searching) - DSA Exercises",
    ]
