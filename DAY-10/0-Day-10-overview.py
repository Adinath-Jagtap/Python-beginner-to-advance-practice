'''
DAY 10: Python NumPy Basics
'''


# =============================================================================
# NUMPY INTRODUCTION
# =============================================================================
'''
NumPy (Numerical Python): Library for numerical computing in Python.
- Fast operations on arrays
- Mathematical functions
- Linear algebra operations
- Random number generation
- Broadcasting capabilities

Why NumPy?
- Faster than Python lists (written in C)
- Less memory consumption
- Convenient array operations
- Foundation for other libraries (Pandas, Matplotlib, Scikit-learn)
'''

# --- Installing NumPy ---
# pip install numpy

import numpy as np

# Check NumPy version
print(np.__version__)


# =============================================================================
# CREATING ARRAYS
# =============================================================================

# --- Creating 1D Arrays ---
# From Python list
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)              # [1 2 3 4 5]
print(type(arr1))        # <class 'numpy.ndarray'>

# From tuple
arr2 = np.array((1, 2, 3, 4, 5))
print(arr2)              # [1 2 3 4 5]

# With specific data type
arr3 = np.array([1, 2, 3], dtype=float)
print(arr3)              # [1. 2. 3.]

arr4 = np.array([1.5, 2.7, 3.9], dtype=int)
print(arr4)              # [1 2 3] (truncated)


# --- Creating 2D Arrays (Matrices) ---
# From list of lists
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)
# [[1 2 3]
#  [4 5 6]]

# 3x3 matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(matrix)


# --- Creating 3D Arrays ---
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3d)
# [[[1 2]
#   [3 4]]
#  [[5 6]
#   [7 8]]]


# --- Array with Zeros ---
zeros_1d = np.zeros(5)
print(zeros_1d)          # [0. 0. 0. 0. 0.]

zeros_2d = np.zeros((3, 4))
print(zeros_2d)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

zeros_int = np.zeros((2, 3), dtype=int)
print(zeros_int)
# [[0 0 0]
#  [0 0 0]]


# --- Array with Ones ---
ones_1d = np.ones(4)
print(ones_1d)           # [1. 1. 1. 1.]

ones_2d = np.ones((2, 3))
print(ones_2d)
# [[1. 1. 1.]
#  [1. 1. 1.]]


# --- Array with Specific Value ---
full_arr = np.full((3, 3), 7)
print(full_arr)
# [[7 7 7]
#  [7 7 7]
#  [7 7 7]]


# --- Identity Matrix ---
identity = np.eye(3)
print(identity)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]


# --- Array with Range ---
# Similar to range()
arr_range = np.arange(10)
print(arr_range)         # [0 1 2 3 4 5 6 7 8 9]

arr_range2 = np.arange(5, 15)
print(arr_range2)        # [5 6 7 8 9 10 11 12 13 14]

arr_range3 = np.arange(0, 10, 2)
print(arr_range3)        # [0 2 4 6 8]

# With float step
arr_float = np.arange(0, 1, 0.1)
print(arr_float)         # [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]


# --- Linearly Spaced Array ---
# Create array with evenly spaced values
linspace = np.linspace(0, 10, 5)
print(linspace)          # [ 0.   2.5  5.   7.5 10. ]

linspace2 = np.linspace(0, 1, 11)
print(linspace2)         # [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1. ]


# --- Random Arrays ---
# Random values between 0 and 1
random_arr = np.random.rand(5)
print(random_arr)        # [0.xxx 0.xxx 0.xxx 0.xxx 0.xxx]

random_2d = np.random.rand(3, 3)
print(random_2d)

# Random integers
random_int = np.random.randint(0, 10, 5)
print(random_int)        # [x x x x x] (0-9)

random_int_2d = np.random.randint(0, 100, (3, 4))
print(random_int_2d)

# Random normal distribution
normal = np.random.randn(5)
print(normal)            # Values from standard normal distribution

# Random choice
choice = np.random.choice([10, 20, 30, 40, 50], 3)
print(choice)            # Random 3 elements from list


# =============================================================================
# ARRAY ATTRIBUTES
# =============================================================================

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

