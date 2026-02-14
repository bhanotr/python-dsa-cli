from typing import Optional


class DLinkedNode:
    """Node for doubly linked list used in LRU Cache."""
    
    def __init__(self, key: int = 0, value: str = ""):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """LRU Cache implementation using doubly linked list and hash map."""
    
    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with positive size capacity.

        Args:
            capacity: Maximum number of items the cache can hold
        """
        self.capacity = capacity
        self.cache = {}
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove_node(self, node: DLinkedNode):
        """
        Remove a node from the linked list.

        Args:
            node: The node to remove
        """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_head(self, node: DLinkedNode):
        """
        Add a node right after the head (most recently used position).

        Args:
            node: The node to add
        """
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _move_to_head(self, node: DLinkedNode):
        """
        Move an existing node to the head (most recently used).

        Args:
            node: The node to move
        """
        self._remove_node(node)
        self._add_to_head(node)
    
    def _pop_tail(self) -> Optional[DLinkedNode]:
        """
        Remove and return the least recently used node (before tail).

        Returns:
            The node that was removed
        """
        lru = self.tail.prev
        self._remove_node(lru)
        return lru
    
    def get(self, key: int) -> str | None:
        """
        Return the value of the key if the key exists, otherwise return None.

        Args:
            key: The key to look up

        Returns:
            The value if key exists, None otherwise
        """
        if key not in self.cache:
            return None
        node = self.cache[key]
        self._move_to_head(node)
        return node.value
    
    def put(self, key: int, value: str) -> None:
        """
        Add or update the value of the key.
        If the cache reaches its capacity, evict the least recently used item.

        Args:
            key: The key to add/update
            value: The value to store
        """
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            node = DLinkedNode(key, value)
            self._add_to_head(node)
            self.cache[key] = node
            
            if len(self.cache) > self.capacity:
                lru = self._pop_tail()
                del self.cache[lru.key]


def main():
    """Test the LRU cache with sample data."""
    print("LRU Cache (Linked List)")
    print("=" * 60)
    
    cache = LRUCache(2)
    
    # Put values
    print("\nPutting values:")
    cache.put(1, "10.0.0.1")
    print("  Put(1, '10.0.0.1')")
    cache.put(2, "10.0.0.2")
    print("  Put(2, '10.0.0.2')")
    
    # Get value
    print("\nGetting values:")
    print(f"  Get(1): {cache.get(1)}")
    
    # Put new value (should evict key 2)
    print("\nPutting new value (should evict least recent):")
    cache.put(3, "10.0.0.3")
    print("  Put(3, '10.0.0.3')")
    
    # Check evicted key
    print(f"  Get(2): {cache.get(2)}  # Should be None (evicted)")
    print(f"  Get(3): {cache.get(3)}")
    print(f"  Get(1): {cache.get(1)}")
    
    # Test update existing key
    print("\nUpdating existing key:")
    cache.put(1, "192.168.1.1")
    print(f"  Put(1, '192.168.1.1')")
    print(f"  Get(1): {cache.get(1)}")


if __name__ == "__main__":
    main()
