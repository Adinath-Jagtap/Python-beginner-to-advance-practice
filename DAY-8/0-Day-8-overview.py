'''
DAY 8: Python Decorators, Generators & Iterators
'''

# =============================================================================
# ITERATORS
# =============================================================================
'''
Iterator: An object that can be iterated (looped) over.
- Implements __iter__() method (returns iterator object)
- Implements __next__() method (returns next value)
- Raises StopIteration when no more items

Iterable vs Iterator:
- Iterable: Object that can return an iterator (list, tuple, string)
- Iterator: Object that produces values one at a time
'''

# --- Understanding Iteration ---
# Lists are iterable but not iterators
my_list = [1, 2, 3, 4, 5]

# Get iterator from iterable
my_iter = iter(my_list)

# Get next items
print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3
print(next(my_iter))  # 4
print(next(my_iter))  # 5
# print(next(my_iter))  # StopIteration error


# --- How for loop works internally ---
# This:
for item in [1, 2, 3]:
    print(item)

# Is equivalent to:
my_list = [1, 2, 3]
my_iter = iter(my_list)
while True:
    try:
        item = next(my_iter)
        print(item)
    except StopIteration:
        break


# --- Creating Custom Iterator ---
class Counter:
    """Iterator that counts from start to end"""
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        """Return iterator object (self)"""
        return self
    
    def __next__(self):
        """Return next value"""
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# Usage
counter = Counter(1, 5)
for num in counter:
    print(num)  # 1, 2, 3, 4, 5

# Manual iteration
counter2 = Counter(10, 12)
print(next(counter2))  # 10
print(next(counter2))  # 11
print(next(counter2))  # 12
# print(next(counter2))  # StopIteration


# --- Iterator for Custom Class ---
class MyRange:
    """Custom implementation of range()"""
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
    
    def __iter__(self):
        self.current = self.start
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = self.current
        self.current += self.step
        return result

# Usage
for num in MyRange(0, 10, 2):
    print(num)  # 0, 2, 4, 6, 8


# --- Iterator with State ---
class Fibonacci:
    """Iterator that generates Fibonacci sequence"""
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return result

# Generate first 10 Fibonacci numbers
fib = Fibonacci(10)
for num in fib:
    print(num, end=" ")  # 0 1 1 2 3 5 8 13 21 34
print()


# --- Infinite Iterator ---
class InfiniteCounter:
    """Iterator that counts infinitely"""
    def __init__(self, start=0):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        result = self.current
        self.current += 1
        return result

# Usage with break
counter = InfiniteCounter()
for num in counter:
    if num >= 5:
        break
    print(num)  # 0, 1, 2, 3, 4


# --- Built-in Iterators ---
# String iterator
text = "Python"
text_iter = iter(text)
print(next(text_iter))  # 'P'
print(next(text_iter))  # 'y'

# Tuple iterator
my_tuple = (1, 2, 3)
tuple_iter = iter(my_tuple)
print(next(tuple_iter))  # 1

# Dictionary iterator (iterates over keys)
my_dict = {'a': 1, 'b': 2, 'c': 3}
dict_iter = iter(my_dict)
print(next(dict_iter))  # 'a'

# File iterator (iterates over lines)
# with open('file.txt') as f:
#     for line in f:  # File is an iterator
#         print(line)


# --- Iterator Tools (itertools module) ---
import itertools

# count() - infinite counter
# for i in itertools.count(10, 2):  # Start at 10, step 2
#     if i > 20:
#         break
#     print(i)  # 10, 12, 14, 16, 18, 20

# cycle() - infinite cycle through iterable
colors = ['red', 'green', 'blue']
color_cycle = itertools.cycle(colors)
for i in range(7):
    print(next(color_cycle))  # red, green, blue, red, green, blue, red

# repeat() - repeat element
for item in itertools.repeat("Hello", 3):
    print(item)  # Hello, Hello, Hello

# chain() - combine iterables
list1 = [1, 2, 3]
list2 = [4, 5, 6]
for item in itertools.chain(list1, list2):
    print(item)  # 1, 2, 3, 4, 5, 6

