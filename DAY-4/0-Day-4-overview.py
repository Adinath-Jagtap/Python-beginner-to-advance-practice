'''
DAY 4: Python Functions & Modules
'''

# =============================================================================
# FUNCTIONS
# =============================================================================
'''
Functions are reusable blocks of code that perform specific tasks.
Benefits:
- Code reusability
- Better organization
- Easier testing and debugging
- Abstraction

Syntax:
def function_name(parameters):
    """Docstring (optional)"""
    # code block
    return value  # optional
'''

# --- Basic Function ---
def greet():
    """Simple function with no parameters"""
    print("Hello, World!")

greet()  # Call the function


# --- Function with Parameters ---
def greet_person(name):
    """Function with one parameter"""
    print(f"Hello, {name}!")

greet_person("Alice")  # Hello, Alice!


# --- Function with Multiple Parameters ---
def add_numbers(a, b):
    """Add two numbers"""
    result = a + b
    return result

sum_result = add_numbers(5, 3)
print(sum_result)  # 8


# --- Function with Return Value ---
def square(x):
    """Return square of a number"""
    return x ** 2

result = square(5)  # 25

# Function can return without value (returns None)
def say_hello():
    print("Hello")
    return  # Optional, function returns None anyway

result = say_hello()  # None


# --- Multiple Return Values ---
# Actually returns a tuple
def get_coordinates():
    x = 10
    y = 20
    return x, y  # Returns tuple (10, 20)

# Unpack return values
x_coord, y_coord = get_coordinates()

# Can also return explicitly as tuple
def get_stats(numbers):
    return (min(numbers), max(numbers), sum(numbers))

minimum, maximum, total = get_stats([1, 2, 3, 4, 5])


# --- Default Parameters ---
def greet(name="Guest", greeting="Hello"):
    """Function with default parameter values"""
    return f"{greeting}, {name}!"

print(greet())                    # Hello, Guest!
print(greet("Alice"))             # Hello, Alice!
print(greet("Bob", "Hi"))         # Hi, Bob!
print(greet(greeting="Hey"))      # Hey, Guest!


# --- Keyword Arguments ---
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

# Positional arguments
describe_person("Alice", 25, "New York")

# Keyword arguments (order doesn't matter)
describe_person(age=25, city="New York", name="Alice")

# Mix of both (positional must come first)
describe_person("Alice", city="New York", age=25)


# --- Variable-Length Arguments (*args) ---
def sum_all(*numbers):
    """Accept any number of positional arguments"""
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))           # 6
print(sum_all(1, 2, 3, 4, 5))     # 15
print(sum_all())                  # 0

# *args creates a tuple
def print_args(*args):
    print(type(args))  # <class 'tuple'>
    for arg in args:
        print(arg)

print_args(1, "hello", True, 3.14)


