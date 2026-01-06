'''
DAY 15: Regular Expressions (Regex)
'''

# =============================================================================
# REGULAR EXPRESSIONS INTRODUCTION
# =============================================================================
'''
Regular Expressions (Regex): Patterns for matching text
- Powerful tool for text processing
- Search, validate, extract, and replace text
- Uses special syntax to define patterns
- Built into Python's 're' module

Why Use Regex?
- Validate input (email, phone, password)
- Extract data from text (URLs, dates, numbers)
- Text cleaning and preprocessing
- Find and replace patterns
- Split strings by complex patterns

Common Use Cases:
- Form validation
- Data extraction from logs
- Text parsing
- Data cleaning
- Pattern matching in files
'''

# --- Importing re module ---
import re

# Check version
print(f"Python re module loaded successfully")


# =============================================================================
# REGEX BASIC SYNTAX
# =============================================================================
'''
Special Characters (Metacharacters):
. (dot)      - Any single character except newline
^ (caret)    - Start of string
$ (dollar)   - End of string
* (asterisk) - 0 or more repetitions
+ (plus)     - 1 or more repetitions
? (question) - 0 or 1 repetition
{m,n}        - m to n repetitions
[] (brackets)- Character set
| (pipe)     - OR operator
() (parens)  - Grouping
\ (backslash)- Escape special characters

Character Classes:
\d - Digit (0-9)
\D - Non-digit
\w - Word character (a-z, A-Z, 0-9, _)
\W - Non-word character
\s - Whitespace (space, tab, newline)
\S - Non-whitespace

Quantifiers:
*  - 0 or more
+  - 1 or more
?  - 0 or 1
{3} - Exactly 3
{2,5} - Between 2 and 5
{2,} - 2 or more

Anchors:
^  - Start of string
$  - End of string
\b - Word boundary
\B - Not a word boundary
'''


# =============================================================================
# BASIC REGEX METHODS
# =============================================================================

# --- re.match() - Match at beginning ---
# Checks if pattern matches at START of string
text = "Hello World"
pattern = r"Hello"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")

# Won't match (pattern not at start)
match = re.match(r"World", text)
print("Match World:", match)  # None


# --- re.search() - Search anywhere ---
# Finds FIRST occurrence anywhere in string
text = "The price is $50"
pattern = r"\$\d+"

match = re.search(pattern, text)
if match:
    print("Found:", match.group())  # $50
    print("Position:", match.span())  # (13, 16)


# --- re.findall() - Find all matches ---
# Returns list of ALL matches
text = "My phone is 123-456-7890 and 987-654-3210"
pattern = r"\d{3}-\d{3}-\d{4}"

matches = re.findall(pattern, text)
print("All phone numbers:", matches)
# ['123-456-7890', '987-654-3210']


# --- re.finditer() - Iterator of matches ---
# Returns iterator with match objects
text = "Email: john@example.com and jane@test.com"
pattern = r"\w+@\w+\.\w+"

for match in re.finditer(pattern, text):
    print(f"Found: {match.group()} at position {match.span()}")


# --- re.sub() - Replace pattern ---
# Replace matches with new text
text = "I have 2 cats and 3 dogs"
pattern = r"\d+"

# Replace all numbers with 'X'
result = re.sub(pattern, "X", text)
print(result)  # I have X cats and X dogs

# Replace with function
def double_number(match):
    return str(int(match.group()) * 2)

result = re.sub(r"\d+", double_number, text)
print(result)  # I have 4 cats and 6 dogs


# --- re.split() - Split by pattern ---
# Split string using regex pattern
text = "apple,banana;orange:grape"
pattern = r"[,;:]"

result = re.split(pattern, text)
print(result)  # ['apple', 'banana', 'orange', 'grape']


# --- re.compile() - Compile pattern ---
# Compile pattern for reuse (faster)
pattern = re.compile(r"\d+")

text1 = "I have 5 apples"
text2 = "She has 10 oranges"

print(pattern.findall(text1))  # ['5']
print(pattern.findall(text2))  # ['10']


