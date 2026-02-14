from typing import List


def find_first_last(nums: List[int], target: int) -> List[int]:
    """
    Find the starting and ending position of a given target value.

    Args:
        nums: Sorted array of integers (non-decreasing)
        target: Target value to find

    Returns:
        [first_position, last_position] or [-1, -1] if not found
    """
    # TODO: Implement find_first_last
    # 1. Use binary search to find first occurrence
    # 2. Use binary search to find last occurrence
    # 3. Return [first, last] or [-1, -1] if not found
    pass


def main():
    """Test the find_first_last function."""
    test_cases = [
        ([5, 7, 7, 8, 8, 10], 8),
        ([5, 7, 7, 8, 8, 10], 6),
        ([], 0),
        ([2, 2], 2),
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 3, 3, 3, 4, 5], 3),
    ]

    print("Find First and Last Position Tests:")
    print("=" * 60)
    
    for nums, target in test_cases:
        result = find_first_last(nums, target)
        print(f"\nInput: {nums}, Target: {target}")
        print(f"Positions: {result}")


if __name__ == "__main__":
    main()
