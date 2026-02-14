def parse_packet(packet: str) -> dict | None:
    """
    Parse a network packet string into its components.

    Packet format: SOURCE:DESTINATION|TYPE:PAYLOAD

    Args:
        packet: The packet string to parse

    Returns:
        A dict with keys: 'source', 'destination', 'packet_type', 'payload'
        Returns None if the packet is malformed
    """
    # TODO: Implement packet parsing
    # 1. Split the packet by '|' to separate addresses from type:payload
    # 2. Split the first part by ':' to get source and destination
    # 3. Split the second part by ':' to get packet_type and payload
    # 4. Return None if any component is missing or malformed
    pass


def is_valid_ip(ip: str) -> bool:
    """
    Validate IP address format.

    Args:
        ip: The IP address string to validate

    Returns:
        True if the IP is in valid format (X.X.X.X where each X is 0-255)
        False otherwise
    """
    # TODO: Implement IP validation
    # 1. Split the IP by '.'
    # 2. Check that there are exactly 4 parts
    # 3. Validate each part is a number between 0 and 255
    # 4. Handle edge cases: empty strings, non-numeric parts
    pass


def get_packet_size(packet: str) -> int:
    """
    Calculate the size of a packet (length of its payload).

    Args:
        packet: The packet string

    Returns:
        The length of the payload, or 0 if the packet is invalid
    """
    # TODO: Implement packet size calculation
    # 1. Parse the packet
    # 2. Extract the payload
    # 3. Return the length of the payload
    pass


def main():
    """Test the packet parser with sample data."""
    test_packets = [
        "192.168.1.1:10.0.0.1|HTTP:GET /index.html",
        "192.168.1.1:10.0.0.1|TCP:SYN",
        "192.168.1.1:10.0.0.1|:",
        "malformed_packet",
        "",
    ]

    for packet in test_packets:
        print(f"\nPacket: {packet}")
        parsed = parse_packet(packet)
        if parsed:
            print(f"  Source: {parsed['source']}")
            print(f"  Destination: {parsed['destination']}")
            print(f"  Type: {parsed['packet_type']}")
            print(f"  Payload: {parsed['payload']}")
            print(f"  Size: {get_packet_size(packet)}")
            print(f"  Valid Source IP: {is_valid_ip(parsed['source'])}")
        else:
            print("  Invalid packet")


if __name__ == "__main__":
    main()
