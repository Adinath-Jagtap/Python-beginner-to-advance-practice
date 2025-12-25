'''
DAY 1: Python Basics - Variables, Data Types, Operators
''' 

# ===========================================================================
# VARIABLES
# ===========================================================================
'''
Variables are names that refer to values stored in memory.
Python uses dynamic typing - no need to declare types explicitly.

Naming Rules:
- Must start with letter (a-z, A-Z) or underscore (_)
- Can contain letters, digits (0-9), and underscores
- Case-sensitive (age, Age, AGE are different)
- Cannot use Python keywords (if, for, while, etc.)
- Use snake_case for variable names (PEP 8 convention)
'''

# Basic assignment
x = 10
y = 5
name = "Adinath"
is_valid = True          # Boolean declaration
PI = 3.14159             # UPPERCASE for constants (convention)

# Multiple assignment
a, b, c = 1, 2, 3        # Parallel assignment

# Swapping values
x, y = y, x              # Pythonic swap (no temp variable needed)

# Same value to multiple variables
p = q = r = 0

# Deleting variables
del x                    # Removes variable from memory


# =============================================================================
# DATA TYPES
# =============================================================================

# --- Numeric Types ---
integer = 42             # int: whole numbers (unlimited precision)
negative = -15           # int: can be negative
floating = 3.14          # float: decimal numbers
scientific = 2.5e3       # float: 2500.0 (scientific notation)
complex_num = 3 + 4j     # complex: real + imaginary

# --- Boolean Type ---
is_active = True         # bool: True or False (capitalized)
is_empty = False

# --- String Type ---
single = 'Hello'         # str: single quotes
double = "World"         # str: double quotes
multi = '''Multiple
lines'''                 # str: triple quotes for multiline
raw = r"C:\new\path"     # str: raw string (ignores escape chars)

# --- None Type ---
result = None            # NoneType: represents absence of value

# --- Sequence Types ---
my_list = [1, 2, 3, "mixed", True]       # list: ordered, mutable
my_tuple = (1, 2, 3)                     # tuple: ordered, immutable
my_tuple2 = 1, 2, 3                      # tuple: parentheses optional
single_tuple = (5,)                      # tuple: comma needed for single item
my_range = range(5)                      # range: 0,1,2,3,4 (immutable sequence)

# --- Set Types ---
my_set = {1, 2, 3, 3}                    # set: unordered, unique values → {1,2,3}
empty_set = set()                        # set: empty (NOT {}, that's dict)
frozen = frozenset([1, 2])               # frozenset: immutable set

# --- Mapping Type ---
my_dict = {'name': 'John', 'age': 25}    # dict: key-value pairs
empty_dict = {}                          # dict: empty dictionary

# --- Binary Types ---
byte_data = b"hello"                     # bytes: immutable byte sequence
byte_arr = bytearray(b"hello")           # bytearray: mutable byte sequence
mem_view = memoryview(bytes(5))          # memoryview: memory buffer interface


# =============================================================================
# TYPE CHECKING & CONVERSION
# =============================================================================

# Check type
print(type(123))         # <class 'int'>
print(type([1, 2]))      # <class 'list'>
print(type(3.14))        # <class 'float'>

# Check instance
print(isinstance(42, int))              # True
print(isinstance("hi", (int, str)))     # True (checks multiple types)

# Type conversion (casting)
int("42")                # 42 (string → int)
int(3.9)                 # 3 (float → int, truncates)
int("1010", 2)           # 10 (binary string → int)

float("3.5")             # 3.5 (string → float)
float(5)                 # 5.0 (int → float)

str(100)                 # "100" (int → string)
str(3.14)                # "3.14" (float → string)

bool(0)                  # False (0, "", [], {}, None are falsy)
bool(1)                  # True (non-zero numbers are truthy)
bool([])                 # False (empty collections are falsy)
bool([1])                # True (non-empty collections are truthy)

list((1, 2, 3))          # [1, 2, 3] (tuple → list)
list("abc")              # ['a', 'b', 'c'] (string → list)

tuple([1, 2, 3])         # (1, 2, 3) (list → tuple)

set([1, 2, 2, 3])        # {1, 2, 3} (list → set, removes duplicates)

dict([('a', 1), ('b', 2)])  # {'a': 1, 'b': 2} (list of tuples → dict)


# =============================================================================
# OPERATORS
# =============================================================================

