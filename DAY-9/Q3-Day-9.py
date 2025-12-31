# 3) Nested list comprehension (2D matrix) — commented version
# We create a 3x3 matrix with values 1..9 using a nested comprehension.
# Outer loop: for i in range(3) creates 3 rows (i = 0,1,2)
# Inner loop: for j in range(3) creates 3 columns (j = 0,1,2)
matrix = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]

# Print the matrix row by row for readability
print("matrix:")
for row in matrix:
    print(row)
# Expected output:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]