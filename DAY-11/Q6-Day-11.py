# 6) Sort a DataFrame by one or more column values
import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "C", "D"],
    "age": [25, 22, 25, 20],
    "score": [80, 95, 70, 88]
})

# Sort by age ascending
sorted_by_age = df.sort_values(by="age")
print("Sorted by age (ascending):")
print(sorted_by_age)

# Sort by age then score (age asc, score desc)
sorted_multi = df.sort_values(by=["age", "score"], ascending=[True, False])
print("\nSorted by age asc, score desc:")
print(sorted_multi)
