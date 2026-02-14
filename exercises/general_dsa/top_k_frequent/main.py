from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Find the k most frequent elements in the array.

    Args:
        nums: List of integers
        k: Number of most frequent elements to return

    Returns:
        List of k most frequent elements
    """
    # TODO: Implement top_k_frequent
    # 1. Use a hash map to count frequencies
    # 2. Sort elements by frequency (descending)
    # 3. Return top k elements
    pass


def main():
    """Test the top_k_frequent function."""
    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2),
        ([1], 1),
        ([4, 1, -1, 2, -1, 2, 3], 2),
        ([1, 2, 2, 3, 3, 3], 1),
        ([1, 2, 3, 4, 5], 3),
    ]

    print("Top K Frequent Tests:")
    print("=" * 60)
    
    for nums, k in test_cases:
        result = top_k_frequent(nums, k)
        print(f"\nInput: {nums}, k: {k}")
        print(f"Top {k} frequent: {result}")


if __name__ == "__main__":
    main()
