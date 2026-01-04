'''
DAY 12: Pandas Data Manipulation (Advanced)
'''

# ============================================================================
# PANDAS INTRODUCTION
# ============================================================================
'''
Pandas: Powerful library for data analysis and manipulation in Python.
- Works with tabular data (like Excel/CSV)
- Built on top of NumPy
- Two main data structures: Series (1D) and DataFrame (2D)
- Great for cleaning, transforming, and analyzing data

Why Pandas?
- Easy data loading from various formats (CSV, Excel, SQL, JSON)
- Powerful data manipulation tools
- Handling missing data
- GroupBy operations
- Data merging and joining
- Time series functionality
'''

# --- Installing Pandas ---
# pip install pandas

import pandas as pd
import numpy as np

# Check Pandas version
print(pd.__version__)


# =============================================================================
# GROUPBY - AGGREGATING DATA BY GROUPS
# =============================================================================
'''
groupby(): Split data into groups based on column values, 
           then apply functions to each group
           
Common aggregation functions:
- sum(), mean(), median(), min(), max()
- count(), std(), var()
- first(), last()
'''

# --- Basic GroupBy ---
# Sample DataFrame
data = {
    'Department': ['Sales', 'Sales', 'HR', 'HR', 'IT', 'IT', 'Sales'],
    'Employee': ['John', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Salary': [50000, 60000, 45000, 48000, 70000, 75000, 55000],
    'Experience': [2, 5, 3, 4, 6, 8, 3]
}

df = pd.DataFrame(data)
print(df)

# Group by Department and calculate mean
grouped = df.groupby('Department').mean()
print(grouped)
#             Salary  Experience
# Department                    
# HR           46500         3.5
# IT           72500         7.0
# Sales        55000         3.3

# Group by Department and sum
total_salary = df.groupby('Department')['Salary'].sum()
print(total_salary)
# Department
# HR       93000
# IT      145000
# Sales   165000


# --- Multiple Aggregations ---
# Apply multiple functions at once
agg_result = df.groupby('Department').agg({
    'Salary': ['mean', 'sum', 'max'],
    'Experience': ['mean', 'min', 'max']
})
print(agg_result)

# Alternative: use agg with list of functions
result = df.groupby('Department')['Salary'].agg(['mean', 'sum', 'count'])
print(result)


# --- GroupBy with Multiple Columns ---
data = {
    'Department': ['Sales', 'Sales', 'HR', 'HR', 'Sales', 'HR'],
    'City': ['NY', 'LA', 'NY', 'LA', 'NY', 'NY'],
    'Sales': [100, 150, 80, 90, 120, 95]
}

df = pd.DataFrame(data)

# Group by multiple columns
grouped = df.groupby(['Department', 'City'])['Sales'].sum()
print(grouped)
# Department  City
# HR          LA       90
#             NY      175
# Sales       LA      150
#             NY      220


# --- GroupBy with Custom Aggregation ---
# Using lambda function
result = df.groupby('Department')['Sales'].agg(lambda x: x.max() - x.min())
print(result)  # Range of sales per department


# --- Iterating Through Groups ---
data = {
    'Category': ['A', 'A', 'B', 'B', 'C'],
    'Value': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

for name, group in df.groupby('Category'):
    print(f"\nCategory: {name}")
    print(group)


# =============================================================================
# MERGING DATAFRAMES
# =============================================================================
'''
merge(): Combine DataFrames based on common columns (like SQL JOIN)

Types of merges:
- inner: Keep only matching rows (default)
- left: Keep all rows from left DataFrame
- right: Keep all rows from right DataFrame
- outer: Keep all rows from both DataFrames
'''

# --- Inner Merge (Default) ---
df1 = pd.DataFrame({
    'EmployeeID': [1, 2, 3, 4],
    'Name': ['John', 'Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'EmployeeID': [1, 2, 5, 6],
    'Department': ['Sales', 'HR', 'IT', 'Finance']
})

# Merge on EmployeeID (keeps only matching: 1, 2)
merged = pd.merge(df1, df2, on='EmployeeID')
print(merged)
#    EmployeeID    Name Department
# 0           1    John      Sales
# 1           2   Alice         HR


# --- Left Merge ---
# Keep all rows from df1
left_merged = pd.merge(df1, df2, on='EmployeeID', how='left')
print(left_merged)
#    EmployeeID     Name Department
# 0           1     John      Sales
# 1           2    Alice         HR
# 2           3      Bob        NaN
# 3           4  Charlie        NaN


# --- Right Merge ---
# Keep all rows from df2
right_merged = pd.merge(df1, df2, on='EmployeeID', how='right')
print(right_merged)
#    EmployeeID   Name Department
# 0           1   John      Sales
# 1           2  Alice         HR
# 2           5    NaN         IT
# 3           6    NaN    Finance


# --- Outer Merge ---
# Keep all rows from both DataFrames
outer_merged = pd.merge(df1, df2, on='EmployeeID', how='outer')
print(outer_merged)
#    EmployeeID     Name Department
# 0           1     John      Sales
# 1           2    Alice         HR
# 2           3      Bob        NaN
# 3           4  Charlie        NaN
# 4           5      NaN         IT
# 5           6      NaN    Finance


# --- Merge on Different Column Names ---
df1 = pd.DataFrame({
    'EmpID': [1, 2, 3],
    'Name': ['John', 'Alice', 'Bob']
})

df2 = pd.DataFrame({
    'EmployeeID': [1, 2, 3],
    'Salary': [50000, 60000, 55000]
})

# Specify left and right column names
merged = pd.merge(df1, df2, left_on='EmpID', right_on='EmployeeID')
print(merged)


# --- Merge on Multiple Columns ---
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Date': ['2024-01', '2024-01', '2024-02'],
    'Sales': [100, 200, 150]
})

df2 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Date': ['2024-01', '2024-01', '2024-02'],
    'Region': ['East', 'West', 'East']
})

