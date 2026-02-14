import pytest
from main import parse_packet, is_valid_ip, get_packet_size


class OperationCounter:
    """Helper class to count operations for performance tracking."""
    
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1


@pytest.fixture
def op_counter():
    """Create a new operation counter for each test."""
    return OperationCounter()


class TestParsePacket:
    """Test suite for parse_packet function."""
    
    def test_parse_valid_packet(self, op_counter):
        """Test parsing a valid packet."""
        packet = "192.168.1.1:10.0.0.1|HTTP:GET /index.html"
        op_counter.increment()
        result = parse_packet(packet)
        
        assert result is not None
        assert result["source"] == "192.168.1.1"
        assert result["destination"] == "10.0.0.1"
        assert result["packet_type"] == "HTTP"
        assert result["payload"] == "GET /index.html"
        print(f" ({op_counter.count} operations)", end="")
    
    def test_parse_simple_packet(self, op_counter):
        """Test parsing a simple packet."""
        packet = "192.168.1.1:10.0.0.1|TCP:SYN"
        op_counter.increment()
        result = parse_packet(packet)
        
        assert result is not None
        assert result["packet_type"] == "TCP"
        assert result["payload"] == "SYN"
        print(f" ({op_counter.count} operations)", end="")
    
    def test_parse_empty_packet(self, op_counter):
        """Test parsing an empty packet."""
        op_counter.increment()
        result = parse_packet("")
        
        assert result is None
        print(f" ({op_counter.count} operations)", end="")
    
    def test_parse_malformed_no_delimiter(self, op_counter):
        """Test parsing packet without main delimiter."""
        op_counter.increment()
        result = parse_packet("192.168.1.1:10.0.0.1")
        
        assert result is None
        print(f" ({op_counter.count} operations)", end="")
    
    def test_parse_malformed_missing_payload(self, op_counter):
        """Test parsing packet with missing payload."""
        packet = "192.168.1.1:10.0.0.1|HTTP:"
        op_counter.increment()
        result = parse_packet(packet)
        
        assert result is None
        print(f" ({op_counter.count} operations)", end="")
    
    def test_parse_packet_with_empty_payload(self, op_counter):
        """Test parsing packet with empty but valid payload."""
        packet = "192.168.1.1:10.0.0.1|HTTP:"
        op_counter.increment()
        result = parse_packet(packet)
        
        # Should return None since payload is missing
        assert result is None
        print(f" ({op_counter.count} operations)", end="")


class TestIsValidIP:
    """Test suite for is_valid_ip function."""
    
    def test_valid_ipv4(self, op_counter):
        """Test valid IPv4 addresses."""
        valid_ips = [
            "192.168.1.1",
            "10.0.0.1",
            "0.0.0.0",
            "255.255.255.255",
            "127.0.0.1",
        ]
        for ip in valid_ips:
            op_counter.increment()
            assert is_valid_ip(ip), f"{ip} should be valid"
        print(f" ({op_counter.count} operations)", end="")
    
    def test_invalid_ipv4_out_of_range(self, op_counter):
        """Test IPv4 with values out of range."""
        invalid_ips = [
            "256.1.1.1",
            "192.168.300.1",
            "192.168.1.256",
            "999.999.999.999",
        ]
        for ip in invalid_ips:
            op_counter.increment()
            assert not is_valid_ip(ip), f"{ip} should be invalid"
        print(f" ({op_counter.count} operations)", end="")
    
    def test_invalid_ipv4_format(self, op_counter):
        """Test IPv4 with invalid format."""
        invalid_ips = [
            "192.168.1",
            "192.168.1.1.1",
            "192.168..1",
            "192.168.1.a",
            "",
            "...",
            "1.1.1.",
        ]
        for ip in invalid_ips:
            op_counter.increment()
            assert not is_valid_ip(ip), f"{ip} should be invalid"
        print(f" ({op_counter.count} operations)", end="")
    
    def test_negative_numbers(self, op_counter):
        """Test IPv4 with negative numbers."""
        op_counter.increment()
        assert not is_valid_ip("-1.0.0.1")
        assert not is_valid_ip("192.168.-1.1")
        print(f" ({op_counter.count} operations)", end="")


class TestGetPacketSize:
    """Test suite for get_packet_size function."""
    
    def test_get_size_valid_packet(self, op_counter):
        """Test getting size of valid packet."""
        packet = "192.168.1.1:10.0.0.1|HTTP:GET /index.html"
        op_counter.increment()
        size = get_packet_size(packet)
        
        assert size == 16  # "GET /index.html" has 16 characters
        print(f" ({op_counter.count} operations)", end="")
    
    def test_get_size_empty_payload(self, op_counter):
        """Test getting size of packet with empty payload."""
        packet = "192.168.1.1:10.0.0.1|HTTP:"
        op_counter.increment()
        size = get_packet_size(packet)
        
        assert size == 0
        print(f" ({op_counter.count} operations)", end="")
    
    def test_get_size_invalid_packet(self, op_counter):
        """Test getting size of invalid packet."""
        op_counter.increment()
        size = get_packet_size("invalid_packet")
        
        assert size == 0
        print(f" ({op_counter.count} operations)", end="")
    
    def test_get_size_various_payloads(self, op_counter):
        """Test getting size of packets with various payload lengths."""
        test_cases = [
            ("192.168.1.1:10.0.0.1|HTTP:A", 1),
            ("192.168.1.1:10.0.0.1|HTTP:ABCD", 4),
            ("192.168.1.1:10.0.0.1|HTTP:" + "X" * 100, 100),
        ]
        for packet, expected_size in test_cases:
            op_counter.increment()
            assert get_packet_size(packet) == expected_size
        print(f" ({op_counter.count} operations)", end="")


class TestIntegration:
    """Integration tests combining multiple functions."""
    
    def test_parse_and_validate(self, op_counter):
        """Test parsing and then validating IPs."""
        packet = "192.168.1.1:10.0.0.1|HTTP:GET /index.html"
        op_counter.increment()
        parsed = parse_packet(packet)
        
        assert parsed is not None
        op_counter.increment()
        assert is_valid_ip(parsed["source"])
        op_counter.increment()
        assert is_valid_ip(parsed["destination"])
        print(f" ({op_counter.count} operations)", end="")
    
    def test_parse_invalid_ip(self, op_counter):
        """Test that invalid IPs are detected."""
        packet = "256.1.1.1:10.0.0.1|HTTP:GET"
        op_counter.increment()
        parsed = parse_packet(packet)
        
        # Parse should still work, but IP should be invalid
        assert parsed is not None
        op_counter.increment()
        assert not is_valid_ip(parsed["source"])
        print(f" ({op_counter.count} operations)", end="")


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "Packet Parser - DSA Exercises",
        "Performance tracking enabled - operation counts shown in parentheses",
    ]


def pytest_runtest_teardown(item, nextitem):
    """Print operation count after each test."""
    # This will show additional performance info
    pass
