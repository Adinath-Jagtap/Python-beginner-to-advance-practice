#Q8 Armstrong Number Checker

#Input
number = input("Enter Number: ")

#finding the lenght of or no of digits in the Number
n = len(number)

#Init sum as 0
sum = 0

#Sum of digits of the number
for i in number:
    sum = sum + int(i)**n

#Printing the final result
if (sum == int(number)):
    print(number,"is a Armstrong Number.")
else: 
    print(number,"is not a Armstrong Number.")