# =============================================================================
# MATCHING EXACT PATTERNS
# =============================================================================
'''
Exact Pattern Matching: Find specific text patterns
- Use raw strings r"pattern" to avoid escaping issues
- Literal characters match themselves
- Case-sensitive by default
'''

# --- Match Exact Word ---
text = "Hello World"
pattern = r"Hello"

if re.match(pattern, text):
    print("Pattern matches!")

# Match exact string
text = "Python 3.9"
pattern = r"Python 3.9"

if re.search(pattern, text):
    print("Exact match found!")


# --- Match with Anchors ---
# Start of string (^)
text = "Hello World"
pattern = r"^Hello"

match = re.match(pattern, text)
print("Starts with Hello:", match is not None)

# End of string ($)
pattern = r"World$"
match = re.search(pattern, text)
print("Ends with World:", match is not None)

# Exact full string match
pattern = r"^Hello World$"
match = re.match(pattern, text)
print("Exact full match:", match is not None)


# --- Case Insensitive Matching ---
text = "Hello World"
pattern = r"hello"

# Case sensitive (no match)
match = re.search(pattern, text)
print("Case sensitive:", match)

# Case insensitive (match)
match = re.search(pattern, text, re.IGNORECASE)
print("Case insensitive:", match.group() if match else None)


# --- Match Multiple Options ---
text = "I like cats"
pattern = r"cats|dogs|birds"

if re.search(pattern, text):
    print("Match found!")

# Match any of these exact words
text = "The color is red"
pattern = r"\b(red|blue|green)\b"

match = re.search(pattern, text)
if match:
    print("Color found:", match.group())


# --- Word Boundaries ---
text = "cat cats caterpillar"
pattern = r"\bcat\b"

# Only matches exact word "cat"
matches = re.findall(pattern, text)
print("Exact word matches:", matches)  # ['cat']

# Without word boundary
pattern = r"cat"
matches = re.findall(pattern, text)
print("All matches:", matches)  # ['cat', 'cat', 'cat']


# =============================================================================
# FINDING EMAIL ADDRESSES
# =============================================================================
'''
Email Pattern: username@domain.extension
- Username: letters, numbers, dots, underscores
- @ symbol
- Domain: letters, numbers, hyphens
- Extension: .com, .org, etc.
'''

# --- Basic Email Pattern ---
text = "Contact us at info@example.com or support@test.org"
pattern = r"\w+@\w+\.\w+"

emails = re.findall(pattern, text)
print("Emails found:", emails)


# --- More Robust Email Pattern ---
text = """
Contact: john.doe@example.com
Support: support_team@company.co.uk
Sales: sales123@test-site.org
Invalid: @notanemail.com
"""

# Better pattern (handles dots, underscores, hyphens)
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = re.findall(pattern, text)
print("All valid emails:")
for email in emails:
    print(f"  - {email}")


# --- Extract Email Components ---
text = "Email: john.doe@example.com"
pattern = r"([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})"

match = re.search(pattern, text)
if match:
    username = match.group(1)
    domain = match.group(2)
    extension = match.group(3)
    
    print(f"Username: {username}")
    print(f"Domain: {domain}")
    print(f"Extension: {extension}")


# --- Validate Email Function ---
def is_valid_email(email):
    """Check if email format is valid"""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

# Test
test_emails = [
    "john@example.com",      # Valid
    "jane.doe@test.co.uk",   # Valid
    "@invalid.com",          # Invalid
    "no-at-sign.com",        # Invalid
    "user@domain",           # Invalid (no extension)
]

for email in test_emails:
    print(f"{email}: {'Valid' if is_valid_email(email) else 'Invalid'}")


# =============================================================================
# VALIDATING PHONE NUMBERS
# =============================================================================
'''
Phone Number Patterns:
- Different formats: (123) 456-7890, 123-456-7890, 1234567890
- Country codes: +1-123-456-7890
- Extensions: 123-456-7890 ext. 123
'''

# --- Basic Phone Pattern (US) ---
text = "Call me at 123-456-7890 or 987-654-3210"
pattern = r"\d{3}-\d{3}-\d{4}"

