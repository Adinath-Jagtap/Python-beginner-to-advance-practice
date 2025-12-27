'''
DAY 5: Python String Methods & Manipulation
'''

# =============================================================================
# STRING BASICS
# =============================================================================
'''
Strings are immutable sequences of characters.
- Enclosed in single (''), double (""), or triple (''' ''' or """ """) quotes
- Immutable: cannot be changed after creation
- Indexed starting at 0
- Support slicing and iteration
'''

# --- Creating Strings ---
single = 'Hello'
double = "World"
triple_single = '''Multiple
lines
text'''
triple_double = """Another
multiline
string"""

# Empty string
empty = ""
empty2 = str()

# String from other types
num_str = str(123)                   # "123"
bool_str = str(True)                 # "True"
list_str = str([1, 2, 3])           # "[1, 2, 3]"


# --- String Indexing ---
text = "Python"

# Positive indexing (left to right)
print(text[0])                       # 'P' (first character)
print(text[1])                       # 'y'
print(text[5])                       # 'n' (last character)

# Negative indexing (right to left)
print(text[-1])                      # 'n' (last character)
print(text[-2])                      # 'o' (second last)
print(text[-6])                      # 'P' (first character)


# --- String Slicing ---
text = "Python Programming"

# Basic slicing: string[start:stop:step]
print(text[0:6])                     # 'Python' (0 to 5)
print(text[:6])                      # 'Python' (start defaults to 0)
print(text[7:])                      # 'Programming' (stop defaults to end)
print(text[:])                       # 'Python Programming' (full copy)

# Step in slicing
print(text[::2])                     # 'Pto rgamn' (every 2nd character)
print(text[::3])                     # 'Ph ormn' (every 3rd character)
print(text[::-1])                    # 'gnimmargorP nohtyP' (reverse)

# Negative indices in slicing
print(text[-11:-1])                  # 'Programmin' (from -11 to -2)
print(text[7:-1])                    # 'Programmin' (mixed indices)


# --- String Concatenation ---
first = "Hello"
last = "World"

# Using + operator
combined = first + " " + last        # "Hello World"

# Using += operator
greeting = "Hello"
greeting += " World"                 # "Hello World"

# Using join() (more efficient for multiple strings)
words = ["Hello", "World", "Python"]
sentence = " ".join(words)           # "Hello World Python"


# --- String Repetition ---
text = "Ha"
repeated = text * 3                  # "HaHaHa"

separator = "-" * 20                 # "--------------------"


# =============================================================================
# STRING METHODS - CASE CONVERSION
# =============================================================================

text = "Hello World"

# Convert to uppercase
print(text.upper())                  # "HELLO WORLD"

# Convert to lowercase
print(text.lower())                  # "hello world"

# Capitalize first letter
print(text.capitalize())             # "Hello world"

# Title case (capitalize each word)
print(text.title())                  # "Hello World"

# Swap case
print(text.swapcase())               # "hELLO wORLD"

# Case folding (aggressive lowercase for comparison)
print(text.casefold())               # "hello world"
print("ß".casefold())                # "ss" (German ß becomes ss)


# =============================================================================
# STRING METHODS - SEARCHING & CHECKING
# =============================================================================

text = "Python Programming Language"

# Find substring (returns index or -1)
print(text.find("Programming"))      # 7 (starting index)
print(text.find("Java"))             # -1 (not found)
print(text.find("o"))                # 4 (first occurrence)
print(text.find("o", 5))             # 8 (search from index 5)

# Right find (search from right)
print(text.rfind("o"))               # 8 (last occurrence)

# Index (like find but raises error if not found)
print(text.index("Programming"))     # 7
# print(text.index("Java"))          # ValueError

# Check if string starts with
print(text.startswith("Python"))     # True
print(text.startswith("Java"))       # False
print(text.startswith("Prog", 7))    # True (check from index 7)

# Check if string ends with
print(text.endswith("Language"))     # True
print(text.endswith("guage"))        # True
print(text.endswith("Python"))       # False

# Count occurrences
print(text.count("a"))               # 4 (count 'a' in string)
print(text.count("o"))               # 2
print(text.count("th"))              # 1

