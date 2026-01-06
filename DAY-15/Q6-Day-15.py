# 6) Find all words starting with a capital letter
import re

text = "Alice and Bob went to New York City. the quick Brown fox."
# \b[A-Z][a-zA-Z]*\b finds words starting with uppercase letter
cap_words = re.findall(r"\b[A-Z][a-zA-Z]*\b", text)
print("Capitalized words:", cap_words)
