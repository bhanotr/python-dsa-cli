from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Group anagrams together from the given list of strings.

    Args:
        strs: List of strings

    Returns:
        List of groups where each group contains anagrams
    """
    # TODO: Implement group_anagrams
    # 1. Create a hash map to store groups
    # 2. Use sorted string as key for each anagram group
    # 3. Group strings with the same sorted key
    # 4. Return all groups as a list
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