# Check if substring is in string
print("Python" in text)              # True
print("Java" in text)                # False
print("Python" not in text)          # False


# =============================================================================
# STRING METHODS - CHECKING STRING TYPES
# =============================================================================

# Check if all characters are alphabetic
print("Python".isalpha())            # True
print("Python3".isalpha())           # False (has digit)
print("Hello World".isalpha())       # False (has space)

# Check if all characters are digits
print("12345".isdigit())             # True
print("123.45".isdigit())            # False (has decimal point)
print("12a34".isdigit())             # False (has letter)

# Check if all characters are alphanumeric
print("Python3".isalnum())           # True
print("Python 3".isalnum())          # False (has space)
print("Hello123".isalnum())          # True

# Check if all characters are numeric
print("12345".isnumeric())           # True
print("½".isnumeric())               # True (fraction)
print("12.34".isnumeric())           # False

# Check if all characters are decimal
print("12345".isdecimal())           # True
print("½".isdecimal())               # False

# Check if all characters are whitespace
print("   ".isspace())               # True
print(" \t\n ".isspace())            # True (space, tab, newline)
print("  a  ".isspace())             # False (has letter)

# Check if string is title case
print("Hello World".istitle())       # True
print("Hello world".istitle())       # False
print("HELLO WORLD".istitle())       # False

# Check if string is uppercase
print("HELLO".isupper())             # True
print("Hello".isupper())             # False

# Check if string is lowercase
print("hello".islower())             # True
print("Hello".islower())             # False

# Check if string is identifier (valid variable name)
print("variable_name".isidentifier()) # True
print("2variable".isidentifier())    # False (starts with digit)
print("my-var".isidentifier())       # False (has hyphen)

# Check if string is printable
print("Hello".isprintable())         # True
print("Hello\n".isprintable())       # False (has newline)


# =============================================================================
# STRING METHODS - TRIMMING & PADDING
# =============================================================================

text = "   Hello World   "

# Remove leading and trailing whitespace
print(text.strip())                  # "Hello World"
print(text.lstrip())                 # "Hello World   " (left strip)
print(text.rstrip())                 # "   Hello World" (right strip)

# Remove specific characters
text2 = "***Hello***"
print(text2.strip("*"))              # "Hello"

text3 = "www.example.com"
print(text3.strip("cmowz."))         # "example"

# Left justify (pad right)
print("Hello".ljust(10))             # "Hello     "
print("Hello".ljust(10, "-"))        # "Hello-----"

# Right justify (pad left)
print("Hello".rjust(10))             # "     Hello"
print("Hello".rjust(10, "-"))        # "-----Hello"

# Center justify
print("Hello".center(10))            # "  Hello   "
print("Hello".center(10, "-"))       # "--Hello---"

# Zero fill (pad with zeros)
print("42".zfill(5))                 # "00042"
print("-42".zfill(5))                # "-0042"
print("123".zfill(2))                # "123" (no change if already longer)


# =============================================================================
# STRING METHODS - SPLITTING & JOINING
# =============================================================================

text = "Python,Java,JavaScript,Ruby"

# Split by delimiter
words = text.split(",")              # ['Python', 'Java', 'JavaScript', 'Ruby']
print(words)

# Split by whitespace (default)
sentence = "Hello World Python"
words = sentence.split()             # ['Hello', 'World', 'Python']

# Split with max splits
text2 = "a,b,c,d,e"
parts = text2.split(",", 2)          # ['a', 'b', 'c,d,e'] (max 2 splits)

# Right split (split from right)
parts = text2.rsplit(",", 2)         # ['a,b,c', 'd', 'e']

# Split lines
multiline = "Line 1\nLine 2\nLine 3"
lines = multiline.splitlines()       # ['Line 1', 'Line 2', 'Line 3']

# Split lines keeping line breaks
lines = multiline.splitlines(True)   # ['Line 1\n', 'Line 2\n', 'Line 3']

# Partition (split into 3 parts)
text3 = "Hello-World-Python"
parts = text3.partition("-")         # ('Hello', '-', 'World-Python')

# Right partition
parts = text3.rpartition("-")        # ('Hello-World', '-', 'Python')

