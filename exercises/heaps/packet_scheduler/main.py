import heapq
from typing import Optional, List, Tuple


class PacketScheduler:
    """Priority queue for scheduling packets by priority."""
    
    def __init__(self):
        """Initialize an empty packet scheduler."""
        # TODO: Initialize heap attribute
        # Store tuples of (-priority, counter, packet) for max-heap behavior
        # Counter ensures FIFO for same priority
        pass
    
    def enqueue(self, packet: str, priority: int) -> None:
        """
        Add a packet with given priority.

        Args:
            packet: The packet data
            priority: Priority value (higher = more important)
        """
        # TODO: Implement enqueue
        # 1. Use negative priority for max-heap
        # 2. Use counter for tie-breaking
        # 3. Push (-priority, counter, packet) to heap
        pass
    
    def dequeue(self) -> Optional[str]:
        """
        Remove and return the highest priority packet.

        Returns:
            The packet, or None if empty
        """
        # TODO: Implement dequeue
        # 1. Check if heap is empty
        # 2. Pop from heap
        # 3. Return packet from tuple
        pass
    
    def peek(self) -> Optional[str]:
        """
        Return the highest priority packet without removing.

        Returns:
            The packet, or None if empty
        """
        # TODO: Implement peek
        # 1. Check if heap is empty
        # 2. Return packet at index 0
        pass
    
    def is_empty(self) -> bool:
        """Check if scheduler is empty."""
        # TODO: Return True if empty, False otherwise
        pass
    
    def size(self) -> int:
        """Return the number of packets."""
        # TODO: Return heap size
        pass


def main():
    """Test the packet scheduler with sample data."""
    print("Packet Scheduler (Priority Queue)")
    print("=" * 60)
    
    scheduler = PacketScheduler()
    
    # Enqueue packets with different priorities
    print("\nEnqueueing packets:")
    packets = [
        ("GET /api/users", 1),
        ("POST /api/data", 3),
        ("DELETE /api/item", 2),
        ("PUT /api/update", 2),
        ("CRITICAL ALERT", 5)
    ]
    for packet, priority in packets:
        scheduler.enqueue(packet, priority)
        print(f"  Enqueued (priority {priority}): {packet}")
    
    print(f"\nScheduler size: {scheduler.size()}")
    print(f"Peek: {scheduler.peek()}")
    
    # Dequeue packets
    print("\nDequeueing packets (highest priority first):")
    while not scheduler.is_empty():
        packet = scheduler.dequeue()
        print(f"  Dequeued: {packet}")


if __name__ == "__main__":
    main()
