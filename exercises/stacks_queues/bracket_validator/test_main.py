import pytest
from main import is_valid_config, get_invalid_position, get_matching_pairs


class TestIsValidConfig:
    """Test suite for is_valid_config function."""
    
    def test_valid_single_pair(self):
        """Test valid single bracket pairs."""
        assert is_valid_config("()") == True
        assert is_valid_config("[]") == True
        assert is_valid_config("{}") == True
    
    def test_valid_multiple_pairs(self):
        """Test valid multiple bracket pairs."""
        assert is_valid_config("()[]{}") == True
        assert is_valid_config("[]{}()") == True
        assert is_valid_config("({}[])") == True
    
    def test_valid_nested(self):
        """Test valid nested brackets."""
        assert is_valid_config("{[]}") == True
        assert is_valid_config("([{}])") == True
        assert is_valid_config("(((())))") == True
        assert is_valid_config("{[()]}") == True
    
    def test_invalid_mismatched(self):
        """Test invalid mismatched brackets."""
        assert is_valid_config("(]") == False
        assert is_valid_config("[)") == False
        assert is_valid_config("{)") == False
        assert is_valid_config("(}") == False
    
    def test_invalid_wrong_order(self):
        """Test invalid bracket order."""
        assert is_valid_config("([)]") == False
        assert is_valid_config("{(]})") == False
        assert is_valid_config("[{)]") == False
    
    def test_invalid_unclosed(self):
        """Test unclosed brackets."""
        assert is_valid_config("(") == False
        assert is_valid_config("[") == False
        assert is_valid_config("{") == False
        assert is_valid_config("((()") == False
    
    def test_invalid_extra_closing(self):
        """Test extra closing brackets."""
        assert is_valid_config(")") == False
        assert is_valid_config("]") == False
        assert is_valid_config("}") == False
        assert is_valid_config("())") == False
    
    def test_empty_string(self):
        """Test empty string is valid."""
        assert is_valid_config("") == True
    
    def test_complex_valid(self):
        """Test complex valid configurations."""
        assert is_valid_config("({[]})[]{}") == True
        assert is_valid_config("[{({})}]") == True
        assert is_valid_config("(){}[]") == True


class TestGetInvalidPosition:
    """Test suite for get_invalid_position function."""
    
    def test_invalid_position_unclosed(self):
        """Test position of unclosed bracket."""
        assert get_invalid_position("(") == 0
        assert get_invalid_position("(]") == 1
        assert get_invalid_position("()(") == 2
    
    def test_invalid_position_extra_closing(self):
        """Test position of extra closing bracket."""
        assert get_invalid_position(")") == 0
        assert get_invalid_position("()])") == 2
    
    def test_valid_returns_minus_one(self):
        """Test valid configs return -1."""
        assert get_invalid_position("()") == -1
        assert get_invalid_config("{[]}") == True
        assert get_invalid_position("") == -1
    
    def test_first_invalid_position(self):
        """Test first invalid bracket position."""
        assert get_invalid_position("([)]") == 2
        assert get_invalid_position("(]") == 1


class TestGetMatchingPairs:
    """Test suite for get_matching_pairs function."""
    
    def test_single_pair(self):
        """Test single matching pair."""
        pairs = get_matching_pairs("()")
        assert pairs == [(0, 1)]
    
    def test_multiple_pairs(self):
        """Test multiple matching pairs."""
        pairs = get_matching_pairs("()[]{}")
        assert pairs == [(0, 1), (2, 3), (4, 5)]
    
    def test_nested_pairs(self):
        """Test nested matching pairs."""
        pairs = get_matching_pairs("{[]}")
        assert (1, 2) in pairs
        assert (0, 3) in pairs
        assert len(pairs) == 2
    
    def test_complex_nested(self):
        """Test complex nested configuration."""
        pairs = get_matching_pairs("({[]})")
        # Inner []
        assert (2, 3) in pairs
        # Middle {}
        assert (1, 4) in pairs
        # Outer ()
        assert (0, 5) in pairs
        assert len(pairs) == 3
    
    def test_empty_returns_empty(self):
        """Test empty string returns empty list."""
        assert get_matching_pairs("") == []
    
    def test_invalid_returns_empty(self):
        """Test invalid config returns empty list."""
        assert get_matching_pairs("([") == []
        assert get_matching_pairs("(]") == []


class TestIntegration:
    """Integration tests for bracket validator."""
    
    def test_all_functions_on_valid(self):
        """Test all functions on valid config."""
        config = "{[()]}"
        assert is_valid_config(config) == True
        assert get_invalid_position(config) == -1
        pairs = get_matching_pairs(config)
        assert len(pairs) == 3
    
    def test_all_functions_on_invalid(self):
        """Test all functions on invalid config."""
        config = "([)]"
        assert is_valid_config(config) == False
        assert get_invalid_position(config) == 2
        pairs = get_matching_pairs(config)
        assert pairs == []


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "Bracket Validator (Stack) - DSA Exercises",
    ]