merged = pd.merge(df1, df2, on=['ID', 'Date'])
print(merged)


# =============================================================================
# CONCATENATING DATAFRAMES
# =============================================================================
'''
concat(): Stack DataFrames vertically or horizontally
- Useful for combining multiple DataFrames with same structure
- Can concatenate along rows (axis=0, default) or columns (axis=1)
'''

# --- Vertical Concatenation (Stacking Rows) ---
df1 = pd.DataFrame({
    'Name': ['John', 'Alice'],
    'Age': [25, 30]
})

df2 = pd.DataFrame({
    'Name': ['Bob', 'Charlie'],
    'Age': [35, 28]
})

# Concatenate vertically (one below the other)
result = pd.concat([df1, df2])
print(result)
#       Name  Age
# 0     John   25
# 1    Alice   30
# 0      Bob   35
# 1  Charlie   28

# Reset index after concatenation
result = pd.concat([df1, df2], ignore_index=True)
print(result)
#       Name  Age
# 0     John   25
# 1    Alice   30
# 2      Bob   35
# 3  Charlie   28


# --- Horizontal Concatenation (Stacking Columns) ---
df1 = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob']
})

df2 = pd.DataFrame({
    'Age': [25, 30, 35]
})

df3 = pd.DataFrame({
    'City': ['NY', 'LA', 'Chicago']
})

# Concatenate horizontally (side by side)
result = pd.concat([df1, df2, df3], axis=1)
print(result)
#     Name  Age     City
# 0   John   25       NY
# 1  Alice   30       LA
# 2    Bob   35  Chicago


# --- Concatenating with Keys ---
df1 = pd.DataFrame({'Value': [1, 2]})
df2 = pd.DataFrame({'Value': [3, 4]})

result = pd.concat([df1, df2], keys=['Group1', 'Group2'])
print(result)
#          Value
# Group1 0      1
#        1      2
# Group2 0      3
#        1      4


# --- Handling Missing Values in Concat ---
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'B': [5, 6], 'C': [7, 8]})

# Concatenate with different columns
result = pd.concat([df1, df2], ignore_index=True)
print(result)
#      A  B    C
# 0  1.0  3  NaN
# 1  2.0  4  NaN
# 2  NaN  5  7.0
# 3  NaN  6  8.0

