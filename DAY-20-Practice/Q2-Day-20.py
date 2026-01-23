# 2) Find all unique pairs with given sum (O(n) using a hash set)
def find_pairs_with_sum(nums, target):
    """
    Returns a list of unique pairs (a, b) where a + b == target.
    Each pair is returned as a tuple with smaller element first.
    Example: [(1, 4), (2, 3)]
    """
    seen = set()
    pairs = set()  # use set to avoid duplicates (unordered pairs)
    for x in nums:
        needed = target - x
        if needed in seen:
            # store ordered tuple so (2,3) and (3,2) are same
            pair = tuple(sorted((x, needed)))
            pairs.add(pair)
        seen.add(x)
    return sorted(pairs)

# Sample usage
nums = [1, 2, 3, 2, 4, 0, 5, -1]
target = 4
print(find_pairs_with_sum(nums, target))  # -> [( -1, 5 ), (0,4), (1,3), (2,2)]