import time
from typing import Optional


class DNSCache:
    """DNS cache with TTL (time-to-live) support."""
    
    def __init__(self):
        self.cache = {}
    
    def put(self, hostname: str, ip: str, ttl: int) -> None:
        expires_at = time.time() + ttl
        self.cache[hostname] = {
            "ip": ip,
            "expires_at": expires_at
        }
    
    def get(self, hostname: str) -> Optional[str]:
        if hostname not in self.cache:
            return None
        
        entry = self.cache[hostname]
        current_time = time.time()
        
        if entry["expires_at"] <= current_time:
            return None
        
        return entry["ip"]
    
    def cleanup(self) -> int:
        current_time = time.time()
        expired = []
        
        for hostname, entry in self.cache.items():
            if entry["expires_at"] <= current_time:
                expired.append(hostname)
        
        for hostname in expired:
            del self.cache[hostname]
        
        return len(expired)
    
    def size(self) -> int:
        return len(self.cache)


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
    time.sleep(1)
    removed = cache.cleanup()
    print(f"  Removed {removed} expired entries")
    print(f"  Cache size: {cache.size()}")


if __name__ == "__main__":
    main()
