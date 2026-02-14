from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merge all overlapping intervals.

    Args:
        intervals: List of intervals [start, end]

    Returns:
        List of merged non-overlapping intervals
    """
    # TODO: Implement merge
    # 1. Sort intervals by start time
    # 2. Iterate through sorted intervals
    # 3. Merge overlapping intervals
    # 4. Return merged intervals
    pass


def main():
    """Test the merge function."""
    test_cases = [
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 4], [4, 5]],
        [[1, 4], [0, 4]],
        [],
        [[1, 4], [2, 3]],
        [[1, 4], [0, 2], [3, 5]],
    ]

    print("Merge Intervals Tests:")
    print("=" * 60)
    
    for intervals in test_cases:
        result = merge(intervals)
        print(f"\nInput: {intervals}")
        print(f"Merged: {result}")


if __name__ == "__main__":
    main()
