SAFE_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.~"


def url_encode(url: str) -> str:
    """
    Encode a URL string by replacing special characters with %XX format.

    Args:
        url: The URL string to encode

    Returns:
        The URL encoded string
    """
    # TODO: Implement URL encoding
    # 1. Iterate through each character
    # 2. If character is safe, add it as-is
    # 3. Otherwise, encode as %XX where XX is hex value
    # 4. Return encoded string
    pass


def url_decode(encoded_url: str) -> str:
    """
    Decode an encoded URL string.

    Args:
        encoded_url: The URL encoded string to decode

    Returns:
        The decoded URL string
    """
    # TODO: Implement URL decoding
    # 1. Iterate through characters
    # 2. When you see '%', extract next 2 characters
    # 3. Convert hex digits back to character
    # 4. Return decoded string
    pass


def is_valid_encoded(encoded_url: str) -> bool:
    """
    Validate that a URL is properly encoded.

    Args:
        encoded_url: The encoded URL to validate

    Returns:
        True if properly encoded, False otherwise
    """
    # TODO: Implement validation
    # 1. Check that every '%' is followed by 2 hex digits
    # 2. Handle edge cases like '%' at end of string
    # 3. Return True if valid, False if not
    pass


def main():
    """Test the URL encoder with sample data."""
    test_urls = [
        "hello world",
        "hello@world!",
        "https://example.com/path?query=value",
        "user@email.com",
        "special#$%^&*()",
    ]

    print("URL Encoding Tests:")
    print("=" * 60)
    
    for url in test_urls:
        encoded = url_encode(url)
        decoded = url_decode(encoded)
        valid = is_valid_encoded(encoded)
        
        print(f"\nOriginal: {url}")
        print(f"Encoded:  {encoded}")
        print(f"Decoded:  {decoded}")
        print(f"Valid:    {valid}")
        print(f"Match:    {url == decoded}")


if __name__ == "__main__":
    main()
