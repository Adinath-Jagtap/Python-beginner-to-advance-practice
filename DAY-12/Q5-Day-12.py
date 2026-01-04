# 5) Apply custom function to column 
import pandas as pd

df = pd.DataFrame({
    "name": ["alice", "BOB", "Charlie"],
    "score": [88, 92, 75]
})

# Define a custom function to normalize names
def normalize_name(s: str) -> str:
    return s.strip().title()  # remove whitespace and title-case

# Use .apply() on the column
df["name_normalized"] = df["name"].apply(normalize_name)

# Or use a lambda inline to scale score to 0-1
df["score_scaled"] = df["score"].apply(lambda x: x / 100)

print("After applying custom functions:")
print(df)