# --- Arithmetic Operators ---
5 + 2                    # 7    Addition
5 - 2                    # 3    Subtraction
5 * 2                    # 10   Multiplication
5 / 2                    # 2.5  Division (always returns float)
5 // 2                   # 2    Floor division (rounds down)
5 % 2                    # 1    Modulus (remainder)
2 ** 3                   # 8    Exponentiation (power)
-5                       # -5   Unary negation
+5                       # 5    Unary plus

# String/list operations
"Hi" + " there"          # "Hi there"  (concatenation)
"Ha" * 3                 # "HaHaHa"    (repetition)
[1, 2] + [3, 4]          # [1, 2, 3, 4] (list concatenation)


# --- Assignment Operators ---
x = 5                    # Assignment
x += 3                   # x = x + 3  → 8
x -= 2                   # x = x - 2  → 6
x *= 2                   # x = x * 2  → 12
x /= 4                   # x = x / 4  → 3.0
x //= 2                  # x = x // 2 → 1
x %= 2                   # x = x % 2  → 1
x **= 3                  # x = x ** 3 → 1

# Walrus operator (Python 3.8+)
if (n := len([1, 2, 3])) > 2:  # Assign and check in one line
    print(f"Length is {n}")


# --- Comparison Operators ---
3 == 3                   # True   Equal to
3 != 4                   # True   Not equal to
5 > 3                    # True   Greater than
5 < 10                   # True   Less than
5 >= 5                   # True   Greater than or equal to
5 <= 4                   # False  Less than or equal to

# Chaining comparisons
1 < x <= 10              # True if x is between 1 and 10 (inclusive)
x == y == z              # True if all three are equal


# --- Logical Operators ---
True and False           # False  (both must be True)
True or False            # True   (at least one must be True)
not True                 # False  (inverts boolean)

# Short-circuit evaluation
x > 0 and x < 10         # Second check only if first is True
x == 0 or y == 0         # Second check only if first is False

# Combining conditions
(x > 0) and (y > 0) and (x + y < 100)


# --- Bitwise Operators (work on binary representation) ---
5 & 3                    # 1    AND  (0101 & 0011 = 0001)
5 | 3                    # 7    OR   (0101 | 0011 = 0111)
5 ^ 3                    # 6    XOR  (0101 ^ 0011 = 0110)
~5                       # -6   NOT  (inverts bits)
5 << 1                   # 10   Left shift  (multiply by 2)
5 >> 1                   # 2    Right shift (divide by 2)


# --- Membership Operators ---
"p" in "python"          # True   (substring check)
"x" not in "python"      # True   (not present)
3 in [1, 2, 3]           # True   (element in list)
'a' in {'a': 1, 'b': 2}  # True   (key in dictionary)


# --- Identity Operators ---
# Check if two variables refer to the SAME object in memory (not just equal values)
a = [1, 2]
b = a                    # b points to same list as a
c = [1, 2]               # c is a new list with same values

a is b                   # True  (same object)
a is c                   # False (different objects)
a == c                   # True  (equal values)
a is not c               # True  (different objects)

# Common use with None
x = None
x is None                # True  (recommended way to check for None)
x == None                # True  (works but 'is' is preferred)


# --- Operator Precedence (highest to lowest) ---
'''
1. ()                    Parentheses
2. **                    Exponentiation
3. +x, -x, ~x            Unary plus, minus, bitwise NOT
4. *, /, //, %           Multiplication, division, floor division, modulo
5. +, -                  Addition, subtraction
6. <<, >>                Bitwise shifts
7. &                     Bitwise AND
8. ^                     Bitwise XOR
9. |                     Bitwise OR
10. ==, !=, >, <, >=, <= Comparisons
11. is, is not           Identity
12. in, not in           Membership
13. not                  Logical NOT
14. and                  Logical AND
15. or                   Logical OR
'''

# Example of precedence
result = 2 + 3 * 4       # 14 (not 20, because * has higher precedence)
result = (2 + 3) * 4     # 20 (parentheses override precedence)


# =============================================================================
# Key Takeaways
# =============================================================================

'''
1. Python uses dynamic typing - types are determined at runtime
2. Everything in Python is an object
3. Use meaningful variable names (snake_case convention)
4. Understand mutability: lists/dicts are mutable, tuples/strings are immutable
5. Remember operator precedence or use parentheses for clarity
6. Use 'is' for None checks, '==' for value comparisons
7. Boolean context: 0, None, "", [], {}, () are all falsy
'''
