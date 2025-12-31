# 10) Combine map, filter, lambda in one expression — commented version
# Example: from a list of numbers, keep only evens, then square each remaining number.
numbers = [1, 2, 3, 4, 5, 6]

# Step-by-step:     
# - filter(lambda x: x % 2 == 0,numbers) selects even numbers
# - map(lambda x: x * x, ...) squares each selected number
# Wrap with list() to realize the result.
squared_evens = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, numbers)))

# Print final result
print("squared_evens:", squared_evens)  # -> [4, 16, 36]