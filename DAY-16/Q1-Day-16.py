# Q1. Read a CSV file, count rows where a column value is greater than 50, and write the result to a new file

import pandas as pd #imports

# read sample file
df = pd.read_csv("DAY-16/sample-data-files/numbers.csv")

# count rows where 'value' > 50
count_gt_50 = (df["value"] > 50).sum()
print("Rows with value > 50:", count_gt_50)

# write the count and filtered rows to files
with open("Q1-count_result.txt", "w") as f:
    f.write(f"Rows with value > 50: {count_gt_50}\n")

df[df["value"] > 50].to_csv("Q1_filtered_numbers.csv", index=False) #saving filtered number in the given file