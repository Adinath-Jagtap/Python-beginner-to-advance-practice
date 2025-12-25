'''
DAY 2: Python Data Structures - Lists, Tuples, Dictionaries
''' 

# =============================================================================
# LISTS
# =============================================================================
'''
Lists are ordered, mutable (changeable) collections that can hold mixed data types.
- Allow duplicate elements
- Indexed starting at 0
- Support negative indexing (-1 for last element)
- Dynamic size (grow/shrink automatically)
'''

# --- Creating Lists ---
empty_list = []
empty_list2 = list()

numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, [1, 2]]     # Can contain different types
nested = [[1, 2], [3, 4], [5, 6]]            # List of lists

# List comprehension (elegant way to create lists)
squares = [x**2 for x in range(5)]           # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0] # [0, 2, 4, 6, 8]

# Create list from other iterables
from_string = list("abc")                    # ['a', 'b', 'c']
from_tuple = list((1, 2, 3))                 # [1, 2, 3]
from_range = list(range(5))                  # [0, 1, 2, 3, 4]


# --- Accessing Elements ---
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Indexing
first = fruits[0]                            # "apple"
second = fruits[1]                           # "banana"
last = fruits[-1]                            # "elderberry" (negative indexing)
second_last = fruits[-2]                     # "date"

# Slicing: list[start:stop:step]
fruits[1:3]                                  # ['banana', 'cherry'] (stop not included)
fruits[:3]                                   # ['apple', 'banana', 'cherry'] (start defaults to 0)
fruits[2:]                                   # ['cherry', 'date', 'elderberry'] (stop defaults to end)
fruits[::2]                                  # ['apple', 'cherry', 'elderberry'] (every 2nd element)
fruits[::-1]                                 # Reverse the list
fruits[-3:-1]                                # ['cherry', 'date'] (negative indices in slicing)


# --- Modifying Lists ---
fruits = ["apple", "banana", "cherry"]

# Change single element
fruits[1] = "blueberry"                      # ['apple', 'blueberry', 'cherry']

# Change range of elements
fruits[0:2] = ["apricot", "blackberry"]      # ['apricot', 'blackberry', 'cherry']

# Add elements
fruits.append("date")                        # Add to end → ['apricot', 'blackberry', 'cherry', 'date']
fruits.insert(1, "banana")                   # Insert at index 1 → ['apricot', 'banana', 'blackberry', 'cherry', 'date']
fruits.extend(["fig", "grape"])              # Add multiple → ['apricot', 'banana', ..., 'fig', 'grape']
fruits += ["kiwi"]                           # Same as extend

# Remove elements
fruits.remove("banana")                      # Remove first occurrence of value
popped = fruits.pop()                        # Remove and return last element
popped = fruits.pop(0)                       # Remove and return element at index 0
del fruits[1]                                # Delete element at index 1
del fruits[1:3]                              # Delete slice
fruits.clear()                               # Remove all elements


# --- List Methods ---
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Searching
numbers.count(1)                             # 2 (count occurrences)
numbers.index(5)                             # 4 (first index of value, raises ValueError if not found)

# Sorting and reversing
numbers.sort()                               # [1, 1, 2, 3, 4, 5, 5, 6, 9] (sorts in place)
numbers.sort(reverse=True)                   # [9, 6, 5, 5, 4, 3, 2, 1, 1] (descending)
sorted_nums = sorted(numbers)                # Returns new sorted list (original unchanged)
numbers.reverse()                            # Reverse in place

# Copy
shallow = numbers.copy()                     # Shallow copy
shallow2 = numbers[:]                        # Another way to shallow copy
import copy
deep = copy.deepcopy(nested_list)            # Deep copy (for nested lists)


# --- List Operations ---
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2                     # [1, 2, 3, 4, 5, 6]

# Repetition
repeated = list1 * 3                         # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Membership
2 in list1                                   # True
7 not in list1                               # True

# Length
len(list1)                                   # 3

# Min, Max, Sum (for numeric lists)
min([3, 1, 4])                               # 1
max([3, 1, 4])                               # 4
sum([3, 1, 4])                               # 8


# --- Iterating Through Lists ---
fruits = ["apple", "banana", "cherry"]

