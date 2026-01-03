# 6) Handle duplicate rows — commented version
import pandas as pd

df = pd.DataFrame({
    "id": [1, 2, 2, 3, 4, 4, 4],
    "value": ["a", "b", "b", "c", "d", "d", "d"]
})

# Detect duplicates (returns boolean Series)
dupes_bool = df.duplicated()  # marks True for all but first occurrence
print("Duplicated mask (default keep='first'):")
print(dupes_bool)

# Show duplicate rows
print("\nDuplicate rows:")
print(df[df.duplicated(keep=False)])  # keep=False shows all occurrences of duplicates

# Drop duplicates (keep first occurrence)
df_no_dupes = df.drop_duplicates()
print("\nAfter drop_duplicates (keep first):")
print(df_no_dupes)

# Drop duplicates based on subset of columns (e.g., 'id' only), keeping last
df_no_dupes_subset = df.drop_duplicates(subset=["id"], keep="last")
print("\nAfter drop_duplicates on 'id' (keep last):")
print(df_no_dupes_subset)
