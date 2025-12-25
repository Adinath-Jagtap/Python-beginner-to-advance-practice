#Q9 Find GCD of Two Numbers

#Take inputs of Two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

#factors of each number
factors1 = []
factors2 = []

#factors of number a
for i in range(1, a + 1):
    if a % i == 0:
        factors1.append(i)

#factors of number b
for i in range(1, b + 1):
    if b % i == 0:
        factors2.append(i)

#Finding common elements 
common_elements_list=[]
for i in factors1:
    if i in factors2 :
        common_elements_list.append(i)

GCD = max(common_elements_list)

#printing GCD
print(GCD,"is the GCD of two numbers")