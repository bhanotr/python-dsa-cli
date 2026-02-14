# Exercise 3: Network Flow (Linked List)

## Meta Interview Pattern
This exercise is based on the **Linked List** pattern and **Two Pointers** problems commonly asked at Meta. Similar to:
- **Linked List Cycle** - LeetCode 141
- **Reverse Linked List** - LeetCode 206
- **Remove Nth Node From End** - LeetCode 19

## Task
Implement a singly linked list to track network traffic flows between nodes. Each node represents a connection point in a network, and the list tracks the path of a flow.

## What you'll learn
- Linked list structure and operations
- Node creation and linking
- Traversing linked lists
- Finding and removing nodes
- Two pointers technique

## Instructions
Complete the functions in `main.py`:

1. **FlowNode class** - Node for the linked list
   - Attributes: `destination`, `bandwidth`, `next`

2. **append_flow(head, destination, bandwidth)** - Add flow to end of list
   - Return the head of the list

3. **find_flow(head, destination)** - Find a flow by destination
   - Return the node if found, None otherwise

4. **remove_flow(head, destination)** - Remove a flow from the list
   - Return the new head of the list

5. **get_total_bandwidth(head)** - Calculate total bandwidth
   - Return sum of all bandwidths

6. **reverse_flows(head)** - Reverse the flow list
   - Return the new head

## Examples

```python
# Create flow list
head = None
head = append_flow(head, "10.0.0.1", 100)
head = append_flow(head, "10.0.0.2", 200)

# Find flow
node = find_flow(head, "10.0.0.1")
assert node.bandwidth == 100

# Get total bandwidth
total = get_total_bandwidth(head)
assert total == 300

# Remove flow
head = remove_flow(head, "10.0.0.1")
```

## Testing
Run tests with:
```bash
cd exercises/linked_lists/network_flow
pytest test_main.py -v
```

Or use the CLI:
```bash
dsa test network_flow
```

## Hints
If you get stuck, run:
```bash
dsa hint network_flow [1|2|3]
```

## Concepts

### Linked List Structure
```python
class FlowNode:
    def __init__(self, destination: str, bandwidth: int):
        self.destination = destination
        self.bandwidth = bandwidth
        self.next = None
```

### Traversal
```python
current = head
while current:
    # Process current node
    current = current.next
```

### Two Pointers
```python
# Use two pointers to find nth from end
fast = slow = head
for _ in range(n):
    fast = fast.next
while fast:
    fast = fast.next
    slow = slow.next
```

## Time Complexity Analysis
- `append_flow`: O(n) - Must traverse to end
- `find_flow`: O(n) - May need to traverse entire list
- `remove_flow`: O(n) - Find node, then remove
- `get_total_bandwidth`: O(n) - Traverse all nodes
- `reverse_flows`: O(n) - Single traversal

## Space Complexity
- O(1) for all operations (not counting the list itself)