phones = re.findall(pattern, text)
print("Phone numbers:", phones)


# --- Multiple Phone Formats ---
text = """
Contact numbers:
123-456-7890
(123) 456-7890
123.456.7890
1234567890
+1-123-456-7890
"""

# Pattern for various formats
pattern = r"\+?1?\s*\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}"

phones = re.findall(pattern, text)
print("All phone formats:")
for phone in phones:
    print(f"  - {phone}")


# --- Validate Specific Format ---
def validate_phone_format1(phone):
    """Validate format: 123-456-7890"""
    pattern = r"^\d{3}-\d{3}-\d{4}$"
    return re.match(pattern, phone) is not None

def validate_phone_format2(phone):
    """Validate format: (123) 456-7890"""
    pattern = r"^\(\d{3}\)\s\d{3}-\d{4}$"
    return re.match(pattern, phone) is not None

# Test
test_phones = [
    "123-456-7890",
    "(123) 456-7890",
    "1234567890",
    "123.456.7890"
]

for phone in test_phones:
    print(f"{phone}:")
    print(f"  Format 1: {validate_phone_format1(phone)}")
    print(f"  Format 2: {validate_phone_format2(phone)}")


# --- Extract and Normalize Phone Numbers ---
def normalize_phone(phone):
    """Extract digits and format as XXX-XXX-XXXX"""
    # Extract only digits
    digits = re.findall(r"\d", phone)
    
    # Take last 10 digits
    digits = digits[-10:]
    
    if len(digits) == 10:
        return f"{digits[0]}{digits[1]}{digits[2]}-{digits[3]}{digits[4]}{digits[5]}-{digits[6]}{digits[7]}{digits[8]}{digits[9]}"
    return None

# Test
test_phones = [
    "(123) 456-7890",
    "123.456.7890",
    "+1-123-456-7890",
    "1234567890"
]

for phone in test_phones:
    normalized = normalize_phone(phone)
    print(f"{phone} -> {normalized}")


# =============================================================================
# EXTRACTING URLs
# =============================================================================
'''
URL Pattern: protocol://domain.extension/path
- Protocol: http, https, ftp
- Domain: letters, numbers, hyphens
- Extension: .com, .org, etc.
- Optional path, query, fragment
'''

# --- Basic URL Pattern ---
text = "Visit https://example.com or http://test.org for more info"
pattern = r"https?://\w+\.\w+"

urls = re.findall(pattern, text)
print("URLs found:", urls)


# --- Comprehensive URL Pattern ---
text = """
Visit these sites:
https://www.example.com
http://test.org/page
https://site.com/path?query=value
ftp://files.example.com/download
www.noprotocol.com
"""

# Pattern for various URL formats
pattern = r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}[^\s]*"

urls = re.findall(pattern, text)
print("All URLs:")
for url in urls:
    print(f"  - {url}")


# --- Extract URL Components ---
text = "Visit https://www.example.com/page?id=123"
pattern = r"(https?)://([a-zA-Z0-9.-]+)(/[^\s]*)?"

match = re.search(pattern, text)
if match:
    protocol = match.group(1)
    domain = match.group(2)
    path = match.group(3) if match.group(3) else "/"
    
    print(f"Protocol: {protocol}")
    print(f"Domain: {domain}")
    print(f"Path: {path}")


# --- Find URLs with or without Protocol ---
text = """
Links:
https://example.com
www.test.org
example.net/page
"""

# Pattern for URLs with optional protocol
pattern = r"(?:https?://)?(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?"

urls = re.findall(pattern, text)
print("All URLs (with/without protocol):")
for url in urls:
    print(f"  - {url}")


# --- Validate URL Function ---
def is_valid_url(url):
    """Check if URL format is valid"""
    pattern = r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?$"
    return re.match(pattern, url) is not None

# Test
test_urls = [
    "https://example.com",           # Valid
    "http://test.org/page",          # Valid
    "https://site.com/path?q=1",     # Valid
    "not-a-url",                     # Invalid
    "www.example.com"                # Invalid (no protocol)
]

