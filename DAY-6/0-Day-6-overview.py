'''
DAY 6: Python File Handling & Error Handling
'''

# =============================================================================
# FILE HANDLING - BASICS
# =============================================================================
'''
File handling allows reading from and writing to files.

File Modes:
'r'  - Read (default) - Error if file doesn't exist
'w'  - Write - Creates new file or overwrites existing
'a'  - Append - Creates new file or appends to existing
'x'  - Exclusive creation - Error if file exists
'r+' - Read and Write - Error if file doesn't exist
'w+' - Write and Read - Creates new or overwrites
'a+' - Append and Read - Creates new or appends

Additional flags:
'b'  - Binary mode (rb, wb, ab)
't'  - Text mode (default) (rt, wt, at)
'''

# --- Opening and Closing Files ---

# Method 1: Manual open/close
file = open("example.txt", "r")
content = file.read()
file.close()  # Must remember to close!

# Method 2: Using with statement (RECOMMENDED)
# Automatically closes file even if error occurs
with open("example.txt", "r") as file:
    content = file.read()
    # File automatically closed after this block


# =============================================================================
# READING FILES
# =============================================================================

# --- read() - Read entire file ---
with open("example.txt", "r") as file:
    content = file.read()  # Returns entire file as string
    print(content)

# Read specific number of characters
with open("example.txt", "r") as file:
    content = file.read(10)  # Read first 10 characters
    print(content)


# --- readline() - Read one line at a time ---
with open("example.txt", "r") as file:
    line1 = file.readline()  # Read first line
    line2 = file.readline()  # Read second line
    print(line1)
    print(line2)


# --- readlines() - Read all lines into list ---
with open("example.txt", "r") as file:
    lines = file.readlines()  # Returns list of lines
    print(lines)  # ['line 1\n', 'line 2\n', 'line 3\n']


# --- Iterating through file (BEST for large files) ---
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # Process each line


# --- Reading with encoding ---
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()


# --- Check if file is readable ---
file = open("example.txt", "r")
print(file.readable())  # True
file.close()


# =============================================================================
# WRITING FILES
# =============================================================================

# --- write() - Write string to file ---
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")

# Note: write() doesn't add newline automatically
# Returns number of characters written


# --- writelines() - Write list of strings ---
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)

# Note: writelines() doesn't add newlines automatically


# --- Append mode ---
with open("output.txt", "a") as file:
    file.write("This line is appended.\n")


# --- Write mode overwrites entire file ---
with open("output.txt", "w") as file:
    file.write("Old content is gone!\n")


# --- Exclusive creation (error if exists) ---
try:
    with open("newfile.txt", "x") as file:
        file.write("File created successfully!\n")
except FileExistsError:
    print("File already exists!")


# --- Read and Write mode ---
with open("example.txt", "r+") as file:
    content = file.read()
    file.write("\nNew content added")


# --- Check if file is writable ---
file = open("output.txt", "w")
print(file.writable())  # True
file.close()


# =============================================================================
# FILE POINTER POSITION
# =============================================================================

# --- tell() - Get current position ---
with open("example.txt", "r") as file:
    print(file.tell())  # 0 (start of file)
    file.read(5)
    print(file.tell())  # 5 (after reading 5 characters)


# --- seek() - Move to specific position ---
with open("example.txt", "r") as file:
    file.seek(10)  # Move to position 10
    content = file.read()  # Read from position 10

# seek(offset, whence)
# whence: 0 = beginning, 1 = current, 2 = end
with open("example.txt", "r") as file:
    file.seek(0, 0)  # Move to beginning
    file.seek(5, 1)  # Move 5 bytes forward from current
    file.seek(-10, 2)  # Move 10 bytes back from end


# =============================================================================
# WORKING WITH DIRECTORIES
# =============================================================================

import os

# --- Check if file exists ---
if os.path.exists("example.txt"):
    print("File exists")

# Check if it's a file
if os.path.isfile("example.txt"):
    print("It's a file")

# Check if it's a directory
if os.path.isdir("myfolder"):
    print("It's a directory")


# --- Get file information ---
import os

# File size in bytes
size = os.path.getsize("example.txt")
print(f"Size: {size} bytes")

# Absolute path
abs_path = os.path.abspath("example.txt")
print(f"Absolute path: {abs_path}")

