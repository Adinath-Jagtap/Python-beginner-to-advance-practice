# 2) Merge two DataFrames
import pandas as pd

# Left table: students and their IDs
students = pd.DataFrame({
    "student_id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"]
})

# Right table: scores for some students
scores = pd.DataFrame({
    "student_id": [1, 2, 4],
    "score": [85, 92, 78]
})

# Inner join (only matching keys)
inner = pd.merge(students, scores, on="student_id", how="inner")
print("Inner join (matching IDs):")
print(inner)

# Left join (all students, scores where available)
left = pd.merge(students, scores, on="student_id", how="left")
print("\nLeft join (all students):")
print(left)

# Outer join (all records from both)
outer = pd.merge(students, scores, on="student_id", how="outer", indicator=True)
print("\nOuter join with indicator (shows merge origin):")
print(outer)