# Only keep common columns
result = pd.concat([df1, df2], join='inner', ignore_index=True)
print(result)
#    B
# 0  3
# 1  4
# 2  5
# 3  6


# =============================================================================
# PIVOT TABLES
# =============================================================================
'''
pivot_table(): Create Excel-style pivot tables
- Summarize data by grouping and aggregating
- Useful for creating cross-tabulations
'''

# --- Basic Pivot Table ---
data = {
    'Date': ['2024-01', '2024-01', '2024-02', '2024-02', '2024-01', '2024-02'],
    'Product': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Sales': [100, 150, 120, 180, 110, 160],
    'Quantity': [10, 15, 12, 18, 11, 16]
}

df = pd.DataFrame(data)
print(df)

# Create pivot table: Products as rows, Dates as columns
pivot = df.pivot_table(values='Sales', index='Product', columns='Date')
print(pivot)
# Date        2024-01  2024-02
# Product                     
# A             105.0    120.0
# B             150.0    170.0


# --- Pivot Table with Aggregation Function ---
# Using sum instead of mean (default)
pivot = df.pivot_table(values='Sales', index='Product', columns='Date', aggfunc='sum')
print(pivot)
# Date        2024-01  2024-02
# Product                     
# A               210      120
# B               150      340


# --- Multiple Values in Pivot Table ---
pivot = df.pivot_table(values=['Sales', 'Quantity'], 
                       index='Product', 
                       columns='Date', 
                       aggfunc='sum')
print(pivot)


# --- Pivot Table with Multiple Aggregations ---
pivot = df.pivot_table(values='Sales', 
                       index='Product', 
                       columns='Date',
                       aggfunc=['sum', 'mean', 'count'])
print(pivot)


# --- Pivot Table with Margins (Totals) ---
pivot = df.pivot_table(values='Sales', 
                       index='Product', 
                       columns='Date',
                       aggfunc='sum',
                       margins=True,  # Add row and column totals
                       margins_name='Total')
print(pivot)


# --- Alternative: pivot() for Reshaping ---
# Note: pivot() doesn't aggregate, just reshapes
data = {
    'Date': ['2024-01', '2024-02', '2024-03'],
    'Product': ['A', 'A', 'A'],
    'Sales': [100, 120, 130]
}
df = pd.DataFrame(data)

# Simple reshape without aggregation
pivoted = df.pivot(index='Product', columns='Date', values='Sales')
print(pivoted)


# =============================================================================
# APPLY - CUSTOM FUNCTIONS ON DATAFRAME
# =============================================================================
'''
apply(): Apply a function along DataFrame axis
- Can use built-in functions, lambda functions, or custom functions
- Works on entire columns/rows
'''

# --- Apply Function to Column ---
df = pd.DataFrame({
    'Name': ['john', 'alice', 'bob'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 55000]
})

# Apply built-in function
df['Name'] = df['Name'].apply(str.upper)
print(df)
#     Name  Age  Salary
# 0   JOHN   25   50000
# 1  ALICE   30   60000
# 2    BOB   35   55000


# --- Apply Lambda Function ---
# Calculate bonus (10% of salary)
df['Bonus'] = df['Salary'].apply(lambda x: x * 0.1)
print(df)

