# 4) Select specific columns from a DataFrame — commented version
import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "C"],
    "age": [20, 21, 22],
    "score": [88, 92, 75]
})

# Select a single column (returns a Series)
age_series = df["age"]
print("Single column (Series):")
print(age_series)

# Select multiple columns (returns a DataFrame)
subset = df[["name", "score"]]
print("\nMultiple columns (DataFrame):")
print(subset)