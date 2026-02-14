from typing import Dict, List


class IPClassifier:
    """Classify IP addresses by subnet and count them."""
    
    def __init__(self):
        self.networks = {}
    
    def _extract_network(self, ip: str) -> str:
        parts = ip.split('.')
        return f"{parts[0]}.{parts[1]}.{parts[2]}.0"
    
    def add_ip(self, ip: str) -> None:
        network = self._extract_network(ip)
        if network not in self.networks:
            self.networks[network] = []
        self.networks[network].append(ip)
    
    def get_network_count(self, network: str) -> int:
        if network not in self.networks:
            return 0
        return len(self.networks[network])
    
    def get_all_networks(self) -> Dict[str, int]:
        return {network: len(ips) for network, ips in self.networks.items()}
    
    def get_ips_in_network(self, network: str) -> List[str]:
        return self.networks.get(network, [])


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
