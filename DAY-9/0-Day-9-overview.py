'''
DAY 9: List Comprehensions, Lambda, Map/Filter/Reduce
'''

# =============================================================================
# LIST COMPREHENSIONS
# =============================================================================
'''
List Comprehension: Concise way to create lists in Python.
- More readable than traditional loops
- Faster than append() in loops
- Can include conditions

Basic Syntax:
[expression for item in iterable]
[expression for item in iterable if condition]
[expression if condition else other for item in iterable]
'''

# --- Traditional Way vs List Comprehension ---
# Traditional way using loop
squares = []
for x in range(5):
    squares.append(x ** 2)
print(squares)  # [0, 1, 4, 9, 16]

# List comprehension (cleaner and faster)
squares = [x ** 2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]


# --- Basic List Comprehensions ---
# Create list of numbers
numbers = [x for x in range(10)]
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Square each number
squares = [x ** 2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# Double each number
doubled = [x * 2 for x in range(5)]
print(doubled)  # [0, 2, 4, 6, 8]

# String operations
names = ['alice', 'bob', 'charlie']
uppercase_names = [name.upper() for name in names]
print(uppercase_names)  # ['ALICE', 'BOB', 'CHARLIE']

# Get length of each string
lengths = [len(name) for name in names]
print(lengths)  # [5, 3, 7]


# --- List Comprehension with Conditions (Filtering) ---
# Get even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# Get odd numbers
odds = [x for x in range(10) if x % 2 != 0]
print(odds)  # [1, 3, 5, 7, 9]

# Numbers divisible by 3
div_by_3 = [x for x in range(20) if x % 3 == 0]
print(div_by_3)  # [0, 3, 6, 9, 12, 15, 18]

# Filter strings longer than 4 characters
names = ['alice', 'bob', 'charlie', 'dan', 'elizabeth']
long_names = [name for name in names if len(name) > 4]
print(long_names)  # ['alice', 'charlie', 'elizabeth']

# Positive numbers from mixed list
numbers = [-5, 3, -2, 8, -1, 10]
positive = [x for x in numbers if x > 0]
print(positive)  # [3, 8, 10]


# --- List Comprehension with If-Else ---
# Mark numbers as even or odd
labels = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
print(labels)  # ['even', 'odd', 'even', 'odd', 'even']

# Double even numbers, triple odd numbers
numbers = [x * 2 if x % 2 == 0 else x * 3 for x in range(6)]
print(numbers)  # [0, 3, 4, 9, 8, 15]

# Replace negative with 0, keep positive
numbers = [-5, 3, -2, 8, -1, 10]
result = [x if x >= 0 else 0 for x in numbers]
print(result)  # [0, 3, 0, 8, 0, 10]


# --- Nested List Comprehensions ---
# Create 2D matrix
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# Multiplication table
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
for row in table:
    print(row)

# Flatten 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Flatten with condition
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
even_flat = [num for row in matrix for num in row if num % 2 == 0]
print(even_flat)  # [2, 4, 6, 8]


# --- Working with Strings ---
# Get first character of each word
sentence = "Hello World Python Programming"
first_chars = [word[0] for word in sentence.split()]
print(first_chars)  # ['H', 'W', 'P', 'P']

# Convert characters to ASCII
text = "ABC"
ascii_values = [ord(char) for char in text]
print(ascii_values)  # [65, 66, 67]

# Remove vowels from string
text = "Hello World"
consonants = [char for char in text if char.lower() not in 'aeiou']
print(''.join(consonants))  # 'Hll Wrld'


# --- Working with Multiple Lists ---
# Combine two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = [x + y for x, y in zip(list1, list2)]
print(combined)  # [5, 7, 9]

# Multiply elements of two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
products = [x * y for x, y in zip(list1, list2)]
print(products)  # [4, 10, 18]

# Cartesian product (all pairs)
list1 = [1, 2]
list2 = ['a', 'b']
pairs = [(x, y) for x in list1 for y in list2]
print(pairs)  # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]


# --- Dictionary Comprehension ---
# Create dictionary from lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = {k: v for k, v in zip(keys, values)}
print(my_dict)  # {'a': 1, 'b': 2, 'c': 3}

# Square numbers as dictionary
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Swap keys and values
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}

# Filter dictionary by condition
scores = {'Alice': 85, 'Bob': 65, 'Charlie': 92, 'Dan': 58}
passed = {name: score for name, score in scores.items() if score >= 70}
print(passed)  # {'Alice': 85, 'Charlie': 92}


