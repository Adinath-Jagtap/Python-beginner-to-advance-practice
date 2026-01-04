# 8) Convert data types of columns 
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "id": ["1", "2", "3"],
    "price": ["10.5", "20", "30.75"],
    "flag": [1, 0, 1]
})

# Convert 'id' to integers
df["id"] = df["id"].astype(int)

# Convert 'price' to float (handles string numbers)
df["price"] = df["price"].astype(float)

# Convert 'flag' to boolean
df["flag"] = df["flag"].astype(bool)

print("After type conversions:")
print(df.dtypes)
print(df)
