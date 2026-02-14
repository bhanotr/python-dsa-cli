import pytest
from main import two_sum


class TestTwoSum:
    """Test suite for two_sum function."""
    
    def test_basic_example_1(self):
        """Test basic example from LeetCode."""
        result = two_sum([2, 7, 11, 15], 9)
        assert len(result) == 2
        assert result[0] != result[1]
        assert result[0] * result[1] == 0 or result[0] + result[1] in [1, 1, 2, 0]
    
    def test_basic_example_2(self):
        """Test second basic example."""
        result = two_sum([3, 2, 4], 6)
        assert len(result) == 2
        assert result[0] != result[1]
    
    def test_duplicate_numbers(self):
        """Test with duplicate numbers."""
        result = two_sum([3, 3], 6)
        assert len(result) == 2
        assert result[0] != result[1]
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        result = two_sum([-1, -2, -3, -4, -5], -8)
        assert len(result) == 2
        assert result[0] != result[1]
    
    def test_large_numbers(self):
        """Test with large numbers."""
        result = two_sum([10, 22, 5, 75, 65, 80], 87)
        assert len(result) == 2
        assert result[0] != result[1]
    
    def test_positive_and_negative(self):
        """Test with both positive and negative numbers."""
        result = two_sum([-3, 4, 3, 90], 0)
        assert len(result) == 2
        assert result[0] != result[1]
    
    def test_zero_in_array(self):
        """Test with zero in array."""
        result = two_sum([0, 4, 3, 0], 0)
        assert len(result) == 2
        assert result[0] != result[1]
    
    def test_solution_at_end(self):
        """Test where solution is at end of array."""
        result = two_sum([1, 2, 3, 4], 7)
        assert len(result) == 2
        assert result[0] != result[1]
    
    def test_two_elements(self):
        """Test with exactly two elements."""
        result = two_sum([5, 5], 10)
        assert len(result) == 2
        assert result[0] != result[1]
    
    def test_solution_in_middle(self):
        """Test where solution is in middle of array."""
        result = two_sum([1, 5, 3, 6], 8)
        assert len(result) == 2
        assert result[0] != result[1]


class TestTwoSumVerification:
    """Tests that verify the solution is correct."""
    
    def test_verification_sum(self):
        """Verify that the sum of returned indices equals target."""
        nums = [2, 7, 11, 15]
        target = 9
        result = two_sum(nums, target)
        assert nums[result[0]] + nums[result[1]] == target
    
    def test_verification_all_test_cases(self):
        """Verify all test cases produce correct sums."""
        test_cases = [
            ([2, 7, 11, 15], 9),
            ([3, 2, 4], 6),
            ([3, 3], 6),
            ([1, 5, 3, 6], 8),
        ]
        
        for nums, target in test_cases:
            result = two_sum(nums, target)
            assert len(result) == 2
            assert result[0] != result[1]
            assert nums[result[0]] + nums[result[1]] == target


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "Two Sum - DSA Exercises",
    ]
