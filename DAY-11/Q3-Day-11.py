# 3) Display first/last N rows with head() and tail() — commented version
import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    "A": range(1, 11),
    "B": list("abcdefghij")
})

# head(n) shows the first n rows (default n=5)
print("First 3 rows:")
print(df.head(3))

# tail(n) shows the last n rows
print("\nLast 4 rows:")
print(df.tail(4))