# 4) Reshape array from 1D to 2D 
import numpy as np

# Create a 1D array with 6 elements
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape into a 2x3 matrix
reshaped = arr.reshape(3, 2)

print("Original 1D array:", arr)
print("Reshaped 2D array:\n", reshaped)
