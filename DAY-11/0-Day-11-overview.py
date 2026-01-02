'''
DAY 11: Python Pandas Basics
'''

# =============================================================================
# PANDAS INTRODUCTION
# =============================================================================
'''
Pandas: Powerful data analysis and manipulation library for Python.
- Built on NumPy
- Two main data structures: Series and DataFrame
- Easy data cleaning, exploration, and analysis
- Handles missing data efficiently
- Works with various file formats (CSV, Excel, JSON, SQL)

Why Pandas?
- Fast and efficient for large datasets
- Easy data manipulation and analysis
- Built-in visualization capabilities
- Integration with other libraries (NumPy, Matplotlib, Scikit-learn)
'''

# --- Installing Pandas ---
# pip install pandas

import pandas as pd
import numpy as np

# Check Pandas version
print(pd.__version__)


# =============================================================================
# PANDAS SERIES
# =============================================================================
'''
Series: One-dimensional labeled array (like a column in a table)
- Can hold any data type
- Has index labels
- Similar to NumPy array but with labels
'''

# --- Creating Series ---
# From list
series1 = pd.Series([10, 20, 30, 40, 50])
print(series1)
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64

# From list with custom index
series2 = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(series2)
# a    10
# b    20
# c    30
# d    40
# e    50
# dtype: int64

# From dictionary
data_dict = {'a': 10, 'b': 20, 'c': 30}
series3 = pd.Series(data_dict)
print(series3)
# a    10
# b    20
# c    30
# dtype: int64

# From NumPy array
arr = np.array([1, 2, 3, 4, 5])
series4 = pd.Series(arr)
print(series4)


# --- Accessing Series Elements ---
series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

# By index label
print(series['a'])       # 10
print(series['c'])       # 30

# By position
print(series[0])         # 10
print(series[2])         # 30

# Slicing
print(series['a':'c'])   # a, b, c
print(series[0:3])       # First 3 elements


# --- Series Attributes ---
series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

print(series.values)     # [10 20 30 40 50]
print(series.index)      # Index(['a', 'b', 'c', 'd', 'e'])
print(series.dtype)      # int64
print(series.shape)      # (5,)
print(series.size)       # 5


# =============================================================================
# PANDAS DATAFRAME
# =============================================================================
'''
DataFrame: Two-dimensional labeled data structure (like a table/spreadsheet)
- Columns can be different types
- Has row and column labels
- Most commonly used Pandas object
'''

# --- Creating DataFrame from Dictionary ---
# Dictionary with lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney']
}
df = pd.DataFrame(data)
print(df)
#       Name  Age      City
# 0    Alice   25  New York
# 1      Bob   30    London
# 2  Charlie   35     Paris
# 3    David   28     Tokyo
# 4      Eve   32    Sydney


# Dictionary with custom index
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}
df = pd.DataFrame(data, index=['Row1', 'Row2', 'Row3'])
print(df)
#           Name  Age      City
# Row1     Alice   25  New York
# Row2       Bob   30    London
# Row3   Charlie   35     Paris


# --- Creating DataFrame from List of Dictionaries ---
data = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'London'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Paris'}
]
df = pd.DataFrame(data)
print(df)


# --- Creating DataFrame from NumPy Array ---
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
df = pd.DataFrame(arr, columns=['A', 'B', 'C'])
print(df)
#    A  B  C
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9


# --- Creating DataFrame from Series ---
series1 = pd.Series([10, 20, 30], name='Column1')
series2 = pd.Series([40, 50, 60], name='Column2')
df = pd.DataFrame([series1, series2])
print(df)


# =============================================================================
# READING DATA FROM FILES
# =============================================================================

# --- Reading CSV File ---
# df = pd.read_csv('data.csv')
# print(df)

# With specific delimiter
# df = pd.read_csv('data.txt', delimiter='\t')

# With custom column names
# df = pd.read_csv('data.csv', names=['Col1', 'Col2', 'Col3'])