# Join list elements
words = ["Hello", "World", "Python"]
sentence = " ".join(words)           # "Hello World Python"
comma_sep = ",".join(words)          # "Hello,World,Python"
dash_sep = "-".join(words)           # "Hello-World-Python"

# Join with empty string
chars = ['P', 'y', 't', 'h', 'o', 'n']
word = "".join(chars)                # "Python"


# =============================================================================
# STRING METHODS - REPLACING & REMOVING
# =============================================================================

text = "Hello World World"

# Replace substring
new_text = text.replace("World", "Python")  # "Hello Python Python"
print(new_text)

# Replace with count limit
new_text = text.replace("World", "Python", 1)  # "Hello Python World"

# Remove substring (replace with empty string)
text2 = "Python Programming"
cleaned = text2.replace(" ", "")     # "PythonProgramming"

# Replace multiple spaces with single space
text3 = "Hello    World"
cleaned = " ".join(text3.split())    # "Hello World"

# Translate (replace multiple characters)
text4 = "Hello World"
translation = str.maketrans("elo", "310")
translated = text4.translate(translation)  # "H3ll0 W0rld"

# Remove characters using translate
remove_chars = str.maketrans("", "", "aeiou")
text5 = "Hello World"
no_vowels = text5.translate(remove_chars)  # "Hll Wrld"

# Expand tabs
text6 = "Name\tAge\tCity"
expanded = text6.expandtabs(4)       # "Name    Age    City" (tab size 4)
expanded = text6.expandtabs(10)      # "Name      Age       City" (tab size 10)


# =============================================================================
# STRING FORMATTING
# =============================================================================

# --- Old Style (%) Formatting ---
name = "Alice"
age = 25

# String substitution
print("Hello, %s!" % name)           # "Hello, Alice!"

# Multiple substitutions
print("Name: %s, Age: %d" % (name, age))  # "Name: Alice, Age: 25"

# Format specifiers
print("Price: $%.2f" % 19.99)        # "Price: $19.99" (2 decimal places)
print("Number: %05d" % 42)           # "Number: 00042" (pad with zeros)


# --- str.format() Method ---
name = "Alice"
age = 25

# Positional arguments
print("Hello, {}!".format(name))     # "Hello, Alice!"
print("{} is {} years old".format(name, age))  # "Alice is 25 years old"

# Indexed arguments
print("{0} is {1} years old. {0} lives in NYC".format(name, age))

# Named arguments
print("{name} is {age} years old".format(name="Bob", age=30))

# Formatting numbers
print("Price: ${:.2f}".format(19.99))       # "Price: $19.99"
print("Number: {:05d}".format(42))          # "Number: 00042"
print("Percent: {:.1%}".format(0.856))      # "Percent: 85.6%"

# Alignment
print("{:<10}".format("left"))              # "left      "
print("{:>10}".format("right"))             # "     right"
print("{:^10}".format("center"))            # "  center  "

# With fill character
print("{:*<10}".format("left"))             # "left******"
print("{:*>10}".format("right"))            # "*****right"
print("{:*^10}".format("center"))           # "**center**"


# --- f-strings (Python 3.6+) - RECOMMENDED ---
name = "Alice"
age = 25
price = 19.99

# Basic usage
print(f"Hello, {name}!")                    # "Hello, Alice!"
print(f"{name} is {age} years old")         # "Alice is 25 years old"

# Expressions inside f-strings
print(f"Next year: {age + 1}")              # "Next year: 26"
print(f"Double price: {price * 2}")         # "Double price: 39.98"

# Formatting numbers
print(f"Price: ${price:.2f}")               # "Price: $19.99"
print(f"Number: {42:05d}")                  # "Number: 00042"
print(f"Percent: {0.856:.1%}")              # "Percent: 85.6%"

# Alignment
print(f"{'left':<10}")                      # "left      "
print(f"{'right':>10}")                     # "     right"
print(f"{'center':^10}")                    # "  center  "

# With fill character
print(f"{'left':*<10}")                     # "left******"
print(f"{'right':*>10}")                    # "*****right"
print(f"{'center':*^10}")                   # "**center**"

# Calling methods
name = "alice"
print(f"Name: {name.upper()}")              # "Name: ALICE"

