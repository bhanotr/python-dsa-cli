from typing import List, Dict


def optimize_bandwidth(segments: List[Dict[str, int]], total_capacity: int) -> int:
    """
    Optimize bandwidth allocation across network segments.

    Args:
        segments: List of dicts with 'capacity' and 'throughput'
        total_capacity: Total bandwidth available

    Returns:
        Maximum achievable throughput
    """
    n = len(segments)
    
    if n == 0 or total_capacity == 0:
        return 0
    
    # DP: dp[i][b] = max throughput using first i segments with bandwidth b
    dp = [[0] * (total_capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for b in range(total_capacity + 1):
            # Don't use segment i
            dp[i][b] = dp[i - 1][b]
            
            # Use segment i if possible
            if segments[i - 1]['capacity'] <= b:
                dp[i][b] = max(dp[i][b],
                                 dp[i - 1][b - segments[i - 1]['capacity']] +
                                 segments[i - 1]['throughput'])
    
    return dp[n][total_capacity]


def main():
    """Test bandwidth optimization."""
    segments = [
        {'capacity': 2, 'throughput': 3},
        {'capacity': 3, 'throughput': 4},
        {'capacity': 4, 'throughput': 5},
        {'capacity': 5, 'throughput': 8},
    ]
    total_capacity = 10
    
    result = optimize_bandwidth(segments, total_capacity)
    
    print("Bandwidth Optimization Test:")
    print("=" * 60)
    print(f"Segments: {segments}")
    print(f"Total Capacity: {total_capacity}")
    print(f"Maximum Throughput: {result}")


if __name__ == "__main__":
    main()
