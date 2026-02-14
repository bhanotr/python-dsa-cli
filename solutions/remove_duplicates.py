from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """
    Remove duplicates from sorted array in-place.

    Args:
        nums: Sorted array of integers

    Returns:
        Number of unique elements (k)
    """
    if not nums:
        return 0
    
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1


def main():
    """Test the remove_duplicates function."""
    test_cases = [
        [1, 1, 2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        [1],
        [1, 1, 1, 1],
        [],
        [1, 2, 3, 4, 5],
    ]

    print("Remove Duplicates Tests:")
    print("=" * 60)
    
    for nums in test_cases:
        original = nums.copy()
        k = remove_duplicates(nums)
        print(f"\nOriginal: {original}")
        print(f"Unique count (k): {k}")
        print(f"First {k} elements: {nums[:k]}")


if __name__ == "__main__":
    main()
