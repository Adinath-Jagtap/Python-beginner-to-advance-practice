# 9) Handle missing values: isnull(), fillna(), dropna() 
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": [1, np.nan, 3],
    "B": ["x", "y", None],
    "C": [10, 20, 30]
})

# Check missing values
print("Isnull DataFrame:")
print(df.isnull())

# Fill missing numeric values with 0 and missing strings with 'missing'
df_filled = df.fillna({"A": 0, "B": "missing"})
print("\nAfter fillna:")
print(df_filled)

# Drop rows that have any missing values
df_dropped_na = df.dropna()
print("\nRows after dropna (no missing values):")
print(df_dropped_na)
