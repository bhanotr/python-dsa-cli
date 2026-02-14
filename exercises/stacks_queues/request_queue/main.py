from collections import deque
from typing import Optional


class RequestQueue:
    """FIFO Queue for tracking network requests in order."""
    
    def __init__(self):
        """
        Initialize an empty request queue.
        """
        # TODO: Initialize queue attribute using deque
        pass
    
    def enqueue(self, request: str) -> None:
        """
        Add a request to the back of the queue.

        Args:
            request: The request string to add
        """
        # TODO: Add request to back of queue
        pass
    
    def dequeue(self) -> Optional[str]:
        """
        Remove and return the request from the front of the queue.

        Returns:
            The request at the front, or None if queue is empty
        """
        # TODO: Remove and return front request
        # Return None if queue is empty
        pass
    
    def peek(self) -> Optional[str]:
        """
        Return the request at the front of the queue without removing it.

        Returns:
            The request at the front, or None if queue is empty
        """
        # TODO: Return front request without removing
        # Return None if queue is empty
        pass
    
    def is_empty(self) -> bool:
        """
        Check if the queue is empty.

        Returns:
            True if queue is empty, False otherwise
        """
        # TODO: Return True if empty, False otherwise
        pass
    
    def size(self) -> int:
        """
        Get the number of requests in the queue.

        Returns:
            Number of requests in the queue
        """
        # TODO: Return queue size
        pass


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
