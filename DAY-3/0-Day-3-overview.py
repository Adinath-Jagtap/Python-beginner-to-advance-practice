'''
DAY 3: Python Control Flow - Conditionals & Loops
'''

# =============================================================================
# CONDITIONAL STATEMENTS (if, elif, else)
# =============================================================================
'''
Conditional statements allow you to execute code based on conditions.
- if: executes block if condition is True
- elif: checks another condition if previous conditions were False
- else: executes if all previous conditions were False

Syntax:
if condition:
    # code block
elif another_condition:
    # code block
else:
    # code block
'''

# --- Basic if Statement ---
age = 18

if age >= 18:
    print("You are an adult")

# Single line if (when block is one statement)
if age >= 18: print("Adult")


# --- if-else Statement ---
age = 15

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")


# --- if-elif-else Statement ---
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")


# --- Nested if Statements ---
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")


# --- Ternary Operator (Conditional Expression) ---
# Syntax: value_if_true if condition else value_if_false

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # "Adult"

# Nested ternary (use sparingly for readability)
num = 5
result = "Positive" if num > 0 else "Zero" if num == 0 else "Negative"


# --- Multiple Conditions (Logical Operators) ---
age = 25
citizen = True

# Using 'and' - both conditions must be True
if age >= 18 and citizen:
    print("Eligible to vote")

# Using 'or' - at least one condition must be True
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("It's weekend!")

# Using 'not' - inverts the condition
is_raining = False
if not is_raining:
    print("Go for a walk")


# --- Membership Operators in Conditions ---
fruits = ["apple", "banana", "cherry"]

if "apple" in fruits:
    print("Apple is available")

if "grape" not in fruits:
    print("Grape is not available")

# With strings
text = "Hello World"
if "World" in text:
    print("Found 'World'")


# --- Identity Operators in Conditions ---
x = None

if x is None:
    print("x is None")

if x is not None:
    print("x has a value")

# Be careful with 'is' vs '=='
a = [1, 2, 3]
b = [1, 2, 3]
c = a

if a == b:      # True (same values)
    print("Equal values")

if a is b:      # False (different objects)
    print("Same object")

if a is c:      # True (same object)
    print("Same object")


# --- Truthy and Falsy Values ---
'''
Falsy values (evaluate to False):
- False
- None
- 0, 0.0, 0j
- "" (empty string)
- [] (empty list)
- () (empty tuple)
- {} (empty dict)
- set() (empty set)

Everything else is Truthy
'''

# Checking empty collections
my_list = []
if my_list:
    print("List has items")
else:
    print("List is empty")  # This executes

# Checking None
value = None
if value:
    print("Has value")
else:
    print("No value")  # This executes

# Explicit vs implicit checking
name = ""
if name:                    # Implicit: checks if name is truthy
    print("Name provided")

if name != "":              # Explicit: checks if name is not empty string
    print("Name provided")

if len(name) > 0:           # Explicit: checks length
    print("Name provided")


# --- Match-Case Statement (Python 3.10+) ---
'''
Similar to switch-case in other languages.
Uses structural pattern matching.
'''

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6 | 7:                      # Multiple values using |
        print("Weekend")
    case _:                          # Default case (like else)
        print("Invalid day")


# Pattern matching with conditions
point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):                     # Matches any point on y-axis
        print(f"On y-axis at y={y}")
    case (x, 0):                     # Matches any point on x-axis
        print(f"On x-axis at x={x}")
    case (x, y):                     # Matches any other point
        print(f"Point at ({x}, {y})")


# Match with guard (additional condition)
def classify_number(num):
    match num:
        case n if n < 0:
            return "Negative"
        case 0:
            return "Zero"
        case n if n > 0:
            return "Positive"


# =============================================================================
# FOR LOOPS
# =============================================================================
'''
For loops iterate over sequences (lists, tuples, strings, ranges, etc.)
Syntax:
for variable in iterable:
    # code block
'''

# --- Basic for Loop ---
# Iterate through list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterate through string
for char in "Python":
    print(char)

# Iterate through tuple
coordinates = (10, 20, 30)
for coord in coordinates:
    print(coord)


# --- Using range() ---
# range(stop) - from 0 to stop-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop) - from start to stop-1
for i in range(2, 7):
    print(i)  # 2, 3, 4, 5, 6

# range(start, stop, step) - with custom step
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Reverse iteration
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, ..., 1

# Negative range
for i in range(5, -5, -2):
    print(i)  # 5, 3, 1, -1, -3


# --- enumerate() Function ---
# Get both index and value
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry

# Start index from different number
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
# Output:
# 1. apple
# 2. banana
# 3. cherry


# --- zip() Function ---
# Iterate through multiple sequences simultaneously
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Tokyo"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

# zip stops at shortest sequence
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
for num, letter in zip(list1, list2):
    print(num, letter)  # Only 3 pairs: (1,a), (2,b), (3,c)