# File name from path
filename = os.path.basename("/path/to/example.txt")
print(f"Filename: {filename}")  # example.txt

# Directory from path
directory = os.path.dirname("/path/to/example.txt")
print(f"Directory: {directory}")  # /path/to

# Split path
path, filename = os.path.split("/path/to/example.txt")
print(path, filename)  # /path/to example.txt


# --- Create directory ---
# Create single directory
os.mkdir("newfolder")

# Create nested directories
os.makedirs("parent/child/grandchild")


# --- Remove files and directories ---
# Remove file
os.remove("example.txt")

# Remove empty directory
os.rmdir("emptyfolder")

# Remove directory with contents
import shutil
shutil.rmtree("myfolder")


# --- Rename files/directories ---
os.rename("oldname.txt", "newname.txt")


# --- List files in directory ---
files = os.listdir(".")  # Current directory
print(files)

# List only files (not directories)
files = [f for f in os.listdir(".") if os.path.isfile(f)]

# List only directories
dirs = [d for d in os.listdir(".") if os.path.isdir(d)]


# --- Walk through directory tree ---
for root, dirs, files in os.walk("."):
    print(f"Directory: {root}")
    print(f"Subdirectories: {dirs}")
    print(f"Files: {files}")


# --- Current working directory ---
cwd = os.getcwd()
print(f"Current directory: {cwd}")

# Change directory
os.chdir("/path/to/directory")


# --- Path joining (OS-independent) ---
path = os.path.join("folder", "subfolder", "file.txt")
print(path)  # folder/subfolder/file.txt (or folder\subfolder\file.txt on Windows)


# =============================================================================
# BINARY FILES
# =============================================================================

# --- Read binary file ---
with open("image.jpg", "rb") as file:
    binary_data = file.read()
    print(type(binary_data))  # <class 'bytes'>


# --- Write binary file ---
with open("output.bin", "wb") as file:
    file.write(b'\x00\x01\x02\x03')


# --- Copy binary file ---
with open("source.jpg", "rb") as source:
    with open("destination.jpg", "wb") as dest:
        dest.write(source.read())


# =============================================================================
# CSV FILES
# =============================================================================

import csv

# --- Writing CSV ---
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "London"],
    ["Charlie", 35, "Tokyo"]
]

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)


# --- Reading CSV ---
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# --- CSV with DictWriter ---
data = [
    {"Name": "Alice", "Age": 25, "City": "New York"},
    {"Name": "Bob", "Age": 30, "City": "London"}
]

with open("data.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)


# --- CSV with DictReader ---
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"], row["Age"])


# =============================================================================
# JSON FILES
# =============================================================================

import json

# --- Writing JSON ---
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "coding"]
}

# Write to file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

# Convert to JSON string
json_string = json.dumps(data, indent=4)


# --- Reading JSON ---
with open("data.json", "r") as file:
    data = json.load(file)
    print(data["name"])

# Parse JSON string
json_string = '{"name": "Bob", "age": 30}'
data = json.loads(json_string)


# =============================================================================
# ERROR HANDLING - EXCEPTIONS
# =============================================================================
'''
Exceptions are errors that occur during program execution.
Python has many built-in exception types:

Common Exceptions:
- ZeroDivisionError: Division by zero
- ValueError: Invalid value
- TypeError: Wrong type
- IndexError: Invalid index
- KeyError: Invalid dictionary key
- FileNotFoundError: File doesn't exist
- IOError: Input/output error
- AttributeError: Invalid attribute
- NameError: Variable not defined
- ImportError: Import fails
- KeyboardInterrupt: User interrupts (Ctrl+C)
'''


# =============================================================================
# TRY-EXCEPT BASICS
# =============================================================================

# --- Basic try-except ---
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")


# --- Catching specific exceptions ---
try:
    num = int("abc")
except ValueError:
    print("Invalid number format!")


# --- Multiple except blocks ---
try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError:
    print("Index out of range!")
except ValueError:
    print("Invalid value!")
except TypeError:
    print("Type error occurred!")


# --- Catching multiple exceptions in one block ---
try:
    # Some code
    pass
except (ValueError, TypeError, IndexError):
    print("One of the errors occurred!")