# Shape (dimensions)
print(arr.shape)         # (3, 4) - 3 rows, 4 columns

# Number of dimensions
print(arr.ndim)          # 2

# Total number of elements
print(arr.size)          # 12

# Data type
print(arr.dtype)         # int64 (or int32)

# Size of each element in bytes
print(arr.itemsize)      # 8 (bytes)

# Total bytes consumed
print(arr.nbytes)        # 96 (12 * 8)


# =============================================================================
# ARRAY INDEXING AND SLICING
# =============================================================================

# --- 1D Array Indexing ---
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])            # 10 (first element)
print(arr[2])            # 30
print(arr[-1])           # 50 (last element)
print(arr[-2])           # 40


# --- 1D Array Slicing ---
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr[2:5])          # [2 3 4]
print(arr[:5])           # [0 1 2 3 4]
print(arr[5:])           # [5 6 7 8 9]
print(arr[::2])          # [0 2 4 6 8] (every 2nd element)
print(arr[::-1])         # [9 8 7 6 5 4 3 2 1 0] (reversed)


# --- 2D Array Indexing ---
arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])

print(arr2d[0, 0])       # 1 (row 0, col 0)
print(arr2d[0, 2])       # 3 (row 0, col 2)
print(arr2d[1, 3])       # 8 (row 1, col 3)
print(arr2d[-1, -1])     # 12 (last row, last col)

# Access entire row
print(arr2d[0])          # [1 2 3 4]
print(arr2d[1])          # [5 6 7 8]

# Access entire column
print(arr2d[:, 0])       # [1 5 9] (all rows, col 0)
print(arr2d[:, 2])       # [3 7 11] (all rows, col 2)


# --- 2D Array Slicing ---
arr2d = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20]])

# First 2 rows, first 3 columns
print(arr2d[:2, :3])
# [[1 2 3]
#  [6 7 8]]

# All rows, columns 1 to 3
print(arr2d[:, 1:4])
# [[ 2  3  4]
#  [ 7  8  9]
#  [12 13 14]
#  [17 18 19]]

# Rows 1 to 3, columns 2 to 4
print(arr2d[1:3, 2:4])
# [[ 8  9]
#  [13 14]]


# --- Modifying Array Elements ---
arr = np.array([1, 2, 3, 4, 5])
arr[2] = 10
print(arr)               # [1 2 10 4 5]

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
arr2d[1, 2] = 99
print(arr2d)
# [[ 1  2  3]
#  [ 4  5 99]]

# Modify slice
arr = np.array([1, 2, 3, 4, 5])
arr[1:4] = [20, 30, 40]
print(arr)               # [1 20 30 40 5]


# =============================================================================
# RESHAPING ARRAYS
# =============================================================================

# --- Reshape 1D to 2D ---
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)
print(reshaped)
# [[1 2 3]
#  [4 5 6]]

reshaped2 = arr.reshape(3, 2)
print(reshaped2)
# [[1 2]
#  [3 4]
#  [5 6]]


# --- Reshape with -1 (Auto-calculate) ---
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
reshaped = arr.reshape(2, -1)  # Auto-calculate columns
print(reshaped)
# [[1 2 3 4]
#  [5 6 7 8]]

reshaped2 = arr.reshape(-1, 2)  # Auto-calculate rows
print(reshaped2)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]


# --- Flatten Array (2D to 1D) ---
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

# Method 1: flatten()
flat1 = arr2d.flatten()
print(flat1)             # [1 2 3 4 5 6]

# Method 2: ravel()
flat2 = arr2d.ravel()
print(flat2)             # [1 2 3 4 5 6]

# Method 3: reshape(-1)
flat3 = arr2d.reshape(-1)
print(flat3)             # [1 2 3 4 5 6]


# --- Transpose ---
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
transposed = arr.T
print(transposed)
# [[1 4]
#  [2 5]
#  [3 6]]


# =============================================================================
# ARRAY OPERATIONS
# =============================================================================

# --- Arithmetic Operations ---
arr = np.array([1, 2, 3, 4, 5])

