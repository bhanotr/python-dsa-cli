import pytest
from main import merge


class TestMergeIntervals:
    """Test suite for merge function."""
    
    def test_basic_example(self):
        """Test basic example from LeetCode."""
        result = merge([[1, 3], [2, 6], [8, 10], [15, 18]])
        assert len(result) == 3
        assert result == [[1, 6], [8, 10], [15, 18]]
    
    def test_touching_intervals(self):
        """Test intervals that touch at boundaries."""
        result = merge([[1, 4], [4, 5]])
        assert result == [[1, 5]]
    
    def test_nested_intervals(self):
        """Test nested intervals."""
        result = merge([[1, 4], [0, 4]])
        assert result == [[0, 4]]
    
    def test_empty_array(self):
        """Test empty array."""
        result = merge([])
        assert result == []
    
    def test_single_interval(self):
        """Test single interval."""
        result = merge([[1, 3]])
        assert result == [[1, 3]]
    
    def test_all_overlapping(self):
        """Test all intervals overlapping."""
        result = merge([[1, 10], [2, 9], [3, 8]])
        assert result == [[1, 10]]
    
    def test_no_overlap(self):
        """Test intervals with no overlap."""
        result = merge([[1, 2], [3, 4], [5, 6]])
        assert result == [[1, 2], [3, 4], [5, 6]]
    
    def test_unsorted_input(self):
        """Test unsorted intervals."""
        result = merge([[15, 18], [1, 3], [8, 10], [2, 6]])
        assert result == [[1, 6], [8, 10], [15, 18]]
    
    def test_multiple_same_intervals(self):
        """Test multiple identical intervals."""
        result = merge([[1, 4], [1, 4], [1, 4]])
        assert result == [[1, 4]]
    
    def test_partially_overlapping(self):
        """Test partially overlapping intervals."""
        result = merge([[1, 4], [3, 5]])
        assert result == [[1, 5]]


class TestMergeIntervalsVerification:
    """Tests that verify the solution is correct."""
    
    def test_no_overlaps_in_result(self):
        """Verify result has no overlapping intervals."""
        test_cases = [
            [[1, 3], [2, 6], [8, 10], [15, 18]],
            [[1, 4], [4, 5]],
            [[1, 10], [2, 9], [3, 8]],
        ]
        
        for intervals in test_cases:
            result = merge(intervals)
            for i in range(len(result) - 1):
                assert result[i][1] < result[i + 1][0]
    
    def test_sorted_by_start(self):
        """Verify result is sorted by start time."""
        test_cases = [
            [[1, 3], [2, 6], [8, 10], [15, 18]],
            [[15, 18], [1, 3], [8, 10], [2, 6]],
        ]
        
        for intervals in test_cases:
            result = merge(intervals)
            for i in range(len(result) - 1):
                assert result[i][0] <= result[i + 1][0]


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "Merge Intervals - DSA Exercises",
    ]
