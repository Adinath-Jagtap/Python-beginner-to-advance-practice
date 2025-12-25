#Q1 Print multiplication table

#Input
number = int(input("Enter the number for multiplication table: "))

#Printing Multiplication Table
for i in range(1,13):
    print(number,"✖",i,"=",number*i)