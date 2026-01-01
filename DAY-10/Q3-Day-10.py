# 3) Array slicing and indexing — commented version
import numpy as np

# Create a 1D array
arr = np.array([10, 20, 30, 40, 50])

# Slicing extracts a portion of the array
print("Original array:", arr)
print("First three elements:", arr[:3])
print("Last two elements:", arr[-2:])
print("Every second element:", arr[::2])