# Categorize age
df['Age_Group'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Senior')
print(df)


# --- Apply Custom Function ---
def categorize_salary(salary):
    if salary < 55000:
        return 'Low'
    elif salary < 65000:
        return 'Medium'
    else:
        return 'High'

df['Salary_Category'] = df['Salary'].apply(categorize_salary)
print(df)


# --- Apply Function to Multiple Columns ---
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Apply function to entire DataFrame (column-wise)
result = df.apply(lambda x: x.sum())
print(result)
# A     6
# B    15

# Apply row-wise (axis=1)
df['Total'] = df.apply(lambda row: row['A'] + row['B'], axis=1)
print(df)
#    A  B  Total
# 0  1  4      5
# 1  2  5      7
# 2  3  6      9


# --- Apply with Arguments ---
def calculate_percentage(value, total):
    return (value / total) * 100

df = pd.DataFrame({'Score': [80, 90, 70]})
df['Percentage'] = df['Score'].apply(calculate_percentage, total=100)
print(df)


# --- applymap() - Apply to Every Element (deprecated, use map()) ---
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Apply function to every element
result = df.map(lambda x: x * 2)  # New method (Pandas 2.1+)
print(result)


# =============================================================================
# HANDLING DUPLICATE ROWS
# =============================================================================
'''
Duplicates: Rows with identical values
- duplicated(): Check for duplicate rows
- drop_duplicates(): Remove duplicate rows
'''

# --- Check for Duplicates ---
df = pd.DataFrame({
    'Name': ['John', 'Alice', 'John', 'Bob', 'Alice'],
    'Age': [25, 30, 25, 35, 30],
    'City': ['NY', 'LA', 'NY', 'Chicago', 'LA']
})

# Check which rows are duplicates
duplicates = df.duplicated()
print(duplicates)
# 0    False
# 1    False
# 2     True  (duplicate of row 0)
# 3    False
# 4     True  (duplicate of row 1)

# Show duplicate rows
print(df[df.duplicated()])


# --- Check Duplicates in Specific Columns ---
# Check duplicates based on 'Name' only
duplicates = df.duplicated(subset=['Name'])
print(duplicates)

# Check duplicates based on multiple columns
duplicates = df.duplicated(subset=['Name', 'Age'])
print(duplicates)


# --- Keep First or Last Occurrence ---
# Keep first occurrence, mark rest as duplicates
duplicates = df.duplicated(keep='first')  # Default
print(duplicates)

# Keep last occurrence
duplicates = df.duplicated(keep='last')
print(duplicates)

# Mark all duplicates as True
duplicates = df.duplicated(keep=False)
print(duplicates)


# --- Remove Duplicates ---
# Remove all duplicate rows
cleaned = df.drop_duplicates()
print(cleaned)

# Remove duplicates based on specific columns
cleaned = df.drop_duplicates(subset=['Name'])
print(cleaned)

# Remove duplicates, keep last occurrence
cleaned = df.drop_duplicates(keep='last')
print(cleaned)

# Inplace modification
df.drop_duplicates(inplace=True)


# =============================================================================
# RENAMING COLUMNS
# =============================================================================
'''
rename(): Change column or index names
- Can rename specific columns or all at once
'''

# --- Rename Specific Columns ---
df = pd.DataFrame({
    'old_name1': [1, 2, 3],
    'old_name2': [4, 5, 6],
    'old_name3': [7, 8, 9]
})

# Rename using dictionary
df_renamed = df.rename(columns={'old_name1': 'new_name1', 'old_name2': 'new_name2'})
print(df_renamed)
#    new_name1  new_name2  old_name3
# 0          1          4          7
# 1          2          5          8
# 2          3          6          9

# Inplace renaming
df.rename(columns={'old_name1': 'Column_A'}, inplace=True)


# --- Rename All Columns ---
df = pd.DataFrame({
    'A': [1, 2],
    'B': [3, 4],
    'C': [5, 6]
})

# Set new column names
df.columns = ['Col1', 'Col2', 'Col3']
print(df)


# --- Rename Using Function ---
df = pd.DataFrame({
    'name': [1, 2],
    'age': [3, 4],
    'salary': [5, 6]
})

# Convert all column names to uppercase
df_renamed = df.rename(columns=str.upper)
print(df_renamed)
#    NAME  AGE  SALARY
# 0     1    3       5
# 1     2    4       6

# Add prefix to all columns
df_renamed = df.rename(columns=lambda x: 'prefix_' + x)
print(df_renamed)


# --- Rename Index ---
df = pd.DataFrame({
    'A': [1, 2, 3]
}, index=['row1', 'row2', 'row3'])

# Rename specific index values
df_renamed = df.rename(index={'row1': 'first', 'row3': 'third'})
print(df_renamed)


# =============================================================================
# CONVERTING DATA TYPES
# =============================================================================
'''
astype(): Convert column data types
- Common types: int, float, str, bool, datetime
- Important for memory optimization and operations
'''

# --- Check Current Data Types ---
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [1.5, 2.5, 3.5],
    'C': ['10', '20', '30'],
    'D': [True, False, True]
})

