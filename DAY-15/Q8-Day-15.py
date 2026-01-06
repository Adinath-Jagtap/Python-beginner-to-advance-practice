# 8) Extract numbers from string 
import re

text = "Invoice #12345: 2 items at $19 each, tax 5 -> total 43"
# \d+ finds sequences of digits
nums = re.findall(r"\d+", text)
# Convert to integers if needed
nums_int = [int(n) for n in nums]
print("Numbers as strings:", nums)
print("Numbers as ints   :", nums_int)