# Skip rows
# df = pd.read_csv('data.csv', skiprows=2)

# Read only specific columns
# df = pd.read_csv('data.csv', usecols=['Name', 'Age'])

# Specify index column
# df = pd.read_csv('data.csv', index_col='ID')


# --- Reading Excel File ---
# df = pd.read_excel('data.xlsx')
# df = pd.read_excel('data.xlsx', sheet_name='Sheet1')


# --- Reading JSON File ---
# df = pd.read_json('data.json')


# --- Creating Sample CSV for Practice ---
# Let's create a sample CSV file for practice
sample_data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 
             'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],
    'Age': [25, 30, 35, 28, 32, 45, 29, 38, 26, 41],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney',
             'Berlin', 'Madrid', 'Rome', 'Mumbai', 'Toronto'],
    'Salary': [50000, 60000, 75000, 55000, 65000,
               80000, 52000, 70000, 48000, 85000]
}
sample_df = pd.DataFrame(sample_data)
sample_df.to_csv('employees.csv', index=False)
print("Sample CSV created: employees.csv")


# =============================================================================
# VIEWING DATA
# =============================================================================

# Create sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 
             'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],
    'Age': [25, 30, 35, 28, 32, 45, 29, 38, 26, 41],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney',
             'Berlin', 'Madrid', 'Rome', 'Mumbai', 'Toronto'],
    'Salary': [50000, 60000, 75000, 55000, 65000,
               80000, 52000, 70000, 48000, 85000]
}
df = pd.DataFrame(data)


# --- Head and Tail ---
# Display first 5 rows (default)
print(df.head())

# Display first N rows
print(df.head(3))
#       Name  Age      City  Salary
# 0    Alice   25  New York   50000
# 1      Bob   30    London   60000
# 2  Charlie   35     Paris   75000

# Display last 5 rows (default)
print(df.tail())

# Display last N rows
print(df.tail(3))
#     Name  Age     City  Salary
# 7  Henry   38     Rome   70000
# 8    Ivy   26   Mumbai   48000
# 9   Jack   41  Toronto   85000


# --- Display Specific Range ---
print(df[2:5])           # Rows 2 to 4


# --- Basic Information ---
# Shape (rows, columns)
print(df.shape)          # (10, 4)

# Column names
print(df.columns)        # Index(['Name', 'Age', 'City', 'Salary'])

# Index
print(df.index)          # RangeIndex(start=0, stop=10, step=1)

# Data types
print(df.dtypes)
# Name      object
# Age        int64
# City      object
# Salary     int64
# dtype: object

# Info (detailed information)
print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10 entries, 0 to 9
# Data columns (total 4 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   Name    10 non-null     object
#  1   Age     10 non-null     int64
#  2   City    10 non-null     object
#  3   Salary  10 non-null     int64


# --- Statistical Summary ---
# Describe numeric columns
print(df.describe())
#              Age        Salary
# count  10.000000     10.000000
# mean   32.900000  64000.000000
# std     6.345106  12832.005607
# min    25.000000  48000.000000
# 25%    28.250000  53500.000000
# 50%    31.000000  62500.000000
# 75%    36.750000  73750.000000
# max    45.000000  85000.000000

# Describe all columns
print(df.describe(include='all'))


# =============================================================================
# SELECTING DATA
# =============================================================================

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney'],
    'Salary': [50000, 60000, 75000, 55000, 65000]
})


# --- Selecting Single Column ---
# Returns Series
names = df['Name']
print(names)
print(type(names))       # <class 'pandas.core.series.Series'>

# Alternative (returns Series)
ages = df.Age
print(ages)


# --- Selecting Multiple Columns ---
# Returns DataFrame
subset = df[['Name', 'Salary']]
print(subset)
#       Name  Salary
# 0    Alice   50000
# 1      Bob   60000
# 2  Charlie   75000
# 3    David   55000
# 4      Eve   65000