# --- Iterating Through Dictionaries ---
person = {"name": "John", "age": 30, "city": "New York"}

# Iterate through keys (default)
for key in person:
    print(key)

# Iterate through keys explicitly
for key in person.keys():
    print(key)

# Iterate through values
for value in person.values():
    print(value)

# Iterate through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")


# --- Nested for Loops ---
# Print multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i*j}")

# Iterate through 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # New line after each row


# --- List Comprehension (Compact for Loop) ---
# Create new list from existing sequence
numbers = [1, 2, 3, 4, 5]

# Traditional way
squares = []
for num in numbers:
    squares.append(num ** 2)

# List comprehension (more Pythonic)
squares = [num ** 2 for num in numbers]  # [1, 4, 9, 16, 25]

# With condition
evens = [num for num in numbers if num % 2 == 0]  # [2, 4]

# With if-else
labels = ["even" if num % 2 == 0 else "odd" for num in numbers]

# Nested list comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


# --- Dictionary Comprehension ---
# Create dictionary using comprehension
numbers = [1, 2, 3, 4, 5]
squares_dict = {num: num**2 for num in numbers}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# From two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = {k: v for k, v in zip(keys, values)}

# With condition
evens_dict = {num: num**2 for num in numbers if num % 2 == 0}


# --- Set Comprehension ---
numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique_squares = {num**2 for num in numbers}  # {1, 4, 9, 16, 25}


# =============================================================================
# WHILE LOOPS
# =============================================================================
'''
While loops execute as long as condition is True.
Syntax:
while condition:
    # code block
'''

# --- Basic while Loop ---
count = 0
while count < 5:
    print(count)
    count += 1  # Important: update condition variable

# Countdown
num = 5
while num > 0:
    print(num)
    num -= 1
print("Blast off!")


# --- while with else ---
# else executes when condition becomes False (not with break)
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("Loop completed normally")


# --- Infinite Loop ---
# Use with caution! Make sure there's a way to exit
# while True:
#     print("This runs forever")

# Practical use with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break
    print(f"You entered: {user_input}")


# --- Input Validation with while ---
# Keep asking until valid input
age = -1
while age < 0 or age > 120:
    age = int(input("Enter your age (0-120): "))
print(f"Your age is {age}")

# Another pattern
while True:
    password = input("Enter password: ")
    if len(password) >= 8:
        break
    print("Password must be at least 8 characters")


# =============================================================================
# LOOP CONTROL STATEMENTS
# =============================================================================

# --- break Statement ---
# Exits the loop immediately
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0, 1, 2, 3, 4

# Find first even number
numbers = [1, 3, 5, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number: {num}")
        break

# break in nested loops (only breaks inner loop)
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(f"i={i}, j={j}")


# --- continue Statement ---
# Skips rest of current iteration, continues with next
for i in range(5):
    if i == 2:
        continue  # Skip when i is 2
    print(i)  # Prints 0, 1, 3, 4

# Print only odd numbers
for num in range(10):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)  # Only prints odd: 1, 3, 5, 7, 9


# --- pass Statement ---
# Does nothing, placeholder for future code
for i in range(5):
    if i == 2:
        pass  # TODO: add logic later
    print(i)

# Useful for empty functions/classes during development
def future_function():
    pass  # Will implement later

class FutureClass:
    pass  # Will add methods later


# --- else with Loops ---
# else executes when loop completes normally (without break)

# for-else
for i in range(5):
    print(i)
else:
    print("Loop completed!")  # This executes

# for-else with break
numbers = [1, 3, 5, 7, 9]
target = 6
for num in numbers:
    if num == target:
        print(f"Found {target}")
        break
else:
    print(f"{target} not found")  # This executes because no break

# while-else
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("While loop finished")  # This executes

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
'''
CONDITIONALS:
✓ if-elif-else for multiple conditions
✓ Ternary operator for simple conditions: value_if_true if condition else value_if_false
✓ Use 'and', 'or', 'not' for logical operations
✓ Remember truthy/falsy values
✓ match-case for pattern matching (Python 3.10+)

FOR LOOPS:
✓ Iterate over sequences: lists, tuples, strings, ranges
✓ Use enumerate() for index + value
✓ Use zip() for parallel iteration
✓ List/dict/set comprehensions for compact code
✓ Nested loops for multidimensional data

WHILE LOOPS:
✓ Execute while condition is True
✓ Useful for unknown number of iterations
✓ Remember to update condition variable
✓ Good for input validation

LOOP CONTROL:
✓ break: exit loop immediately
✓ continue: skip to next iteration
✓ pass: do nothing (placeholder)
✓ else: executes when loop completes normally

BEST PRACTICES:
- Use for loops when you know number of iterations
- Use while loops when condition-based
- Break early when possible
- Use comprehensions for readable, fast code
- Avoid modifying collections while iterating
- Use built-in functions when available
'''