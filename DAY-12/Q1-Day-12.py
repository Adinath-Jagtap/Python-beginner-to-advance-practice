# 1) Group data by column and aggregate (groupby) 
import pandas as pd

# Example DataFrame: sales by store and product
df = pd.DataFrame({
    "store": ["A", "A", "B", "B", "A"],
    "product": ["x", "y", "x", "y", "x"],
    "units": [10, 5, 8, 7, 3],
    "revenue": [100, 60, 80, 70, 30]
})

# Group by 'store' and compute sum of units and revenue
grouped_store = df.groupby("store").agg({"units": "sum", "revenue": "sum"})
print("Group by store (sum):")
print(grouped_store)

# Group by multiple columns and compute multiple aggregations
grouped_multi = df.groupby(["store", "product"]).agg(
    total_units=pd.NamedAgg(column="units", aggfunc="sum"),
    avg_revenue=pd.NamedAgg(column="revenue", aggfunc="mean"),
    count=pd.NamedAgg(column="units", aggfunc="count")
)
print("\nGroup by store & product (multiple aggs):")
print(grouped_multi)
