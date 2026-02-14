from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Group anagrams together from the given list of strings.

    Args:
        strs: List of strings

    Returns:
        List of groups where each group contains anagrams
    """
    # THINK: What makes two strings anagrams of each other?
    # - Anagrams have the same characters (same frequency, same letters)
    # - If we sort them, they become identical!
    # - Key insight: Use sorted string as hash map key
    pass


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
