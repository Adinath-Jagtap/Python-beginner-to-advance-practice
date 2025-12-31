# 5) Set comprehension — commented version
# Use a set comprehension to get unique squared values from a list that may contain duplicates.
numbers = [1, 2, 2, 3, 4, 4]

# Curly braces with an expression create a set: duplicates are removed automatically.
square_set = {x * x for x in numbers}

# Print the set (order may vary because sets are unordered)
print("square_set:", square_set)  # -> {1, 4, 9, 16}