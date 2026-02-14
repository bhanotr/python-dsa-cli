from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merge all overlapping intervals.

    Args:
        intervals: List of intervals [start, end]

    Returns:
        List of merged non-overlapping intervals
    """
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for interval in intervals[1:]:
        last = merged[-1]
        
        if interval[0] <= last[1]:
            last[1] = max(last[1], interval[1])
        else:
            merged.append(interval)
    
    return merged


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
