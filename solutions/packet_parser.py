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
    if not packet:
        return None
    
    # Split main parts
    parts = packet.split('|')
    if len(parts) != 2:
        return None
    
    # Split source:destination
    source_dest = parts[0].split(':')
    if len(source_dest) != 2:
        return None
    
    # Split type:payload
    type_payload = parts[1].split(':')
    if len(type_payload) != 2:
        return None
    
    return {
        'source': source_dest[0],
        'destination': source_dest[1],
        'packet_type': type_payload[0],
        'payload': type_payload[1]
    }


def is_valid_ip(ip: str) -> bool:
    """
    Validate IP address format.

    Args:
        ip: The IP address string to validate

    Returns:
        True if the IP is in valid format (X.X.X.X where each X is 0-255)
        False otherwise
    """
    parts = ip.split('.')
    
    # Must have exactly 4 parts
    if len(parts) != 4:
        return False
    
    for part in parts:
        # Must not be empty
        if not part:
            return False
        
        # Must be numeric
        if not part.isdigit():
            return False
        
        # Must be in range 0-255
        value = int(part)
        if value < 0 or value > 255:
            return False
    
    return True


def get_packet_size(packet: str) -> int:
    """
    Calculate the size of a packet (length of its payload).

    Args:
        packet: The packet string

    Returns:
        The length of the payload, or 0 if the packet is invalid
    """
    parsed = parse_packet(packet)
    if parsed is None:
        return 0
    return len(parsed['payload'])


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