# islice() - slice iterator
for num in itertools.islice(range(10), 2, 7):
    print(num)  # 2, 3, 4, 5, 6


# =============================================================================
# GENERATORS
# =============================================================================
'''
Generator: Special type of iterator that generates values on-the-fly.
- Uses 'yield' keyword instead of 'return'
- More memory efficient (doesn't store all values)
- State is automatically maintained
- Simpler syntax than iterators

Generator vs List:
- List: Stores all values in memory
- Generator: Generates values one at a time
'''

# --- Basic Generator Function ---
def simple_generator():
    """Generator that yields three values"""
    print("First")
    yield 1
    print("Second")
    yield 2
    print("Third")
    yield 3

# Create generator object
gen = simple_generator()

# Get values one by one
print(next(gen))  # Prints "First", returns 1
print(next(gen))  # Prints "Second", returns 2
print(next(gen))  # Prints "Third", returns 3
# print(next(gen))  # StopIteration

# Iterate using for loop
gen = simple_generator()
for value in gen:
    print(value)


# --- Generator vs Regular Function ---
# Regular function returns all values at once
def get_numbers_list():
    result = []
    for i in range(5):
        result.append(i)
    return result

# Generator yields values one at a time
def get_numbers_generator():
    for i in range(5):
        yield i

# Memory comparison
nums_list = get_numbers_list()  # Stores [0, 1, 2, 3, 4] in memory
nums_gen = get_numbers_generator()  # Stores only generator object

print(type(nums_list))  # <class 'list'>
print(type(nums_gen))   # <class 'generator'>


# --- Generator for Large Sequences ---
# Memory inefficient (creates million-element list)
def large_list():
    return [i for i in range(1000000)]

# Memory efficient (generates one at a time)
def large_generator():
    for i in range(1000000):
        yield i

# Usage
# big_list = large_list()  # Uses lots of memory
big_gen = large_generator()  # Uses minimal memory


# --- Generator with Multiple Yields ---
def countdown(n):
    """Count down from n to 1"""
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)  # 5, 4, 3, 2, 1


# --- Fibonacci Generator ---
def fibonacci_gen(n):
    """Generate first n Fibonacci numbers"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

for num in fibonacci_gen(10):
    print(num, end=" ")  # 0 1 1 2 3 5 8 13 21 34
print()


# --- Infinite Generator ---
def infinite_sequence():
    """Generate infinite sequence"""
    num = 0
    while True:
        yield num
        num += 1

# Usage with break
gen = infinite_sequence()
for num in gen:
    if num > 5:
        break
    print(num)  # 0, 1, 2, 3, 4, 5


# --- Generator with State ---
def even_numbers(start, end):
    """Generate even numbers in range"""
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num

for num in even_numbers(1, 10):
    print(num)  # 2, 4, 6, 8, 10


# --- Generator Expressions (Generator Comprehension) ---
# List comprehension (stores all in memory)
squares_list = [x**2 for x in range(5)]
print(squares_list)  # [0, 1, 4, 9, 16]

# Generator expression (generates on demand)
squares_gen = (x**2 for x in range(5))
print(type(squares_gen))  # <class 'generator'>

for square in squares_gen:
    print(square)  # 0, 1, 4, 9, 16

# Generator expressions with conditions
even_squares = (x**2 for x in range(10) if x % 2 == 0)
for square in even_squares:
    print(square)  # 0, 4, 16, 36, 64


# --- Generator with Return Value ---
def generator_with_return():
    """Generator can have return statement"""
    yield 1
    yield 2
    yield 3
    return "Done!"

gen = generator_with_return()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
try:
    print(next(gen))
except StopIteration as e:
    print(e.value)  # "Done!"


# --- Reading Large Files with Generator ---
def read_large_file(file_path):
    """Read large file line by line"""
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Usage (doesn't load entire file into memory)
# for line in read_large_file('large_file.txt'):
#     print(line)


# --- Generator for Data Processing ---
def process_data(data):
    """Process data items one by one"""
    for item in data:
        # Simulate processing
        processed = item * 2
        yield processed

numbers = [1, 2, 3, 4, 5]
for result in process_data(numbers):
    print(result)  # 2, 4, 6, 8, 10


# --- Chaining Generators ---
def numbers_gen():
    """Generate numbers"""
    for i in range(5):
        yield i

def square_gen(numbers):
    """Square each number"""
    for num in numbers:
        yield num ** 2

def add_ten_gen(numbers):
    """Add 10 to each number"""
    for num in numbers:
        yield num + 10

# Chain generators
nums = numbers_gen()
squared = square_gen(nums)
final = add_ten_gen(squared)

for result in final:
    print(result)  # 10, 11, 14, 19, 26


# --- Generator Methods: send(), throw(), close() ---
def generator_with_send():
    """Generator that receives values"""
    value = None
    while True:
        value = yield value
        if value is not None:
            value = value * 2

gen = generator_with_send()
next(gen)  # Prime the generator
print(gen.send(5))   # 10
print(gen.send(10))  # 20
print(gen.send(3))   # 6


# =============================================================================
# DECORATORS
# =============================================================================
'''
Decorator: Function that modifies behavior of another function.
- Takes a function as argument
- Returns a modified function
- Uses @ syntax for cleaner code
- Used for logging, timing, authentication, etc.

Syntax:
@decorator
def function():
    pass

Is equivalent to:
function = decorator(function)
'''

# --- Basic Decorator ---
def my_decorator(func):
    """Basic decorator that wraps a function"""
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

# Without @ syntax
def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
say_hello()
# Output:
# Before function call
# Hello!
# After function call


# --- Using @ Syntax ---
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def greet():
    print("Hello, World!")

greet()
# Output:
# Before
# Hello, World!
# After


# --- Decorator with Function Arguments ---
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

result = add(5, 3)
print(result)
greet("Alice")


# --- Decorator that Returns Value ---
def uppercase_decorator(func):
    """Decorator that converts result to uppercase"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def get_greeting(name):
    return f"hello, {name}"

