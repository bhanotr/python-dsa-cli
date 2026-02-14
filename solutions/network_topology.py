from typing import Optional, List, Tuple


class TreeNode:
    """Node in a network topology binary tree."""
    
    def __init__(self, device_id: int, ip: str):
        self.device_id = device_id
        self.ip = ip
        self.left = None
        self.right = None


class NetworkTopology:
    """Binary tree for network device hierarchy."""
    
    def __init__(self):
        self.root = None
    
    def insert(self, device_id: int, ip: str) -> None:
        new_node = TreeNode(device_id, ip)
        
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while current:
            if device_id < current.device_id:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
    
    def find(self, device_id: int) -> Optional[TreeNode]:
        current = self.root
        while current:
            if device_id == current.device_id:
                return current
            elif device_id < current.device_id:
                current = current.left
            else:
                current = current.right
        return None
    
    def _inorder_helper(self, node: Optional[TreeNode], result: List[Tuple[int, str]]) -> None:
        if node is None:
            return
        self._inorder_helper(node.left, result)
        result.append((node.device_id, node.ip))
        self._inorder_helper(node.right, result)
    
    def inorder_traversal(self) -> List[Tuple[int, str]]:
        result = []
        self._inorder_helper(self.root, result)
        return result
    
    def _preorder_helper(self, node: Optional[TreeNode], result: List[Tuple[int, str]]) -> None:
        if node is None:
            return
        result.append((node.device_id, node.ip))
        self._preorder_helper(node.left, result)
        self._preorder_helper(node.right, result)
    
    def preorder_traversal(self) -> List[Tuple[int, str]]:
        result = []
        self._preorder_helper(self.root, result)
        return result
    
    def _postorder_helper(self, node: Optional[TreeNode], result: List[Tuple[int, str]]) -> None:
        if node is None:
            return
        self._postorder_helper(node.left, result)
        self._postorder_helper(node.right, result)
        result.append((node.device_id, node.ip))
    
    def postorder_traversal(self) -> List[Tuple[int, str]]:
        result = []
        self._postorder_helper(self.root, result)
        return result
    
    def _get_depth_helper(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        return 1 + max(self._get_depth_helper(node.left), self._get_depth_helper(node.right))
    
    def get_depth(self) -> int:
        return self._get_depth_helper(self.root)


def main():
    print("Network Topology (Binary Tree)")
    print("=" * 60)
    
    tree = NetworkTopology()
    
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
    
    print("\nFinding devices:")
    node = tree.find(40)
    if node:
        print(f"  Found: Device {node.device_id} ({node.ip})")
    
    print("\nIn-order traversal:")
    for device_id, ip in tree.inorder_traversal():
        print(f"  Device {device_id} ({ip})")
    
    print("\nPre-order traversal:")
    for device_id, ip in tree.preorder_traversal():
        print(f"  Device {device_id} ({ip})")
    
    print("\nPost-order traversal:")
    for device_id, ip in tree.postorder_traversal():
        print(f"  Device {device_id} ({ip})")
    
    print(f"\nTree depth: {tree.get_depth()}")


if __name__ == "__main__":
    main()
