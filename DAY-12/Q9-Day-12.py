# 9) Filter with multiple conditions (AND/OR) — commented version
import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "C", "D"],
    "age": [20, 25, 30, 22],
    "score": [70, 85, 90, 60]
})

# Condition 1: age > 21
# Condition 2: score >= 80
# Use & for AND, | for OR, and wrap each condition in parentheses
and_filtered = df[(df["age"] > 21) & (df["score"] >= 80)]
print("Rows with age > 21 AND score >= 80:")
print(and_filtered)

or_filtered = df[(df["age"] < 21) | (df["score"] < 65)]
print("\nRows with age < 21 OR score < 65:")
print(or_filtered)