# --- Variable-Length Keyword Arguments (**kwargs) ---
def print_info(**kwargs):
    """Accept any number of keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York

# **kwargs creates a dictionary
def show_kwargs(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    print(kwargs)

show_kwargs(a=1, b=2, c=3)


# --- Combining *args and **kwargs ---
def full_signature(required, *args, default="value", **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

full_signature(1, 2, 3, 4, default="custom", key1="val1", key2="val2")
# Output:
# Required: 1
# Args: (2, 3, 4)
# Default: custom
# Kwargs: {'key1': 'val1', 'key2': 'val2'}


# --- Unpacking Arguments ---
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = add(*numbers)  # Unpacks list into arguments
print(result)  # 6

# Unpacking dictionary
def greet(name, age):
    print(f"{name} is {age} years old")

person = {"name": "Alice", "age": 25}
greet(**person)  # Unpacks dict as keyword arguments


# --- Positional-Only Parameters (Python 3.8+) ---
def divide(a, b, /):
    """Parameters before / are positional-only"""
    return a / b

print(divide(10, 2))      # Works
# print(divide(a=10, b=2))  # Error: positional-only


# --- Keyword-Only Parameters ---
def create_user(name, *, age, email):
    """Parameters after * are keyword-only"""
    print(f"Name: {name}, Age: {age}, Email: {email}")

create_user("Alice", age=25, email="alice@email.com")  # Works
# create_user("Alice", 25, "alice@email.com")  # Error: age and email must be keyword


# --- Lambda Functions (Anonymous Functions) ---
# Syntax: lambda arguments: expression

# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square_lambda = lambda x: x ** 2
print(square_lambda(5))  # 25

# Multiple arguments
add = lambda a, b: a + b
print(add(3, 5))  # 8

# Lambda with conditional
max_val = lambda a, b: a if a > b else b
print(max_val(10, 20))  # 20


# --- Lambda with Built-in Functions ---
# map() - apply function to all items
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# filter() - filter items based on condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# sorted() with key
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)  # [('Bob', 92), ('Alice', 85), ('Charlie', 78)]


# --- Recursion ---
# Function calling itself
def factorial(n):
    """Calculate factorial recursively"""
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

print(factorial(5))  # 120 (5 * 4 * 3 * 2 * 1)

# Fibonacci using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))  # 13


# --- Nested Functions ---
def outer_function(x):
    """Function inside another function"""
    def inner_function(y):
        return y * 2
    
    result = inner_function(x)
    return result + 5

print(outer_function(10))  # 25


# --- Closures ---
# Inner function accessing outer function's variables
def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

times_3 = multiplier(3)
times_5 = multiplier(5)

print(times_3(10))  # 30
print(times_5(10))  # 50


# --- Decorators ---
# Functions that modify other functions
def uppercase_decorator(func):
    """Decorator that converts result to uppercase"""
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "hello, world"

print(greet())  # HELLO, WORLD

# Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!


# --- Function Annotations (Type Hints) ---
def greet(name: str, age: int) -> str:
    """Type hints for better code documentation"""
    return f"{name} is {age} years old"

# Note: Python doesn't enforce these, they're for documentation/tools
result = greet("Alice", 25)


# --- Docstrings ---
def calculate_area(length, width):
    """
    Calculate area of a rectangle.
    
    Parameters:
        length (float): Length of rectangle
        width (float): Width of rectangle
    
    Returns:
        float: Area of rectangle
    
    Example:
        >>> calculate_area(5, 3)
        15
    """
    return length * width

# Access docstring
print(calculate_area.__doc__)

# Better documentation with Google/NumPy style
def complex_function(param1, param2):
    """
    Brief description of function.
    
    Longer description with more details about what
    the function does and how to use it.
    
    Args:
        param1 (int): Description of param1
        param2 (str): Description of param2
    
    Returns:
        bool: Description of return value
    
    Raises:
        ValueError: When param1 is negative
        TypeError: When param2 is not string
    """
    pass


# --- Global vs Local Scope ---
global_var = "I'm global"

def test_scope():
    local_var = "I'm local"
    print(global_var)   # Can access global
    print(local_var)    # Can access local

test_scope()
print(global_var)       # Works
# print(local_var)      # Error: not defined outside function


# --- Modifying Global Variables ---
count = 0

def increment():
    global count  # Declare we're using global variable
    count += 1

increment()
increment()
print(count)  # 2

# Better approach: return new value
def increment_better(value):
    return value + 1

count = 0
count = increment_better(count)
count = increment_better(count)
print(count)  # 2


# --- nonlocal Keyword ---
def outer():
    x = 10
    
    def inner():
        nonlocal x  # Access outer function's variable
        x += 5
        print(f"Inner x: {x}")
    
    inner()
    print(f"Outer x: {x}")

outer()
# Output:
# Inner x: 15
# Outer x: 15


# =============================================================================
# MODULES
# =============================================================================
'''
Modules are Python files containing functions, classes, and variables.
Benefits:
- Code organization
- Reusability across projects
- Namespace separation
- Easier maintenance
'''

# --- Importing Modules ---

# Import entire module
import math
print(math.pi)           # 3.141592653589793
print(math.sqrt(16))     # 4.0

# Import specific items
from math import pi, sqrt
print(pi)                # 3.141592653589793
print(sqrt(16))          # 4.0

# Import with alias
import math as m
print(m.pi)

from math import sqrt as square_root
print(square_root(25))   # 5.0

# Import all (not recommended)
from math import *
print(cos(0))            # 1.0


# --- Common Built-in Modules ---

# math - Mathematical functions
import math
print(math.ceil(4.3))    # 5 (round up)
print(math.floor(4.7))   # 4 (round down)
print(math.pow(2, 3))    # 8.0 (power)
print(math.factorial(5)) # 120
print(math.gcd(48, 18))  # 6 (greatest common divisor)

# random - Random number generation
import random
print(random.random())              # Random float between 0 and 1
print(random.randint(1, 10))        # Random integer between 1 and 10
print(random.choice([1, 2, 3, 4]))  # Random element from list
print(random.uniform(1.0, 10.0))    # Random float between 1.0 and 10.0

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)             # Shuffle list in place
print(numbers)

print(random.sample([1, 2, 3, 4, 5], 3))  # Random sample of 3 elements

# datetime - Date and time operations
from datetime import datetime, date, time, timedelta

now = datetime.now()
print(now)                          # Current date and time
print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second)

today = date.today()
print(today)                        # Current date

# Create specific date
birthday = date(1990, 5, 15)
print(birthday)

# Date arithmetic
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
print(tomorrow, next_week)

# Format dates
print(now.strftime("%Y-%m-%d"))     # 2025-12-26
print(now.strftime("%B %d, %Y"))    # December 26, 2025

# os - Operating system interface
import os
print(os.getcwd())                  # Current working directory
# os.mkdir("new_folder")            # Create directory
# os.rename("old.txt", "new.txt")   # Rename file
# os.remove("file.txt")             # Delete file
print(os.path.exists("file.txt"))   # Check if file exists
print(os.path.isfile("test.txt"))   # Check if it's a file
print(os.path.isdir("folder"))      # Check if it's a directory

# sys - System-specific parameters
import sys
print(sys.version)                  # Python version
print(sys.platform)                 # Platform (win32, linux, darwin)
# sys.exit()                        # Exit program

# json - JSON encoding/decoding
import json

# Python dict to JSON string
data = {"name": "Alice", "age": 25, "city": "New York"}
json_string = json.dumps(data)
print(json_string)                  # {"name": "Alice", "age": 25, ...}

# Pretty print JSON
json_pretty = json.dumps(data, indent=4)
print(json_pretty)

# JSON string to Python dict
json_data = '{"name": "Bob", "age": 30}'
python_dict = json.loads(json_data)
print(python_dict["name"])          # Bob

# Write to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Read from file
with open("data.json", "r") as f:
    loaded_data = json.load(f)

# collections - Specialized container datatypes
from collections import Counter, defaultdict, namedtuple, deque

# Counter - count hashable objects
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = Counter(words)
print(count)                        # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(count.most_common(2))         # [('apple', 3), ('banana', 2)]

# defaultdict - dict with default values
from collections import defaultdict
dd = defaultdict(list)
dd["fruits"].append("apple")        # No KeyError!
print(dd)                           # {'fruits': ['apple']}

# namedtuple - tuple with named fields
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)                     # 10 20
print(p[0], p[1])                   # 10 20 (also works like tuple)

# deque - double-ended queue (efficient append/pop from both ends)
from collections import deque
dq = deque([1, 2, 3])
dq.append(4)                        # Add to right
dq.appendleft(0)                    # Add to left
print(dq)                           # deque([0, 1, 2, 3, 4])
dq.pop()                            # Remove from right
dq.popleft()                        # Remove from left

# itertools - Iterator functions
from itertools import count, cycle, repeat, chain, combinations, permutations

# count - infinite counter
# for i in count(10, 2):  # Start at 10, step 2
#     print(i)  # 10, 12, 14, ...

# cycle - infinite cycle through iterable
# for item in cycle([1, 2, 3]):
#     print(item)  # 1, 2, 3, 1, 2, 3, ...

# chain - combine iterables
list1 = [1, 2, 3]
list2 = [4, 5, 6]
chained = list(chain(list1, list2))
print(chained)                      # [1, 2, 3, 4, 5, 6]

# combinations - all combinations
items = [1, 2, 3]
combos = list(combinations(items, 2))
print(combos)                       # [(1, 2), (1, 3), (2, 3)]

# permutations - all permutations
perms = list(permutations(items, 2))
print(perms)                        # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]


# --- Creating Your Own Module ---
'''
Create a file named "mymodule.py" with the following content:

# mymodule.py
"""My custom module"""

PI = 3.14159

def greet(name):
    """Greet a person"""
    return f"Hello, {name}!"

def add(a, b):
    """Add two numbers"""
    return a + b

class Calculator:
    """Simple calculator class"""
    def multiply(self, a, b):
        return a * b

# Code that only runs when module is executed directly
if __name__ == "__main__":
    print("Module is being run directly")
    print(greet("World"))
'''

# Then import and use it:
# import mymodule
# print(mymodule.PI)
# print(mymodule.greet("Alice"))
# calc = mymodule.Calculator()
# print(calc.multiply(5, 3))


# --- Module Search Path ---
import sys
print(sys.path)  # List of directories Python searches for modules
# You can add directories:
# sys.path.append("/path/to/my/modules")


# --- Packages ---
'''
A package is a directory containing modules and a special __init__.py file.

Directory structure:
mypackage/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py

Import from package:
from mypackage import module1
from mypackage.subpackage import module3
import mypackage.module2 as m2
'''


# --- __name__ and __main__ ---
'''
Every Python module has a __name__ attribute.
- When run directly: __name__ == "__main__"
- When imported: __name__ == module name

This allows modules to have code that only runs when executed directly.
'''

def main():
    """Main function"""
    print("Running main function")

if __name__ == "__main__":
    # This code only runs when script is executed directly
    # Not when imported as a module
    main()
    print("Script executed directly")


# --- Reloading Modules ---
# Modules are loaded only once per session
# To reload a modified module:
import importlib
# importlib.reload(mymodule)

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================

'''
FUNCTIONS:
✓ Basic: def name(params): return value
✓ Default parameters for optional arguments
✓ *args for variable positional arguments
✓ **kwargs for variable keyword arguments
✓ Lambda for simple anonymous functions
✓ Decorators to modify function behavior
✓ Recursion for self-referential problems

MODULES:
✓ import module - import entire module
✓ from module import item - import specific items
✓ import module as alias - use alias
✓ Create your own modules for reusability
✓ Organize code into packages
✓ Use __name__ == "__main__" pattern

USEFUL BUILT-IN MODULES:
- math: Mathematical operations
- random: Random number generation
- datetime: Date and time handling
- os: Operating system interface
- sys: System-specific parameters
- json: JSON encoding/decoding
- collections: Specialized containers
- itertools: Iterator tools

SCOPE:
- Local: Inside function
- Global: Outside all functions
- Use 'global' to modify global variables
- Use 'nonlocal' for nested functions
- Prefer returning values over modifying globals
'''