from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find two numbers in the array that add up to the target.

    Args:
        nums: List of integers
        target: Target sum to find

    Returns:
        List of two indices whose elements sum to target
    """
    # TODO: Implement two_sum
    # 1. Use a hash map to store {number: index}
    # 2. For each number, calculate complement = target - number
    # 3. Check if complement exists in hash map
    # 4. Return the indices when found
    pass


def main():
    """Test the two_sum function."""
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([1, 5, 3, 6], 8),
        ([10, 22, 5, 75, 65, 80], 87),
    ]

    print("Two Sum Tests:")
    print("=" * 60)
    
    for nums, target in test_cases:
        result = two_sum(nums, target)
        print(f"\nInput: {nums}, Target: {target}")
        print(f"Result indices: {result}")
        if result:
            print(f"Values: {nums[result[0]]} + {nums[result[1]]} = {nums[result[0]] + nums[result[1]]}")


if __name__ == "__main__":
    main()
