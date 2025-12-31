# 9) Reduce to find product of all numbers — commented version
# functools.reduce applies a binary function cumulatively to the items of a sequence.
from functools import reduce

numbers = [1, 2, 3, 4]

# reduce(lambda a, b: a * b, numbers, 1) multiplies all numbers.
# The initial value 1 ensures reduce works even on an empty list.
product = reduce(lambda a, b: a * b, numbers, 1)

# Print product
print("product:", product)  # -> 24