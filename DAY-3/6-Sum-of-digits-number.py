#Q6 Sum of digits in number

#Input
number = input("Enter Number: ")

#Init sum as 0
sum = 0

#Sum of digits of the number
for i in number:
    sum = sum + int(i)

#printing the result
print(sum,"is sum of digits of given number:",number)