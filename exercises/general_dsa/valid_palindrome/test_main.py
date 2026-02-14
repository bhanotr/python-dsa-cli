import pytest
from main import is_palindrome


class TestValidPalindrome:
    """Test suite for is_palindrome function."""
    
    def test_basic_palindrome(self):
        """Test basic palindrome with spaces and punctuation."""
        assert is_palindrome("A man, a plan, a canal: Panama") == True
    
    def test_non_palindrome(self):
        """Test non-palindrome string."""
        assert is_palindrome("race a car") == False
    
    def test_empty_string(self):
        """Test empty string."""
        assert is_palindrome("") == True
    
    def test_single_space(self):
        """Test string with only space."""
        assert is_palindrome(" ") == True
    
    def test_alphanumeric_mixed(self):
        """Test alphanumeric mixed."""
        assert is_palindrome("0P") == False
    
    def test_simple_palindrome(self):
        """Test simple palindrome."""
        assert is_palindrome("abba") == True
    
    def test_single_character(self):
        """Test single character."""
        assert is_palindrome("a") == True
    
    def test_numbers(self):
        """Test with numbers."""
        assert is_palindrome("12321") == True
    
    def test_case_insensitive(self):
        """Test case insensitivity."""
        assert is_palindrome("Aa") == True
    
    def test_with_special_chars(self):
        """Test with special characters."""
        assert is_palindrome("No 'x' in Nixon") == True
    
    def test_only_non_alphanumeric(self):
        """Test string with only non-alphanumeric characters."""
        assert is_palindrome("!@#$%") == True
    
    def test_almost_palindrome(self):
        """Test almost palindrome."""
        assert is_palindrome("abca") == False


class TestValidPalindromeVerification:
    """Tests that verify the solution is correct."""
    
    def test_verification_clean_string(self):
        """Verify by comparing cleaned string."""
        s = "A man, a plan, a canal: Panama"
        result = is_palindrome(s)
        
        if result:
            import re
            cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
            assert cleaned == cleaned[::-1]
    
    def test_verification_all_test_cases(self):
        """Verify test cases produce correct results."""
        test_cases = [
            ("A man, a plan, a canal: Panama", True),
            ("race a car", False),
            (" ", True),
            ("abba", True),
        ]
        
        for s, expected in test_cases:
            result = is_palindrome(s)
            assert result == expected


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "Valid Palindrome - DSA Exercises",
    ]
