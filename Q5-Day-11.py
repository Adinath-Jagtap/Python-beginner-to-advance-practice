# 5) Filter rows based on a condition — commented version
import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "C", "D"],
    "age": [18, 25, 30, 22],
    "passed": [True, True, False, True]
})

# Filter rows where age > 21
older_than_21 = df[df["age"] > 21]
print("Rows with age > 21:")
print(older_than_21)

# Combine conditions: age > 20 AND passed == True
filtered = df[(df["age"] > 20) & (df["passed"] == True)]
print("\nAge > 20 and passed:")
print(filtered)