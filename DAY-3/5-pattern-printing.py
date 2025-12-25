#Q5 Pattern Printing

#Taking input
n = int(input("Enter the number of rows: "))

#printing first pattern
print("First Pattern: ")
for i in range(1,n+1):
    print("*"*i)

print("-------------------------------------------------------------------------------------------------") 

#printing second pattern
print("Second Pattern: ")
for i in range(n,0,-1):
    print("*"*i)

print("-------------------------------------------------------------------------------------------------") 

#printing third pattern
print("Third Pattern: ")
for i in range(n+1):
    print(" "*(n-i) + "*"*(2*i-1))

print("-------------------------------------------------------------------------------------------------") 

#printing fourth pattern
print("Fourth Pattern: ")
for i in range(n+1):
    print(" "*(n-i)+"*"*i)

print("-------------------------------------------------------------------------------------------------") 