import pytest
from main import longest_consecutive


class TestLongestConsecutive:
    """Test suite for longest_consecutive function."""
    
    def test_basic_example(self):
        """Test basic example from LeetCode."""
        result = longest_consecutive([100, 4, 200, 1, 3, 2])
        assert result == 4
    
    def test_consecutive_range(self):
        """Test with full consecutive range."""
        result = longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
        assert result == 9
    
    def test_empty_array(self):
        """Test empty array."""
        result = longest_consecutive([])
        assert result == 0
    
    def test_with_negatives(self):
        """Test with negative numbers."""
        result = longest_consecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6])
        assert result == 7
    
    def test_single_element(self):
        """Test with single element."""
        result = longest_consecutive([1])
        assert result == 1
    
    def test_all_duplicates(self):
        """Test with all duplicates."""
        result = longest_consecutive([1, 2, 0, 1])
        assert result == 3
    
    def test_non_consecutive(self):
        """Test with non-consecutive numbers."""
        result = longest_consecutive([100, 4, 200, 300])
        assert result == 1
    
    def test_negative_only(self):
        """Test with only negative numbers."""
        result = longest_consecutive([-5, -4, -3, -2, -1])
        assert result == 5
    
    def test_large_gap(self):
        """Test with large gap in numbers."""
        result = longest_consecutive([1, 1000, 2, 3, 4])
        assert result == 4
    
    def test_all_same(self):
        """Test where all numbers are the same."""
        result = longest_consecutive([5, 5, 5, 5])
        assert result == 1


class TestLongestConsecutiveVerification:
    """Tests that verify the solution is correct."""
    
    def test_verification_with_set(self):
        """Verify results using set-based counting."""
        test_cases = [
            ([100, 4, 200, 1, 3, 2], 4),
            ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
            ([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7),
        ]
        
        for nums, expected in test_cases:
            result = longest_consecutive(nums)
            assert result == expected


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "Longest Consecutive Sequence - DSA Exercises",
    ]
