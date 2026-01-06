# 1) Match exact pattern in string
import re

# Sample string and exact pattern we want to match
text = "Order-12345"
pattern = r"^Order-\d{5}$"  # ^ and $ ensure the whole string matches: "Order-" followed by exactly 5 digits

match = re.fullmatch(pattern, text)
print("Exact match?:", bool(match))   # True if entire string matches