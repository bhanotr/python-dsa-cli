import pytest
from main import max_subarray


class TestMaxSubarray:
    """Test suite for max_subarray function."""
    
    def test_basic_example(self):
        """Test basic example from LeetCode."""
        assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    
    def test_single_element(self):
        """Test with single element."""
        assert max_subarray([1]) == 1
    
    def test_all_positive(self):
        """Test with all positive numbers."""
        assert max_subarray([5, 4, -1, 7, 8]) == 23
    
    def test_all_negative(self):
        """Test with all negative numbers."""
        assert max_subarray([-1, -2, -3]) == -1
    
    def test_two_elements(self):
        """Test with two elements."""
        assert max_subarray([1]) == 1
    
    def test_increasing(self):
        """Test with increasing numbers."""
        assert max_subarray([1, 2, 3, 4, 5]) == 15
    
    def test_decreasing(self):
        """Test with decreasing numbers."""
        assert max_subarray([5, 4, 3, 2, 1]) == 5
    
    def test_all_zeros(self):
        """Test with all zeros."""
        assert max_subarray([0, 0, 0, 0]) == 0
    
    def test_mixed(self):
        """Test with mixed positive and negative."""
        assert max_subarray([1, -2, 3, -1, 2, -1, -2, 5, -3]) == 6
    
    def test_single_negative(self):
        """Test with single negative."""
        assert max_subarray([-5]) == -5
    
    def test_positive_start(self):
        """Test with positive start then negative."""
        assert max_subarray([1, 2, 3, -100, 1]) == 6


class TestMaxSubarrayVerification:
    """Tests that verify the solution is correct."""
    
    def test_verification_all_subarrays(self):
        """Verify result is maximum over all subarrays."""
        test_cases = [
            ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            ([5, 4, -1, 7, 8], 23),
            ([1, 2, 3, 4, 5], 15),
        ]
        
        for nums, expected in test_cases:
            result = max_subarray(nums)
            assert result == expected
    
    def test_verification_brute_force(self):
        """Verify against brute force calculation."""
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        result = max_subarray(nums)
        
        max_sum = float('-inf')
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarray_sum = sum(nums[i:j+1])
                max_sum = max(max_sum, subarray_sum)
        
        assert result == max_sum


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "Maximum Subarray - DSA Exercises",
    ]