# Dictionary access
person = {"name": "Bob", "age": 30}
print(f"{person['name']} is {person['age']} years old")

# Date formatting
from datetime import datetime
now = datetime.now()
print(f"Date: {now:%Y-%m-%d}")              # "Date: 2025-12-27"
print(f"Time: {now:%H:%M:%S}")              # "Time: 14:30:45"

# Debug mode (Python 3.8+)
x = 10
y = 20
print(f"{x=}, {y=}")                        # "x=10, y=20"
print(f"{x + y=}")                          # "x + y=30"


# =============================================================================
# STRING ENCODING & DECODING
# =============================================================================

text = "Hello World"

# Encode string to bytes
encoded = text.encode()                     # b'Hello World' (default UTF-8)
encoded_utf8 = text.encode("utf-8")         # b'Hello World'
encoded_ascii = text.encode("ascii")        # b'Hello World'

# Decode bytes to string
decoded = encoded.decode()                  # "Hello World"
decoded_utf8 = encoded_utf8.decode("utf-8") # "Hello World"

# Handle encoding errors
text_with_special = "Café"
# encoded_ascii = text_with_special.encode("ascii")  # Error!
encoded_ignore = text_with_special.encode("ascii", errors="ignore")    # b'Caf'
encoded_replace = text_with_special.encode("ascii", errors="replace")  # b'Caf?'


# =============================================================================
# ESCAPE SEQUENCES
# =============================================================================

# Newline
print("Hello\nWorld")                # Hello
                                     # World

# Tab
print("Name:\tAlice")                # Name:    Alice

# Backslash
print("C:\\Users\\Documents")        # C:\Users\Documents

# Single quote
print('It\'s a beautiful day')       # It's a beautiful day

# Double quote
print("She said \"Hello\"")          # She said "Hello"

# Carriage return
print("Hello\rWorld")                # World (overwrites Hello)

# Backspace
print("Hello\bWorld")                # HellWorld

# Unicode character
print("\u0041")                      # A (Unicode for 'A')
print("\u03B1")                      # α (Greek alpha)

# Raw strings (ignore escape sequences)
print(r"C:\Users\new\test")          # C:\Users\new\test (no escape)
print(r"Hello\nWorld")               # Hello\nWorld (literal \n)


# =============================================================================
# STRING COMPARISON
# =============================================================================

# Equality comparison
print("hello" == "hello")            # True
print("hello" == "Hello")            # False (case-sensitive)

# Case-insensitive comparison
print("hello".lower() == "Hello".lower())  # True

# Lexicographic comparison
print("apple" < "banana")            # True
print("zebra" > "apple")             # True
print("abc" <= "abc")                # True

# Length comparison
print(len("hello") == len("world"))  # True (both 5)


# =============================================================================
# MULTILINE STRINGS
# =============================================================================

# Triple quotes for multiline
multiline = """
This is a
multiline
string
"""

# Multiline with proper indentation
text = """
Line 1
Line 2
Line 3
""".strip()  # Remove leading/trailing whitespace

# Using line continuation
long_text = "This is a very long string " \
            "that spans multiple lines " \
            "in the code"

# Using parentheses (implicit concatenation)
long_text = (
    "This is another way "
    "to write long strings "
    "across multiple lines"
)


# =============================================================================
# STRING IMMUTABILITY
# =============================================================================

# Strings are immutable (cannot be changed)
text = "Hello"
# text[0] = "h"  # TypeError: 'str' object does not support item assignment

# Create new string instead
text = "hello"  # Reassign variable

# Modify by creating new string
text = "Hello"
new_text = "h" + text[1:]  # "hello"

# Another way
text = "Hello"
text_list = list(text)  # ['H', 'e', 'l', 'l', 'o']
text_list[0] = 'h'
new_text = "".join(text_list)  # "hello"


# =============================================================================
# STRING MEMORY & PERFORMANCE
# =============================================================================

# String interning (Python optimizes small strings)
a = "hello"
b = "hello"
print(a is b)  # True (same object in memory)

# Larger strings may not be interned
a = "hello" * 1000
b = "hello" * 1000
print(a is b)  # May be False (different objects)

# Efficient string concatenation
# BAD: Using + in loop (creates new string each time)
result = ""
for i in range(1000):
    result += str(i)  # Slow!

