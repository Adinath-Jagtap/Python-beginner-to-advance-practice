# 10) Dot product of two matrices
import numpy as np


# Create two matrices
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

# Dot product (matrix multiplication)
dot_product = np.dot(A, B)

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Dot Product (A · B):\n", dot_product)
