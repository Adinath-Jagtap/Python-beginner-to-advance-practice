#Q2 Check prime number

#Input for number
num = int(input("Enter the number: "))

#Checking whether number(input) is Prime or not
if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is prime number")