print(df.dtypes)
# A      int64
# B    float64
# C     object
# D       bool


# --- Convert to Integer ---
df['B'] = df['B'].astype(int)
print(df.dtypes)
# A      int64
# B      int64  (changed from float)
# C     object
# D       bool


# --- Convert to Float ---
df['C'] = df['C'].astype(float)
print(df['C'])
# 0    10.0
# 1    20.0
# 2    30.0


# --- Convert to String ---
df['A'] = df['A'].astype(str)
print(df['A'])
# 0    1
# 1    2
# 2    3


# --- Convert Multiple Columns ---
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Convert multiple columns to float
df = df.astype({'A': float, 'B': float})
print(df.dtypes)


# --- Convert to Datetime ---
df = pd.DataFrame({
    'Date': ['2024-01-01', '2024-02-01', '2024-03-01']
})

df['Date'] = pd.to_datetime(df['Date'])
print(df['Date'])
print(df['Date'].dtype)  # datetime64[ns]


# --- Convert to Category (Memory Efficient) ---
df = pd.DataFrame({
    'Grade': ['A', 'B', 'A', 'C', 'B', 'A', 'C']
})

# Convert to category (saves memory)
df['Grade'] = df['Grade'].astype('category')
print(df['Grade'].dtype)  # category


# --- Handle Errors in Conversion ---
df = pd.DataFrame({
    'Values': ['1', '2', 'three', '4']
})

# This will raise error: cannot convert 'three' to int
# df['Values'] = df['Values'].astype(int)  # Error!

# Use errors='coerce' to set invalid values as NaN
df['Values'] = pd.to_numeric(df['Values'], errors='coerce')
print(df)
#    Values
# 0     1.0
# 1     2.0
# 2     NaN
# 3     4.0


# =============================================================================
# FILTERING WITH MULTIPLE CONDITIONS
# =============================================================================
'''
Boolean Indexing: Filter DataFrame based on conditions
- & (AND): Both conditions must be True
- | (OR): At least one condition must be True
- ~ (NOT): Negate condition
Note: Use parentheses around each condition!
'''

# --- AND Condition (&) ---
df = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28, 40],
    'Salary': [50000, 60000, 55000, 52000, 70000],
    'Department': ['Sales', 'HR', 'IT', 'Sales', 'IT']
})

# Filter: Age > 28 AND Salary > 55000
filtered = df[(df['Age'] > 28) & (df['Salary'] > 55000)]
print(filtered)
#      Name  Age  Salary Department
# 1   Alice   30   60000         HR
# 2     Bob   35   55000         IT  (not included, salary not > 55000)
# 4   David   40   70000         IT


# --- OR Condition (|) ---
# Filter: Age < 28 OR Salary > 65000
filtered = df[(df['Age'] < 28) | (df['Salary'] > 65000)]
print(filtered)
#      Name  Age  Salary Department
# 0    John   25   50000      Sales
# 4   David   40   70000         IT


# --- NOT Condition (~) ---
# Filter: NOT in IT department
filtered = df[~(df['Department'] == 'IT')]
print(filtered)
#       Name  Age  Salary Department
# 0     John   25   50000      Sales
# 1    Alice   30   60000         HR
# 3  Charlie   28   52000      Sales


# --- Combining Multiple Conditions ---
# Filter: (Age > 25 AND Department is Sales) OR Salary > 65000
filtered = df[((df['Age'] > 25) & (df['Department'] == 'Sales')) | (df['Salary'] > 65000)]
print(filtered)


# --- Using isin() for Multiple Values ---
# Filter rows where Department is Sales or HR
filtered = df[df['Department'].isin(['Sales', 'HR'])]
print(filtered)

# NOT isin
filtered = df[~df['Department'].isin(['IT'])]
print(filtered)


