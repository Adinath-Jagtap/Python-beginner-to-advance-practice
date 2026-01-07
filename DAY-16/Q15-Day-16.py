#15. Read a JSON file, convert it into a Pandas DataFrame, find rows with null values, and fill them

import pandas as pd
import json

# read json file
df = pd.read_json("data.json")

# rows with any null values
rows_with_null = df[df.isnull().any(axis=1)]
print("Rows with nulls:\n", rows_with_null)

# fill missing values: name->"Unknown", age->median or 0, city->"Unknown"
age_fill = int(df["age"].median()) if df["age"].notnull().any() else 0
df_filled = df.fillna({"name":"Unknown", "age":age_fill, "city":"Unknown"})
print("Filled DF:\n", df_filled)

# optionally save
df_filled.to_csv("data_filled.csv", index=False)