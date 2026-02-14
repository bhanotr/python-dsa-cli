import pytest
from main import top_k_frequent


class TestTopKFrequent:
    """Test suite for top_k_frequent function."""
    
    def test_basic_example(self):
        """Test basic example from LeetCode."""
        result = top_k_frequent([1, 1, 1, 2, 2, 3], 2)
        assert len(result) == 2
        assert 1 in result
        assert 2 in result
    
    def test_single_element(self):
        """Test with single element."""
        result = top_k_frequent([1], 1)
        assert result == [1]
    
    def test_all_unique(self):
        """Test with all unique elements."""
        result = top_k_frequent([1, 2, 3, 4, 5], 3)
        assert len(result) == 3
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        result = top_k_frequent([4, 1, -1, 2, -1, 2, 3], 2)
        assert len(result) == 2
        assert -1 in result
        assert 2 in result
    
    def test_k_equals_length(self):
        """Test when k equals number of unique elements."""
        result = top_k_frequent([1, 2, 3], 3)
        assert len(result) == 3
    
    def test_same_frequency(self):
        """Test when multiple elements have same frequency."""
        result = top_k_frequent([1, 2, 2, 3, 3], 2)
        assert len(result) == 2
        assert 2 in result
        assert 3 in result
    
    def test_zero_in_array(self):
        """Test with zero in array."""
        result = top_k_frequent([0, 0, 1, 1, 2], 1)
        assert result == [0] or result == [1]


class TestTopKFrequentVerification:
    """Tests that verify the solution is correct."""
    
    def test_top_k_most_frequent(self):
        """Verify returned elements are indeed the k most frequent."""
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        result = top_k_frequent(nums, k)
        
        from collections import Counter
        counts = Counter(nums)
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        top_k_actual = [item[0] for item in sorted_counts[:k]]
        
        assert set(result) == set(top_k_actual)
    
    def test_return_length(self):
        """Verify exactly k elements are returned."""
        test_cases = [
            ([1, 1, 1, 2, 2, 3], 2),
            ([1, 2, 3, 4, 5], 3),
            ([4, 1, -1, 2, -1, 2, 3], 2),
        ]
        
        for nums, k in test_cases:
            result = top_k_frequent(nums, k)
            assert len(result) == k


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "Top K Frequent - DSA Exercises",
    ]
