# 1) Binary Search (iterative) — returns index or -1 if not found
def binary_search(arr, target):
    """
    Iterative binary search on a sorted list `arr`.
    Returns index of `target` if present, otherwise -1.
    """
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# Sample usage
arr = [1, 3, 5, 7, 9, 11]
print("Index of 7:", binary_search(arr, 7))   # -> 3
print("Index of 2:", binary_search(arr, 2))   # -> -1