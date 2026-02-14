import time
from typing import Optional


class DNSCache:
    """DNS cache with TTL (time-to-live) support."""
    
    def __init__(self):
        """
        Initialize an empty DNS cache.
        """
        # TODO: Initialize cache dictionary
        # Structure: {hostname: {"ip": ip, "expires_at": timestamp}}
        pass
    
    def put(self, hostname: str, ip: str, ttl: int) -> None:
        """
        Store a DNS entry with TTL.

        Args:
            hostname: The domain name
            ip: The IP address
            ttl: Time-to-live in seconds
        """
        # TODO: Store the DNS entry
        # 1. Calculate expiration time: current_time + ttl
        # 2. Store in cache with IP and expiration time
        pass
    
    def get(self, hostname: str) -> Optional[str]:
        """
        Get the IP address for a hostname if not expired.

        Args:
            hostname: The domain name to look up

        Returns:
            The IP address if found and not expired, None otherwise
        """
        # TODO: Retrieve DNS entry
        # 1. Check if hostname exists in cache
        # 2. Check if entry is not expired (expires_at > current_time)
        # 3. Return IP if valid, None otherwise
        pass
    
    def cleanup(self) -> int:
        """
        Remove all expired entries from the cache.

        Returns:
            Number of entries removed
        """
        # TODO: Remove expired entries
        # 1. Iterate through cache
        # 2. Remove entries where expires_at <= current_time
        # 3. Return count of removed entries
        pass
    
    def size(self) -> int:
        """
        Get the number of entries in the cache.

        Returns:
            Number of entries
        """
        # TODO: Return cache size
        pass


def main():
    """Test the DNS cache with sample data."""
    print("DNS Cache with TTL")
    print("=" * 60)
    
    cache = DNSCache()
    
    # Put DNS entries
    print("\nAdding DNS entries:")
    cache.put("example.com", "93.184.216.34", 60)
    print("  example.com -> 93.184.216.34 (TTL: 60s)")
    cache.put("google.com", "142.250.81.46", 30)
    print("  google.com -> 142.250.81.46 (TTL: 30s)")
    cache.put("github.com", "140.82.112.3", 10)
    print("  github.com -> 140.82.112.3 (TTL: 10s)")
    
    print(f"\nCache size: {cache.size()}")
    
    # Get entries
    print("\nRetrieving entries:")
    print(f"  example.com: {cache.get('example.com')}")
    print(f"  google.com: {cache.get('google.com')}")
    print(f"  github.com: {cache.get('github.com')}")
    print(f"  unknown.com: {cache.get('unknown.com')}")
    
    # Cleanup expired
    print("\nCleaning up expired entries:")
    time.sleep(1)  # Simulate some time passing
    removed = cache.cleanup()
    print(f"  Removed {removed} expired entries")
    print(f"  Cache size: {cache.size()}")


if __name__ == "__main__":
    main()
