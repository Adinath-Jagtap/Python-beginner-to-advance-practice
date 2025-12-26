#Q2 Function to find factorial (recursive)

def factorial(num):
    if (num == 0 or num == 1):
        return 1
    else:
         return num*factorial(num-1)

number = int(input("Enter the number: "))
print(factorial(number),"is factorial of",number)