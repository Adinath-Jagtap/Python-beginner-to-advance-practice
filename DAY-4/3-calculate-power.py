#Q3 Function to calculate power (a^b)

#function to calculate power
def power(a,b):
    return a**b

#input the base and power num
base = int(input("Enter the base number: "))
power_num = int(input("Enter the power number: "))

#storing and printing the result
result = power(base,power_num)
print(result,"is the answer.")