print(get_greeting("Alice"))  # HELLO, ALICE


# --- Multiple Decorators ---
def bold(func):
    def wrapper(*args, **kwargs):
        return "<b>" + func(*args, **kwargs) + "</b>"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        return "<i>" + func(*args, **kwargs) + "</i>"
    return wrapper

@bold
@italic
def get_text():
    return "Hello"

print(get_text())  # <b><i>Hello</i></b>
# Decorators are applied bottom-up


# --- Decorator with Arguments ---
def repeat(times):
    """Decorator that repeats function call"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Hello!
# Hello!
# Hello!


@repeat(times=5)
def greet(name):
    print(f"Hi, {name}!")

greet("Bob")


# --- Timing Decorator ---
import time

def timer_decorator(func):
    """Measure function execution time"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(1)
    return "Done"

result = slow_function()


# --- Logging Decorator ---
def logger(func):
    """Log function calls"""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

@logger
def multiply(x, y):
    return x * y

add(5, 3)
multiply(4, 7)


# --- Authentication Decorator ---
def require_auth(func):
    """Check if user is authenticated"""
    def wrapper(*args, **kwargs):
        # Simulate authentication check
        is_authenticated = True  # In real app, check session/token
        
        if is_authenticated:
            return func(*args, **kwargs)
        else:
            print("Access denied! Please login.")
            return None
    return wrapper

@require_auth
def view_profile():
    return "Viewing profile..."

print(view_profile())


# --- Caching Decorator (Memoization) ---
def memoize(func):
    """Cache function results"""
    cache = {}
    def wrapper(*args):
        if args in cache:
            print(f"Returning cached result for {args}")
            return cache[args]
        else:
            print(f"Computing result for {args}")
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))
print(fibonacci(5))  # Uses cached result


# --- Class-based Decorator ---
class CountCalls:
    """Decorator that counts function calls"""
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} has been called {self.count} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

say_hello()
say_hello()
say_hello()


# --- Preserving Function Metadata ---
# Problem: wrapper loses original function's metadata
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@simple_decorator
def my_function():
    """This is my function"""
    pass

print(my_function.__name__)  # 'wrapper' (not 'my_function')
print(my_function.__doc__)   # None (not the docstring)

