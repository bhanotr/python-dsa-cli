SAFE_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.~"


def url_encode(url: str) -> str:
    """
    Encode a URL string by replacing special characters with %XX format.

    Args:
        url: The URL string to encode

    Returns:
        The URL encoded string
    """
    result = []
    for char in url:
        if char in SAFE_CHARS:
            result.append(char)
        else:
            hex_val = hex(ord(char))[2:].upper()
            hex_val = hex_val.zfill(2)
            result.append('%' + hex_val)
    return ''.join(result)


def url_decode(encoded_url: str) -> str:
    """
    Decode an encoded URL string.

    Args:
        encoded_url: The URL encoded string to decode

    Returns:
        The decoded URL string
    """
    result = []
    i = 0
    while i < len(encoded_url):
        if encoded_url[i] == '%' and i + 2 < len(encoded_url):
            hex_str = encoded_url[i+1:i+3]
            try:
                char_code = int(hex_str, 16)
                result.append(chr(char_code))
                i += 3
            except ValueError:
                result.append(encoded_url[i])
                i += 1
        else:
            result.append(encoded_url[i])
            i += 1
    return ''.join(result)


def is_valid_encoded(encoded_url: str) -> bool:
    """
    Validate that a URL is properly encoded.

    Args:
        encoded_url: The encoded URL to validate

    Returns:
        True if properly encoded, False otherwise
    """
    i = 0
    while i < len(encoded_url):
        if encoded_url[i] == '%':
            if i + 2 >= len(encoded_url):
                return False
            hex_str = encoded_url[i+1:i+3]
            if not all(c in '0123456789abcdefABCDEF' for c in hex_str):
                return False
            i += 3
        else:
            i += 1
    return True


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