# --- Catch all exceptions (NOT RECOMMENDED) ---
try:
    # Some code
    pass
except:
    print("An error occurred!")

# Better: Catch Exception (base class)
try:
    # Some code
    pass
except Exception as e:
    print(f"Error: {e}")


# --- Getting exception details ---
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")
    print(f"Error type: {type(e).__name__}")


# =============================================================================
# TRY-EXCEPT-ELSE-FINALLY
# =============================================================================

# --- else block ---
# Executes if no exception occurs
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result: {result}")  # This executes


# --- finally block ---
# Always executes, regardless of exception
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("Cleanup code here")
    # file.close()  # Always close file


# --- Complete structure ---
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result: {result}")
finally:
    print("Operation completed")


# =============================================================================
# RAISING EXCEPTIONS
# =============================================================================

# --- Raise exception manually ---
age = -5
if age < 0:
    raise ValueError("Age cannot be negative!")


# --- Raise with custom message ---
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Divider cannot be zero!")
    return a / b


# --- Re-raising exceptions ---
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Handling error...")
    raise  # Re-raise the same exception


# --- Raising different exception ---
try:
    num = int("abc")
except ValueError:
    raise TypeError("Type conversion failed!")


# =============================================================================
# CUSTOM EXCEPTIONS
# =============================================================================

# --- Creating custom exception ---
class NegativeNumberError(Exception):
    """Exception raised for negative numbers"""
    pass

def square_root(num):
    if num < 0:
        raise NegativeNumberError("Cannot calculate square root of negative number")
    return num ** 0.5

try:
    result = square_root(-4)
except NegativeNumberError as e:
    print(f"Error: {e}")


