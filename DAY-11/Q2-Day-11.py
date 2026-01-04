# 2) Read a CSV file into a DataFrame using pd.read_csv() 
import pandas as pd

# Replace 'data.csv' with the path to your CSV file
# parse_dates can be used if a column contains dates (example below commented)
df = pd.read_csv("data.csv")  # df = pd.read_csv("data.csv", parse_dates=["date_col"])

# Show top rows to check the file loaded correctly
print("First 5 rows from CSV:")
print(df.head())