# Solution: Use functools.wraps
from functools import wraps

def better_decorator(func):
    @wraps(func)  # Preserves metadata
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@better_decorator
def my_function():
    """This is my function"""
    pass

print(my_function.__name__)  # 'my_function'
print(my_function.__doc__)   # 'This is my function'


# --- Decorator Factory ---
def prefix_decorator(prefix):
    """Factory that creates decorators with custom prefix"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{prefix}: {result}"
        return wrapper
    return decorator

@prefix_decorator("INFO")
def get_message():
    return "Hello, World!"

@prefix_decorator("ERROR")
def get_error():
    return "Something went wrong"

print(get_message())  # INFO: Hello, World!
print(get_error())    # ERROR: Something went wrong


# --- Decorator with Optional Arguments ---
from functools import wraps

def smart_decorator(arg=None):
    """Decorator that works with or without arguments"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Argument: {arg}")
            return func(*args, **kwargs)
        return wrapper
    
    # If called without parentheses: @smart_decorator
    if callable(arg):
        return decorator(arg)
    # If called with parentheses: @smart_decorator(value)
    else:
        return decorator

@smart_decorator
def func1():
    print("Function 1")

@smart_decorator("Custom")
def func2():
    print("Function 2")

func1()
func2()


# --- Real-world Decorator Examples ---

# 1. Debug decorator
def debug(func):
    """Print function signature and return value"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

add(5, 3)


# 2. Retry decorator
def retry(max_attempts=3):
    """Retry function if it fails"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
                    if attempts == max_attempts:
                        raise
        return wrapper
    return decorator

@retry(max_attempts=3)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success!"


# 3. Validate arguments decorator
def validate_positive(func):
    """Ensure all arguments are positive"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError("All arguments must be positive")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def calculate_area(length, width):
    return length * width

print(calculate_area(5, 3))   # 15
# print(calculate_area(-5, 3))  # ValueError


# =============================================================================
# COMBINING CONCEPTS
# =============================================================================

# --- Generator with Decorator ---
def timer_decorator(func):
    """Time a generator function"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        # Generator is created, not executed yet
        for item in result:
            yield item
        end = time.time()
        print(f"Generator took {end - start:.4f} seconds")
    return wrapper

@timer_decorator
def number_generator(n):
    """Generate numbers with delay"""
    for i in range(n):
        time.sleep(0.1)
        yield i

for num in number_generator(5):
    print(num)


# --- Iterator with Decorator ---
@timer_decorator
class RangeIterator:
    """Custom range iterator"""
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = self.current
        self.current += 1
        return result


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
'''
ITERATORS:
✓ Object that implements __iter__() and __next__()
✓ __iter__() returns iterator object (usually self)
✓ __next__() returns next value or raises StopIteration
✓ Can be infinite or finite
✓ State is maintained between calls

GENERATORS:
✓ Function that uses 'yield' instead of 'return'
✓ Simpler way to create iterators
✓ Memory efficient (lazy evaluation)
✓ State automatically maintained
✓ Generator expression: (x for x in iterable)
✓ Use for large datasets, infinite sequences

GENERATOR vs ITERATOR:
- Generator: Uses yield, simpler syntax
- Iterator: Uses __iter__ and __next__, more control

DECORATORS:
✓ Modify function behavior without changing code
✓ Syntax: @decorator before function definition
✓ Take function as argument, return modified function
✓ Use @wraps to preserve metadata
✓ Can be stacked (applied bottom-up)
✓ Can accept arguments (requires nested functions)

COMMON USE CASES:
Iterators:
- Custom iteration logic
- Complex state management
- File reading line by line

Generators:
- Large sequences (memory efficient)
- Data pipelines
- Infinite sequences
- On-the-fly data generation

Decorators:
- Logging
- Timing/profiling
- Authentication/authorization
- Caching/memoization
- Input validation
- Retry logic

BEST PRACTICES:
✓ Use generators for large datasets
✓ Use decorators for cross-cutting concerns
✓ Always use @wraps in decorators
✓ Keep decorators simple and focused
✓ Use generator expressions for simple cases
✓ Document what decorators do
'''