# 7) Add a new column to a DataFrame (derived or constant) — commented version
import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "C"],
    "math": [80, 90, 75],
    "science": [85, 95, 70]
})

# Add a derived column 'total' (sum of math and science)
df["total"] = df["math"] + df["science"]

# Add a constant column 'school'
df["school"] = "ABC High"

print("DataFrame with new columns:")
print(df)