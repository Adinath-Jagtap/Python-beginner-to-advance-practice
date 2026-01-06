# 5) Replace multiple spaces with a single space
import re

text = "This   is   text   with   multiple    spaces.\nAnd\twith\t tabs too."
# \s+ matches one or more whitespace characters (spaces, tabs, newlines)
normalized = re.sub(r"\s+", " ", text).strip()
print("Before:", repr(text))
print("After :", repr(normalized))