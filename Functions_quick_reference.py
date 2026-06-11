from pandas import DataFrame, concat, merge
import numpy as np

# ==============================================================================
# 1. INITIALIZING DATA & MODIFYING DATAFRAMES
# ==============================================================================
# # # How to modify data in a DataFrame
# # # DataFrames are 2D labeled data structures with columns of potentially 
# # # different types. They accept standard Python dicts, NumPy arrays, or Series.

data = {
    "Name": ["Ram", "Shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance_Score": [85, 90, 78, 92, 88, 95, 80, 89]
}

df = DataFrame(data)
print("--- Initial Baseline DataFrame ---")
print(df)


# ==============================================================================
# 2. FEATURE ENGINEERING: ADDING NEW COLUMNS
# ==============================================================================
# # # Method A: Standard Bracket Assignment
# # # Syntax: df["New_Column_Name"] = array_like_data / scalar / expression
# # # This appends the new column implicitly to the end of the DataFrame structure.

df["Bonus"] = df["Salary"] * 0.1
print("\n--- Column Added via Bracket Notation (Bonus) ---")
print(df)

# # # Method B: Explicit Position Insert Method
# # # Syntax: df.insert(loc, column, value, allow_duplicates=False)
# # # Parameters:
# # # loc: int -> Index position where the column gets explicitly injected (0-indexed).
# # # column: str -> Target column name identifier string.
# # # value: array-like / scalar -> Data values populating the target coordinates.

df.insert(2, "Employee id", [10, 20, 30, 40, 50, 60, 70, 80])
print("\n--- Column Inserted at Index Position 2 (Employee id) ---")
print(df)


# ==============================================================================
# 3. COORDINATE TRANSFORMATION & UPDATING VALUES
# ==============================================================================
# # # Method A: Granular Label-Based Location Modification
# # # Syntax: df.loc[row_index, "Column_Name"] = new_value
# # # Explicitly targets a precise data coordinate using standard index identifiers.

df.loc[0, "Salary"] = 55000
print("\n--- Single Value Update via .loc[0, 'Salary'] ---")
print(df)

# # # Method B: Vectorized Broadcast Modification
# # # Syntax: df["Column_Name"] = df["Column_Name"] * scale_factor
# # # Modifies the continuous values across an entire structural column uniformly.

df["Salary"] = df["Salary"] * 1.5
print("\n--- Vectorized Column In-Place Scaling (Salary * 1.5) ---")
print(df)


# ==============================================================================
# 4. MEMORY CLEANUP & DELETING DATA METRICS
# ==============================================================================
# # # Dropping Data Columns
# # # Syntax: df.drop(labels=None, axis=0, index=None, columns=None, inplace=False)
# # # Parameters:
# # # columns: single label or list -> Names of explicit columns intended to be dropped.
# # # inplace: bool -> True overwrites original object; False yields a clean modified copy.

df.drop(columns=['Performance_Score'], inplace=True)
print("\n--- Column Dropped In-Place (Performance_Score Removed) ---")
print(df)


# ==============================================================================
# 5. DATA CLEANING: DETECTING MISSING VALUE VARIATIONS
# ==============================================================================
# # # Handling Missing Data Matrices
# # # Missing elements (None or np.nan) disrupt computational execution flows.

data_missing = {
    "Name": ["Ram", None, "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age": [28, 34, None, 30, None, 40, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance_Score": [85, 90, 78, 92, 88, 95, 80, 89]
}

df_nan = DataFrame(data_missing)
print("\n--- Baseline DataFrame with Structural Missing Values ---")
print(df_nan)

# # # Technique A: Coordinate-Wise Boolean Flags
# # # Syntax: df.isnull() or df.isna() -> Maps cell validations to boolean arrays.

print("\n--- Scalar Boolean Flag Matrix (.isnull()) ---")
print(df_nan.isnull())

# # # Technique B: Structural Aggregate Log Counts
# # # Syntax: df.isnull().sum() -> Collates aggregate totals per vertical structural column.

print("\n--- Cumulative Count of Missing Matrix Profiles (.isnull().sum()) ---")
print(df_nan.isnull().sum())


# ==============================================================================
# 6. RESOLUTION WORKFLOWS: REMOVING MISSING RECORDS
# ==============================================================================
# # # Dropping Missing Values from Memory
# # # Syntax: df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
# # # Parameters:
# # # axis: 0 or 'index' -> Deletes lines containing nan indexes.
# # # axis: 1 or 'columns' -> Deletes columns containing nan indexes.
# # # inplace: bool -> Overwrites underlying data directly when assigned True.

# Creating a fresh scratchpad workspace copy for manipulation
df_drop_col = df_nan.copy()
df_drop_col.dropna(axis=1, inplace=True)
print("\n--- Columns Drop Strategy (.dropna(axis=1)): Columns with NaN removed ---")
print(df_drop_col)

df_drop_row = df_nan.copy()
df_drop_row.dropna(axis=0, inplace=True)
print("\n--- Rows Drop Strategy (.dropna(axis=0)): Rows with NaN removed ---")
print(df_drop_row)

# Default behavior execution check: defaults directly to tracking axis=0
df_default_drop = df_nan.copy()
df_default_drop.dropna(inplace=True)


# ==============================================================================
# 7. IMPUTATION WORKFLOWS: FILLING MISSING OBSERVATIONS
# ==============================================================================
# # # Missing Value Imputation
# # # Syntax: df.fillna(value=None, method=None, axis=None, inplace=False)
# # # Replaces missing values with continuous baselines or structural descriptive statistics.

df_fill_static = df_nan.copy()
df_fill_static.fillna(1, inplace=True)
print("\n--- Scalar Value Imputation (.fillna(1)) ---")
print(df_fill_static)

# Imputing columns dynamically using calculated historical minima
df_fill_metric = df_nan.copy()
df_fill_metric['Age'] = df_fill_metric['Age'].fillna(df_fill_metric['Age'].min())
print("\n--- Descriptive Metric Imputation (Imputing Age with Column Minimum) ---")
print(df_fill_metric)


# ==============================================================================
# 8. ANALYTICAL WORKFLOWS: COGNITIVE INTERPOLATION VARIATIONS
# ==============================================================================
# # # Mathematical Interpolation Estimation
# # # Syntax: df.interpolate(method='linear', axis=0, limit_direction='forward', inplace=False)
# # # Best Practice Deployment Profiles:
# # # Used for: Sequential time-series configurations or numeric sequences exhibiting systemic trends.
# # # Avoid for: Arbitrary categorical string identifiers or random independent sequences.

time_series_data = {
    "Time": [1, 2, 3, 4, 5],
    "Values": [10.0, None, 30.0, None, 50.0]
}
df_time = DataFrame(time_series_data)
print("\n--- Unprocessed Continuous Sample Track ---")
print(df_time)

# --- Interpolation Mode 1: Linear Spline Strategy ---
# Treats missing points as equidistant values on a flat geometric line.
df_linear = df_time.copy()
df_linear['Values'] = df_linear['Values'].interpolate(method='linear')
print("\n--- Linear Spline Prediction Method ---")
print(df_linear)

# --- Interpolation Mode 2: Polynomial Modeling Strategy ---
# Requires order parameter; fits values along non-linear curves.
df_poly = df_time.copy()
df_poly['Values'] = df_poly['Values'].interpolate(method='polynomial', order=2)
print("\n--- Polynomial Spline Prediction Method ---")
print(df_poly)

# --- Interpolation Mode 3: Index-Based Time Optimization ---
# Interpolates data by tracking actual datetime distances or chronological index trends.
df_index_time = df_time.copy()
df_index_time['Values'] = df_index_time['Values'].interpolate(method='time')
print("\n--- Chronological Time-Dependent Optimization ---")
print(df_index_time)


# ==============================================================================
# 9. ORDER MANIPULATION: STRUCTURAL DATA SORTING
# ==============================================================================
# # # Sorting Rows by Axis Values
# # # Syntax: df.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort')
# # # Parameters:
# # # by: str or list of str -> Target names of vertical structural columns to sort by.
# # # ascending: bool or list of bools -> True orders elements upward; False descends.

sort_data = {
    "Name": ['Sherry', 'Nisar', 'Wasio'],
    "Age": [25, 29, 30],
    "Salary": [1000, 2000, 3000]
}
df_sort = DataFrame(sort_data)

df_sort.sort_values(by="Age", ascending=True, inplace=True)
print("\n--- Ascending Ordered Structure Matrix (Sorted by Age) ---")
print(df_sort)


# ==============================================================================
# 10. DESCRIPTIVE AGGREGATION ARCHITECTURES
# ==============================================================================
# # # Column-Wise Summary Mathematical Operations
# # # Functions scan across dimensions to compress observations into structural scalar metrics.

df_metrics = DataFrame({
    "Name": ['Sherry', 'Nisar', 'Wasio'],
    "Age": [25, 29, 30],
    "Salary": [1000, 2000, 3000]
})

print("\n--- Summary Performance Statistics: 'Age' Column Analysis ---")
print(f"Mean (Average Point) Value Log : {df_metrics['Age'].mean():.2f}")
print(f"Minimum Observed Coordinate    : {df_metrics['Age'].min()}")
print(f"Maximum Observed Coordinate    : {df_metrics['Age'].max()}")
print(f"Summed Vector Aggregation      : {df_metrics['Age'].sum()}")
print(f"Valid Elements Track Count     : {df_metrics['Age'].count()}")
print(f"Standard Deviation Dispersion   : {df_metrics['Age'].std():.4f}")


# ==============================================================================
# 11. DATA SPLITTING & GROUPBY VECTOR AGGREGATIONS
# ==============================================================================
# # # The Split-Apply-Combine Workflow Strategy
# # # Syntax: df.groupby(by=None, axis=0, level=None, as_index=True).sum()
# # # Splits rows across matching grouping flags before collapsing records mathematically.

df_group_source = DataFrame({
    "Name": ['Sherry', 'Nisar', 'Wasio', 'Narejo', 'shaikh'],
    "Age": [25, 29, 30, 25, 65],
    "Salary": [1000, 2000, 3000, 52000, 48000]
})

# --- Operation A: Single Matrix Field Grouping ---
grouped_single = df_group_source.groupby('Age')['Salary'].sum()
print("\n--- Single Column Sub-Grouping Matrix (Group by Age -> Sum Salary) ---")
print(grouped_single)

# --- Operation B: Multi-Dimensional Pivot Grouping ---
grouped_multi = df_group_source.groupby(['Age', 'Name'])['Salary'].sum()
print("\n--- Multi-Dimensional Sub-Grouping Matrix (Group by [Age, Name] -> Sum Salary) ---")
print(grouped_multi)


# ==============================================================================
# 12. RATIONAL DATABASE STRUCTURE MANIPULATION: MERGING & JOINS
# ==============================================================================
# # # Key-Based Structural Merges
# # # Syntax: merge(left, right, how='inner', on=None, left_on=None, right_on=None)
# # # Join Strategies via the 'how' parameter:
# # # inner: Retains overlapping keys across both components exclusively.
# # # outer: Retains all structural indices from both sides; fills cracks with NaN.
# # # left: Holds all indexes from original left frame; appends matching right components.
# # # right: Holds all indexes from original right frame; appends matching left components.
# # # cross: Generates a cartesian product matrix grid spanning all row variations.

df_customer = DataFrame({
    "Customer": ['Sherry', 'Nisar', 'Wasio'],
    "name_id": [1, 2, 3]
})

df_order = DataFrame({
    "Customer": ['Sherry', 'Nisar', 'Unknown_Client'], # Shared key mapping array
    "OrderAmount": [250, 450, 350]
})

# Executing Relational Configurations Evaluated Across Matching Keys
print("\n--- Relational Database Joining Operations Matrix ---")
print("\n[Inner Join View]")
print(merge(df_customer, df_order, on='Customer', how='inner'))

print("\n[Outer Join View]")
print(merge(df_customer, df_order, on='Customer', how='outer'))

print("\n[Left Join View]")
print(merge(df_customer, df_order, on='Customer', how='left'))

print("\n[Right Join View]")
print(merge(df_customer, df_order, on='Customer', how='right'))

print("\n[Cross Product Matrix View]")
print(merge(df_customer, df_order, how='cross'))


# ==============================================================================
# 13. DATA STACKING: CONCATENATION LIFECYCLES
# ==============================================================================
# # # Structural Object Concatenation
# # # Syntax: concat(objs, axis=0, join='outer', ignore_index=False)
# # # Operational Alignments:
# # # axis = 0 -> Vertical operation stacking blocks downward as row expansions.
# # # axis = 1 -> Horizontal operation stitching objects rightward as column expansions.

df_concat_A = DataFrame({
    "Name": ['Sherry', 'Nisar'],
    "name_id": [1, 2]
})

df_concat_B = DataFrame({
    "CustomerId": [1, 2],
    "OrderAmount": [250, 450]
})

# --- Stacking Axis Verification 1: Horizontal Column-Wise Stacking ---
con_axis1 = concat([df_concat_A, df_concat_B], axis=1, ignore_index=True)
print("\n--- Horizontal Structural Concatenation Matrix (axis=1) ---")
print(con_axis1)

# --- Stacking Axis Verification 2: Vertical Row-Wise Stacking ---
con_axis0 = concat([df_concat_A, df_concat_B], axis=0, ignore_index=True)
print("\n--- Vertical Structural Concatenation Matrix (axis=0) ---")
print(con_axis0)# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# # Function in python
# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# # 1. Function Introduction
# # 2. Defining and Calling Functions
# # 3. Function Arguments
# # 4. Actual and Formal Arguments
# # 5. Types of Arguments
# #      Position Arguments
# #      Keyword Arguments
# #      Default Arguments
# #      Variable Length Arguments
# # 6. Passing list as Arguments
# # 7. Pass by Value vs Pass by Reference
# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# # Python Functions and Arguments
# ## What is a Function?
# A function is a block of reusable code that performs a specific task.
# Functions help in:
# * Reducing code repetition
# * Improving readability
# * Making programs modular
# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# # Defining a Function
# A function is defined using the `def` keyword.
# def function_name():
#     statements
# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# ## Example
def greet():
    print("Hello World")

greet() # Hello World



# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# # Function with Parameters
# Parameters allow us to pass data into a function.
# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
def greet(name):
    print("Hello", name)

greet("Sherry") # Hello Sherry









# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# # Actual Argument and Formal Argument
# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>

# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# ## Formal Argument
# The variable written in the function definition is called a Formal Argument
# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
def greet(name):
    print(name)
# Here, `name` is a Formal Argument.

# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# ## Actual Argument
# The value passed during function call is called an Actual Argument.
# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
greet("Sherry")
# Here, `"Sherry"` is the Actual Argument.
# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>











# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# # Types of Arguments
# Python supports four types of arguments:
# 1. Position Arguments
# 2. Keyword Arguments
# 3. Default Arguments
# 4. Variable Length Arguments
# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>

# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# # 1. Position Arguments
# Values are assigned according to their position.
# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# ## Example
def person(name, age):
    print(name)
    print(age)
person("Sherry", 22)
# Sherry
# 22

# ### Wrong Order
person(22, "Sherry")
# 22
# Sherry
# The values are assigned based on position.


# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# # 2. Keyword Arguments
# Arguments are passed using parameter names.
# Order does not matter.
# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# ## Example
def person(name, age):
    print(name)
    print(age)
person(age=22, name="Sherry")
# Sherry
# 22

# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# # 3. Default Arguments
# A default value is assigned to a parameter.
# If no value is provided during function call, the default value is used.
# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# ## Example
def person(name, age=18):
    print(name)
    print(age)

person("Sherry")
# Sherry
# 18

# ### Overriding Default Value
person("Sherry", 22)
# Sherry
# 22


# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# # 4. Variable Length Arguments
# When the number of arguments is unknown, variable length arguments are used.
# They are represented using `*`.
# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# ## Example
def add(*nums):

    total = 0

    for i in nums:
        total += i

    print(total)

add(10, 20, 30) # 60

# ## Example with Different Number of Values
add(1, 2) #3
add(1, 2, 3, 4, 5) #15
# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>












# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# # Keyword Variable Length Arguments
# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
def person(**data):
    print(data)

person(name="Sherry", age=22, city="Delhi") #{'name': 'Sherry', 'age': 22, 'city': 'Delhi'}
# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>

# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# # Passing list as Arguments
def EvenOdd(lis):
    odd = 0
    even = 0

    for x in lis:
        if x%2==0:
            even+=x
        else:
            odd+=x
#     return odd , even


lis = (1,2,3,4,5,6,7,8,9,10)
even,odd = EvenOdd(lis)
print("Even = {} and Odd = {}".format(even,odd))            
# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>









# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# # Pass by Value and Pass by Reference
# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# Many languages support pass-by-value and pass-by-reference.
# Python works differently.
# Python uses **Object Reference Passing** (also called Pass-by-Assignment).
# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>

# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# # Example with Immutable Object
# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
def update(x):
    x = 8
    print("Inside Function:", x)

a = 10
update(a)
print("Outside Function:", a)
# Inside Function: 8
# Outside Function: 10
# The original value remains unchanged.

# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# # Example with Mutable Object
# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
def update(lst):
    lst.append(100)

nums = [10, 20, 30]
update(nums)
print(nums)
# [10, 20, 30, 100]
# The original list changes because lists are mutable.


# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
# Note: Python is neither strictly pass-by-value nor pass-by-reference.
# Python uses Pass by Object Reference or Pass by Assignment

# The function receives a reference to the same object.
# Behavior depends on whether the object is:
# * Immutable (int, float, str, tuple)
# * Mutable (list, set, dictionary)
# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>