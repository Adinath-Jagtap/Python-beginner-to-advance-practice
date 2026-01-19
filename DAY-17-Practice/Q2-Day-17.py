# Sample sorted array
arr = [1, 1, 2, 2, 3, 4, 4]

# Pointer for unique position
k = 1

for i in range(1, len(arr)):
    if arr[i] != arr[i - 1]:
        arr[k] = arr[i]
        k += 1

# Result: first k elements are unique
print("Unique count:", k)
print("Array after removing duplicates:", arr[:k])
