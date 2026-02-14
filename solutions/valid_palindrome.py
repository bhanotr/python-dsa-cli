def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome, ignoring non-alphanumeric characters and case.

    Args:
        s: Input string

    Returns:
        True if palindrome, False otherwise
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


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
