#7. Load a CSV into a Pandas DataFrame, filter rows, group by a column, and calculate the sum

import pandas as pd

df = pd.read_csv("DAY-16/sample-data-files/sales.csv")
# filter: keep rows with units >= 7
filtered = df[df["units"] >= 7]
# group by 'store' and sum units & revenue
grouped = filtered.groupby("store").agg({"units":"sum", "revenue":"sum"}).reset_index()
print(grouped)
grouped.to_csv("Q7_grouped_sales.csv", index=False)