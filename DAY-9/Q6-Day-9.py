# 6) Lambda to sort list of tuples by second element — commented version
# We have a list of (fruit, count) tuples and want to sort by count (the second item).
tuples = [("apple", 5), ("banana", 2), ("pear", 8), ("kiwi", 2)]

# sorted(..., key=lambda t: t[1]) tells sorted() to use the tuple's second element as the sort key.
sorted_by_second = sorted(tuples, key=lambda t: t[1])

# Print sorted result
print("sorted_by_second:", sorted_by_second)
# -> [('banana', 2), ('kiwi', 2), ('apple', 5), ('pear', 8)]