# --- Set Comprehension ---
# Create set of squares
squares_set = {x**2 for x in range(5)}
print(squares_set)  # {0, 1, 4, 9, 16}

# Remove duplicates and square
numbers = [1, 2, 2, 3, 3, 4]
unique_squares = {x**2 for x in numbers}
print(unique_squares)  # {1, 4, 9, 16}


# --- Real-world Examples ---
# Extract all emails from text
text = "Contact us at support@example.com or sales@example.com"
words = text.split()
emails = [word for word in words if '@' in word]
print(emails)  # ['support@example.com', 'sales@example.com']

# Parse and convert data
prices = ["$10.50", "$25.00", "$8.99"]
numeric_prices = [float(price[1:]) for price in prices]
print(numeric_prices)  # [10.5, 25.0, 8.99]

# Grade students
scores = [85, 92, 78, 90, 88]
grades = ['Pass' if score >= 80 else 'Fail' for score in scores]
print(grades)  # ['Pass', 'Pass', 'Fail', 'Pass', 'Pass']

# Extract file extensions
files = ['document.pdf', 'image.jpg', 'script.py', 'data.csv']
extensions = [file.split('.')[-1] for file in files]
print(extensions)  # ['pdf', 'jpg', 'py', 'csv']


# =============================================================================
# LAMBDA FUNCTIONS
# =============================================================================
'''
Lambda Function: Anonymous (unnamed) function defined in single line.
- Used for simple, short operations
- Can have multiple arguments but only one expression
- Returns result automatically (no return keyword needed)

Syntax:
lambda arguments: expression

Regular function:
def add(x, y):
    return x + y

Lambda equivalent:
add = lambda x, y: x + y
'''

# --- Basic Lambda Functions ---
# Regular function
def square(x):
    return x ** 2

print(square(5))  # 25

# Lambda equivalent
square_lambda = lambda x: x ** 2
print(square_lambda(5))  # 25

# Lambda with multiple arguments
add = lambda x, y: x + y
print(add(3, 5))  # 8

multiply = lambda x, y: x * y
print(multiply(4, 6))  # 24

# Lambda with three arguments
sum_three = lambda a, b, c: a + b + c
print(sum_three(1, 2, 3))  # 6


# --- Lambda with Conditions ---
# Check if even
is_even = lambda x: x % 2 == 0
print(is_even(4))  # True
print(is_even(5))  # False

# Maximum of two numbers
max_of_two = lambda a, b: a if a > b else b
print(max_of_two(10, 5))  # 10

# Absolute value
absolute = lambda x: x if x >= 0 else -x
print(absolute(-5))  # 5
print(absolute(3))   # 3


# --- Lambda with Strings ---
# Convert to uppercase
uppercase = lambda s: s.upper()
print(uppercase("hello"))  # HELLO

# Get length
length = lambda s: len(s)
print(length("Python"))  # 6

# Reverse string
reverse = lambda s: s[::-1]
print(reverse("hello"))  # olleh


# --- Lambda in Sorting ---
# Sort by second element of tuple
students = [('Alice', 85), ('Bob', 75), ('Charlie', 90)]
students.sort(key=lambda x: x[1])  # Sort by score
print(students)  # [('Bob', 75), ('Alice', 85), ('Charlie', 90)]

# Sort strings by length
words = ['python', 'is', 'awesome', 'fun']
words.sort(key=lambda x: len(x))
print(words)  # ['is', 'fun', 'python', 'awesome']

# Sort dictionary by values
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print(sorted_scores)  # [('Bob', 92), ('Alice', 85), ('Charlie', 78)]


# --- Lambda with List Methods ---
# Using lambda with max/min
numbers = [5, 2, 8, 1, 9]
maximum = max(numbers, key=lambda x: x)
print(maximum)  # 9

# Find longest string
words = ['cat', 'elephant', 'dog']
longest = max(words, key=lambda x: len(x))
print(longest)  # elephant


# --- Immediately Invoked Lambda ---
# Call lambda immediately
result = (lambda x, y: x + y)(5, 3)
print(result)  # 8

# Calculate area immediately
area = (lambda length, width: length * width)(5, 3)
print(area)  # 15


# --- Lambda Limitations ---
# Lambda can only have ONE expression
# This works:
square = lambda x: x ** 2

# This DOESN'T work (multiple statements):
# invalid = lambda x: 
#     y = x ** 2
#     return y

# For complex logic, use regular functions
def complex_function(x):
    y = x ** 2
    z = y + 10
    return z


