#Q1: Find second largest number in list

#Take input of list
numbers = list(map(int,input("ENTER LIST INPUT: ").split(",")))

#Finding max from list 
max_number = max(numbers)

#Loop for finding 2nd largest number in the List
second_max = -1  #initially assigning second_max as -1 
for i in numbers:
    if i>second_max and i != max_number :
        second_max = i

#Printing the second largest number from the list 
print(second_max,"is second largest number from the string :",numbers)