# --- Using between() for Range ---
# Filter Age between 28 and 35 (inclusive)
filtered = df[df['Age'].between(28, 35)]
print(filtered)


# --- String Filtering ---
df = pd.DataFrame({
    'Name': ['John Smith', 'Alice Johnson', 'Bob Williams', 'Charlie Brown']
})

# Contains substring
filtered = df[df['Name'].str.contains('John')]
print(filtered)
#            Name
# 0    John Smith
# 1  Alice Johnson

# Starts with
filtered = df[df['Name'].str.startswith('Bob')]
print(filtered)

# Ends with
filtered = df[df['Name'].str.endswith('son')]
print(filtered)


# --- Query Method (Alternative) ---
df = pd.DataFrame({
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
})

# Using query() - cleaner syntax
filtered = df.query('Age > 28 and Salary > 55000')
print(filtered)

# Can use variables with @
min_age = 28
filtered = df.query('Age > @min_age')
print(filtered)


# =============================================================================
# CREATE NEW COLUMNS FROM EXISTING COLUMNS
# =============================================================================
'''
Adding new columns based on calculations or transformations
- Direct assignment
- Using apply()
- Using mathematical operations
- Using conditions (np.where, np.select)
'''

# --- Simple Column Creation ---
df = pd.DataFrame({
    'First_Name': ['John', 'Alice', 'Bob'],
    'Last_Name': ['Doe', 'Smith', 'Johnson'],
    'Salary': [50000, 60000, 55000]
})

# Create Full_Name by combining columns
df['Full_Name'] = df['First_Name'] + ' ' + df['Last_Name']
print(df)


# --- Mathematical Operations ---
df = pd.DataFrame({
    'Price': [100, 200, 150],
    'Quantity': [2, 3, 4]
})

# Calculate total
df['Total'] = df['Price'] * df['Quantity']
print(df)
#    Price  Quantity  Total
# 0    100         2    200
# 1    200         3    600
# 2    150         4    600

# Multiple columns calculation
df['Price_Per_Unit'] = df['Total'] / df['Quantity']
print(df)


# --- Using apply() for Complex Logic ---
df = pd.DataFrame({
    'Age': [25, 30, 35, 40]
})

