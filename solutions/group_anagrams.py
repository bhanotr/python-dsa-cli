from typing import List
from collections import defaultdict


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Group anagrams together from the given list of strings.

    Args:
        strs: List of strings

    Returns:
        List of groups where each group contains anagrams
    """
    groups = defaultdict(list)
    
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())


def main():
    """Test the group_anagrams function."""
    test_cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"],
        ["abc", "bca", "cab", "xyz", "zyx"],
        ["", ""],
    ]

    print("Group Anagrams Tests:")
    print("=" * 60)
    
    for strs in test_cases:
        result = group_anagrams(strs)
        print(f"\nInput: {strs}")
        print(f"Groups: {result}")
        print(f"Number of groups: {len(result)}")


if __name__ == "__main__":
    main()