for url in test_urls:
    print(f"{url}: {'Valid' if is_valid_url(url) else 'Invalid'}")


# =============================================================================
# REPLACING MULTIPLE SPACES
# =============================================================================
'''
Replace Multiple Spaces: Clean up text formatting
- \s+ matches one or more whitespace characters
- Useful for data cleaning
'''

# --- Replace Multiple Spaces with Single Space ---
text = "Hello    World     Python    Programming"
pattern = r"\s+"

# Replace with single space
result = re.sub(pattern, " ", text)
print(result)  # Hello World Python Programming


# --- Replace Multiple Spaces and Tabs ---
text = "Hello  \t\t World   \t  Python"
pattern = r"[ \t]+"

result = re.sub(pattern, " ", text)
print(result)


# --- Remove Leading/Trailing Spaces ---
text = "   Hello World   "

# Remove leading spaces
result = re.sub(r"^\s+", "", text)
print(f"'{result}'")  # 'Hello World   '

# Remove trailing spaces
result = re.sub(r"\s+$", "", text)
print(f"'{result}'")  # '   Hello World'

# Remove both
result = re.sub(r"^\s+|\s+$", "", text)
print(f"'{result}'")  # 'Hello World'


# --- Clean Up Text Function ---
def clean_text(text):
    """Remove extra whitespace from text"""
    # Replace multiple spaces with single space
    text = re.sub(r"\s+", " ", text)
    # Remove leading/trailing whitespace
    text = text.strip()
    return text

# Test
messy_text = "  Hello    World     \t  Python   "
cleaned = clean_text(messy_text)
print(f"Original: '{messy_text}'")
print(f"Cleaned: '{cleaned}'")


# --- Replace Newlines and Spaces ---
text = """Hello
World

Python"""

# Replace newlines and spaces with single space
result = re.sub(r"\s+", " ", text)
print(result)  # Hello World Python


# =============================================================================
# FINDING CAPITALIZED WORDS
# =============================================================================
'''
Capitalized Words: Words starting with uppercase letter
- Useful for finding proper nouns, sentence starts
- Pattern: \b[A-Z][a-z]*\b
'''

# --- Find Words Starting with Capital Letter ---
text = "Python is Great for Data Science and Machine Learning"
pattern = r"\b[A-Z][a-z]*"

capitalized = re.findall(pattern, text)
print("Capitalized words:", capitalized)


# --- Find All-Caps Words ---
text = "I love PYTHON and JAVA programming"
pattern = r"\b[A-Z]+\b"

all_caps = re.findall(pattern, text)
print("All-caps words:", all_caps)


# --- Find Proper Nouns (Title Case) ---
text = "John Smith lives in New York and works at Google Inc."
pattern = r"\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*"

proper_nouns = re.findall(pattern, text)
print("Proper nouns:", proper_nouns)


# --- Find Capitalized Words with Length Filter ---
text = "A Good Python Developer Should Know About OOP"

# Capitalized words with at least 3 characters
pattern = r"\b[A-Z][a-z]{2,}"

words = re.findall(pattern, text)
print("Capitalized words (3+ chars):", words)


# --- Count Capitalized Words ---
text = "Python Java JavaScript C++ Ruby Go"
pattern = r"\b[A-Z][a-z]*"

count = len(re.findall(pattern, text))
print(f"Number of capitalized words: {count}")


# --- Extract Acronyms ---
text = "NASA, FBI, and CIA are government agencies"
pattern = r"\b[A-Z]{2,}\b"

acronyms = re.findall(pattern, text)
print("Acronyms:", acronyms)


# =============================================================================
# VALIDATING PASSWORDS
# =============================================================================
'''
Password Validation: Check password strength
- Minimum length (usually 8 characters)
- Contains uppercase letter
- Contains lowercase letter
- Contains digit
- Contains special character
'''

# --- Basic Password Validation ---
def validate_password_basic(password):
    """Check if password is at least 8 characters"""
    pattern = r".{8,}"
    return re.match(pattern, password) is not None


