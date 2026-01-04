# 7) Rename columns
import pandas as pd

df = pd.DataFrame({
    "FirstName": ["A", "B"],
    "LastName": ["X", "Y"],
    "Age": [20, 21]
})

# Rename single column
df_renamed = df.rename(columns={"FirstName": "first_name"})
print("Rename single column:")
print(df_renamed)

# Rename multiple columns and do it in-place
df.rename(columns={"LastName": "last_name", "Age": "age"}, inplace=True)
print("\nAfter renaming multiple columns in-place:")
print(df)
