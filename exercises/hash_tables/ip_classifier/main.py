from typing import Dict, List


class IPClassifier:
    """Classify IP addresses by subnet and count them."""
    
    def __init__(self):
        """
        Initialize an empty IP classifier.
        """
        # TODO: Initialize network groups dictionary
        # Structure: {network_prefix: [ip1, ip2, ...]}
        pass
    
    def _extract_network(self, ip: str) -> str:
        """
        Extract the network prefix from an IP address.

        Args:
            ip: The IP address (e.g., "192.168.1.100")

        Returns:
            The network prefix (e.g., "192.168.1.0")
        """
        # TODO: Extract network prefix (first 3 octets + .0)
        # 1. Split IP by '.'
        # 2. Take first 3 parts
        # 3. Add '.0' at the end
        pass
    
    def add_ip(self, ip: str) -> None:
        """
        Add an IP address to its network group.

        Args:
            ip: The IP address to add
        """
        # TODO: Add IP to its network group
        # 1. Extract network prefix
        # 2. Add IP to the network's list in the dictionary
        pass
    
    def get_network_count(self, network: str) -> int:
        """
        Get the number of IPs in a specific network.

        Args:
            network: The network prefix (e.g., "192.168.1.0")

        Returns:
            Number of IPs in the network
        """
        # TODO: Return count of IPs in network
        # Return 0 if network doesn't exist
        pass
    
    def get_all_networks(self) -> Dict[str, int]:
        """
        Get all networks and their IP counts.

        Returns:
            Dictionary of network prefix to count
        """
        # TODO: Return all networks with their counts
        pass
    
    def get_ips_in_network(self, network: str) -> List[str]:
        """
        Get all IPs in a specific network.

        Args:
            network: The network prefix

        Returns:
            List of IPs in the network
        """
        # TODO: Return list of IPs in network
        # Return empty list if network doesn't exist
        pass


def main():
    """Test the IP classifier with sample data."""
    print("IP Classifier")
    print("=" * 60)
    
    classifier = IPClassifier()
    
    # Add IPs
    print("\nAdding IPs:")
    ips = [
        "192.168.1.1",
        "192.168.1.2",
        "192.168.1.3",
        "10.0.0.1",
        "10.0.0.2",
        "172.16.0.1"
    ]
    for ip in ips:
        classifier.add_ip(ip)
        print(f"  Added: {ip}")
    
    # Get network counts
    print("\nNetwork counts:")
    all_networks = classifier.get_all_networks()
    for network, count in all_networks.items():
        print(f"  {network}: {count} IPs")
    
    # Get specific network count
    print(f"\n192.168.1.0 count: {classifier.get_network_count('192.168.1.0')}")
    
    # Get IPs in specific network
    print("\nIPs in 192.168.1.0:")
    for ip in classifier.get_ips_in_network("192.168.1.0"):
        print(f"  {ip}")


if __name__ == "__main__":
    main()
