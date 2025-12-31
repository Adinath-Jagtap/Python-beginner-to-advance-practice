# 4) Dictionary comprehension — commented version
# Build a dict mapping each number to its square.
numbers = [1, 2, 3, 4, 5]

# {x: x*x for x in numbers} creates key:value pairs directly.
square_dict = {x: x * x for x in numbers}

# Print the dictionary
print("square_dict:", square_dict)  # -> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 4b) Dictionary comprehension with a condition (only odd keys)
odd_square_dict = {x: x * x for x in numbers if x % 2 == 1}
print("odd_square_dict:", odd_square_dict)  # -> {1: 1, 3: 9, 5: 25}