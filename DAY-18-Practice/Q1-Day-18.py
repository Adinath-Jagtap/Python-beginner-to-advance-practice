# 1) Reverse a string — simple function + example
def reverse_string(s: str) -> str:
    """
    Return the reverse of the input string.
    Uses Python slicing which is concise and fast.
    """
    return s[::-1]

# Example
sample = "hello"
print("Original:", sample)
print("Reversed:", reverse_string(sample))  # -> "olleh"
