#Q1 Basic calculator: Calculator (add, subtract, multiply, divide)

#assigning variables by taking input 
number1 = float(input("Enter your first number: "))

#Choose operator to perform calculation
print("Choose operation to perfom")
Operator = int(input("Choose 1 = add ; 2 = subs ; 3 = multiply & 4 = division : "))

#assigning variables by taking input
number2 = float(input("Enter your second number: "))

#if else if for performing calculations 

if (Operator == 1):
    print(number1+number2)
elif (Operator == 2):
    print(number1-number2)
elif (Operator == 3):
    print(number1*number2)
elif (Operator == 4):
    print(number1/number2)
else:
    print("Enter a valid operator")