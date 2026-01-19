import re

# Sample string
s = "A man, a plan, a canal: Panama"

# Remove non-alphanumeric and lowercase
clean = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

# Check palindrome
is_palindrome = clean == clean[::-1]
print("Is palindrome:", is_palindrome)