# --- Selecting Rows by Index ---
# Using loc (label-based)
print(df.loc[0])         # First row
print(df.loc[0:2])       # Rows 0 to 2 (inclusive)

# Using iloc (position-based)
print(df.iloc[0])        # First row
print(df.iloc[0:3])      # Rows 0 to 2 (exclusive)


# --- Selecting Specific Rows and Columns ---
# loc[rows, columns]
print(df.loc[0:2, ['Name', 'Age']])
#       Name  Age
# 0    Alice   25
# 1      Bob   30
# 2  Charlie   35

# iloc[row_positions, column_positions]
print(df.iloc[0:3, 0:2])
#       Name  Age
# 0    Alice   25
# 1      Bob   30
# 2  Charlie   35


# --- Selecting Single Cell ---
# loc
print(df.loc[0, 'Name'])      # 'Alice'

# iloc
print(df.iloc[0, 0])          # 'Alice'

# at (fastest for single value)
print(df.at[0, 'Name'])       # 'Alice'

# iat (fastest for single value by position)
print(df.iat[0, 0])           # 'Alice'


# =============================================================================
# FILTERING DATA
# =============================================================================

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Age': [25, 30, 35, 28, 32, 45],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney', 'Berlin'],
    'Salary': [50000, 60000, 75000, 55000, 65000, 80000]
})


# --- Single Condition ---
# Age greater than 30
filtered = df[df['Age'] > 30]
print(filtered)
#       Name  Age    City  Salary
# 2  Charlie   35   Paris   75000
# 4      Eve   32  Sydney   65000
# 5    Frank   45  Berlin   80000

# Salary less than or equal to 60000
filtered = df[df['Salary'] <= 60000]
print(filtered)


# --- Multiple Conditions (AND) ---
# Age > 30 AND Salary > 60000
filtered = df[(df['Age'] > 30) & (df['Salary'] > 60000)]
print(filtered)
#       Name  Age    City  Salary
# 2  Charlie   35   Paris   75000
# 4      Eve   32  Sydney   65000
# 5    Frank   45  Berlin   80000


# --- Multiple Conditions (OR) ---
# Age < 30 OR Salary > 70000
filtered = df[(df['Age'] < 30) | (df['Salary'] > 70000)]
print(filtered)


# --- String Filtering ---
# Names starting with 'A'
filtered = df[df['Name'].str.startswith('A')]
print(filtered)

# City contains 'on'
filtered = df[df['City'].str.contains('on')]
print(filtered)


# --- isin() Method ---
# Filter by specific values
cities = ['New York', 'Paris', 'Tokyo']
filtered = df[df['City'].isin(cities)]
print(filtered)


# --- NOT Condition ---
# Age NOT equal to 30
filtered = df[df['Age'] != 30]
print(filtered)

# NOT in list
filtered = df[~df['City'].isin(['London', 'Berlin'])]
print(filtered)


# =============================================================================
# SORTING DATA
# =============================================================================

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney'],
    'Salary': [50000, 60000, 75000, 55000, 65000]
})


# --- Sort by Single Column ---
# Ascending (default)
sorted_df = df.sort_values('Age')
print(sorted_df)
#       Name  Age      City  Salary
# 0    Alice   25  New York   50000
# 3    David   28     Tokyo   55000
# 1      Bob   30    London   60000
# 4      Eve   32    Sydney   65000
# 2  Charlie   35     Paris   75000

# Descending
sorted_df = df.sort_values('Salary', ascending=False)
print(sorted_df)
#       Name  Age      City  Salary
# 2  Charlie   35     Paris   75000
# 4      Eve   32    Sydney   65000
# 1      Bob   30    London   60000
# 3    David   28     Tokyo   55000
# 0    Alice   25  New York   50000


# --- Sort by Multiple Columns ---
# Sort by Age, then by Salary
sorted_df = df.sort_values(['Age', 'Salary'])
print(sorted_df)