# =============================================================================
# MAP FUNCTION
# =============================================================================
'''
map(): Applies a function to every item in an iterable.
- Returns map object (iterator)
- Convert to list/tuple to see results
- More efficient than loops for simple operations

Syntax:
map(function, iterable)
'''

# --- Basic Map Usage ---
# Square all numbers
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # [1, 4, 9, 16, 25]

# Double all numbers
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# Convert to uppercase
names = ['alice', 'bob', 'charlie']
uppercase = list(map(lambda x: x.upper(), names))
print(uppercase)  # ['ALICE', 'BOB', 'CHARLIE']


# --- Map with Built-in Functions ---
# Convert strings to integers
string_numbers = ['1', '2', '3', '4', '5']
numbers = list(map(int, string_numbers))
print(numbers)  # [1, 2, 3, 4, 5]

# Convert to float
prices = ['10.50', '25.00', '8.99']
float_prices = list(map(float, prices))
print(float_prices)  # [10.5, 25.0, 8.99]

# Get length of each string
words = ['cat', 'elephant', 'dog']
lengths = list(map(len, words))
print(lengths)  # [3, 8, 3]


# --- Map with Multiple Iterables ---
# Add two lists element-wise
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sums = list(map(lambda x, y: x + y, list1, list2))
print(sums)  # [5, 7, 9]

# Multiply two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
products = list(map(lambda x, y: x * y, list1, list2))
print(products)  # [4, 10, 18]

# Combine three lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
result = list(map(lambda x, y, z: x + y + z, list1, list2, list3))
print(result)  # [12, 15, 18]


# --- Map with Custom Functions ---
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(celsius_to_fahrenheit, celsius))
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]


# --- Map vs List Comprehension ---
# Both achieve same result
numbers = [1, 2, 3, 4, 5]

# Using map
squared_map = list(map(lambda x: x ** 2, numbers))

# Using list comprehension (more Pythonic)
squared_comp = [x ** 2 for x in numbers]

print(squared_map)   # [1, 4, 9, 16, 25]
print(squared_comp)  # [1, 4, 9, 16, 25]


# =============================================================================
# FILTER FUNCTION
# =============================================================================
'''
filter(): Filters items in an iterable based on a condition.
- Returns filter object (iterator)
- Only keeps items where function returns True
- Convert to list/tuple to see results

Syntax:
filter(function, iterable)
'''

# --- Basic Filter Usage ---
# Get even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # [2, 4, 6, 8, 10]

# Get odd numbers
odds = list(filter(lambda x: x % 2 != 0, numbers))
print(odds)  # [1, 3, 5, 7, 9]

# Filter positive numbers
numbers = [-5, 3, -2, 8, -1, 10]
positive = list(filter(lambda x: x > 0, numbers))
print(positive)  # [3, 8, 10]


# --- Filter with Strings ---
# Filter long words
words = ['cat', 'elephant', 'dog', 'butterfly']
long_words = list(filter(lambda x: len(x) > 5, words))
print(long_words)  # ['elephant', 'butterfly']

# Filter words starting with 'a'
words = ['apple', 'banana', 'avocado', 'cherry']
a_words = list(filter(lambda x: x.startswith('a'), words))
print(a_words)  # ['apple', 'avocado']

# Filter non-empty strings
strings = ['hello', '', 'world', '', 'python']
non_empty = list(filter(lambda x: x != '', strings))
print(non_empty)  # ['hello', 'world', 'python']


# --- Filter with None (Remove Falsy Values) ---
# Remove all falsy values (0, '', None, False)
mixed = [1, 0, 'hello', '', None, 'world', False, True]
truthy = list(filter(None, mixed))
print(truthy)  # [1, 'hello', 'world', True]


# --- Filter with Custom Functions ---
def is_adult(age):
    return age >= 18

ages = [15, 22, 17, 30, 12, 25]
adults = list(filter(is_adult, ages))
print(adults)  # [22, 30, 25]

# Filter passing students
def passed(score):
    return score >= 60

scores = [45, 78, 56, 89, 92, 34]
passing_scores = list(filter(passed, scores))
print(passing_scores)  # [78, 89, 92]


# --- Filter vs List Comprehension ---
# Both achieve same result
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter
evens_filter = list(filter(lambda x: x % 2 == 0, numbers))

# Using list comprehension (more Pythonic)
evens_comp = [x for x in numbers if x % 2 == 0]

print(evens_filter)  # [2, 4, 6, 8, 10]
print(evens_comp)    # [2, 4, 6, 8, 10]


