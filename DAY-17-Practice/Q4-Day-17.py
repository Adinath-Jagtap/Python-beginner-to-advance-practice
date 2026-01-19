# Sample data (1 to 5, missing 4)
arr = [1, 2, 3, 5]
n = 5

# Expected sum - actual sum
missing = n * (n + 1) // 2 - sum(arr)
print("Missing number:", missing)
