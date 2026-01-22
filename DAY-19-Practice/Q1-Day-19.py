def merge_sorted(a, b):
    """
    Merge two sorted lists a and b and return a new sorted list.
    Time: O(len(a)+len(b)), Space: O(len(a)+len(b))
    """
    i, j = 0, 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i]); i += 1
        else:
            out.append(b[j]); j += 1
    # append leftovers
    if i < len(a):
        out.extend(a[i:])
    if j < len(b):
        out.extend(b[j:])
    return out

# Sample usage
A = [1, 3, 5, 7]
B = [2, 4, 6, 8, 9]
print("Merged:", merge_sorted(A, B))  # -> [1,2,3,4,5,6,7,8,9]