# --- Complex Filtering ---
# Filter dictionaries
students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 65},
    {'name': 'Charlie', 'score': 92}
]
passed_students = list(filter(lambda x: x['score'] >= 70, students))
print(passed_students)
# [{'name': 'Alice', 'score': 85}, {'name': 'Charlie', 'score': 92}]


# =============================================================================
# REDUCE FUNCTION
# =============================================================================
'''
reduce(): Applies function cumulatively to items, reducing to single value.
- Must import from functools
- Takes two arguments: accumulated result and next item
- Processes left to right

Syntax:
from functools import reduce
reduce(function, iterable, initial_value)
'''

from functools import reduce

# --- Basic Reduce Usage ---
# Sum all numbers
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15
# How it works: ((((1+2)+3)+4)+5)

# Product of all numbers
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120
# How it works: ((((1*2)*3)*4)*5)


# --- Reduce with Initial Value ---
# Sum with initial value
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers, 10)
print(total)  # 25 (10 + 1 + 2 + 3 + 4 + 5)

# Product with initial value
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers, 2)
print(product)  # 48 (2 * 1 * 2 * 3 * 4)


# --- Finding Maximum/Minimum ---
# Find maximum
numbers = [3, 7, 2, 9, 1, 8]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # 9

# Find minimum
minimum = reduce(lambda x, y: x if x < y else y, numbers)
print(minimum)  # 1


# --- String Operations ---
# Concatenate strings
words = ['Hello', ' ', 'World', '!']
sentence = reduce(lambda x, y: x + y, words)
print(sentence)  # 'Hello World!'

# Build sentence with spaces
words = ['Python', 'is', 'awesome']
sentence = reduce(lambda x, y: x + ' ' + y, words)
print(sentence)  # 'Python is awesome'


# --- Reduce vs Built-in Functions ---
numbers = [1, 2, 3, 4, 5]

# Using reduce
sum_reduce = reduce(lambda x, y: x + y, numbers)

# Using built-in sum (preferred)
sum_builtin = sum(numbers)

print(sum_reduce)   # 15
print(sum_builtin)  # 15

# Note: For simple operations like sum, max, min, use built-in functions
# Use reduce for custom accumulation logic


# --- Complex Reduce Examples ---
# Count occurrences
numbers = [1, 2, 1, 3, 2, 1, 4]
# Build dictionary of counts
counts = reduce(
    lambda acc, x: {**acc, x: acc.get(x, 0) + 1},
    numbers,
    {}
)
print(counts)  # {1: 3, 2: 2, 3: 1, 4: 1}

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = reduce(lambda x, y: x + y, nested)
print(flat)  # [1, 2, 3, 4, 5, 6]


# =============================================================================
# COMBINING MAP, FILTER, AND REDUCE
# =============================================================================

# --- Example 1: Process and Sum ---
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Square even numbers and sum them
result = reduce(
    lambda x, y: x + y,
    map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
)
print(result)  # 220 (4 + 16 + 36 + 64 + 100)

# Step by step:
# 1. filter: [2, 4, 6, 8, 10]
# 2. map: [4, 16, 36, 64, 100]
# 3. reduce: 4 + 16 + 36 + 64 + 100 = 220


# --- Example 2: Data Pipeline ---
# Process sales data
sales = [
    {'product': 'A', 'price': 100, 'quantity': 2},
    {'product': 'B', 'price': 50, 'quantity': 5},
    {'product': 'C', 'price': 200, 'quantity': 1}
]

# Calculate total revenue from sales over 100
total_revenue = reduce(
    lambda x, y: x + y,
    map(
        lambda x: x['price'] * x['quantity'],
        filter(lambda x: x['price'] * x['quantity'] > 100, sales)
    )
)
print(total_revenue)  # 450 (200 + 250)


# --- Example 3: Using All Together ---
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get average of squared even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
squared = list(map(lambda x: x ** 2, evens))
total = reduce(lambda x, y: x + y, squared)
average = total / len(squared)
print(f"Average: {average}")  # 44.0


# =============================================================================
# LIST COMPREHENSION vs MAP/FILTER
# =============================================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# --- Map Equivalent ---
# Using map
squared_map = list(map(lambda x: x ** 2, numbers))

# Using list comprehension (MORE PYTHONIC)
squared_comp = [x ** 2 for x in numbers]


# --- Filter Equivalent ---
# Using filter
evens_filter = list(filter(lambda x: x % 2 == 0, numbers))

# Using list comprehension (MORE PYTHONIC)
evens_comp = [x for x in numbers if x % 2 == 0]


