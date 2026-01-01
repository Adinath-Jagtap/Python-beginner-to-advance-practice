# 7) Create array with zeros, ones, random values — commented version
import numpy as np

# Create arrays using NumPy utility functions
zeros_arr = np.zeros((2, 3))     # 2x3 array of zeros
ones_arr = np.ones((3, 2))       # 3x2 array of ones
random_arr = np.random.rand(2, 2) # random values between 0 and 1

print("Zeros array:\n", zeros_arr)
print("Ones array:\n", ones_arr)
print("Random array:\n", random_arr)