# Different order for each column
sorted_df = df.sort_values(['Age', 'Salary'], ascending=[True, False])
print(sorted_df)


# --- Sort by Index ---
df_indexed = df.set_index('Name')
sorted_df = df_indexed.sort_index()
print(sorted_df)


# --- In-place Sorting ---
df_copy = df.copy()
df_copy.sort_values('Age', inplace=True)
print(df_copy)


# =============================================================================
# ADDING COLUMNS
# =============================================================================

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'Salary': [50000, 60000, 75000, 55000, 65000]
})


# --- Add Column with Constant Value ---
df['Country'] = 'USA'
print(df)
#       Name  Age  Salary Country
# 0    Alice   25   50000     USA
# 1      Bob   30   60000     USA
# 2  Charlie   35   75000     USA
# 3    David   28   55000     USA
# 4      Eve   32   65000     USA


# --- Add Column with List ---
df['City'] = ['New York', 'London', 'Paris', 'Tokyo', 'Sydney']
print(df)


# --- Add Column Based on Calculation ---
# Calculate bonus (10% of salary)
df['Bonus'] = df['Salary'] * 0.1
print(df)

# Calculate total compensation
df['Total'] = df['Salary'] + df['Bonus']
print(df)


# --- Add Column Based on Condition ---
# Age category
df['Age_Group'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Senior')
print(df)

# Using np.where
df['High_Earner'] = np.where(df['Salary'] > 60000, 'Yes', 'No')
print(df)


# --- Add Column with Function ---
def categorize_salary(salary):
    if salary < 55000:
        return 'Low'
    elif salary < 70000:
        return 'Medium'
    else:
        return 'High'

df['Salary_Category'] = df['Salary'].apply(categorize_salary)
print(df)


# --- Insert Column at Specific Position ---
df.insert(2, 'Department', 'IT')
print(df)
# Column 'Department' inserted at position 2


# =============================================================================
# DROPPING COLUMNS AND ROWS
# =============================================================================

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney'],
    'Salary': [50000, 60000, 75000, 55000, 65000],
    'Bonus': [5000, 6000, 7500, 5500, 6500]
})


# --- Drop Single Column ---
df_dropped = df.drop('Bonus', axis=1)
print(df_dropped)

# Alternative
df_dropped = df.drop(columns=['Bonus'])
print(df_dropped)


# --- Drop Multiple Columns ---
df_dropped = df.drop(['Bonus', 'City'], axis=1)
print(df_dropped)

# Alternative
df_dropped = df.drop(columns=['Bonus', 'City'])
print(df_dropped)


# --- Drop Column In-place ---
df_copy = df.copy()
df_copy.drop('Bonus', axis=1, inplace=True)
print(df_copy)


# --- Drop Rows ---
# Drop by index
df_dropped = df.drop(0)          # Drop row at index 0
print(df_dropped)

df_dropped = df.drop([0, 2, 4])  # Drop multiple rows
print(df_dropped)


# --- Drop Rows by Condition ---
# Drop rows where Age < 30
df_filtered = df[df['Age'] >= 30]
print(df_filtered)


# =============================================================================
# HANDLING MISSING VALUES
# =============================================================================

# Create DataFrame with missing values
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', None, 'David', 'Eve', 'Frank'],
    'Age': [25, 30, np.nan, 28, 32, np.nan],
    'City': ['New York', None, 'Paris', 'Tokyo', 'Sydney', 'Berlin'],
    'Salary': [50000, 60000, 75000, np.nan, 65000, 80000]
})

print("DataFrame with missing values:")
print(df)
#     Name   Age      City   Salary
# 0  Alice  25.0  New York  50000.0
# 1    Bob  30.0      None  60000.0
# 2   None   NaN     Paris  75000.0
# 3  David  28.0     Tokyo      NaN
# 4    Eve  32.0    Sydney  65000.0
# 5  Frank   NaN    Berlin  80000.0


