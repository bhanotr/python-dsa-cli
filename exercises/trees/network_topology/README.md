# Exercise 10: Network Topology

## Meta Interview Pattern
This exercise is based on the **Binary Tree** pattern and **Tree Traversal** problems commonly asked at Meta. Similar to:
- **Binary Tree Inorder Traversal** - LeetCode 94
- **Maximum Depth of Binary Tree** - LeetCode 104

## Task
Implement a binary tree to represent network device hierarchy. Support traversal, search, and depth calculation.

## What you'll learn
- Binary tree structure
- Tree traversal algorithms (in-order, pre-order, post-order)
- Searching in binary trees
- Calculating tree depth

## Instructions
Complete the functions in `main.py`:

1. **TreeNode class** - Node for binary tree
   - Attributes: `device_id`, `ip`, `left`, `right`

2. **NetworkTopology class** - Tree operations
   - `insert(device_id, ip)` - Insert node into tree
   - `find(device_id)` - Find node by device_id
   - `inorder_traversal()` - Return list in in-order
   - `preorder_traversal()` - Return list in pre-order
   - `postorder_traversal()` - Return list in post-order
   - `get_depth()` - Return tree depth

## Examples

```python
tree = NetworkTopology()
tree.insert(1, "10.0.0.1")
tree.insert(2, "10.0.0.2")
tree.insert(3, "10.0.0.3")

# Traversals return lists of (device_id, ip)
assert tree.find(2).ip == "10.0.0.2"
assert tree.get_depth() == 2
```

## Testing
Run tests with:
```bash
cd exercises/trees/network_topology
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test network_topology
```

## Hints
If you get stuck, run:
```bash
dsa hint network_topology [1|2|3]
```

## Concepts

### Binary Tree Structure
```python
class TreeNode:
    def __init__(self, device_id, ip):
        self.device_id = device_id
        self.ip = ip
        self.left = None
        self.right = None
```

### Traversals
- **In-order**: Left, Root, Right
- **Pre-order**: Root, Left, Right
- **Post-order**: Left, Right, Root

### Tree Depth
- Depth = maximum distance from root to leaf
- Recursively: 1 + max(depth(left), depth(right))

## Time Complexity Analysis
- `insert`: O(h) where h is tree height
- `find`: O(h)
- Traversals: O(n) where n is number of nodes
- `get_depth`: O(n)

## Space Complexity
- O(n) for storing tree
- O(h) for recursion stack
