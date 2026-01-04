# 2) List comprehension with if condition 
# We filter the input list to only include even numbers, then square those.
numbers = [1, 2, 3, 4, 5, 6, 7]  

# The 'if x % 2 == 0' part keeps only numbers that are even.
even_squares = [x * x for x in numbers if x % 2 == 0]

# Show the output
print("even_squares:", even_squares)  # -> [4, 16, 36]
