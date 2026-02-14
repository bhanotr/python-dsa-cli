import pytest
from main import IPClassifier


class TestIPClassifierInit:
    """Test suite for IPClassifier initialization."""
    
    def test_init_empty(self):
        """Test that new classifier is empty."""
        classifier = IPClassifier()
        assert len(classifier.get_all_networks()) == 0


class TestExtractNetwork:
    """Test suite for _extract_network method."""
    
    def test_extract_standard_ip(self):
        """Test extracting network from standard IP."""
        classifier = IPClassifier()
        assert classifier._extract_network("192.168.1.100") == "192.168.1.0"
        assert classifier._extract_network("10.0.0.1") == "10.0.0.0"
    
    def test_extract_different_ranges(self):
        """Test extracting network from different IP ranges."""
        classifier = IPClassifier()
        assert classifier._extract_network("172.16.0.1") == "172.16.0.0"
        assert classifier._extract_network("8.8.8.8") == "8.8.8.0"


class TestAddIP:
    """Test suite for add_ip operation."""
    
    def test_add_single_ip(self):
        """Test adding a single IP."""
        classifier = IPClassifier()
        classifier.add_ip("192.168.1.1")
        all_networks = classifier.get_all_networks()
        assert "192.168.1.0" in all_networks
        assert all_networks["192.168.1.0"] == 1
    
    def test_add_multiple_ips_same_network(self):
        """Test adding multiple IPs in same network."""
        classifier = IPClassifier()
        classifier.add_ip("192.168.1.1")
        classifier.add_ip("192.168.1.2")
        classifier.add_ip("192.168.1.3")
        assert classifier.get_network_count("192.168.1.0") == 3
    
    def test_add_multiple_ips_different_networks(self):
        """Test adding IPs from different networks."""
        classifier = IPClassifier()
        classifier.add_ip("192.168.1.1")
        classifier.add_ip("10.0.0.1")
        assert classifier.get_network_count("192.168.1.0") == 1
        assert classifier.get_network_count("10.0.0.0") == 1


class TestGetNetworkCount:
    """Test suite for get_network_count operation."""
    
    def test_get_existing_network(self):
        """Test getting count of existing network."""
        classifier = IPClassifier()
        classifier.add_ip("192.168.1.1")
        classifier.add_ip("192.168.1.2")
        assert classifier.get_network_count("192.168.1.0") == 2
    
    def test_get_nonexistent_network(self):
        """Test getting count of non-existent network."""
        classifier = IPClassifier()
        assert classifier.get_network_count("192.168.1.0") == 0
    
    def test_get_count_empty_classifier(self):
        """Test getting count from empty classifier."""
        classifier = IPClassifier()
        assert classifier.get_network_count("192.168.1.0") == 0


class TestGetAllNetworks:
    """Test suite for get_all_networks operation."""
    
    def test_get_empty_classifier(self):
        """Test getting all networks from empty classifier."""
        classifier = IPClassifier()
        assert classifier.get_all_networks() == {}
    
    def test_get_single_network(self):
        """Test getting all networks with single network."""
        classifier = IPClassifier()
        classifier.add_ip("192.168.1.1")
        classifier.add_ip("192.168.1.2")
        all_networks = classifier.get_all_networks()
        assert len(all_networks) == 1
        assert all_networks["192.168.1.0"] == 2
    
    def test_get_multiple_networks(self):
        """Test getting all networks with multiple networks."""
        classifier = IPClassifier()
        classifier.add_ip("192.168.1.1")
        classifier.add_ip("10.0.0.1")
        classifier.add_ip("172.16.0.1")
        all_networks = classifier.get_all_networks()
        assert len(all_networks) == 3
        assert all_networks["192.168.1.0"] == 1
        assert all_networks["10.0.0.0"] == 1
        assert all_networks["172.16.0.0"] == 1


class TestGetIPsInNetwork:
    """Test suite for get_ips_in_network operation."""
    
    def test_get_ips_existing_network(self):
        """Test getting IPs from existing network."""
        classifier = IPClassifier()
        classifier.add_ip("192.168.1.1")
        classifier.add_ip("192.168.1.2")
        ips = classifier.get_ips_in_network("192.168.1.0")
        assert len(ips) == 2
        assert "192.168.1.1" in ips
        assert "192.168.1.2" in ips
    
    def test_get_ips_nonexistent_network(self):
        """Test getting IPs from non-existent network."""
        classifier = IPClassifier()
        ips = classifier.get_ips_in_network("192.168.1.0")
        assert ips == []
    
    def test_get_ips_empty_classifier(self):
        """Test getting IPs from empty classifier."""
        classifier = IPClassifier()
        ips = classifier.get_ips_in_network("192.168.1.0")
        assert ips == []


class TestIntegration:
    """Integration tests for IP classifier."""
    
    def test_full_workflow(self):
        """Test complete workflow of IP classification."""
        classifier = IPClassifier()
        
        # Add IPs from different networks
        ips = [
            "192.168.1.1", "192.168.1.2",
            "10.0.0.1", "10.0.0.2", "10.0.0.3",
            "172.16.0.1"
        ]
        
        for ip in ips:
            classifier.add_ip(ip)
        
        # Check all networks
        all_networks = classifier.get_all_networks()
        assert len(all_networks) == 3
        
        # Check individual counts
        assert classifier.get_network_count("192.168.1.0") == 2
        assert classifier.get_network_count("10.0.0.0") == 3
        assert classifier.get_network_count("172.16.0.0") == 1
        
        # Check IPs in specific network
        ips_10_network = classifier.get_ips_in_network("10.0.0.0")
        assert len(ips_10_network) == 3
        assert "10.0.0.1" in ips_10_network
        assert "10.0.0.2" in ips_10_network
        assert "10.0.0.3" in ips_10_network


def pytest_report_header(config):
    """Add custom header to pytest report."""
    return [
        "",
        "IP Classifier (Hash Tables) - DSA Exercises",
    ]