# Scalar operations
print(arr + 5)           # [6 7 8 9 10]
print(arr - 2)           # [-1  0  1  2  3]
print(arr * 3)           # [ 3  6  9 12 15]
print(arr / 2)           # [0.5 1.  1.5 2.  2.5]
print(arr ** 2)          # [ 1  4  9 16 25]
print(arr % 2)           # [1 0 1 0 1]


# --- Element-wise Operations (Broadcasting) ---
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([10, 20, 30, 40])

print(arr1 + arr2)       # [11 22 33 44]
print(arr1 - arr2)       # [-9 -18 -27 -36]
print(arr1 * arr2)       # [10 40 90 160]
print(arr1 / arr2)       # [0.1 0.1 0.1 0.1]


# --- 2D Array Operations ---
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

print(arr1 + arr2)
# [[ 6  8]
#  [10 12]]

print(arr1 * arr2)       # Element-wise multiplication
# [[ 5 12]
#  [21 32]]


# --- Mathematical Functions ---
arr = np.array([1, 4, 9, 16, 25])

print(np.sqrt(arr))      # [1. 2. 3. 4. 5.]
print(np.square(arr))    # [  1  16  81 256 625]
print(np.exp(arr))       # [e^1 e^4 e^9 e^16 e^25]
print(np.log(arr))       # Natural logarithm
print(np.log10(arr))     # Base-10 logarithm

# Trigonometric functions
angles = np.array([0, np.pi/2, np.pi])
print(np.sin(angles))    # [0. 1. 0.]
print(np.cos(angles))    # [ 1.  0. -1.]
print(np.tan(angles))    # [0. inf 0.]


# --- Absolute Value ---
arr = np.array([-1, -2, 3, -4, 5])
print(np.abs(arr))       # [1 2 3 4 5]


# --- Rounding ---
arr = np.array([1.234, 2.567, 3.891])
print(np.round(arr))     # [1. 3. 4.]
print(np.round(arr, 2))  # [1.23 2.57 3.89]
print(np.floor(arr))     # [1. 2. 3.]
print(np.ceil(arr))      # [2. 3. 4.]


# =============================================================================
# STATISTICAL FUNCTIONS
# =============================================================================

arr = np.array([10, 20, 30, 40, 50])

# Sum
print(np.sum(arr))       # 150
print(arr.sum())         # 150

# Mean (average)
print(np.mean(arr))      # 30.0
print(arr.mean())        # 30.0

# Median
print(np.median(arr))    # 30.0

# Standard deviation
print(np.std(arr))       # 14.142135623730951

# Variance
print(np.var(arr))       # 200.0

# Minimum and maximum
print(np.min(arr))       # 10
print(np.max(arr))       # 50
print(arr.min())         # 10
print(arr.max())         # 50

# Index of min/max
print(np.argmin(arr))    # 0
print(np.argmax(arr))    # 4

# Cumulative sum
print(np.cumsum(arr))    # [10 30 60 100 150]

# Cumulative product
print(np.cumprod(arr))   # [10 200 6000 240000 12000000]


# --- 2D Array Statistics ---
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# Overall statistics
print(np.sum(arr2d))     # 45
print(np.mean(arr2d))    # 5.0

# Along axis 0 (columns)
print(np.sum(arr2d, axis=0))    # [12 15 18]
print(np.mean(arr2d, axis=0))   # [4. 5. 6.]

# Along axis 1 (rows)
print(np.sum(arr2d, axis=1))    # [ 6 15 24]
print(np.mean(arr2d, axis=1))   # [2. 5. 8.]


# =============================================================================
# BOOLEAN INDEXING AND FILTERING
# =============================================================================

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Boolean array
condition = arr > 50
print(condition)
# [False False False False False  True  True  True  True  True]

# Filter using boolean array
filtered = arr[condition]
print(filtered)          # [60 70 80 90 100]

# One-liner
filtered = arr[arr > 50]
print(filtered)          # [60 70 80 90 100]


# --- Multiple Conditions ---
# AND condition (&)
filtered = arr[(arr > 30) & (arr < 80)]
print(filtered)          # [40 50 60 70]

