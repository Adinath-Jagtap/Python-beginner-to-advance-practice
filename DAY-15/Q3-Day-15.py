# 3) Validate phone number format
import re

# Sample phone numbers in common formats
samples = [
    "1234567890",       # plain 10 digits
    "123-456-7890",     # dashes
    "(123) 456-7890",   # parentheses + space
    "+91 9876543210",   # country code example
    "12345"             # invalid
]

# Pattern to accept: optional +country, optional parentheses area code, digits, dashes or spaces
phone_pattern = r"^(?:\+\d{1,3}\s)?(?:\(\d{3}\)\s?|\d{3}[-\s]?)\d{3}[-\s]?\d{4}$"

for s in samples:
    valid = bool(re.fullmatch(phone_pattern, s))
    print(f"{s:16} -> valid? {valid}")