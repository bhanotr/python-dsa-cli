from typing import Optional, List, Tuple


class TreeNode:
    """Node in a network topology binary tree."""
    
    def __init__(self, device_id: int, ip: str):
        # TODO: Initialize node attributes
        # device_id: Unique device identifier
        # ip: Device IP address
        # left: Left child (default None)
        # right: Right child (default None)
        pass


class NetworkTopology:
    """Binary tree for network device hierarchy."""
    
    def __init__(self):
        """
        Initialize an empty network topology.
        """
        # TODO: Initialize root attribute
        pass
    
    def insert(self, device_id: int, ip: str) -> None:
        """
        Insert a device node into the tree.

        Args:
            device_id: Unique device identifier
            ip: Device IP address
        """
        # TODO: Implement insert
        # 1. Create new TreeNode
        # 2. If root is None, set as root
        # 3. Otherwise, find correct position and insert
        # Use BST-like ordering: left < root < right
        pass
    
    def find(self, device_id: int) -> Optional[TreeNode]:
        """
        Find a device node by device_id.

        Args:
            device_id: Device identifier to find

        Returns:
            The node if found, None otherwise
        """
        # TODO: Implement find
        # 1. Start at root
        # 2. Compare device_id with current node
        # 3. Go left or right based on comparison
        # 4. Return node if found, None if not
        pass
    
    def _inorder_helper(self, node: Optional[TreeNode], result: List[Tuple[int, str]]) -> None:
        """
        Helper for in-order traversal.

        Args:
            node: Current node
            result: List to store traversal results
        """
        # TODO: Implement in-order traversal helper
        # Order: Left, Root, Right
        pass
    
    def inorder_traversal(self) -> List[Tuple[int, str]]:
        """
        Get in-order traversal of the tree.

        Returns:
            List of (device_id, ip) tuples in in-order
        """
        # TODO: Return in-order traversal
        pass
    
    def _preorder_helper(self, node: Optional[TreeNode], result: List[Tuple[int, str]]) -> None:
        """
        Helper for pre-order traversal.

        Args:
            node: Current node
            result: List to store traversal results
        """
        # TODO: Implement pre-order traversal helper
        # Order: Root, Left, Right
        pass
    
    def preorder_traversal(self) -> List[Tuple[int, str]]:
        """
        Get pre-order traversal of the tree.

        Returns:
            List of (device_id, ip) tuples in pre-order
        """
        # TODO: Return pre-order traversal
        pass
    
    def _postorder_helper(self, node: Optional[TreeNode], result: List[Tuple[int, str]]) -> None:
        """
        Helper for post-order traversal.

        Args:
            node: Current node
            result: List to store traversal results
        """
        # TODO: Implement post-order traversal helper
        # Order: Left, Right, Root
        pass
    
    def postorder_traversal(self) -> List[Tuple[int, str]]:
        """
        Get post-order traversal of the tree.

        Returns:
            List of (device_id, ip) tuples in post-order
        """
        # TODO: Return post-order traversal
        pass
    
    def _get_depth_helper(self, node: Optional[TreeNode]) -> int:
        """
        Helper to get depth of subtree.

        Args:
            node: Current node

        Returns:
            Depth of subtree
        """
        # TODO: Implement depth helper
        # Return 1 + max(left_depth, right_depth)
        # Base case: return 0 if node is None
        pass
    
    def get_depth(self) -> int:
        """
        Get the depth of the tree.

        Returns:
            Tree depth (max number of levels)
        """
        # TODO: Return tree depth
        pass


def main():
    """Test the network topology tree with sample data."""
    print("Network Topology (Binary Tree)")
    print("=" * 60)
    
    tree = NetworkTopology()
    
    # Insert devices
    print("\nInserting devices:")
    devices = [
        (50, "10.0.0.50"),
        (30, "10.0.0.30"),
        (70, "10.0.0.70"),
        (20, "10.0.0.20"),
        (40, "10.0.0.40"),
        (60, "10.0.0.60"),
        (80, "10.0.0.80"),
    ]
    for device_id, ip in devices:
        tree.insert(device_id, ip)
        print(f"  Inserted: Device {device_id} ({ip})")
    
    # Find device
    print("\nFinding devices:")
    node = tree.find(40)
    if node:
        print(f"  Found: Device {node.device_id} ({node.ip})")
    
    # Traversals
    print("\nIn-order traversal:")
    for device_id, ip in tree.inorder_traversal():
        print(f"  Device {device_id} ({ip})")
    
    print("\nPre-order traversal:")
    for device_id, ip in tree.preorder_traversal():
        print(f"  Device {device_id} ({ip})")
    
    print("\nPost-order traversal:")
    for device_id, ip in tree.postorder_traversal():
        print(f"  Device {device_id} ({ip})")
    
    # Depth
    print(f"\nTree depth: {tree.get_depth()}")


if __name__ == "__main__":
    main()
