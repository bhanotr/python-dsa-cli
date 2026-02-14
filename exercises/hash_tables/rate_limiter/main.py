import time
from typing import Dict


class RateLimiter:
    """Token bucket rate limiter for API requests."""
    
    def __init__(self, capacity: int, refill_rate: int):
        """
        Initialize the rate limiter.

        Args:
            capacity: Maximum number of tokens in bucket
            refill_rate: Tokens to add per second
        """
        # TODO: Initialize rate limiter attributes
        # capacity: Max tokens
        # refill_rate: Tokens per second
        # clients: Dictionary tracking state per IP
        pass
    
    def _refill_tokens(self, client_state: Dict, current_time: float) -> None:
        """
        Refill tokens based on time elapsed since last refill.

        Args:
            client_state: Dictionary with 'tokens' and 'last_refill_time'
            current_time: Current timestamp
        """
        # TODO: Refill tokens
        # 1. Calculate time elapsed
        # 2. Calculate tokens to add: elapsed * refill_rate
        # 3. Add tokens, cap at capacity
        # 4. Update last_refill_time
        pass
    
    def allow_request(self, ip: str) -> bool:
        """
        Check if a request from this IP should be allowed.

        Args:
            ip: The client IP address

        Returns:
            True if request allowed, False otherwise
        """
        # TODO: Check and allow request
        # 1. Get or create client state
        # 2. Refill tokens based on time
        # 3. Check if tokens >= 1
        # 4. If yes, consume token and return True
        # 5. If no, return False
        pass
    
    def get_token_count(self, ip: str) -> int:
        """
        Get the current token count for an IP.

        Args:
            ip: The client IP address

        Returns:
            Number of tokens available
        """
        # TODO: Return token count for IP
        # Return 0 if IP not tracked
        pass


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
