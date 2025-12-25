#Q4 Fibonacci sequence generator

#Input
num = int(input("Enter the number: "))

#Initialize a and b
a = 0
b = 1

#for loop for printing Fibonacci sequence
for i in range(num):
    print(a, end=" ")
    c = a+b
    a = b
    b = c