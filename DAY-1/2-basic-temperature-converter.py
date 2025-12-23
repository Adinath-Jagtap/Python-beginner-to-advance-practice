#Q2 basic temperature converter Celsius and Fahrenheit

#To know the conversion type
num = int(input("Press 1 for (Celsius ↔ Fahrenheit) Press 2 for (Fahrenheit ↔ Celsius): "))

# if and elif for proper conversions according to conversion type 
if (num == 1):
    c = int(input("Enter the Temperature: "))
    print((9/5) * c + 32)
elif (num == 2):
    c = int(input("Enter the Temperature: "))
    print((c - 32) * 5/9)
else:
    print("enter correct conversion type.")