# --- Custom exception with attributes ---
class InsufficientFundsError(Exception):
    """Exception for insufficient bank balance"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Insufficient funds! Balance: {balance}, Required: {amount}"
        super().__init__(self.message)

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(e.message)
    print(f"Short by: {e.amount - e.balance}")


# =============================================================================
# EXCEPTION HIERARCHY
# =============================================================================
'''
BaseException
    ├── SystemExit
    ├── KeyboardInterrupt
    └── Exception
            ├── ArithmeticError
            │       ├── ZeroDivisionError
            │       └── OverflowError
            ├── LookupError
            │       ├── IndexError
            │       └── KeyError
            ├── ValueError
            ├── TypeError
            ├── NameError
            ├── AttributeError
            ├── IOError / OSError
            │       └── FileNotFoundError
            └── ImportError

Always catch specific exceptions before general ones!
'''


# =============================================================================
# ASSERTIONS
# =============================================================================

# --- Basic assertion ---
assert 5 > 3  # Passes silently
# assert 5 < 3  # Raises AssertionError


# --- Assertion with message ---
age = 15
assert age >= 18, "Must be 18 or older"


# --- Using assertions for debugging ---
def calculate_average(numbers):
    assert len(numbers) > 0, "List cannot be empty"
    return sum(numbers) / len(numbers)

try:
    avg = calculate_average([])
except AssertionError as e:
    print(f"Assertion failed: {e}")


# --- Disable assertions (run with python -O) ---
# Assertions are removed when optimization is enabled
# Don't use for production error handling!


# =============================================================================
# FILE HANDLING WITH ERROR HANDLING
# =============================================================================

# --- Safe file reading ---
def read_file_safe(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None
    except PermissionError:
        print(f"Error: No permission to read {filename}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


# --- Safe file writing ---
def write_file_safe(filename, content):
    try:
        with open(filename, "w") as file:
            file.write(content)
        return True
    except PermissionError:
        print(f"Error: No permission to write to {filename}")
        return False
    except IOError as e:
        print(f"IO Error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False


# --- File operations with multiple error checks ---
def process_file(input_file, output_file):
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"{input_file} does not exist")
        
        # Read input file
        with open(input_file, "r") as f_in:
            content = f_in.read()
        
        # Process content
        processed = content.upper()
        
        # Write to output file
        with open(output_file, "w") as f_out:
            f_out.write(processed)
        
        print("File processed successfully")
        
    except FileNotFoundError as e:
        print(f"File error: {e}")
    except PermissionError:
        print("Permission denied")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Process completed")


# =============================================================================
# CONTEXT MANAGERS
# =============================================================================

# --- Understanding with statement ---
# Without with:
file = open("example.txt", "r")
try:
    content = file.read()
finally:
    file.close()

# With 'with' (cleaner):
with open("example.txt", "r") as file:
    content = file.read()


# --- Multiple context managers ---
with open("input.txt", "r") as f_in, open("output.txt", "w") as f_out:
    content = f_in.read()
    f_out.write(content.upper())


# --- Creating custom context manager ---
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        # Return True to suppress exception, False to propagate
        return False

# Usage
with FileManager("test.txt", "w") as f:
    f.write("Hello, World!")


# --- Context manager using contextlib ---
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    try:
        f = open(filename, mode)
        yield f
    finally:
        f.close()

# Usage
with file_manager("test.txt", "w") as f:
    f.write("Hello, World!")


# =============================================================================
# LOGGING ERRORS
# =============================================================================

import logging

# --- Basic logging ---
logging.basicConfig(level=logging.DEBUG)

try:
    result = 10 / 0
except ZeroDivisionError as e:
    logging.error(f"Error occurred: {e}")


# --- Logging to file ---
logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    with open("nonexistent.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    logging.error(f"File error: {e}")


# --- Different logging levels ---
logging.debug("Debug message")      # Detailed information
logging.info("Info message")        # General information
logging.warning("Warning message")  # Warning
logging.error("Error message")      # Error
logging.critical("Critical message") # Critical error


# =============================================================================
# BEST PRACTICES
# =============================================================================

# --- 1. Always use 'with' for file operations ---
# Good
with open("file.txt", "r") as f:
    content = f.read()

# Avoid
f = open("file.txt", "r")
content = f.read()
f.close()


# --- 2. Catch specific exceptions ---
# Good
try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid number")

# Avoid
try:
    num = int(input("Enter number: "))
except:
    print("Error occurred")


# --- 3. Don't silence errors ---
# Bad
try:
    risky_operation()
except:
    pass  # Silently ignoring errors is dangerous!

# Good
try:
    risky_operation()
except Exception as e:
    logging.error(f"Operation failed: {e}")


# --- 4. Use finally for cleanup ---
try:
    file = open("data.txt", "r")
    # Process file
except FileNotFoundError:
    print("File not found")
finally:
    if 'file' in locals():
        file.close()


# --- 5. Validate before processing ---
def divide_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# --- 6. Provide meaningful error messages ---
# Bad
raise ValueError("Error!")

# Good
raise ValueError(f"Invalid age value: {age}. Age must be between 0 and 120")


# --- 7. Clean up resources in finally ---
connection = None
try:
    connection = open_database_connection()
    # Use connection
except DatabaseError as e:
    logging.error(f"Database error: {e}")
finally:
    if connection:
        connection.close()


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
'''
FILE HANDLING:

MODES:
✓ 'r' - Read (default)
✓ 'w' - Write (overwrites)
✓ 'a' - Append
✓ 'x' - Exclusive creation
✓ 'b' - Binary mode
✓ '+' - Read and write

READING:
✓ read() - Read entire file
✓ readline() - Read one line
✓ readlines() - Read all lines into list
✓ Iterate: for line in file (best for large files)

WRITING:
✓ write() - Write string
✓ writelines() - Write list of strings
✓ Remember: No automatic newlines!

BEST PRACTICES:
✓ Always use 'with' statement
✓ Use encoding="utf-8" for text files
✓ Close files properly
✓ Handle exceptions


ERROR HANDLING:

TRY-EXCEPT STRUCTURE:
try:
    # Risky code
except SpecificException:
    # Handle specific error
except AnotherException as e:
    # Handle another error
else:
    # Runs if no exception
finally:
    # Always runs (cleanup)

BEST PRACTICES:
✓ Catch specific exceptions
✓ Don't silence errors
✓ Use finally for cleanup
✓ Provide meaningful messages
✓ Log errors appropriately
✓ Use assertions for debugging only
✓ Create custom exceptions when needed

COMMON EXCEPTIONS:
- ValueError: Invalid value
- TypeError: Wrong type
- IndexError: Invalid index
- KeyError: Invalid dict key
- FileNotFoundError: File missing
- ZeroDivisionError: Division by zero
- AttributeError: Invalid attribute
- ImportError: Import fails
'''