# Q5. Create a generator for Fibonacci sequence

#creating Fibonacci sequence generator
def fibonacci_gen(num):
    a = 0 
    b = 1
    for i in range(num):
        yield(a) #returns a and then performs below operations
        '''In case of return below operations will be ignored or cause error'''
        c = a+b
        a = b
        b = c

#printing the result and calling the function generator
for i in fibonacci_gen(5):
    print(i)