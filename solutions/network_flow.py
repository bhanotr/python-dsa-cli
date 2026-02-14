from typing import Optional


class FlowNode:
    """Node in a network flow linked list."""
    
    def __init__(self, destination: str, bandwidth: int):
        self.destination = destination
        self.bandwidth = bandwidth
        self.next = None


def append_flow(head: Optional[FlowNode], destination: str, bandwidth: int) -> FlowNode:
    """
    Append a new flow to the end of the list.

    Args:
        head: Head of the linked list (None if empty)
        destination: Destination IP/hostname
        bandwidth: Bandwidth value

    Returns:
        The head of the updated list
    """
    new_node = FlowNode(destination, bandwidth)
    
    if head is None:
        return new_node
    
    current = head
    while current.next:
        current = current.next
    
    current.next = new_node
    return head


def find_flow(head: Optional[FlowNode], destination: str) -> Optional[FlowNode]:
    """
    Find a flow by destination.

    Args:
        head: Head of the linked list
        destination: Destination to find

    Returns:
        The node if found, None otherwise
    """
    current = head
    while current:
        if current.destination == destination:
            return current
        current = current.next
    return None


def remove_flow(head: Optional[FlowNode], destination: str) -> Optional[FlowNode]:
    """
    Remove a flow from the list.

    Args:
        head: Head of the linked list
        destination: Destination to remove

    Returns:
        The new head of the list
    """
    if head is None:
        return None
    
    # Remove head
    if head.destination == destination:
        return head.next
    
    current = head
    while current.next:
        if current.next.destination == destination:
            current.next = current.next.next
            return head
        current = current.next
    
    return head


def get_total_bandwidth(head: Optional[FlowNode]) -> int:
    """
    Calculate total bandwidth of all flows.

    Args:
        head: Head of the linked list

    Returns:
        Total bandwidth
    """
    total = 0
    current = head
    while current:
        total += current.bandwidth
        current = current.next
    return total


def reverse_flows(head: Optional[FlowNode]) -> Optional[FlowNode]:
    """
    Reverse the flow list.

    Args:
        head: Head of the linked list

    Returns:
        The new head of the reversed list
    """
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev


def print_flows(head: Optional[FlowNode]):
    """Print all flows in the list."""
    current = head
    while current:
        print(f"  -> {current.destination}: {current.bandwidth} Mbps")
        current = current.next


def main():
    """Test the network flow linked list."""
    print("Network Flow Tracking")
    print("=" * 60)
    
    # Create flows
    head = None
    print("\nAdding flows:")
    head = append_flow(head, "10.0.0.1", 100)
    print("Added: 10.0.0.1 (100 Mbps)")
    head = append_flow(head, "10.0.0.2", 200)
    print("Added: 10.0.0.2 (200 Mbps)")
    head = append_flow(head, "10.0.0.3", 150)
    print("Added: 10.0.0.3 (150 Mbps)")
    
    # Print all flows
    print("\nCurrent flows:")
    print_flows(head)
    
    # Find flow
    print("\nFinding flow to 10.0.0.2:")
    node = find_flow(head, "10.0.0.2")
    if node:
        print(f"  Found: {node.destination} ({node.bandwidth} Mbps)")
    
    # Get total bandwidth
    total = get_total_bandwidth(head)
    print(f"\nTotal bandwidth: {total} Mbps")
    
    # Remove flow
    print("\nRemoving flow to 10.0.0.2:")
    head = remove_flow(head, "10.0.0.2")
    print_flows(head)
    
    # Reverse flows
    print("\nReversing flows:")
    head = reverse_flows(head)
    print_flows(head)


if __name__ == "__main__":
    main()
