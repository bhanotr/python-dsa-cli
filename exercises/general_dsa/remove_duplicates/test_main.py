import pytest
from main import remove_duplicates


class TestRemoveDuplicates:
    """Test suite for remove_duplicates function."""
    
    def test_basic_example(self):
        """Test basic example from LeetCode."""
        nums = [1, 1, 2]
        k = remove_duplicates(nums)
        assert k == 2
        assert nums[:k] == [1, 2]
    
    def test_long_example(self):
        """Test longer example."""
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = remove_duplicates(nums)
        assert k == 5
        assert nums[:k] == [0, 1, 2, 3, 4]
    
    def test_single_element(self):
        """Test with single element."""
        nums = [1]
        k = remove_duplicates(nums)
        assert k == 1
        assert nums[:k] == [1]
    
    def test_all_duplicates(self):
        """Test where all elements are same."""
        nums = [1, 1, 1, 1]
        k = remove_duplicates(nums)
        assert k == 1
        assert nums[:k] == [1]
    
    def test_empty_array(self):
        """Test empty array."""
        nums = []
        k = remove_duplicates(nums)
        assert k == 0
        assert nums[:k] == []
    
    def test_no_duplicates(self):
        """Test array with no duplicates."""
        nums = [1, 2, 3, 4, 5]
        k = remove_duplicates(nums)
        assert k == 5
        assert nums[:k] == [1, 2, 3, 4, 5]
    
    def test_two_elements_same(self):
        """Test with two identical elements."""
        nums = [1, 1]
        k = remove_duplicates(nums)
        assert k == 1
        assert nums[:k] == [1]
    
    def test_two_elements_different(self):
        """Test with two different elements."""
        nums = [1, 2]
        k = remove_duplicates(nums)
        assert k == 2
        assert nums[:k] == [1, 2]


class TestRemoveDuplicatesVerification:
    """Tests that verify the solution is correct."""
    
    def test_verification_unique_count(self):
        """Verify k equals number of unique elements."""
        test_cases = [
            [1, 1, 2],
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
            [1, 2, 3, 4, 5],
            [1, 1, 1, 1],
        ]
        
        for nums in test_cases:
            original = nums.copy()
            k = remove_duplicates(nums)
            expected_k = len(set(original))
            assert k == expected_k
    
    def test_verification_first_k_unique(self):
        """Verify first k elements are unique."""
        test_cases = [
            [1, 1, 2, 2, 3],
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        ]
        
        for nums in test_cases:
            k = remove_duplicates(nums)
            first_k = nums[:k]
            assert len(first_k) == len(set(first_k))
    
    def test_verification_sorted(self):
        """Verify first k elements are sorted."""
        test_cases = [
            [1, 1, 2, 2, 3],
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        ]
        
        for nums in test_cases:
            k = remove_duplicates(nums)
            first_k = nums[:k]
            assert first_k == sorted(first_k)


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "Remove Duplicates - DSA Exercises",
    ]
