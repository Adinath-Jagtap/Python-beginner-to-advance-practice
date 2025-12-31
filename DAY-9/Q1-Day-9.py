# Q1 List comprehension to create squares — commented version
# We take a list of numbers and create a new list with each number squared.
numbers = [1, 2, 3, 4, 5]

# The expression [x * x for x in numbers] builds a list by evaluating x*x for each x.
squares = [x * x for x in numbers]

# Print the result so you can see the output when running this script.
print("squares:", squares)  # -> [1, 4, 9, 16, 25]