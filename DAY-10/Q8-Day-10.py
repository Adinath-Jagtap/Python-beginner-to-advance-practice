# 8) Boolean indexing (filter array based on condition) 
import numpy as np

# Create an array
arr = np.array([5, 10, 15, 20, 25])

# Boolean condition to filter elements
filtered = arr[arr > 15]

print("Original array:", arr)
print("Elements greater than 15:", filtered)
