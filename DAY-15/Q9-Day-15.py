# 9) Split string by multiple delimiters
import re

text = "apple, banana;orange|pear  grape"
# Split on comma, semicolon, pipe or whitespace (one or more): use character class [...]
parts = re.split(r"[,\;\|\s]+", text)
# Filter out any empty strings (if leading/trailing delimiters exist)
parts = [p for p in parts if p]
print("Split parts:", parts)
