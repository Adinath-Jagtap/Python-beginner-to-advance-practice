# Q7. Difference between generator expression and list comprehension

#sample
nums = [1, 2, 3, 4, 5]

# Creating list of squares of elems of nums
list_comp = [n * 2 for n in nums]

# Generator expression
gen_exp = (n * 2 for n in nums)

print("List:", list_comp) #printing list
print(gen_exp) #printing the object
print("Generator values:")
for value in gen_exp: 
    print(value) #printing value one by one