# --- Map + Filter ---
# Using map and filter
result_mf = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))

# Using list comprehension (MORE PYTHONIC AND READABLE)
result_comp = [x ** 2 for x in numbers if x % 2 == 0]

print(result_mf)    # [4, 16, 36, 64, 100]
print(result_comp)  # [4, 16, 36, 64, 100]


# =============================================================================
# REAL-WORLD EXAMPLES
# =============================================================================

# --- Example 1: Data Cleaning ---
# Clean and process user data
raw_data = [
    '  Alice  ',
    '  bob',
    'CHARLIE  ',
    '  dave  '
]

# Clean: strip whitespace, capitalize
cleaned = list(map(lambda x: x.strip().capitalize(), raw_data))
print(cleaned)  # ['Alice', 'Bob', 'Charlie', 'Dave']

# List comprehension version (preferred)
cleaned_comp = [name.strip().capitalize() for name in raw_data]
print(cleaned_comp)


# --- Example 2: Grade Processing ---
scores = [45, 78, 56, 89, 92, 34, 67]

# Filter passing scores, calculate average
passing = list(filter(lambda x: x >= 60, scores))
average = reduce(lambda x, y: x + y, passing) / len(passing)
print(f"Passing average: {average:.2f}")  # 81.50


# --- Example 3: Price Calculation ---
items = [
    {'name': 'Apple', 'price': 1.50, 'quantity': 5},
    {'name': 'Banana', 'price': 0.80, 'quantity': 8},
    {'name': 'Orange', 'price': 2.00, 'quantity': 3}
]

# Calculate total cost
total = reduce(
    lambda x, y: x + y,
    map(lambda item: item['price'] * item['quantity'], items)
)
print(f"Total: ${total:.2f}")  # $20.40

# List comprehension version (preferred)
total_comp = sum([item['price'] * item['quantity'] for item in items])
print(f"Total: ${total_comp:.2f}")


# --- Example 4: Email Validation ---
emails = [
    'user@example.com',
    'invalid.email',
    'another@test.com',
    'bad@',
    'good@domain.org'
]

# Simple validation: contains @ and .
valid_emails = list(filter(lambda email: '@' in email and '.' in email, emails))
print(valid_emails)
# ['user@example.com', 'another@test.com', 'good@domain.org']


# --- Example 5: Temperature Conversion ---
celsius_temps = [0, 10, 20, 30, 40]

# Convert to Fahrenheit
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius_temps))
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]

# List comprehension version
fahrenheit_comp = [(c * 9/5) + 32 for c in celsius_temps]
print(fahrenheit_comp)


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
'''
LIST COMPREHENSIONS:
✓ Syntax: [expression for item in iterable]
✓ With condition: [expression for item in iterable if condition]
✓ With if-else: [expression if condition else other for item in iterable]
✓ More Pythonic than map/filter for most cases
✓ More readable and faster than loops
✓ Can create lists, sets, and dictionaries
✓ Can be nested for complex operations

LAMBDA FUNCTIONS:
✓ Anonymous functions: lambda arguments: expression
✓ Single expression only (no multiple statements)
✓ Commonly used with map, filter, reduce, sort
✓ Good for simple, one-time operations
✓ For complex logic, use regular functions

MAP:
✓ Applies function to each item: map(function, iterable)
✓ Returns iterator (convert to list to see results)
✓ Can work with multiple iterables
✓ List comprehension often more Pythonic

FILTER:
✓ Filters items by condition: filter(function, iterable)
✓ Returns iterator (convert to list to see results)
✓ Keeps items where function returns True
✓ Use filter(None, iterable) to remove falsy values
✓ List comprehension with if often more Pythonic

REDUCE:
✓ Reduces to single value: reduce(function, iterable, initial)
✓ Must import from functools
✓ Processes left to right cumulatively
✓ For sum, max, min use built-in functions instead
✓ Use for custom accumulation logic

WHEN TO USE WHAT:
✓ List Comprehension: Most readable for simple transformations
✓ Map: When applying existing function to all items
✓ Filter: When filtering with existing function
✓ Reduce: For accumulation operations beyond sum/max/min
✓ Lambda: For simple, throwaway functions with map/filter/sort
BEST PRACTICES:
✓ Prefer list comprehensions over map/filter (more Pythonic)
✓ Use built-in functions (sum, max, min) over reduce
✓ Keep lambdas simple (one expression)
✓ Use regular functions for complex logic
✓ Choose readability over cleverness
'''