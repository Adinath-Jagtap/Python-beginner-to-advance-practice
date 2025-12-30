# Q1. Simple decorator that prints the function name when it is called

#creating decorator named decor
def decor(func): 
    def wrapper():
        print("function name is",func.__name__)
        func()
    return wrapper

@decor #option 1 : shortcut one
def say_hello(): #define function
    print("hello")

'''say_hello = decor(say_hello)''' #option 2 to call the decorator

say_hello() #calling define function