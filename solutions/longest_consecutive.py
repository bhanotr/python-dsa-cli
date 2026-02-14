from typing import List


def longest_consecutive(nums: List[int]) -> int:
    """
    Find the length of the longest consecutive elements sequence.

    Args:
        nums: List of integers (unsorted)

    Returns:
        Length of longest consecutive sequence
    """
    num_set = set(nums)
    longest = 0
    
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            longest = max(longest, current_streak)
    
    return longest


def main():
    """Test the longest_consecutive function."""
    test_cases = [
        [100, 4, 200, 1, 3, 2],
        [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
        [],
        [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6],
        [1, 2, 0, 1],
    ]

    print("Longest Consecutive Sequence Tests:")
    print("=" * 60)
    
    for nums in test_cases:
        result = longest_consecutive(nums)
        print(f"\nInput: {nums}")
        print(f"Longest consecutive length: {result}")


if __name__ == "__main__":
    main()
