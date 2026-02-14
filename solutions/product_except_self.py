from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    """
    Return array where answer[i] is product of all elements except nums[i].

    Args:
        nums: List of integers

    Returns:
        Array of products (excluding self at each position)
    """
    n = len(nums)
    answer = [1] * n
    
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]
    
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
    
    return answer


def main():
    """Test the product_except_self function."""
    test_cases = [
        [1, 2, 3, 4],
        [-1, 1, 0, -3, 3],
        [1, 2],
        [0, 0],
        [1, 0, 3, 0],
    ]

    print("Product Except Self Tests:")
    print("=" * 60)
    
    for nums in test_cases:
        result = product_except_self(nums)
        print(f"\nInput: {nums}")
        print(f"Product except self: {result}")


if __name__ == "__main__":
    main()
