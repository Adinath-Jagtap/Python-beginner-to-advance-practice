# Q3. Create a decorator that accepts arguments

#creating decor that accepts arg
def hello_decor(message): #
    def decor(func):
        def wrapper():
            print(message)
            func()
        return wrapper
    return decor

@hello_decor("hello") #calling decorator with arg
def greet(): #creating function
    print("welcome")

greet() #calling a function