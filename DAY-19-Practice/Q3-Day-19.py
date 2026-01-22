def rotate_right(nums, k):
    """
    Rotate list nums to the right by k steps in-place.
    Uses the reversal algorithm: reverse whole array, then reverse first k, then reverse rest.
    Time: O(n), Space: O(1)
    """
    n = len(nums)
    if n == 0:
        return
    k %= n
    if k == 0:
        return
    def rev(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1; r -= 1
    rev(0, n-1)
    rev(0, k-1)
    rev(k, n-1)

# Sample usage
arr = [1,2,3,4,5,6,7]
rotate_right(arr, 3)
print("Rotated by 3:", arr)  # -> [5,6,7,1,2,3,4]

# Alternate simple approach (returns new list) using slicing:
def rotate_right_new(nums, k):
    if not nums: return nums
    k %= len(nums)
    return nums[-k:] + nums[:-k]

print("Rotate new:", rotate_right_new([1,2,3,4,5], 2))  # -> [4,5,1,2,3]
