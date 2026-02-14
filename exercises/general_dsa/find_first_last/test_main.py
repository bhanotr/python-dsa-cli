import pytest
from main import find_first_last


class TestFindFirstLast:
    """Test suite for find_first_last function."""
    
    def test_basic_example(self):
        """Test basic example from LeetCode."""
        result = find_first_last([5, 7, 7, 8, 8, 10], 8)
        assert result == [3, 4]
    
    def test_not_found(self):
        """Test when target not found."""
        result = find_first_last([5, 7, 7, 8, 8, 10], 6)
        assert result == [-1, -1]
    
    def test_empty_array(self):
        """Test empty array."""
        result = find_first_last([], 0)
        assert result == [-1, -1]
    
    def test_single_occurrence(self):
        """Test with single occurrence."""
        result = find_first_last([5, 7, 7, 8, 8, 10], 5)
        assert result == [0, 0]
    
    def test_all_same(self):
        """Test where all elements are target."""
        result = find_first_last([2, 2], 2)
        assert result == [0, 1]
    
    def test_at_start(self):
        """Test target at start of array."""
        result = find_first_last([1, 2, 3, 4, 5], 1)
        assert result == [0, 0]
    
    def test_at_end(self):
        """Test target at end of array."""
        result = find_first_last([1, 2, 3, 4, 5], 5)
        assert result == [4, 4]
    
    def test_multiple_occurrences(self):
        """Test with many occurrences."""
        result = find_first_last([1, 2, 3, 3, 3, 3, 4, 5], 3)
        assert result == [2, 5]
    
    def test_single_element_found(self):
        """Test single element array with target."""
        result = find_first_last([3], 3)
        assert result == [0, 0]
    
    def test_single_element_not_found(self):
        """Test single element array without target."""
        result = find_first_last([3], 5)
        assert result == [-1, -1]
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        result = find_first_last([-5, -3, -3, 0, 2], -3)
        assert result == [1, 2]


class TestFindFirstLastVerification:
    """Tests that verify the solution is correct."""
    
    def test_verification_positions(self):
        """Verify returned positions are correct."""
        test_cases = [
            ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
            ([1, 2, 3, 3, 3, 3, 4, 5], 3, [2, 5]),
            ([-5, -3, -3, 0, 2], -3, [1, 2]),
        ]
        
        for nums, target, expected in test_cases:
            result = find_first_last(nums, target)
            assert result == expected
    
    def test_verification_first_index(self):
        """Verify first index is correct when found."""
        nums = [1, 2, 3, 3, 3, 3, 4, 5]
        target = 3
        result = find_first_last(nums, target)
        
        if result[0] != -1:
            assert nums[result[0]] == target
            assert result[0] == 0 or nums[result[0] - 1] < target
    
    def test_verification_last_index(self):
        """Verify last index is correct when found."""
        nums = [1, 2, 3, 3, 3, 3, 4, 5]
        target = 3
        result = find_first_last(nums, target)
        
        if result[1] != -1:
            assert nums[result[1]] == target
            assert result[1] == len(nums) - 1 or nums[result[1] + 1] > target


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "Find First and Last Position - DSA Exercises",
    ]
