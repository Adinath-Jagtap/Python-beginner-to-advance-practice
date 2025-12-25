#Q10 Print all factors of a number

#Take input
a = int(input("Enter second number: "))

#factors of each number
factors1 = []

#factors of number a
for i in range(1, a + 1):
    if a % i == 0:
        factors1.append(i)

print(factors1,"are factors of",a)