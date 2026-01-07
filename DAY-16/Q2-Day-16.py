# 2. Create a list of squares for even numbers from 1 to 50 using list comprehension

even_squares = [x*x for x in range(1, 51) if x % 2 == 0]
print(even_squares)