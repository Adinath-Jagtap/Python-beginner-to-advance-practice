# Q8 returning multiple values and printing them 

#function to calculate
def calculate(a, b):
    sum_val = a + b
    diff_val = a - b
    prod_val = a * b
    return sum_val, diff_val, prod_val

#storing the result by calling calculate function
result = calculate(10, 5)

#printing the three outputs from function using indexing
print("Sum:", result[0])
print("Difference:", result[1])
print("Product:", result[2])