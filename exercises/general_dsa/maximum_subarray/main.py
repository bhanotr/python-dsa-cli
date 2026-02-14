from typing import List


def max_subarray(nums: List[int]) -> int:
    """
    Find the subarray with the largest sum.

    Args:
        nums: List of integers

    Returns:
        Maximum sum of any contiguous subarray
    """
    # TODO: Implement max_subarray (Kadane's algorithm)
    # 1. Track current sum (local maximum)
    # 2. Track best sum (global maximum)
    # 3. Decide at each step: extend or restart
    # 4. Return the best sum
    pass


def main():
    """Test the max_subarray function."""
    test_cases = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1],
        [5, 4, -1, 7, 8],
        [-1, -2, -3],
        [1, 2, 3, 4, 5],
        [1],
    ]

    print("Maximum Subarray Tests:")
    print("=" * 60)
    
    for nums in test_cases:
        result = max_subarray(nums)
        print(f"\nInput: {nums}")
        print(f"Max subarray sum: {result}")


if __name__ == "__main__":
    main()
