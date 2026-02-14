from typing import Optional


class DLinkedNode:
    """Node for doubly linked list used in LRU Cache."""
    
    def __init__(self, key: int = 0, value: str = ""):
        # TODO: Initialize node attributes
        # key: The cache key
        # value: The cached value
        # prev: Pointer to previous node
        # next: Pointer to next node
        pass


class LRUCache:
    """LRU Cache implementation using doubly linked list and hash map."""
    
    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with positive size capacity.

        Args:
            capacity: Maximum number of items the cache can hold
        """
        # TODO: Initialize cache attributes
        # capacity: Maximum number of items
        # cache: Dictionary mapping key to DLinkedNode
        # head: Dummy head node (most recently used side)
        # tail: Dummy tail node (least recently used side)
        pass
    
    def _remove_node(self, node: DLinkedNode):
        """
        Remove a node from the linked list.

        Args:
            node: The node to remove
        """
        # TODO: Remove node from list by updating neighbors' pointers
        pass
    
    def _add_to_head(self, node: DLinkedNode):
        """
        Add a node right after the head (most recently used position).

        Args:
            node: The node to add
        """
        # TODO: Insert node right after head
        pass
    
    def _move_to_head(self, node: DLinkedNode):
        """
        Move an existing node to the head (most recently used).

        Args:
            node: The node to move
        """
        # TODO: Remove node from current position and add to head
        pass
    
    def _pop_tail(self) -> Optional[DLinkedNode]:
        """
        Remove and return the least recently used node (before tail).

        Returns:
            The node that was removed
        """
        # TODO: Remove and return the node before tail
        pass
    
    def get(self, key: int) -> str | None:
        """
        Return the value of the key if the key exists, otherwise return None.

        Args:
            key: The key to look up

        Returns:
            The value if key exists, None otherwise
        """
        # TODO: Implement get operation
        # 1. Check if key exists in cache
        # 2. If exists, move node to head and return value
        # 3. If not exists, return None
        pass
    
    def put(self, key: int, value: str) -> None:
        """
        Add or update the value of the key.
        If the cache reaches its capacity, evict the least recently used item.

        Args:
            key: The key to add/update
            value: The value to store
        """
        # TODO: Implement put operation
        # 1. If key exists, update value and move to head
        # 2. If key doesn't exist:
        #    a. Create new node and add to head
        #    b. Add to cache dictionary
        #    c. If over capacity, remove tail node from list and cache
        pass


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
