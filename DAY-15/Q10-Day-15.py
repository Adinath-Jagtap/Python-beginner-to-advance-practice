# 10) Remove all non-alphabetic characters 
import re

text = "Hello, World! 123 -- Welcome_to Python3."
# Keep only letters and spaces: replace anything not A-Z or a-z or space with empty string
clean = re.sub(r"[^A-Za-z\s]", "", text)
# Optionally normalize multiple spaces to single and strip ends
clean = re.sub(r"\s+", " ", clean).strip()
print("Original:", text)
print("Alphabetic only:", clean)
