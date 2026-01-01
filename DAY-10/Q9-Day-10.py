# 9) Stack arrays vertically and horizontally — commented version
import numpy as np

# Create two arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Stack arrays
vertical = np.vstack((a, b))     # stack as rows
horizontal = np.hstack((a, b))   # stack as columns

print("Vertical Stack:\n", vertical)
print("Horizontal Stack:", horizontal)