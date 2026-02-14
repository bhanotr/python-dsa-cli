import time
from typing import Dict


class RateLimiter:
    """Token bucket rate limiter for API requests."""
    
    def __init__(self, capacity: int, refill_rate: int):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.clients = {}
    
    def _refill_tokens(self, client_state: Dict, current_time: float) -> None:
        last_time = client_state["last_refill_time"]
        time_elapsed = current_time - last_time
        tokens_to_add = time_elapsed * self.refill_rate
        
        client_state["tokens"] += tokens_to_add
        if client_state["tokens"] > self.capacity:
            client_state["tokens"] = self.capacity
        
        client_state["last_refill_time"] = current_time
    
    def allow_request(self, ip: str) -> bool:
        current_time = time.time()
        
        if ip not in self.clients:
            self.clients[ip] = {
                "tokens": self.capacity,
                "last_refill_time": current_time
            }
        
        client_state = self.clients[ip]
        self._refill_tokens(client_state, current_time)
        
        if client_state["tokens"] >= 1:
            client_state["tokens"] -= 1
            return True
        return False
    
    def get_token_count(self, ip: str) -> int:
        if ip not in self.clients:
            return 0
        return int(self.clients[ip]["tokens"])


def main():
    """Test the rate limiter with sample data."""
    print("Rate Limiter (Token Bucket)")
    print("=" * 60)
    
    limiter = RateLimiter(capacity=5, refill_rate=1)
    
    # Test requests from same IP
    print("\nRequests from 192.168.1.1:")
    ip = "192.168.1.1"
    for i in range(7):
        allowed = limiter.allow_request(ip)
        tokens = limiter.get_token_count(ip)
        print(f"  Request {i+1}: {'Allowed' if allowed else 'Blocked'} (tokens: {tokens})")
    
    # Wait for refill
    print("\nWaiting 2 seconds for refill...")
    time.sleep(2)
    
    # Test after refill
    print("\nRequests after refill:")
    for i in range(3):
        allowed = limiter.allow_request(ip)
        tokens = limiter.get_token_count(ip)
        print(f"  Request {i+1}: {'Allowed' if allowed else 'Blocked'} (tokens: {tokens})")
    
    # Test multiple IPs
    print("\nRequests from different IPs:")
    ips = ["10.0.0.1", "10.0.0.2"]
    for ip in ips:
        allowed = limiter.allow_request(ip)
        print(f"  {ip}: {'Allowed' if allowed else 'Blocked'}")


if __name__ == "__main__":
    main()
