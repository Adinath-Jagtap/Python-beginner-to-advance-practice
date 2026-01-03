# 10) Create new column from existing columns — commented version
import pandas as pd

df = pd.DataFrame({
    "first_name": ["John", "Jane"],
    "last_name": ["Doe", "Smith"],
    "math": [80, 90],
    "english": [70, 95]
})

# Simple concatenation of strings to form full name
df["full_name"] = df["first_name"] + " " + df["last_name"]

# Derived numeric column (total and average)
df["total"] = df["math"] + df["english"]
df["average"] = df["total"] / 2

print("After creating new columns from existing ones:")
print(df)
