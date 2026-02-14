from typing import List, Tuple, Optional


def find_first_log(logs: List[Tuple[int, str]], timestamp: int) -> Optional[int]:
    """
    Find the first log entry with the given timestamp.

    Args:
        logs: List of (timestamp, message) tuples, sorted by timestamp
        timestamp: Timestamp to search for

    Returns:
        Index of first matching log, or None if not found
    """
    # TODO: Implement binary search for first occurrence
    # 1. Initialize left = 0, right = len(logs) - 1
    # 2. While left <= right:
    #    a. mid = (left + right) // 2
    #    b. If logs[mid].timestamp == target:
    #       - Store result, continue searching left
    #    c. If logs[mid].timestamp < target: left = mid + 1
    #    d. If logs[mid].timestamp > target: right = mid - 1
    # 3. Return result (None if not found)
    pass


def find_last_log(logs: List[Tuple[int, str]], timestamp: int) -> Optional[int]:
    """
    Find the last log entry with the given timestamp.

    Args:
        logs: List of (timestamp, message) tuples, sorted by timestamp
        timestamp: Timestamp to search for

    Returns:
        Index of last matching log, or None if not found
    """
    # TODO: Implement binary search for last occurrence
    # Similar to find_first_log, but search right when match found
    pass


def find_log_range(logs: List[Tuple[int, str]], start_ts: int, end_ts: int) -> List[Tuple[int, str]]:
    """
    Find all log entries within a timestamp range [start_ts, end_ts].

    Args:
        logs: List of (timestamp, message) tuples, sorted by timestamp
        start_ts: Start timestamp (inclusive)
        end_ts: End timestamp (inclusive)

    Returns:
        List of log entries in the range
    """
    # TODO: Find logs in range
    # 1. Find first index with timestamp >= start_ts
    # 2. Find last index with timestamp <= end_ts
    # 3. Return slice of logs in that range
    pass


def main():
    """Test the log analyzer with sample data."""
    print("Log Analyzer (Binary Search)")
    print("=" * 60)
    
    logs = [
        (100, "Error: Connection failed"),
        (100, "Error: Timeout"),
        (150, "Warning: High latency"),
        (200, "Info: Request received"),
        (250, "Info: Processing"),
        (300, "Info: Complete"),
        (350, "Warning: High memory"),
        (400, "Error: Disk full"),
        (400, "Error: Disk full retry"),
        (500, "Info: Shutdown")
    ]
    
    print("\nLogs (sorted by timestamp):")
    for ts, msg in logs:
        print(f"  [{ts}] {msg}")
    
    # Find first log
    target = 100
    first_idx = find_first_log(logs, target)
    print(f"\nFirst log with timestamp {target}:")
    if first_idx is not None:
        ts, msg = logs[first_idx]
        print(f"  Index {first_idx}: [{ts}] {msg}")
    else:
        print("  Not found")
    
    # Find last log
    last_idx = find_last_log(logs, 400)
    print(f"\nLast log with timestamp 400:")
    if last_idx is not None:
        ts, msg = logs[last_idx]
        print(f"  Index {last_idx}: [{ts}] {msg}")
    else:
        print("  Not found")
    
    # Find range
    print("\nLogs in range [150, 350]:")
    range_logs = find_log_range(logs, 150, 350)
    for ts, msg in range_logs:
        print(f"  [{ts}] {msg}")
    print(f"  Total: {len(range_logs)} logs")


if __name__ == "__main__":
    main()
