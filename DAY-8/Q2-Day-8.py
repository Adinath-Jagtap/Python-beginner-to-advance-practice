# Q2. Create a decorator to measure execution time of a function

#importing time module/library
import time 

#decorator that  calculates time
def time_calc_decor(func):
    def wrapper(number): #number arg required
        start = time.time()
        func(number) #number arg required
        end = time.time()
        print("Time taken:",end - start,"seconds")
    return wrapper

@time_calc_decor #calling the decor
def calculate(number): #defining calculate function
    sum = 0
    i = 0
    while(i<=number):
        sum = sum + i
        i = i+1

num = int(input("Enter the number: "))
calculate(num) #function call