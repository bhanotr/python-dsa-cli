from collections import deque
from typing import Optional


class RequestQueue:
    """FIFO Queue for tracking network requests in order."""
    
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, request: str) -> None:
        self.queue.append(request)
    
    def dequeue(self) -> Optional[str]:
        if self.is_empty():
            return None
        return self.queue.popleft()
    
    def peek(self) -> Optional[str]:
        if self.is_empty():
            return None
        return self.queue[0]
    
    def is_empty(self) -> bool:
        return len(self.queue) == 0
    
    def size(self) -> int:
        return len(self.queue)


def main():
    """Test the request queue with sample data."""
    print("Request Queue (FIFO)")
    print("=" * 60)
    
    queue = RequestQueue()
    
    # Enqueue requests
    print("\nEnqueueing requests:")
    requests = [
        "GET /api/users",
        "POST /api/data",
        "DELETE /api/item/1",
        "PUT /api/item/2"
    ]
    for req in requests:
        queue.enqueue(req)
        print(f"  Enqueue: {req}")
    
    # Check size and peek
    print(f"\nQueue size: {queue.size()}")
    print(f"Front request: {queue.peek()}")
    
    # Dequeue requests
    print("\nDequeueing requests:")
    while not queue.is_empty():
        req = queue.dequeue()
        print(f"  Dequeue: {req} (size: {queue.size()})")
    
    # Test empty queue operations
    print("\nEmpty queue operations:")
    print(f"  Peek (empty): {queue.peek()}")
    print(f"  Dequeue (empty): {queue.dequeue()}")
    print(f"  Is empty: {queue.is_empty()}")


if __name__ == "__main__":
    main()
