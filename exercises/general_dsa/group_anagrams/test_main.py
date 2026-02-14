import pytest
from main import group_anagrams


class TestGroupAnagrams:
    """Test suite for group_anagrams function."""
    
    def test_basic_example(self):
        """Test basic example from LeetCode."""
        result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        assert len(result) == 3
        flattened = [sorted(item) for group in result for item in group]
        assert sorted(flattened) == sorted([['a', 'e', 't'], ['a', 'e', 't'], ['a', 'e', 't'], ['a', 'n', 't'], ['a', 'n', 't'], ['a', 'b', 't']])
    
    def test_single_element(self):
        """Test with single string."""
        result = group_anagrams(["a"])
        assert result == [["a"]]
    
    def test_empty_string(self):
        """Test with empty string."""
        result = group_anagrams([""])
        assert result == [[""]]
    
    def test_multiple_empty_strings(self):
        """Test with multiple empty strings."""
        result = group_anagrams(["", ""])
        assert len(result) == 1
        assert result[0] == ["", ""]
    
    def test_no_anagrams(self):
        """Test with no anagrams."""
        result = group_anagrams(["abc", "def", "ghi"])
        assert len(result) == 3
        assert sorted([sorted(g[0]) for g in result]) == sorted([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']])
    
    def test_all_anagrams(self):
        """Test where all strings are anagrams."""
        result = group_anagrams(["abc", "bca", "cab"])
        assert len(result) == 1
        assert len(result[0]) == 3
    
    def test_mixed_anagrams(self):
        """Test with mixed anagram groups."""
        result = group_anagrams(["abc", "bca", "xyz", "zyx"])
        assert len(result) == 2
        for group in result:
            assert len(group) == 2
    
    def test_case_sensitive(self):
        """Test that strings are case-sensitive by default."""
        result = group_anagrams(["Eat", "tea", "Ate"])
        # These are not anagrams due to case
        assert len(result) == 3


class TestGroupAnagramsVerification:
    """Tests that verify the solution is correct."""
    
    def test_anagram_groups_correct(self):
        """Verify that strings in same group are anagrams."""
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = group_anagrams(strs)
        
        for group in result:
            if len(group) > 1:
                sorted_first = sorted(group[0])
                for s in group[1:]:
                    assert sorted(s) == sorted_first
    
    def test_all_strings_present(self):
        """Verify all input strings are in result."""
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = group_anagrams(strs)
        
        result_strings = [s for group in result for s in group]
        assert sorted(result_strings) == sorted(strs)


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "Group Anagrams - DSA Exercises",
    ]