# OR condition (|)
filtered = arr[(arr < 30) | (arr > 80)]
print(filtered)          # [10 20 90 100]

# NOT condition (~)
filtered = arr[~(arr % 2 == 0)]  # Odd numbers
print(filtered)          # [] (all are even)


# --- Modify Based on Condition ---
arr = np.array([10, 20, 30, 40, 50])
arr[arr > 30] = 0
print(arr)               # [10 20 30  0  0]


# --- where() Function ---
arr = np.array([10, 20, 30, 40, 50])

# Replace values > 30 with 99, else keep original
result = np.where(arr > 30, 99, arr)
print(result)            # [10 20 30 99 99]

# Replace even with 0, odd with 1
arr = np.array([1, 2, 3, 4, 5])
result = np.where(arr % 2 == 0, 0, 1)
print(result)            # [1 0 1 0 1]


# =============================================================================
# STACKING ARRAYS
# =============================================================================

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# --- Vertical Stack (vstack) ---
vstacked = np.vstack((arr1, arr2))
print(vstacked)
# [[1 2 3]
#  [4 5 6]]


# --- Horizontal Stack (hstack) ---
hstacked = np.hstack((arr1, arr2))
print(hstacked)          # [1 2 3 4 5 6]


# --- 2D Array Stacking ---
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Vertical stack
vstacked = np.vstack((arr1, arr2))
print(vstacked)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# Horizontal stack
hstacked = np.hstack((arr1, arr2))
print(hstacked)
# [[1 2 5 6]
#  [3 4 7 8]]


# --- Concatenate (More Flexible) ---
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Concatenate along axis 0 (vertical)
concat0 = np.concatenate((arr1, arr2), axis=0)
print(concat0)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# Concatenate along axis 1 (horizontal)
concat1 = np.concatenate((arr1, arr2), axis=1)
print(concat1)
# [[1 2 5 6]
#  [3 4 7 8]]


# =============================================================================
# MATRIX OPERATIONS
# =============================================================================

# --- Dot Product (Matrix Multiplication) ---
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Method 1: np.dot()
result = np.dot(arr1, arr2)
print(result)
# [[19 22]
#  [43 50]]

# Method 2: @ operator
result = arr1 @ arr2
print(result)
# [[19 22]
#  [43 50]]

# Method 3: .dot() method
result = arr1.dot(arr2)
print(result)
# [[19 22]
#  [43 50]]


# --- Vector Dot Product ---
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])

result = np.dot(vec1, vec2)
print(result)            # 32 (1*4 + 2*5 + 3*6)


# --- Matrix Properties ---
matrix = np.array([[1, 2], [3, 4]])

# Determinant
det = np.linalg.det(matrix)
print(det)               # -2.0

# Inverse
inv = np.linalg.inv(matrix)
print(inv)
# [[-2.   1. ]
#  [ 1.5 -0.5]]

# Verify inverse
identity = matrix @ inv
print(np.round(identity))
# [[1. 0.]
#  [0. 1.]]


# =============================================================================
# COPYING ARRAYS
# =============================================================================

arr = np.array([1, 2, 3, 4, 5])

# View (shares data with original)
view = arr.view()
view[0] = 100
print(arr)               # [100   2   3   4   5] (modified!)

# Copy (independent)
arr = np.array([1, 2, 3, 4, 5])
copy = arr.copy()
copy[0] = 100
print(arr)               # [1 2 3 4 5] (not modified)
print(copy)              # [100   2   3   4   5]


# =============================================================================
# PYTHON PRACTICE QUESTIONS - NUMPY
# =============================================================================
'''
1. Create a 1D NumPy array and perform basic arithmetic operations
2. Create a 2D NumPy array (matrix) and access elements by index
3. Use array slicing and advanced indexing
4. Reshape a 1D array into a 2D array using np.reshape()
5. Perform element-wise operations (add, multiply, square)
6. Find mean, median, and standard deviation of an array
7. Create arrays of zeros, ones, and random values
8. Use boolean indexing to filter an array based on a condition
9. Stack arrays vertically (vstack) and horizontally (hstack)
10. Compute the dot product of two matrices (np.dot or @ operator)
'''
