from typing import Optional


class FlowNode:
    """Node in a network flow linked list."""
    
    def __init__(self, destination: str, bandwidth: int):
        # TODO: Initialize node attributes
        # destination: IP address or hostname
        # bandwidth: Bandwidth value
        # next: Reference to next node (default None)
        pass


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
    # TODO: Implement append
    # 1. Create new node
    # 2. If head is None, return new node
    # 3. Otherwise, traverse to end and append
    pass


def find_flow(head: Optional[FlowNode], destination: str) -> Optional[FlowNode]:
    """
    Find a flow by destination.

    Args:
        head: Head of the linked list
        destination: Destination to find

    Returns:
        The node if found, None otherwise
    """
    # TODO: Implement find
    # 1. Traverse the list
    # 2. Check each node's destination
    # 3. Return node if found, None if not
    pass


def remove_flow(head: Optional[FlowNode], destination: str) -> Optional[FlowNode]:
    """
    Remove a flow from the list.

    Args:
        head: Head of the linked list
        destination: Destination to remove

    Returns:
        The new head of the list
    """
    # TODO: Implement remove
    # 1. Handle empty list
    # 2. Handle removing head
    # 3. Traverse and remove if found
    # 4. Return new head
    pass


def get_total_bandwidth(head: Optional[FlowNode]) -> int:
    """
    Calculate total bandwidth of all flows.

    Args:
        head: Head of the linked list

    Returns:
        Total bandwidth
    """
    # TODO: Implement total bandwidth calculation
    # 1. Traverse the list
    # 2. Sum up all bandwidths
    # 3. Return total
    pass


def reverse_flows(head: Optional[FlowNode]) -> Optional[FlowNode]:
    """
    Reverse the flow list.

    Args:
        head: Head of the linked list

    Returns:
        The new head of the reversed list
    """
    # TODO: Implement reverse
    # 1. Use three pointers: prev, current, next_node
    # 2. Iterate through list, reversing links
    # 3. Return new head (prev)
    pass


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
