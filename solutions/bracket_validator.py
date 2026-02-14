from typing import List


def is_valid_config(config: str) -> bool:
    """
    Validate that brackets in the configuration are properly nested and closed.

    Args:
        config: String containing brackets: {}, [], ()

    Returns:
        True if brackets are valid, False otherwise
    """
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in config:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0


def get_invalid_position(config: str) -> int:
    """
    Find the position of the first invalid bracket.

    Args:
        config: String containing brackets

    Returns:
        Index of first invalid bracket, or -1 if valid
    """
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for pos, char in enumerate(config):
        if char in '([{':
            stack.append((char, pos))
        elif char in ')]}':
            if not stack:
                return pos
            if stack[-1][0] != pairs[char]:
                return pos
            stack.pop()
    
    return stack[0][1] if stack else -1


def get_matching_pairs(config: str) -> List[tuple[int, int]]:
    """
    Get list of matching bracket positions.

    Args:
        config: String containing brackets

    Returns:
        List of tuples (open_pos, close_pos) for each pair
    """
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    result = []
    
    for pos, char in enumerate(config):
        if char in '([{':
            stack.append((char, pos))
        elif char in ')]}':
            if not stack or stack[-1][0] != pairs[char]:
                return []
            open_pos = stack.pop()[1]
            result.append((open_pos, pos))
    
    return result if not stack else []


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
