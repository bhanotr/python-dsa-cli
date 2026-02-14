from typing import List


def is_valid_config(config: str) -> bool:
    """
    Validate that brackets in the configuration are properly nested and closed.

    Args:
        config: String containing brackets: {}, [], ()

    Returns:
        True if brackets are valid, False otherwise
    """
    # TODO: Implement bracket validation using stack
    # 1. Create a stack (list)
    # 2. Define bracket pairs: closing -> opening
    # 3. Iterate through each character:
    #    - If opening bracket, push to stack
    #    - If closing bracket, check if stack top matches
    # 4. At the end, stack should be empty for valid config
    pass


def get_invalid_position(config: str) -> int:
    """
    Find the position of the first invalid bracket.

    Args:
        config: String containing brackets

    Returns:
        Index of first invalid bracket, or -1 if valid
    """
    # TODO: Find position of first invalid bracket
    # Return -1 if config is valid
    pass


def get_matching_pairs(config: str) -> List[tuple[int, int]]:
    """
    Get list of matching bracket positions.

    Args:
        config: String containing brackets

    Returns:
        List of tuples (open_pos, close_pos) for each pair
    """
    # TODO: Return list of matching bracket positions
    # Use a stack that stores positions
    pass


def main():
    """Test the bracket validator with sample data."""
    print("Bracket Validator (Stack)")
    print("=" * 60)
    
    test_configs = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}",
        "",
        "((()))",
        "([{}])",
        "((()",
    ]
    
    print("\nValidating configurations:")
    for config in test_configs:
        is_valid = is_valid_config(config)
        print(f"  '{config}': {'Valid' if is_valid else 'Invalid'}")
        if not is_valid:
            pos = get_invalid_position(config)
            if pos >= 0:
                print(f"    First invalid at position {pos}")
        else:
            pairs = get_matching_pairs(config)
            if pairs:
                print(f"    Matching pairs: {pairs}")


if __name__ == "__main__":
    main()
