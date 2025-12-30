# Q10: Chain multiple decorators — commented version

# A decorator is a function that takes another function and returns a new function.
# Decorator 1: prints the function's name before calling it
def print_name(func):
    # wrapper will replace the original function
    def wrapper():
        # func.__name__ gives the name of the original function as text
        print("Function name:", func.__name__)
        # Call the original function
        func()
    # Return the wrapper so Python uses it instead of the original function
    return wrapper

# Decorator 2: prints a "Start" message, calls the function, then prints "End"
def start_end(func):
    # wrapper replaces the original function
    def wrapper():
        print("Start")    # message before the original function runs
        func()            # run the original function
        print("End")      # message after the original function runs
    return wrapper

# Applying two decorators to the function `greet`.
@print_name
@start_end
def greet():
    # This is the original function body that will be called inside the wrappers
    print("Hello!")

# Call the decorated function
greet()