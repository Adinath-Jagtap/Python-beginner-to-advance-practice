#Q3 Find all prime numbers up to N

#Input number for N
num = int(input("Enter the number: "))

#Empty prime numbers from 0 to N numbers
Prime_numbers = []

#Creating the list
for element in range(2,num+1):
        for i in range(2, element):
            if element % i == 0:
                break
        else:
            Prime_numbers.append(element)

#Printing the list
if len(Prime_numbers) > 0:
     print(Prime_numbers)
else:
     print("NO Prime numbers avaliable")