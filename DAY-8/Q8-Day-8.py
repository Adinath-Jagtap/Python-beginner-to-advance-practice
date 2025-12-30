# Q8. Use yield to create a custom range() function

# creating function my_range
def my_range(start, end):
    while start <= end:
        yield start
        start += 1

#calling the function and prints value
print("Custom range output:")
for i in my_range(3, 8):
    print(i)