# Basic loop
for fruit in fruits:
    print(fruit)

# With index using enumerate
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# With index starting from 1
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")


# --- Nested Lists (2D Lists / Matrix) ---
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access elements
matrix[0][0]                                 # 1 (first row, first column)
matrix[1][2]                                 # 6 (second row, third column)
matrix[-1][-1]                               # 9 (last row, last column)

# Iterate through 2D list
for row in matrix:
    for element in row:
        print(element, end=" ")


# --- List Unpacking ---
a, b, c = [1, 2, 3]                          # a=1, b=2, c=3
first, *middle, last = [1, 2, 3, 4, 5]       # first=1, middle=[2,3,4], last=5
*head, tail = [1, 2, 3]                      # head=[1,2], tail=3


# --- Common List Patterns ---

# Filter list
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]  # [2, 4, 6]

# Transform list
squared = [x**2 for x in numbers]            # [1, 4, 9, 16, 25, 36]

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]  # [1, 2, 3, 4, 5, 6]

# Remove duplicates (preserves order)
items = [1, 2, 2, 3, 3, 3, 4]
unique = []
[unique.append(x) for x in items if x not in unique]  # [1, 2, 3, 4]

# Or use dict (Python 3.7+ preserves insertion order)
unique = list(dict.fromkeys(items))          # [1, 2, 3, 4]


# =============================================================================
# TUPLES
# =============================================================================
'''
Tuples are ordered, immutable (unchangeable) collections.
- Allow duplicate elements
- Indexed starting at 0
- Faster than lists (because immutable)
- Can be used as dictionary keys (lists cannot)
- Use less memory than lists
'''

# --- Creating Tuples ---
empty_tuple = ()
empty_tuple2 = tuple()

single = (5,)                                # Note: comma needed for single element
single2 = 5,                                 # Parentheses optional

numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)
without_parens = 1, 2, 3                     # Valid tuple (parentheses optional)

nested = ((1, 2), (3, 4), (5, 6))

# Convert from other iterables
from_list = tuple([1, 2, 3])                 # (1, 2, 3)
from_string = tuple("abc")                   # ('a', 'b', 'c')


# --- Accessing Elements ---
fruits = ("apple", "banana", "cherry", "date")

# Indexing (same as lists)
first = fruits[0]                            # "apple"
last = fruits[-1]                            # "date"

# Slicing (same as lists)
fruits[1:3]                                  # ('banana', 'cherry')
fruits[:2]                                   # ('apple', 'banana')
fruits[::2]                                  # ('apple', 'cherry')
fruits[::-1]                                 # Reverse tuple


# --- Tuple Operations ---
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined = tuple1 + tuple2                   # (1, 2, 3, 4, 5, 6)

# Repetition
repeated = tuple1 * 3                        # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Membership
2 in tuple1                                  # True
7 not in tuple1                              # True

# Length
len(tuple1)                                  # 3


# --- Tuple Methods ---
numbers = (1, 2, 3, 2, 4, 2, 5)

numbers.count(2)                             # 3 (count occurrences)
numbers.index(4)                             # 4 (first index of value)


# --- Tuple Unpacking ---
# Very commonly used in Python!
x, y, z = (1, 2, 3)                          # x=1, y=2, z=3
a, b = b, a                                  # Swap without temp variable

# With * operator
first, *rest = (1, 2, 3, 4, 5)               # first=1, rest=[2,3,4,5]
*start, last = (1, 2, 3, 4, 5)               # start=[1,2,3,4], last=5

# In functions (return multiple values)
def get_coordinates():
    return (10, 20)                          # Returns tuple

x, y = get_coordinates()                     # Unpack return values


# --- Why Use Tuples? ---
# 1. Immutability guarantees data won't change
config = ("localhost", 8080, "admin")        # Server configuration

# 2. Tuples as dictionary keys (lists can't be keys)
locations = {
    (0, 0): "origin",
    (1, 2): "point A",
    (3, 4): "point B"
}

# 3. Faster than lists for fixed data
coordinates = (40.7128, -74.0060)            # NYC coordinates

# 4. Unpacking in loops
points = [(1, 2), (3, 4), (5, 6)]
for x, y in points:
    print(f"x={x}, y={y}")


