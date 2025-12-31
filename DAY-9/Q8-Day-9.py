# 8) Filter to get even numbers from list — commented version
# Use filter() with a lambda that keeps only even numbers (x % 2 == 0).
numbers = [1, 2, 3, 4, 5, 6]

# filter returns an iterator; convert to list() to display.
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Print even numbers
print("evens:", evens)  # -> [2, 4, 6]
