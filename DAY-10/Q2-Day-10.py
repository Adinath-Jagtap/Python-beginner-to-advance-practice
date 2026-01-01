# 2) Create 2D array (matrix) and access elements — commented version
import numpy as np

# Create a 2D NumPy array (matrix)
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Access elements using row, column indexing
print("Matrix:\n", matrix)
print(matrix[0,2]) # [a,b] := a is row and b is column
print(matrix[1]) #2nd row
print(matrix[:,1]) #2nd column