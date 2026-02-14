from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    """
    Return array where answer[i] is product of all elements except nums[i].

    Args:
        nums: List of integers

    Returns:
        Array of products (excluding self at each position)
    """
    # TODO: Implement product_except_self
    # 1. Calculate prefix products in first pass
    # 2. Calculate suffix products in second pass
    # 3. Multiply prefix and suffix for each position
    # 4. Cannot use division
    pass


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
