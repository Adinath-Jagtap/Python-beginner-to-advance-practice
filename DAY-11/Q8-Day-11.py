# 8) Drop columns from a DataFrame using drop() — commented version
import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B"],
    "age": [20, 21],
    "city": ["X", "Y"]
})

# Drop a single column (axis=1 for columns)
df_dropped = df.drop("city", axis=1)
print("After dropping 'city' column:")
print(df_dropped)

# Drop multiple columns in-place
df.drop(["age"], axis=1, inplace=True)
print("\nOriginal DataFrame after dropping 'age' in-place:")
print(df)
