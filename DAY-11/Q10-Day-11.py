# 10) Get basic statistics and info using describe() and info() — commented version
import pandas as pd

df = pd.DataFrame({
    "age": [20, 21, 22, 23, 24],
    "score": [80, 90, 75, 88, 92],
    "name": ["A", "B", "C", "D", "E"]
})

# info() shows dtypes and non-null counts (useful for quick schema check)
print("DataFrame info():")
df.info()

# describe() shows summary statistics for numeric columns by default
print("\nNumeric summary describe():")
print(df.describe())

# describe(include="all") will include non-numeric columns too
print("\nFull summary describe(include='all'):")
print(df.describe(include="all"))