# --- Modifying Tuples (Workaround) ---
# Tuples are immutable, but you can convert to list, modify, then convert back
my_tuple = (1, 2, 3)
my_list = list(my_tuple)                     # Convert to list
my_list.append(4)                            # Modify
my_tuple = tuple(my_list)                    # Convert back to tuple → (1, 2, 3, 4)

# Or create new tuple
my_tuple = (1, 2, 3)
my_tuple = my_tuple + (4, 5)                 # (1, 2, 3, 4, 5)


# =============================================================================
# DICTIONARIES
# =============================================================================
'''
Dictionaries are unordered (Python 3.7+ maintains insertion order), mutable collections of key-value pairs.
- Keys must be immutable (strings, numbers, tuples)
- Keys must be unique
- Values can be any type and can duplicate
- Fast lookup by key (O(1) average)
'''

# --- Creating Dictionaries ---
empty_dict = {}
empty_dict2 = dict()

# Direct creation
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Using dict() constructor 
person2 = dict(name="Jane", age=25, city="Boston")

# From list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
my_dict = dict(pairs)                        # {'a': 1, 'b': 2, 'c': 3}

# From two lists using zip
keys = ["name", "age", "city"]
values = ["Alice", 28, "Chicago"]
person3 = dict(zip(keys, values))

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}        # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
filtered = {k: v for k, v in squares.items() if v > 5}  # {3: 9, 4: 16}


# --- Accessing Values ---
person = {"name": "John", "age": 30, "city": "New York"}

# Using key
name = person["name"]                        # "John" (raises KeyError if key doesn't exist)

# Using get() method (safer)
age = person.get("age")                      # 30
country = person.get("country")              # None (returns None if key doesn't exist)
country = person.get("country", "USA")       # "USA" (returns default value)


# --- Modifying Dictionaries ---
person = {"name": "John", "age": 30}

# Add/Update single key
person["city"] = "New York"                  # Add new key
person["age"] = 31                           # Update existing key

# Update multiple keys
person.update({"age": 32, "job": "Engineer"})
person.update(name="Johnny", city="Boston")  # Keyword arguments

# Add key only if it doesn't exist
person.setdefault("country", "USA")          # Adds only if "country" doesn't exist
person.setdefault("name", "Default")         # Doesn't change existing "name"


# --- Removing Items ---
person = {"name": "John", "age": 30, "city": "New York", "job": "Engineer"}

# Remove specific key
del person["job"]                            # Remove "job" (raises KeyError if not found)
age = person.pop("age")                      # Remove and return value (30)
age = person.pop("age", None)                # Returns None if key doesn't exist (no error)

# Remove and return last inserted item (Python 3.7+)
item = person.popitem()                      # Returns tuple: ('city', 'New York')

# Clear all items
person.clear()                               # {} (empty dict)


# --- Dictionary Methods ---
person = {"name": "John", "age": 30, "city": "New York"}

# Get all keys
keys = person.keys()                         # dict_keys(['name', 'age', 'city'])
key_list = list(person.keys())               # Convert to list

# Get all values
values = person.values()                     # dict_values(['John', 30, 'New York'])
value_list = list(person.values())

# Get all key-value pairs
items = person.items()                       # dict_items([('name', 'John'), ('age', 30), ...])
item_list = list(person.items())

# Check if key exists
"name" in person                             # True
"job" not in person                          # True

# Copy dictionary
shallow = person.copy()                      # Shallow copy
import copy
deep = copy.deepcopy(nested_dict)            # Deep copy (for nested dicts)


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

# Iterate through key-value pairs (most common)
for key, value in person.items():
    print(f"{key}: {value}")


# --- Nested Dictionaries ---
students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "grades": [85, 90, 92]
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "grades": [78, 88, 85]
    }
}

# Access nested values
alice_name = students["student1"]["name"]              # "Alice"
alice_grades = students["student1"]["grades"][0]       # 85

# Iterate through nested dict
for student_id, info in students.items():
    print(f"{student_id}: {info['name']}, Age: {info['age']}")


# --- Dictionary with Default Values ---
from collections import defaultdict

# Regular dict - KeyError if key doesn't exist
# regular = {}
# regular["key"] += 1  # KeyError

