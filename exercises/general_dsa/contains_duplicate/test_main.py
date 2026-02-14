import pytest
from main import contains_duplicate


class TestContainsDuplicate:
    """Test suite for contains_duplicate function."""
    
    def test_duplicate_present(self):
        """Test with duplicates."""
        assert contains_duplicate([1, 2, 3, 1]) == True
    
    def test_no_duplicate(self):
        """Test without duplicates."""
        assert contains_duplicate([1, 2, 3, 4]) == False
    
    def test_multiple_duplicates(self):
        """Test with multiple duplicates."""
        assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    
    def test_empty_array(self):
        """Test empty array."""
        assert contains_duplicate([]) == False
    
    def test_single_element(self):
        """Test with single element."""
        assert contains_duplicate([1]) == False
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        assert contains_duplicate([-1, -2, -3, -1]) == True
    
    def test_all_same(self):
        """Test where all elements are same."""
        assert contains_duplicate([1, 1, 1, 1]) == True
    
    def test_large_numbers(self):
        """Test with large numbers."""
        assert contains_duplicate([1000000, 2000000, 1000000]) == True
    
    def test_zero_duplicates(self):
        """Test with zeros."""
        assert contains_duplicate([0, 0]) == True
    
    def test_many_unique(self):
        """Test with many unique elements."""
        assert contains_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False


class TestContainsDuplicateVerification:
    """Tests that verify the solution is correct."""
    
    def test_verification_with_set(self):
        """Verify results using set comparison."""
        test_cases = [
            [1, 2, 3, 1],
            [1, 2, 3, 4],
            [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
        ]
        
        for nums in test_cases:
            result = contains_duplicate(nums)
            expected = len(nums) != len(set(nums))
            assert result == expected


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "Contains Duplicate - DSA Exercises",
    ]
