import heapq
from typing import Optional


class PacketScheduler:
    """Priority queue for scheduling packets by priority."""
    
    def __init__(self):
        self.heap = []
        self.counter = 0
    
    def enqueue(self, packet: str, priority: int) -> None:
        heapq.heappush(self.heap, (-priority, self.counter, packet))
        self.counter += 1
    
    def dequeue(self) -> Optional[str]:
        if not self.heap:
            return None
        return heapq.heappop(self.heap)[2]
    
    def peek(self) -> Optional[str]:
        if not self.heap:
            return None
        return self.heap[0][2]
    
    def is_empty(self) -> bool:
        return len(self.heap) == 0
    
    def size(self) -> int:
        return len(self.heap)


def main():
    print("Packet Scheduler (Priority Queue)")
    print("=" * 60)
    
    scheduler = PacketScheduler()
    
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
    
    print("\nDequeueing packets (highest priority first):")
    while not scheduler.is_empty():
        packet = scheduler.dequeue()
        print(f"  Dequeued: {packet}")


if __name__ == "__main__":
    main()