# defaultdict - provides default value
counts = defaultdict(int)                    # Default value is 0 for int
counts["apple"] += 1                         # Works! counts["apple"] = 1

word_lists = defaultdict(list)               # Default value is [] for list
word_lists["fruits"].append("apple")         # Works!


# --- Merging Dictionaries ---
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"b": 5, "e": 6}                     # Has overlapping key "b"

# Method 1: update() (modifies dict1)
dict1.update(dict2)                          # dict1 now has all keys from dict2

# Method 2: unpacking (Python 3.5+)
merged = {**dict1, **dict2, **dict3}         # Later dicts override earlier ones

# Method 3: union operator (Python 3.9+)
merged = dict1 | dict2 | dict3               # dict3["b"] overwrites dict1["b"]


# --- Common Dictionary Patterns ---

# Count occurrences
text = "hello world"
counts = {}
for char in text:
    counts[char] = counts.get(char, 0) + 1
# Or use Counter
from collections import Counter
counts = Counter(text)                       # Counter({'l': 3, 'o': 2, ...})

# Group items
students = [("Alice", "A"), ("Bob", "B"), ("Charlie", "A"), ("David", "B")]
by_grade = {}
for name, grade in students:
    by_grade.setdefault(grade, []).append(name)
# Result: {'A': ['Alice', 'Charlie'], 'B': ['Bob', 'David']}

# Invert dictionary (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}  # {1: 'a', 2: 'b', 3: 'c'}

# Filter dictionary
numbers = {"a": 1, "b": 2, "c": 3, "d": 4}
evens = {k: v for k, v in numbers.items() if v % 2 == 0}  # {'b': 2, 'd': 4}

# Sort dictionary by key
sorted_dict = dict(sorted(person.items()))

# Sort dictionary by value
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
sorted_by_score = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
# {'Bob': 92, 'Alice': 85, 'Charlie': 78}


# =============================================================================
# COMPARISON: LIST vs TUPLE vs DICTIONARY
# =============================================================================
'''
╔════════════════╦═══════════╦═══════════╦═══════════════╗
║   Feature      ║   List    ║   Tuple   ║  Dictionary   ║
╠════════════════╬═══════════╬═══════════╬═══════════════╣
║ Ordered        ║    Yes    ║    Yes    ║  Yes (3.7+)   ║
║                ║           ║           ║               ║
║ Mutable        ║    Yes    ║    No     ║     Yes       ║
║                ║           ║           ║               ║
║ Indexed        ║    Yes    ║    Yes    ║     No        ║
║                ║           ║           ║               ║
║ Duplicates     ║    Yes    ║    Yes    ║  Keys: No     ║
║                ║           ║           ║  Values: Yes  ║
║                ║           ║           ║               ║
║ Syntax         ║    []     ║    ()     ║     {}        ║
║                ║           ║           ║               ║
║ Access         ║  By index ║  By index ║   By key      ║
║                ║           ║           ║               ║
║ Speed          ║  Medium   ║   Fast    ║   Fastest     ║
║                ║           ║           ║               ║
║ Use Case       ║ Dynamic   ║  Fixed    ║  Key-value    ║
║                ║           ║           ║               ║
║                ║collection ║  data     ║   mapping     ║
║                ║           ║           ║               ║
╚════════════════╩═══════════╩═══════════╩═══════════════╝
'''


# =============================================================================
# Key Takeaways
# =============================================================================

'''
LISTS:
✓ Use when you need ordered, changeable collection
✓ Best for collections that grow/shrink dynamically
✓ Methods: append(), extend(), insert(), remove(), pop(), sort(), reverse()

TUPLES:
✓ Use when data shouldn't change (immutable)
✓ Faster and use less memory than lists
✓ Can be dictionary keys (lists cannot)
✓ Great for returning multiple values from functions

DICTIONARIES:
✓ Use for key-value relationships
✓ Fast lookup by key (O(1) average complexity)
✓ Keys must be immutable (str, int, tuple)
✓ Python 3.7+ maintains insertion order

CHOOSING:
- Need order + changes? → List
- Need order + no changes? → Tuple
- Need key-value lookup? → Dictionary
- Need unique values? → Set (covered in advanced topics)
'''
