#Q1 Function to check leap year

#function for checking the input year is leap year or not
def checker(num):
    if (num % 4 == 0):
        print(num,"is leap year")
    else:
        print(num,"is not leap year")

#taking input of year
a = int(input("Enter the year: "))
checker(a) #calling the checker function