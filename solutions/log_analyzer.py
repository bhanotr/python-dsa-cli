from typing import List, Tuple, Optional


def find_first_log(logs: List[Tuple[int, str]], timestamp: int) -> Optional[int]:
    if not logs:
        return None
    
    left, right = 0, len(logs) - 1
    result = None
    
    while left <= right:
        mid = (left + right) // 2
        if logs[mid][0] == timestamp:
            result = mid
            right = mid - 1
        elif logs[mid][0] < timestamp:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def find_last_log(logs: List[Tuple[int, str]], timestamp: int) -> Optional[int]:
    if not logs:
        return None
    
    left, right = 0, len(logs) - 1
    result = None
    
    while left <= right:
        mid = (left + right) // 2
        if logs[mid][0] == timestamp:
            result = mid
            left = mid + 1
        elif logs[mid][0] < timestamp:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def find_log_range(logs: List[Tuple[int, str]], start_ts: int, end_ts: int) -> List[Tuple[int, str]]:
    if not logs:
        return []
    
    # Find first index with timestamp >= start_ts
    left, right = 0, len(logs)
    while left < right:
        mid = (left + right) // 2
        if logs[mid][0] < start_ts:
            left = mid + 1
        else:
            right = mid
    
    first = left
    
    # Find first index with timestamp > end_ts
    left, right = 0, len(logs)
    while left < right:
        mid = (left + right) // 2
        if logs[mid][0] <= end_ts:
            left = mid + 1
        else:
            right = mid
    
    last = left - 1
    
    if first > last:
        return []
    
    return logs[first:last + 1]


def main():
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
    
    target = 100
    first_idx = find_first_log(logs, target)
    print(f"\nFirst log with timestamp {target}:")
    if first_idx is not None:
        ts, msg = logs[first_idx]
        print(f"  Index {first_idx}: [{ts}] {msg}")
    else:
        print("  Not found")
    
    last_idx = find_last_log(logs, 400)
    print(f"\nLast log with timestamp 400:")
    if last_idx is not None:
        ts, msg = logs[last_idx]
        print(f"  Index {last_idx}: [{ts}] {msg}")
    else:
        print("  Not found")
    
    print("\nLogs in range [150, 350]:")
    range_logs = find_log_range(logs, 150, 350)
    for ts, msg in range_logs:
        print(f"  [{ts}] {msg}")
    print(f"  Total: {len(range_logs)} logs")


if __name__ == "__main__":
    main()