# --- Password with Digit Requirement ---
def validate_password_with_digit(password):
    """Min 8 chars and at least 1 digit"""
    # Check length
    if len(password) < 8:
        return False
    
    # Check for digit
    if not re.search(r"\d", password):
        return False
    
    return True


# --- Password with Digit and Special Character ---
def validate_password_strong(password):
    """
    Password requirements:
    - Minimum 8 characters
    - At least 1 digit
    - At least 1 special character
    """
    # Check length
    if len(password) < 8:
        return False
    
    # Check for digit
    if not re.search(r"\d", password):
        return False
    
    # Check for special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    
    return True


# --- Comprehensive Password Validation ---
def validate_password_comprehensive(password):
    """
    Strong password requirements:
    - Minimum 8 characters
    - At least 1 uppercase letter
    - At least 1 lowercase letter
    - At least 1 digit
    - At least 1 special character
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters"
    
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"
    
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter"
    
    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit"
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character"
    
    return True, "Password is strong"


# --- Test Password Validation ---
test_passwords = [
    "weak",                    # Too short
    "password123",             # No special char
    "Password!",               # No digit
    "Pass123!",                # Valid but short
    "Password123!",            # Strong
    "MyP@ssw0rd123"           # Strong
]

print("\nPassword Validation Tests:")
for pwd in test_passwords:
    is_valid, message = validate_password_comprehensive(pwd)
    print(f"{pwd:20} - {'✓' if is_valid else '✗'} {message}")


# --- Single Regex Pattern (Advanced) ---
def validate_password_regex(password):
    """Validate using lookahead assertions"""
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$"
    return re.match(pattern, password) is not None

print("\nUsing single regex pattern:")
for pwd in test_passwords:
    is_valid = validate_password_regex(pwd)
    print(f"{pwd:20} - {'Valid' if is_valid else 'Invalid'}")


# =============================================================================
# EXTRACTING NUMBERS
# =============================================================================
'''
Number Extraction: Find numbers in text
- Integers: \d+
- Decimals: \d+\.\d+
- Negative numbers: -?\d+
- Currency: \$\d+\.?\d*
'''

# --- Extract All Digits ---
text = "I have 5 apples and 10 oranges"
pattern = r"\d+"

numbers = re.findall(pattern, text)
print("Numbers:", numbers)  # ['5', '10']

# Convert to integers
numbers = [int(n) for n in re.findall(pattern, text)]
print("As integers:", numbers)


# --- Extract Decimal Numbers ---
text = "Price: $19.99, Weight: 2.5kg, Temperature: -5.2°C"
pattern = r"-?\d+\.?\d*"

numbers = re.findall(pattern, text)
print("All numbers:", numbers)


# --- Extract Only Integers ---
text = "There are 42 students and 3.5 hours of class"
pattern = r"\b\d+\b"

integers = re.findall(pattern, text)
print("Integers only:", integers)


# --- Extract Currency Values ---
text = "Prices: $19.99, $100, $5.50"
pattern = r"\$\d+(?:\.\d{2})?"

prices = re.findall(pattern, text)
print("Prices:", prices)

# Extract just the numbers
pattern = r"\$(\d+(?:\.\d{2})?)"
amounts = re.findall(pattern, text)
print("Amounts:", amounts)


# --- Extract Phone-like Number Sequences ---
text = "Call 123-456-7890 or 9876543210"
pattern = r"\d{3}-\d{3}-\d{4}|\d{10}"

phones = re.findall(pattern, text)
print("Phone-like numbers:", phones)


# --- Extract and Sum Numbers ---
text = "Order total: 10 + 20 + 5.5"
numbers = re.findall(r"\d+\.?\d*", text)
numbers = [float(n) for n in numbers]

total = sum(numbers)
print(f"Numbers: {numbers}")
print(f"Sum: {total}")


# =============================================================================
# SPLITTING BY MULTIPLE DELIMITERS
# =============================================================================
'''
Split by Multiple Delimiters: Split string using various separators
- Use | (OR operator) to specify multiple delimiters
- Useful for parsing complex text formats
'''

# --- Split by Comma or Semicolon ---
text = "apple,banana;orange,grape;mango"
pattern = r"[,;]"

parts = re.split(pattern, text)
print("Parts:", parts)


# --- Split by Multiple Delimiters ---
text = "apple,banana;orange:grape|mango"
pattern = r"[,;:|]"

parts = re.split(pattern, text)
print("Fruits:", parts)


# --- Split by Whitespace or Punctuation ---
text = "Hello, World! How are you?"
pattern = r"[ ,!?.]+"

words = re.split(pattern, text)
# Remove empty strings
words = [w for w in words if w]
print("Words:", words)


# --- Split by Multiple Spaces or Tabs ---
text = "apple  banana\t\torange   grape"
pattern = r"[\s]+"

items = re.split(pattern, text)
print("Items:", items)


# --- Split and Keep Delimiters ---
text = "apple,banana;orange"
# Use parentheses to capture delimiters
pattern = r"([,;])"

parts = re.split(pattern, text)
print("With delimiters:", parts)


# --- Split by Word Boundaries ---
text = "one-two_three.four"
pattern = r"[-_.]"

parts = re.split(pattern, text)
print("Parts:", parts)


# --- Complex Splitting Example ---
text = "Name:John,Age:25;City:NYC|Country:USA"

# Split by : , ; |
pattern = r"[:,;|]"
parts = re.split(pattern, text)

# Create dictionary
data = {}
for i in range(0, len(parts)-1, 2):
    key = parts[i]
    value = parts[i+1]
    data[key] = value

print("Parsed data:", data)


# =============================================================================
# REMOVING NON-ALPHABETIC CHARACTERS
# =============================================================================
'''
Remove Non-Alphabetic: Keep only letters
- Remove numbers, punctuation, special characters
- Useful for text cleaning and analysis
'''

# --- Remove All Non-Letters ---
text = "Hello123 World!!! Python@2024"
pattern = r"[^a-zA-Z]"

# Replace with empty string
result = re.sub(pattern, "", text)
print("Only letters:", result)  # HelloWorldPython


# --- Remove Non-Letters, Keep Spaces ---
text = "Hello123 World!!! Python@2024"
pattern = r"[^a-zA-Z\s]"

result = re.sub(pattern, "", text)
print("Letters and spaces:", result)  # Hello World Python


# --- Remove Everything Except Letters and Numbers ---
text = "User123@email.com!!!"
pattern = r"[^a-zA-Z0-9]"

result = re.sub(pattern, "", text)
print("Alphanumeric only:", result)


# --- Remove Punctuation ---
text = "Hello, World! How are you?"
pattern = r"[^\w\s]"

result = re.sub(pattern, "", text)
print("No punctuation:", result)


# --- Clean Text Function ---
def clean_text_alpha_only(text):
    """Keep only alphabetic characters and spaces"""
    # Remove non-alphabetic (keep spaces)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)
    # Trim
    text = text.strip()
    return text

# Test
messy = "Hello123!!! World@@@   Python2024"
clean = clean_text_alpha_only(messy)
print(f"Original: {messy}")
print(f"Cleaned: {clean}")


# --- Keep Only Specific Characters ---
text = "Price: $19.99"

# Keep only numbers and dot
numbers_only = re.sub(r"[^0-9.]", "", text)
print("Numbers only:", numbers_only)


# --- Remove Emojis and Special Unicode ---
text = "Hello 😊 World 🌍"

# Remove emojis (basic pattern)
text = re.sub(r"[^\x00-\x7F]+", "", text)
print("No emojis:", text)


# =============================================================================
# ADVANCED REGEX PATTERNS
# =============================================================================

# --- Lookahead and Lookbehind ---
# Positive lookahead (?=...)
text = "Password123"
# Check if followed by digit
pattern = r"\w+(?=\d)"
match = re.search(pattern, text)
print("Lookahead:", match.group() if match else None)

# Positive lookbehind (?<=...)
text = "$100"
# Check if preceded by $
pattern = r"(?<=\$)\d+"
match = re.search(pattern, text)
print("Lookbehind:", match.group() if match else None)


# --- Non-Capturing Groups ---
# Regular group (captured)
text = "2024-01-15"
pattern = r"(\d{4})-(\d{2})-(\d{2})"
match = re.search(pattern, text)
print("Captured groups:", match.groups())

# Non-capturing group (?:...)
pattern = r"(?:\d{4})-(\d{2})-(\d{2})"
match = re.search(pattern, text)
print("Non-capturing:", match.groups())  # Only month and day


# --- Named Groups ---
text = "John Doe, Age: 30"
pattern = r"(?P<name>[A-Z][a-z]+ [A-Z][a-z]+), Age: (?P<age>\d+)"

match = re.search(pattern, text)
if match:
    print("Name:", match.group('name'))
    print("Age:", match.group('age'))


# --- Greedy vs Non-Greedy ---
text = "<div>Content</div>"

# Greedy (matches as much as possible)
pattern = r"<.*>"
match = re.search(pattern, text)
print("Greedy:", match.group())  # <div>Content

# -----------------------------------------------------------------------------
# 1) ESSENTIAL RULES / BEST PRACTICES
# -----------------------------------------------------------------------------
# - Use raw strings for patterns: r"\d+\.\d*"   # avoids double-escaping backslashes
# - Prefer re.fullmatch() for full-string validation (emails, phones).
# - Compile frequently-used patterns with re.compile() to improve readability & speed.
#   Example: pat = re.compile(r"\d{3}-\d{3}-\d{4}")
# - Use regex flags:
#     - re.IGNORECASE (case-insensitive)
#     - re.MULTILINE ( ^ and $ match at line boundaries)
#     - re.DOTALL (makes . match newline)
#     - re.VERBOSE (allows spacing/comments inside pattern)
# - Use re.VERBOSE for complex regexes and document them inline.
# - Name groups for clarity: (?P<name>pattern) instead of numeric groups.
# - Use non-capturing groups (?:...) when you don't need the captured text.
# - Anchor when needed: ^ for start, $ for end — prevents accidental partial matches.
# - Escape literal user input with re.escape() before building a pattern from it.
# - Avoid overly complex single-regex solutions — break problems into steps when helpful.
# - Beware of nested quantifiers (e.g., (.+)+ ) — these can cause catastrophic backtracking.
# - Test patterns on edge cases: empty strings, all-punctuation, unicode, very long strings.
# - Use re.sub() with a replacement function for transformations that depend on match content.
# - For critical standards (RFC-compliant email/URL), prefer specialized libraries.

# -----------------------------------------------------------------------------
# 2) QUICK KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# - Regex is powerful for matching, extracting, cleaning text.
# - Readability > cleverness: use comments, named groups, and VERBOSE mode.
# - Use fullmatch() for validation; search() for substring finds.
# - Always handle unexpected inputs (None, "", malformed strings).
# - Unit test your regexes in production code (add test cases with pytest/unittest).
# - Prefer libraries for heavy standards (email, URL parsing).

# -----------------------------------------------------------------------------
# 3) COMMON PATTERNS CHEAT-LIST
# -----------------------------------------------------------------------------
# \d        -> digit [0-9]
# \D        -> non-digit
# \w        -> word character (letters, digits, underscore)
# \W        -> non-word
# \s        -> whitespace
# \S        -> non-whitespace
# .         -> any character except newline (unless DOTALL)
# ^         -> start of string (or line in MULTILINE)
# $         -> end of string (or line in MULTILINE)
# \b        -> word boundary
# +         -> 1 or more
# *         -> 0 or more
# ?         -> 0 or 1 (also makes quantifiers lazy when placed after +/*)
# {m,n}     -> between m and n repetitions
# (?:...)   -> non-capturing group
# (?P<name>...) -> named group
# (?=...)   -> positive lookahead
# (?<=...)  -> positive lookbehind
# (?!...)   -> negative lookahead
# (?<!...)  -> negative lookbehind

# -----------------------------------------------------------------------------
# 4) PRACTICAL DOs and DON'Ts
# -----------------------------------------------------------------------------
# DO:
#   - Use re.compile for patterns used multiple times.
#   - Use named groups when extracting several components.
#   - Use re.VERBOSE + comments for complex patterns.
#   - Use fullmatch() for strict validation.
#   - Escape untrusted user input with re.escape().
# DON'T:
#   - DON'T try to fully implement RFCs (email/URL) with a single regex unless necessary.
#   - DON'T leave huge single-line regexes unexplained — they are fragile.
#   - DON'T ignore unicode and locale issues if your data is multilingual.

# -----------------------------------------------------------------------------
# 5) PERFORMANCE & SAFETY NOTES
# -----------------------------------------------------------------------------
# - Compiling patterns once reduces overhead:
#     pat = re.compile(pattern)
#     pat.findall(text)
# - Avoid catastrophic backtracking:
#     - Problematic: r"(a+)+b" on long "aaaa..." strings without b
#     - Prefer atomic patterns or more specific boundaries if needed.
# - For extremely large inputs, consider streaming/line-by-line processing.
# - Use timeouts or run regexes in controlled environments if inputs may be adversarial.

# -----------------------------------------------------------------------------
# 6) COMMON DEBUGGING TIPS
# -----------------------------------------------------------------------------
# - Use regex101.com or similar to interactively test and explain matches.
# - Add test cases for:
#     - empty string
#     - minimal valid string
#     - maximal/long string
#     - malformed strings
# - Insert printouts of match.groups() or groupdict() in development.
# - If a regex is slow, try simplifying components or pre-filter with simpler checks.

# -----------------------------------------------------------------------------
# 7) SAMPLE USAGE SNIPPETS (commented so you can paste them directly)
# -----------------------------------------------------------------------------
# Example: Raw string + compile + fullmatch
# -----------------------
# import re
# EMAIL_PAT = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
# print(EMAIL_PAT.fullmatch("john.doe@example.com") is not None)  # True
#
# Example: Named groups and extraction
# -----------------------
# import re
# pat = re.compile(r"(?P<user>[A-Za-z0-9._%+-]+)@(?P<domain>[A-Za-z0-9.-]+)\.(?P<tld>[A-Za-z]{2,})")
# m = pat.search("Contact: admin@mail.co.uk")
# if m:
#     print(m.groupdict())  # {'user': 'admin', 'domain': 'mail.co', 'tld': 'uk'}
#
# Example: re.VERBOSE for a readable phone pattern
# -----------------------
# import re
# PHONE = re.compile(r"""
#     ^\+?1?                # optional country code
#     [\s\-\.]?             # optional separator
#     \(?\d{3}\)?           # area code with optional parens
#     [\s\-\.]?             # optional separator
#     \d{3}                 # first 3 digits
#     [\s\-\.]?             # optional separator
#     \d{4}$                # last 4 digits
# """, re.VERBOSE)
# print(bool(PHONE.fullmatch("(123) 456-7890")))  # True
#
# Example: Use re.escape() when matching literal user input
# -----------------------
# import re
# user_input = "hello.world?"
# safe_pat = re.compile(re.escape(user_input))
# print(bool(safe_pat.search("Say hello.world? now")))  # True
#
# Example: Use re.sub() with function for dynamic replacements
# -----------------------
# import re
# def double_num(m): return str(int(m.group())*2)
# print(re.sub(r"\d+", double_num, "I have 2 apples and 3 oranges"))  # "I have 4 apples and 6 oranges"


# =============================================================================
# PYTHON PRACTICE QUESTIONS - REGULAR EXPRESSIONS (REGEX)
# =============================================================================
'''
1. Match an exact pattern within a string using re.search() or re.match()
2. Find all email addresses in a given text using re.findall()
3. Validate a phone number format using regular expressions
4. Extract all URLs from a text string
5. Replace multiple spaces with a single space using re.sub()
6. Find all words that start with a capital letter
7. Validate a password (minimum 8 characters, at least 1 digit and 1 special character)
8. Extract all numbers from a string
9. Split a string using multiple delimiters with re.split()
10. Remove all non-alphabetic characters from a string using regex
'''