# Categorize age
df['Age_Category'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Middle' if x < 40 else 'Senior')
print(df)


# --- Conditional Column Creation ---
import numpy as np

df = pd.DataFrame({
    'Score': [85, 65, 92, 58, 74]
})

# Using np.where (if-else)
df['Pass_Fail'] = np.where(df['Score'] >= 70, 'Pass', 'Fail')
print(df)
#    Score Pass_Fail
# 0     85      Pass
# 1     65      Fail
# 2     92      Pass
# 3     58      Fail
# 4     74      Pass


# --- Multiple Conditions with np.select() ---
conditions = [
    df['Score'] >= 90,
    df['Score'] >= 80,
    df['Score'] >= 70,
    df['Score'] >= 60
]

choices = ['A', 'B', 'C', 'D']

df['Grade'] = np.select(conditions, choices, default='F')
print(df)
#    Score Pass_Fail Grade
# 0     85      Pass     B
# 1     65      Fail     D
# 2     92      Pass     A
# 3     58      Fail     F
# 4     74      Pass     C


# --- Create Column from Multiple Columns ---
df = pd.DataFrame({
    'Hours_Worked': [40, 45, 38, 50],
    'Hourly_Rate': [20, 25, 22, 30]
})

# Calculate weekly pay with overtime (>40 hours = 1.5x rate)
def calculate_pay(row):
    regular_hours = min(row['Hours_Worked'], 40)
    overtime_hours = max(row['Hours_Worked'] - 40, 0)
    regular_pay = regular_hours * row['Hourly_Rate']
    overtime_pay = overtime_hours * row['Hourly_Rate'] * 1.5
    return regular_pay + overtime_pay

df['Weekly_Pay'] = df.apply(calculate_pay, axis=1)
print(df)


# --- Using assign() Method ---
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Create multiple columns at once
df = df.assign(
    C=df['A'] + df['B'],
    D=df['A'] * df['B'],
    E=lambda x: x['C'] + x['D']
)
print(df)


# =============================================================================
# KEY TAKEAWAYS - PANDAS DATA MANIPULATION
# =============================================================================
'''
📌 GROUPBY:
- Use groupby() to aggregate data by categories
- Common functions: sum(), mean(), count(), min(), max()
- Can group by multiple columns: df.groupby(['Col1', 'Col2'])
- Use agg() for multiple aggregations at once

📌 MERGING:
- merge() combines DataFrames like SQL JOIN
- Types: inner (default), left, right, outer
- Specify columns: on='ColumnName' or left_on/right_on for different names
- Inner keeps only matching rows, outer keeps all rows

📌 CONCATENATING:
- concat() stacks DataFrames vertically (axis=0) or horizontally (axis=1)
- Use ignore_index=True to reset index after vertical concat
- join='inner' keeps only common columns, join='outer' keeps all

📌 PIVOT TABLES:
- pivot_table() creates Excel-style summaries
- Specify: values, index (rows), columns, aggfunc
- Use margins=True to add row/column totals
- Default aggregation is mean()

📌 APPLY FUNCTIONS:
- apply() applies functions to columns or rows
- Use lambda for simple operations: df['Col'].apply(lambda x: x * 2)
- axis=1 applies function row-wise, axis=0 column-wise (default)
- Great for complex transformations that can't be done with basic operations

📌 DUPLICATES:
- duplicated() checks for duplicate rows (returns boolean)
- drop_duplicates() removes duplicate rows
- Use subset=['Col1', 'Col2'] to check specific columns only
- keep='first' (default), 'last', or False (mark all duplicates)

📌 RENAMING:
- rename() changes column names: df.rename(columns={'old': 'new'})
- df.columns = ['New1', 'New2'] renames all columns at once
- Use functions: df.rename(columns=str.upper) for all uppercase
- inplace=True modifies original DataFrame

📌 DATA TYPES:
- astype() converts column data types: df['Col'].astype(int)
- pd.to_numeric() converts with error handling: errors='coerce'
- pd.to_datetime() converts strings to datetime objects
- Check types with df.dtypes, optimize memory with 'category' type

📌 FILTERING:
- Use & (AND), | (OR), ~ (NOT) for multiple conditions
- Always use parentheses: df[(condition1) & (condition2)]
- isin() checks if values are in a list: df[df['Col'].isin([1, 2, 3])]
- between() for range filtering: df[df['Col'].between(10, 20)]
- query() provides cleaner syntax: df.query('Age > 25 and Salary > 50000')

📌 NEW COLUMNS:
- Direct assignment: df['New'] = df['A'] + df['B']
- Use apply() for complex logic with multiple columns
- np.where() for conditional values: np.where(condition, value_if_true, value_if_false)
- np.select() for multiple conditions with different outputs
- assign() method creates multiple columns: df.assign(C=..., D=...)

💡 BEST PRACTICES:
- Always check data types before operations (df.dtypes)
- Use inplace=True carefully (it modifies original data)
- Reset index after concatenation to avoid duplicate indices
- Handle missing values (NaN) after merging outer joins
- Use method chaining for cleaner code: df.groupby().sum().reset_index()
- Test on small sample data before applying to large datasets
'''

# =============================================================================
# PYTHON PRACTICE QUESTIONS - PANDAS ADVANCED
# =============================================================================
'''
1. Group data by a column and aggregate results using groupby() and agg()
2. Merge two DataFrames using pd.merge() with different join types (inner, left, right)
3. Concatenate multiple DataFrames using pd.concat()
4. Create a pivot table using DataFrame.pivot_table()
5. Apply a custom function to a column or row using apply() or applymap()
6. Identify and handle duplicate rows using duplicated() and drop_duplicates()
7. Rename columns using DataFrame.rename() (single and multiple columns)
8. Convert data types of columns using astype() and to_datetime()/to_numeric()
9. Filter DataFrame with multiple conditions (AND / OR) using & and | with parentheses
10. Create a new column derived from existing columns (arithmetic or conditional)
'''
