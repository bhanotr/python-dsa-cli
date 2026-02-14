from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """
    Check if the array contains any duplicate values.

    Args:
        nums: List of integers

    Returns:
        True if duplicates exist, False otherwise
    """
    # TODO: Implement contains_duplicate
    # 1. Use a hash set to track seen numbers
    # 2. Iterate through the array
    # 3. Return True if number already in set
    # 4. Return False at the end if no duplicates found
    pass


def main():
    """Test the contains_duplicate function."""
    test_cases = [
        [1, 2, 3, 1],
        [1, 2, 3, 4],
        [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
        [],
        [1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1],
    ]

    print("Contains Duplicate Tests:")
    print("=" * 60)
    
    for nums in test_cases:
        result = contains_duplicate(nums)
        print(f"\nInput: {nums}")
        print(f"Contains duplicate: {result}")


if __name__ == "__main__":
    main()