# GOOD: Using join (much faster)
result = "".join(str(i) for i in range(1000))

# GOOD: Using list and join
parts = []
for i in range(1000):
    parts.append(str(i))
result = "".join(parts)


# =============================================================================
# USEFUL STRING OPERATIONS
# =============================================================================

# Check if string is empty
text = ""
if not text:  # Pythonic way
    print("Empty string")

if len(text) == 0:  # Also works
    print("Empty string")

# Get string length
text = "Python"
length = len(text)  # 6

# Iterate through string
for char in "Python":
    print(char)

# Iterate with index
for i, char in enumerate("Python"):
    print(f"{i}: {char}")

# Reverse string
text = "Python"
reversed_text = text[::-1]  # "nohtyP"
reversed_text = "".join(reversed(text))  # "nohtyP"

# Check palindrome
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print(is_palindrome("A man a plan a canal Panama"))  # True

# Remove whitespace from string
text = "  Hello   World  "
cleaned = text.strip()  # "Hello   World"
cleaned = " ".join(text.split())  # "Hello World"

# Repeat string
print("=" * 50)  # 50 equal signs

# String to list of characters
text = "Python"
chars = list(text)  # ['P', 'y', 't', 'h', 'o', 'n']

# List of characters to string
chars = ['P', 'y', 't', 'h', 'o', 'n']
text = "".join(chars)  # "Python"


# =============================================================================
# COMMON STRING PATTERNS
# =============================================================================

# Title case a sentence
sentence = "hello world python"
title = sentence.title()  # "Hello World Python"

# Count words in sentence
sentence = "Hello World Python Programming"
word_count = len(sentence.split())  # 4

# Get first/last word
words = sentence.split()
first_word = words[0]  # "Hello"
last_word = words[-1]  # "Programming"

# Capitalize first letter only
text = "hello world"
capitalized = text[0].upper() + text[1:]  # "Hello world"

# Remove punctuation
import string
text = "Hello, World! How are you?"
no_punct = text.translate(str.maketrans("", "", string.punctuation))
# "Hello World How are you"

# Extract numbers from string
text = "Price is $25.99 and quantity is 10"
numbers = ''.join(c for c in text if c.isdigit() or c == '.')
# "25.9910"

# Better approach for extracting numbers
import re
numbers = re.findall(r'\d+\.?\d*', text)  # ['25.99', '10']

# Truncate string with ellipsis
def truncate(text, max_length):
    if len(text) > max_length:
        return text[:max_length-3] + "..."
    return text

print(truncate("This is a very long string", 15))  # "This is a ve..."

# Word wrap
def wrap_text(text, width):
    words = text.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + len(current_line) <= width:
            current_line.append(word)
            current_length += len(word)
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_length = len(word)
    
    if current_line:
        lines.append(" ".join(current_line))
    
    return "\n".join(lines)


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
'''
STRING BASICS:
✓ Immutable sequence of characters
✓ Created with '', "", ''' ''', or """ """
✓ Indexed starting at 0
✓ Support slicing: [start:stop:step]

CASE CONVERSION:
✓ upper(), lower(), capitalize(), title(), swapcase()

SEARCHING:
✓ find(), rfind(), index(), count()
✓ startswith(), endswith(), in operator

CHECKING:
✓ isalpha(), isdigit(), isalnum(), isnumeric()
✓ isspace(), isupper(), islower(), istitle()

TRIMMING & PADDING:
✓ strip(), lstrip(), rstrip()
✓ ljust(), rjust(), center(), zfill()

SPLITTING & JOINING:
✓ split(), rsplit(), splitlines()
✓ join(), partition(), rpartition()

REPLACING:
✓ replace(), translate(), maketrans()

FORMATTING:
✓ Old style: "Hello, %s" % name
✓ format(): "Hello, {}".format(name)
✓ f-strings: f"Hello, {name}" (RECOMMENDED)

BEST PRACTICES:
- Use f-strings for formatting (Python 3.6+)
- Use join() for concatenating many strings
- Use in operator for membership testing
- Remember strings are immutable
- Use strip() to remove whitespace
- Use lower() for case-insensitive comparison
'''