# 3) Concatenate multiple DataFrames — commented version
import pandas as pd

# Two DataFrames with same columns (vertical concat)
df1 = pd.DataFrame({"A": [1, 2], "B": ["x", "y"]})
df2 = pd.DataFrame({"A": [3, 4], "B": ["z", "w"]})

# Concatenate vertically (stack rows)
vertical = pd.concat([df1, df2], ignore_index=True)
print("Vertical concat (rows stacked):")
print(vertical)

# Concatenate horizontally (side-by-side) — axis=1
left = pd.DataFrame({"key": [1, 2], "val1": ["a", "b"]})
right = pd.DataFrame({"key": [1, 2], "val2": ["c", "d"]})
horizontal = pd.concat([left, right], axis=1)
print("\nHorizontal concat (columns side-by-side):")
print(horizontal)
