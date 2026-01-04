# 4) Pivot table creation 
import pandas as pd

# Example sales data
df = pd.DataFrame({
    "region": ["North", "North", "South", "South", "North"],
    "product": ["A", "B", "A", "B", "A"],
    "sales": [100, 150, 80, 120, 130]
})

# Create pivot table: rows=region, columns=product, values=sales (sum)
pivot = pd.pivot_table(df, index="region", columns="product", values="sales", aggfunc="sum", fill_value=0)
print("Pivot table (sales sum by region & product):")
print(pivot)

# Pivot table with margins (totals)
pivot_margins = pd.pivot_table(df, index="region", columns="product", values="sales", aggfunc="sum", margins=True)
print("\nPivot table with totals (margins=True):")
print(pivot_margins)
