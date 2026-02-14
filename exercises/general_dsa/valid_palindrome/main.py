def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome, ignoring non-alphanumeric characters and case.

    Args:
        s: Input string

    Returns:
        True if palindrome, False otherwise
    """
    pass


def main():
    """Test the is_palindrome function."""
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
        "0P",
        "abba",
        "a",
        "",
        "No 'x' in Nixon",
    ]

    print("Valid Palindrome Tests:")
    print("=" * 60)
    
    for s in test_cases:
        result = is_palindrome(s)
        print(f"\nInput: '{s}'")
        print(f"Is palindrome: {result}")


if __name__ == "__main__":
    main()
