from typing import List
from collections import Counter


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Find the k most frequent elements in the array.

    Args:
        nums: List of integers
        k: Number of most frequent elements to return

    Returns:
        List of k most frequent elements
    """
    count = Counter(nums)
    
    sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
    
    return [item[0] for item in sorted_items[:k]]


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
