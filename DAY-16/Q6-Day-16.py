# 6. Create a 2D NumPy array, calculate the mean of each row, and find the maximum value

import numpy as np

arr = np.array([[1,2,3],[10,20,30],[5,6,7]])
row_means = arr.mean(axis=1)   # mean of each row
max_val = arr.max()
print("Array:\n", arr)
print("Row means:", row_means)
print("Max value:", max_val)