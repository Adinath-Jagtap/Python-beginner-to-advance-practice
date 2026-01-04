# 7) Map to apply function to all list elements
# We use map() with a lambda to double every number in the list.
numbers = [1, 2, 3, 4]

# map(lambda x: x * 2, numbers) returns an iterator; wrap with list() to see the values.
doubled = list(map(lambda x: x * 2, numbers))

# Print doubled numbers
print("doubled:", doubled)  # -> [2, 4, 6, 8]
