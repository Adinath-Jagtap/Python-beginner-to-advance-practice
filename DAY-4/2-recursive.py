#Q2 Function to find factorial (recursive)

#function for factorial
def factorial(num):
    if (num == 0 or num == 1):
        return 1
    else:
         return num*factorial(num-1) #recursion

#taking input
number = int(input("Enter the number: "))

#printing result
print(factorial(number),"is factorial of",number)