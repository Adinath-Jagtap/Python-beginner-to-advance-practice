# 3) Check if two strings are anagrams
from collections import Counter

def are_anagrams(s1, s2):
    """
    Returns True if s1 and s2 are anagrams (same letters, same counts).
    Ignores spaces and is case-insensitive by default.
    """
    # normalize: remove spaces and lowercase (modify if you want to keep spaces)
    a = s1.replace(" ", "").lower()
    b = s2.replace(" ", "").lower()
    return Counter(a) == Counter(b)

# Sample usage
print(are_anagrams("Listen", "Silent"))             # -> True
print(are_anagrams("A gentleman", "Elegant man"))  # -> True
print(are_anagrams("abc", "abcc"))                 # -> False
