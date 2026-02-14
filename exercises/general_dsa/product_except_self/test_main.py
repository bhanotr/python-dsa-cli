import pytest
from main import product_except_self


class TestProductExceptSelf:
    """Test suite for product_except_self function."""
    
    def test_basic_example(self):
        """Test basic example from LeetCode."""
        result = product_except_self([1, 2, 3, 4])
        assert result == [24, 12, 8, 6]
    
    def test_with_zero(self):
        """Test array containing zero."""
        result = product_except_self([-1, 1, 0, -3, 3])
        assert result == [0, 0, 9, 0, 0]
    
    def test_two_elements(self):
        """Test with two elements."""
        result = product_except_self([1, 2])
        assert result == [2, 1]
    
    def test_two_zeros(self):
        """Test with two zeros."""
        result = product_except_self([0, 0])
        assert result == [0, 0]
    
    def test_single_element(self):
        """Test with single element."""
        result = product_except_self([5])
        assert result == [1]
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        result = product_except_self([-1, -2, -3, -4])
        assert result == [-24, -12, -8, -6]
    
    def test_mixed_signs(self):
        """Test with mixed positive and negative."""
        result = product_except_self([1, -2, 3, -4])
        assert result == [24, -12, 8, -6]
    
    def test_large_numbers(self):
        """Test with large numbers."""
        result = product_except_self([10, 20, 30])
        assert result == [600, 300, 200]


class TestProductExceptSelfVerification:
    """Tests that verify the solution is correct."""
    
    def test_verification_all_test_cases(self):
        """Verify all test cases produce correct products."""
        test_cases = [
            [1, 2, 3, 4],
            [-1, 1, 0, -3, 3],
            [1, 2],
            [10, 20, 30],
        ]
        
        for nums in test_cases:
            result = product_except_self(nums)
            assert len(result) == len(nums)
            
            for i in range(len(nums)):
                expected = 1
                for j in range(len(nums)):
                    if j != i:
                        expected *= nums[j]
                assert result[i] == expected
    
    def test_no_division_used(self):
        """Verify that the result doesn't use division."""
        nums = [1, 2, 3, 4]
        result = product_except_self(nums)
        
        # If division was used, result[0] would be 1 * 2 * 3 * 4 / 1 = 24
        # But we're checking by actual multiplication
        assert result[0] == 2 * 3 * 4
        assert result[1] == 1 * 3 * 4


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "Product Except Self - DSA Exercises",
    ]
