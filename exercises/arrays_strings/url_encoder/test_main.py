import pytest
from main import url_encode, url_decode, is_valid_encoded


class TestURLEncode:
    """Test suite for url_encode function."""
    
    def test_encode_spaces(self):
        """Test encoding spaces."""
        assert url_encode("hello world") == "hello%20world"
        assert url_encode("hello  world") == "hello%20%20world"
    
    def test_encode_special_chars(self):
        """Test encoding special characters."""
        assert url_encode("hello@world") == "hello%40world"
        assert url_encode("hello!world") == "hello%21world"
        assert url_encode("hello#world") == "hello%23world"
        assert url_encode("hello$world") == "hello%24world"
    
    def test_encode_safe_chars(self):
        """Test that safe characters are not encoded."""
        assert url_encode("hello-world") == "hello-world"
        assert url_encode("hello_world") == "hello_world"
        assert url_encode("hello.world") == "hello.world"
        assert url_encode("hello~world") == "hello~world"
    
    def test_encode_alphanumeric(self):
        """Test that alphanumeric characters are not encoded."""
        assert url_encode("hello123") == "hello123"
        assert url_encode("HelloWorld") == "HelloWorld"
        assert url_encode("HELLO123") == "HELLO123"
    
    def test_encode_empty_string(self):
        """Test encoding empty string."""
        assert url_encode("") == ""
    
    def test_encode_complex_url(self):
        """Test encoding a complex URL."""
        url = "https://example.com/path?query=value&name=test user"
        encoded = url_encode(url)
        assert "test%20user" in encoded
        assert "&" in encoded
        assert "=" in encoded


class TestURLDecode:
    """Test suite for url_decode function."""
    
    def test_decode_spaces(self):
        """Test decoding spaces."""
        assert url_decode("hello%20world") == "hello world"
        assert url_decode("hello%20%20world") == "hello  world"
    
    def test_decode_special_chars(self):
        """Test decoding special characters."""
        assert url_decode("hello%40world") == "hello@world"
        assert url_decode("hello%21world") == "hello!world"
        assert url_decode("hello%23world") == "hello#world"
    
    def test_decode_safe_chars(self):
        """Test decoding safe characters."""
        assert url_decode("hello-world") == "hello-world"
        assert url_decode("hello_world") == "hello_world"
    
    def test_decode_empty_string(self):
        """Test decoding empty string."""
        assert url_decode("") == ""
    
    def test_round_trip(self):
        """Test encoding and decoding round trip."""
        original = "hello world! @#$%"
        encoded = url_encode(original)
        decoded = url_decode(encoded)
        assert decoded == original


class TestIsValidEncoded:
    """Test suite for is_valid_encoded function."""
    
    def test_valid_encoding(self):
        """Test valid encoded URLs."""
        assert is_valid_encoded("hello%20world")
        assert is_valid_encoded("hello%40world")
        assert is_valid_encoded("hello%20%40world")
        assert is_valid_encoded("")
        assert is_valid_encoded("hello-world")
    
    def test_invalid_incomplete_percent(self):
        """Test incomplete % encoding."""
        assert not is_valid_encoded("hello%")
        assert not is_valid_encoded("hello%2")
    
    def test_invalid_hex(self):
        """Test invalid hex digits."""
        assert not is_valid_encoded("hello%ggworld")
        assert not is_valid_encoded("hello%2zworld")
        assert not is_valid_encoded("hello%zzworld")
    
    def test_valid_hex_uppercase(self):
        """Test that uppercase hex is valid."""
        assert is_valid_encoded("hello%20world")
        assert is_valid_encoded("hello%AFworld")
    
    def test_valid_hex_lowercase(self):
        """Test that lowercase hex is valid."""
        assert is_valid_encoded("hello%afworld")
        assert is_valid_encoded("hello%aBworld")


class TestIntegration:
    """Integration tests."""
    
    def test_encode_decode_valid(self):
        """Test that encode-decode preserves validity."""
        original = "hello world! @#$%"
        encoded = url_encode(original)
        assert is_valid_encoded(encoded)
        decoded = url_decode(encoded)
        assert decoded == original
    
    def test_various_special_chars(self):
        """Test various special characters."""
        special = "!@#$%^&*()+={}[]|\\:;\"'<>,?/"
        encoded = url_encode(special)
        assert is_valid_encoded(encoded)
        decoded = url_decode(encoded)
        assert decoded == special


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "URL Encoder - DSA Exercises",
    ]
