from typing import List


def max_subarray(nums: List[int]) -> int:
    """
    Find the subarray with the largest sum.

    Args:
        nums: List of integers

    Returns:
        Maximum sum of any contiguous subarray
    """
    current_sum = 0
    best_sum = float('-inf')
    
    for num in nums:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)
    
    return best_sum


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