# --- Check for Missing Values ---
# isnull() or isna() - returns True for missing values
print(df.isnull())
print(df.isna())         # Same as isnull()

# Count missing values per column
print(df.isnull().sum())
# Name      1
# Age       2
# City      1
# Salary    1
# dtype: int64

# Check if any value is missing
print(df.isnull().any())
# Name      True
# Age       True
# City      True
# Salary    True
# dtype: bool

# Total missing values
print(df.isnull().sum().sum())  # 5


# --- Check for Non-Missing Values ---
# notnull() or notna()
print(df.notnull())
print(df.notna())        # Same as notnull()


# --- Drop Missing Values ---
# Drop rows with any missing value
df_dropped = df.dropna()
print(df_dropped)
#     Name   Age      City   Salary
# 0  Alice  25.0  New York  50000.0
# 4    Eve  32.0    Sydney  65000.0

# Drop rows with all missing values
df_dropped = df.dropna(how='all')

# Drop rows with missing values in specific columns
df_dropped = df.dropna(subset=['Age'])
print(df_dropped)

# Drop columns with missing values
df_dropped = df.dropna(axis=1)
print(df_dropped)


# --- Fill Missing Values ---
# Fill with specific value
df_filled = df.fillna(0)
print(df_filled)

# Fill with different values for each column
df_filled = df.fillna({
    'Name': 'Unknown',
    'Age': df['Age'].mean(),
    'City': 'Not Specified',
    'Salary': df['Salary'].median()
})
print(df_filled)

# Fill with mean
df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df)

# Fill with median
df['Salary'] = df['Salary'].fillna(df['Salary'].median())
print(df)

# Fill with mode (most frequent value)
df['City'] = df['City'].fillna(df['City'].mode()[0])
print(df)

# Forward fill (use previous value)
df_filled = df.fillna(method='ffill')
print(df_filled)

# Backward fill (use next value)
df_filled = df.fillna(method='bfill')
print(df_filled)


# --- Replace Specific Values ---
df = df.replace(np.nan, 0)
print(df)


# =============================================================================
# GROUPING AND AGGREGATION
# =============================================================================

df = pd.DataFrame({
    'Department': ['IT', 'IT', 'HR', 'HR', 'Finance', 'Finance', 'IT'],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Age': [25, 30, 35, 28, 32, 45, 29],
    'Salary': [50000, 60000, 55000, 52000, 65000, 80000, 58000]
})


# --- GroupBy ---
# Group by single column
grouped = df.groupby('Department')

# Calculate mean for each group
print(grouped.mean())
#                   Age        Salary
# Department
# Finance      38.500000  72500.000000
# HR           31.500000  53500.000000
# IT           28.000000  56000.000000

# Calculate sum for each group
print(grouped.sum())

# Count elements in each group
print(grouped.count())

# Multiple aggregations
print(grouped.agg({
    'Age': 'mean',
    'Salary': ['mean', 'sum', 'count']
}))


# --- Group by Multiple Columns ---
df2 = pd.DataFrame({
    'Department': ['IT', 'IT', 'HR', 'HR', 'IT', 'HR'],
    'Gender': ['M', 'F', 'M', 'F', 'M', 'F'],
    'Salary': [50000, 60000, 55000, 52000, 58000, 54000]
})

grouped = df2.groupby(['Department', 'Gender'])
print(grouped.mean())

# =============================================================================
# PYTHON PRACTICE QUESTIONS - PANDAS 
# =============================================================================
'''
1. Create a pandas DataFrame from a dictionary
2. Read a CSV file into a DataFrame using pd.read_csv()
3. Display first/last N rows with head() and tail()
4. Select specific columns from a DataFrame
5. Filter rows based on a condition
6. Sort a DataFrame by one or more column values
7. Add a new column to a DataFrame (derived or constant)
8. Drop columns from a DataFrame using drop()
9. Handle missing values: check (isnull()), fill (fillna()), drop (dropna())
10. Get basic statistics and info using describe() and info()
'''