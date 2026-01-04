# 1) Create a pandas DataFrame from a dictionary 
import pandas as pd

# Create a dictionary where keys are column names and values are lists of column values
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 22],
    "city": ["Mumbai", "Pune", "Nagpur"]
}

# Create the DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the DataFrame to verify
print("DataFrame created from dict:")
print(df)
