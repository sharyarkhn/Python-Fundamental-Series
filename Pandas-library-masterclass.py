# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# PANDAS CORE DEFINITIONS AND FEATURES
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# # # Pandas
# # # Pandas is an open-source data manipulation
# # # library for Python. It is built on top of 
# # # the NumPy library. It introduces two primary 
# # # data structures: Series and DataFrame. A Series is 
# # # one-dimensional labeled data, whereas a DataFrame is 
# # # two-dimensional labeled data resembling a table.

# # # Key Features:
# # # Pandas features DataFrame and Series data structures for handling 
# # # two-dimensional tabular data and one-dimensional arrays.

# # # Pandas offers specialized tools for working with
# # # time series data.

# # # Pandas includes tools for handling missing data, duplication, 
# # # and other data cleaning tasks.


# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
#         WHAT IS A DATAFRAME AND SERIES WITH PRACTICAL ACTIONS
#           Use of Head tail info discription type methods
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# # What is a DataFrame and a Series, and how do we perform actions on them?
# # ////////////////////////////////////////////////////////////////////////////
# # Age FirstName LastName
# # 18   Sherry     khn
# # 20   Nisar      Ahmed
# # 25   Hasaan     Ahmed
# #
# # We call this simple data because it looks like standard Excel table data.
# #
# # However, when we use the Pandas library to read it, it converts it by default 
# # into a specific data structure that we call a DataFrame.
# #
# # It contains row indices, column indices, and the structured data elements.
# # ////////////////////////////////////////////////////////////////////////////

# Example:
from pandas import *
from numpy import *

data = arange(1,21).reshape(5,4)
index = ["Row1" , "Row2" , "Row3" , "Row4" ,"Row5"]
columns = ["Column1" , "Column2" , "Column3" , "Column4"] 
dataFrame = DataFrame(data=data , index=index , columns=columns)
print(dataFrame)
#       Column1  Column2  Column3  Column4
# Row1        1        2        3        4
# Row2        5        6        7        8
# Row3        9       10       11       12
# Row4       13       14       15       16
# Row5       17       18       19       20

print(dataFrame.head()) # It returns the top 5 records
print(dataFrame.tail()) # It returns the last 5 records
print(type(dataFrame))  # <class 'pandas.DataFrame'>
print(dataFrame.info()) # It provides concise schema and data type information
print(dataFrame.describe()) # It calculates basic summary statistics





# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
#                                    Indexing 
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# 1. Column Name Selection
# 2. Row Index Selection using .loc
# 3. Positional Integer Slicing for Rows and Columns using .iloc
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# Note: If we extract a single row or column, it returns a Series structure.
# If we extract more than one row or column, it returns a DataFrame structure.


# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# Using column names: xyz['column']
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
print(dataFrame['Column1']) # For a single column, we use a single set of brackets []
print(type(dataFrame['Column1'])) # <class 'pandas.Series'>

print(dataFrame[['Column1' , 'Column2' , 'Column3']]) # For multiple columns,
# we must use double sets of brackets [[]]
print(type(dataFrame[['Column1' , 'Column2' , 'Column3']]))
# <class 'pandas.DataFrame'>



# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# Using row label methods: loc['row'] 
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
print(dataFrame.loc['Row2']) # Accessing a single row yields a Series structure
print(dataFrame.loc[['Row1' , 'Row2' ,'Row3']]) # Accessing multiple row labels


# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# Position-based index slicing: .iloc[row_index, column_index]
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# Note that during slicing, the stop index boundary is exclusive.
# For example, to retrieve up to index position 5, we must specify index 6.
print(dataFrame.iloc[0:3 , 1:3])
print(dataFrame.iloc[0: , 2:])
print(dataFrame.iloc[: , 1:])


# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# To extract the underlying data as a raw array, append the .values attribute 
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# to the end of the statement.
arrSingle = dataFrame['Column1'].values
print(arrSingle) # [ 1  5  9 13 17]
arrMul = dataFrame.iloc[0:2 , 0:2].values
print(arrMul)
# [[1 2]
#  [5 6]]
print(dataFrame.isnull()) # Evaluates null statuses for individual elements across columns
print(dataFrame.isnull().sum()) # Computes missing value counts across the DataFrame rows.
# If an element is missing, it registers as a 1; otherwise, it records a 0.


# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# AUDITING, CLEANING, AND BOOLEAN FILTERING
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
from pandas import*
from numpy import*

dataFrame2 = DataFrame(data=[[1,nan,3] , [4,5,6]] , index=['Row1','Row2'] , columns=['Column1' , 'Column2' ,'Column3'])
print(dataFrame2)
print(dataFrame2.isnull())
print(dataFrame2.isnull().sum())
print(dataFrame2.isnull().sum()==0)

print(dataFrame2['Column1'].value_counts())
print(dataFrame2['Column1'].unique())

print(dataFrame2>2)
print(dataFrame2['Column1']>2)











# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# READING COMMA SEPARATED VALUES (CSV) & STRINGIO OPERATORS
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<  
# # How do we read comma-separated files?
# # We can parse multiple file variations using Pandas, including JSON, Excel, CSV, and HTML formats.


# #>>>>>>>>> How to read CSV files using pandas.read_csv >>>>>>>>>>>>>>>>>>>>>>
# When we load an external file like a CSV, Pandas converts its contents into an internal 
# data structure called a DataFrame. Behind the scenes, processing text data directly 
# often requires utilizing a StringIO object.
# What is a StringIO format? It serves as an in-memory stream file object that holds text records.

from io import StringIO
from pandas import *

data = ('Column1,Column2,Column3\n''x, y , 1\n''a,b,2\n''p,q,3')
print(type(data))
# In-memory file format object creation
data = StringIO(data)
print(type(data))
print(read_csv(data))

file = arange(0,20).reshape(4,5)
data = ('Column1,Column2,Column3\n''x, y , 1\n''a,b,2\n''p,q,3')
file = StringIO(data)
print(read_csv(file , usecols=['Column1' , 'Column2']))
dataFram = type(read_csv(file , usecols=['Column1' , 'Column2']))
print(dataFram)

# Note: If we extract columns from an external file source using the workflow above, it produces a DataFrame.
# To convert that structure back out to a flat file, we apply the .to_csv method.
# csvFile = to_csv('Data.csv')
# Specifying index=False prevents Pandas from exporting the automatic numeric row identifiers.
# csvFile = to_csv('Data.csv' , index = False)


# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# IMPLICIT AND EXPLICIT DATA TYPE ASSIGNMENT (DTYPE) & INDEXING
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
data = ('Column1,Column2,Column3\n''x, y , 1\n''a,b,2\n''p,3')
data = StringIO(data)
# df = read_csv(data)
# print(type(df))
# print(df.info())

# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# We can implicitly assign a universal structural type during parsing:
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
dff = read_csv(data , dtype = 'str')
print(type(dff))
print(dff.info())
print(dff.head())


data = ('Column1,Column2,Column3\n''x, y , 1\n''a,b,2\n''p,3')
data = StringIO(data) # Parsing as CSV text
df = read_csv(data)
print(df.isnull())
print(df.isnull().sum())

# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# We can also explicitly target individual columns with unique data types using a dictionary map:
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
text = ('Column1,Column2,Column3,Column4\n''1,2,3,4\n''5,6,7,8\n''a,b,c,d')
fileCsv = StringIO(text)
print(type(fileCsv))
df = read_csv(fileCsv , dtype={'Column1':str , 'Column2':str})
print(type(df))
print(df.info())


# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# What if we want to override or discard the default numerical index entirely?
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
text = ('index,Column2,Column3,Column4\n''1,2,3,4\n''5,6,7,8\n''a,b,c,d')
fileCsv = StringIO(text)
df = read_csv(fileCsv , index_col=False)
print(df)


text = ('index,Column2,Column3,Column4\n''1,2,3,4\n''5,6,7,8\n''a,b,c,d')
fileCsv = StringIO(text)
# Modifying index configurations while filtering down attributes:
X = read_csv(fileCsv , usecols=['Column2' , 'Column3'] , index_col=False)
print(X)
# # # Remember, setting index_col=False preserves the standard auto-generated numeric index 
# # # while only returning the target attributes specified inside usecols. 
# # # However, setting index_col=0 converts the very first chosen attribute (Column2) into 
# # # the actual row tracking index labels, removing the default sequential numbering.
Y = read_csv(fileCsv , usecols=['Column2' , 'Column3'] , index_col = 0)
print(Y)


# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# Example structure for file round-trips:
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
from pandas import read_csv
D = read_csv('/media/sherry/Personal/python-series/practice.csv', sep=',')
D.to_csv('xyz.csv', index=False)
print(D.head())




















# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# WORKING WITH JSON FILES AND CONVERTING SCHEMAS
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# How to work with JSON files
# Remember: JSON key-value text maps must be enclosed within single quotes as a Python string.
# To transform raw JSON strings into a target DataFrame, we route them through a StringIO buffer first.
# Working with JSON structures helps us interface smoothly with NoSQL engines like MongoDB.

from numpy import*
from pandas import*
from io import StringIO
import json

# # Example:
data = '{"employee_name": "James","email": "james@gmail.com", "job_profile": [{"title1": "Team Lead","title2": "Senior Developer"}]}'
print(type(data))  # <class 'str'>
dform1 = read_json(StringIO(data)) # Converts directly to DataFrame
print(dform1)

# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# # We can isolate nested elements out of a complex JSON string and convert them 
# # into standalone DataFrames using the following step-by-step workflow:
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
obj = json.loads(data) # Parse the raw JSON text into a Python dictionary object
data2 = obj["job_profile"] # Isolate the target internal nested list array
print(data2)
data2 = json.dumps(data2) # Serialize the target object back into a valid JSON string format
dform2 = read_json(StringIO(data2)) # Load the final string structure directly into a DataFrame
print(dform2)


# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# Understanding structural orientations (orient) during JSON import processing:
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
data = '{"employee_name": "James","email": "james@gmail.com", "job_profile": [{"title1": "Team Lead","title2": "Senior Developer"}]}'
# Setting orient='records', orient='columns', or orient='values' produces closely aligned output 
# configurations here because Python structurally interprets this layout pattern as record blocks.
X = read_json(StringIO(data) , orient='records')
# X = read_json(StringIO(data) , orient='columns')
# X = read_json(StringIO(data) , orient='values')
print(X)


# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# If we change the configuration to orient='index', the parent keys are restructured into row identifiers:
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
Y = read_json(StringIO(data) , orient='index')
print(Y)


# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# Conversely, we can serialize structured DataFrames back out into explicit JSON text strings:
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
df = DataFrame(data = [[1,2,3] , [4,5,6] , [7,8,9]],index=['row1','row2','row3'] , columns = ['col1','col2','col3'])
jstr = df.to_json() # Default behavior prioritizes column keys, matching orient='columns' format.
print(jstr) 
# {"col1":{"row1":1,"row2":4,"row3":7},"col2":{"row1":2,"row2":5,"row3":8},"col3":{"row1":3,"row2":6,"row3":9}}
print(type(jstr))


# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# # # Using orient='index' shifts serialization priority to index positions as primary keys:
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
jstr2 = df.to_json(orient='index')
print(jstr2)#{"row1":{"col1":1,"col2":2,"col3":3},"row2":{"col1":4,"col2":5,"col3":6},"row3":{"col1":7,"col2":8,"col3":9}}

# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# # # Using orient='values' outputs only raw inner data values, stripping structural metadata:
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
jstr2 = df.to_json(orient='values')
print(jstr2) #[[1,2,3],[4,5,6],[7,8,9]]

# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# # # Using orient='records' ignores row indexes completely and outputs a list of column-mapped dictionaries:
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
jstr2 = df.to_json(orient='records')
print(jstr2)# [{"col1":1,"col2":2,"col3":3},{"col1":4,"col2":5,"col3":6},{"col1":7,"col2":8,"col3":9}]

# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# # Using orient='split' isolates metadata by partitioning components into separate arrays:
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
jstr2 = df.to_json(orient='split')
print(jstr2)#{"columns":["col1","col2","col3"],"index":["row1","row2","row3"],"data":[[1,2,3],[4,5,6],[7,8,9]]}

# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# # Using orient='table' encapsulates schemas along with records to form comprehensive tables:
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
jstr2 = df.to_json(orient='table')
print(jstr2)#{"schema":{...},"data":[{"index":"row1","col1":1,"col2":2,"col3":3},...]}


# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# We can reconstruct unstructured text representations back into clean DataFrames at any time:
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
schema = '{"col1":{"row1":1,"row2":4,"row3":7},"col2":{"row1":2,"row2":5,"row3":8},"col3":{"row1":3,"row2":6,"row3":9}}'
df = read_json(StringIO(schema) , orient='columns') # Matching layout structure with original column tracking
print(df)
#       col1  col2  col3
# row1     1     2     3
# row2     4     5     6
# row3     7     8     9


# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# File path execution handling notes:
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
D = read_csv('/media/sherry/Personal/python-series/xyz.csv', sep=',')
jsonF = D.to_json('json.json' , index=False)
# Crucial Note: The .to_json() method returns None when a target export filename path is provided.
# It writes data straight to disk. Attempting to call print(jsonF) or print(jsonF.head()) 
# causes errors since a NoneType object lacks printable text attributes.

# To write out data assets to external locations safely while continuing active terminal audits:
D = read_csv('/media/sherry/Personal/python-series/xyz.csv')
D.to_json('json.json')
print(D.head())


# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# WORKING WITH NESTED STRINGS NATIVELY (JSON_NORMALIZE)
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# # Working with json_normalize() 
# # Standard file engines struggle to parse deep multi-tier hierarchical JSON inputs.
# # When lists contain nested dictionaries, json_normalize() untangles those multi-level 
# # objects into distinct, separate column variables.

data = [{"id": 1, "name": "Cole Volk", "fitness": {"height": 130, "weight": 60}}, {"name": "Mark Reg", "fitness": {"height": 130, "weight": 60}}, {"id": 2, "name": "Faye Raker", "fitness": {"height": 130, "weight": 60}}]
print(json_normalize(data))
#     id        name  fitness.height  fitness.weight
# 0  1.0   Cole Volk             130              60
# 1  NaN    Mark Reg             130              60
# 2  2.0  Faye Raker             130              60

# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# If we want to restrict parsing depth to a certain depth layer, we pass the max_level argument.
# For example, max_level=0 reads root elements only and does not unpack nested objects inside.
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
print(json_normalize(data, max_level=0))

# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# What if records contain primary object keys paired with nested child list tracks?
# We can tell the function to target an isolated node array by defining its key directly as an argument,
# though this action initially omits parent elements.
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
data = [{"state": "Florida", "shortname": "FL", "info": {"governor": "Rick Scott"}, "counties": [{"name": "Dade", "population": 12345}, {"name": "Broward", "population": 40000}, {"name": "Palm Beach", "population": 60000}]}, {"state": "Ohio", "shortname": "OH", "info": {"governor": "John Kasich"}, "counties": [{"name": "Summit", "population": 12344}, {"name": "Cuyahoga", "population": 1337}]}]
print(json_normalize(data, "counties"))
#          name  population
# 0        Dade       12345
# 1     Broward       40000
# 2  Palm Beach       60000
# 3      Summit       12344
# 4    Cuyahoga        1337

# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# To reconstruct relationship tracks, map out parent keys using the meta parameter:
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
print(json_normalize(data, "counties" , ["state" , "info"]))
#          name  population    state                         info
# 0        Dade       12345  Florida   {'governor': 'Rick Scott'}
# 1     Broward       40000  Florida   {'governor': 'Rick Scott'}
# 2  Palm Beach       60000  Florida   {'governor': 'Rick Scott'}
# 3      Summit       12344     Ohio  {'governor': 'John Kasich'}
# 4    Cuyahoga        1337     Ohio  {'governor': 'John Kasich'}

# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# If a metadata source key contains nested dictionary objects, we extract the inner fields 
# by wrapping the parent node and the child item together inside a list array:
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
print(json_normalize(data, "counties", ["state", ["info", "governor"]]))
#          name  population    state info.governor
# 0        Dade       12345  Florida    Rick Scott
# 1     Broward       40000  Florida    Rick Scott
# 2  Palm Beach       60000  Florida    Rick Scott
# 3      Summit       12344     Ohio   John Kasich
# 4    Cuyahoga        1337     Ohio   John Kasich





















# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# WORKING WITH MICROSOFT EXCEL WORKBOOKS (READ_EXCEL & TO_EXCEL)
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# Working with Excel Files (read_excel & to_excel)
# Pandas provides native support for reading and writing Microsoft 
# Excel formats (.xls, .xlsx, .xlsm). Under the hood, Pandas relies on 
# external engines like openpyxl (for .xlsx) and xlrd (for legacy .xls files).
import pandas as pd


# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# A:Mock data resembling an Excel table
# To export an in-memory DataFrame into an Excel spreadsheet, use the 
# .to_excel() method.
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
excel_data = pd.DataFrame({
    'Employee_ID': [101, 102, 103],
    'Name': ['Sherry', 'Nisar', 'Hasaan'],
    'Department': ['Data Science', 'Development', 'Design']
})
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# Basic Export: index=False drops the default numeric row indexing column
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
excel_data.to_excel('Company_Data.xlsx', index=False)

# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# Exporting to a specific worksheet name within the workbook.
# By default, worksheets are automatically named Sheet1, Sheet2, etc.
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
excel_data.to_excel('Company_Data.xlsx', sheet_name='Quarter_1_Data', index=False)



# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# B. Reading Data From Excel (read_excel)
# By default, pd.read_excel() will only scan and extract data 
# from the first worksheet (Index 0) of your workbook unless 
# explicitly told otherwise.
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# Read the first sheet by default
df_default = pd.read_excel('Company_Data.xlsx')

# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# Read a specific sheet by its explicit string name
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
df_sheet_name = pd.read_excel('Company_Data.xlsx', sheet_name='Quarter_1_Data')

# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# Read a specific sheet using its integer index position (0-indexed)
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
df_sheet_index = pd.read_excel('Company_Data.xlsx', sheet_name=0)





# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# C. Advanced read_excel Parameters
# When dealing with massive or poorly structured spreadsheets, loading the entire file
# can strain system memory. Use these structural parameters to fine-tune your data 
# import pipelines:
# 1. usecols
# 2. skiprows
# 3. nrows
# 4. na_values
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
df = pd.DataFrame({
    'Name': ['Ali', 'Sara', 'John', 'Ahmed', 'Maria'],
    'Age': [25, 30, 28, 35, 29],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'HR'],
    'Salary': [50000, 60000, 55000, 70000, 62000]
})
df.to_excel('practice.xlsx', index=False)



# <<<<<<>>>>>><<<<<<<<<<>>>>>><<<<<<<<<<>>>>>><<<<<<<<<<>>>>>><<<<
# 1. usecols
# Selects only specific columns.
# We can target columns by index using Excel letter blocks (e.g., 'A:C').
# <<<<<<>>>>>><<<<<<<<<<>>>>>><<<<<<<<<<>>>>>><<<<<<<<<<>>>>>><<<<
# Example: Using column letters
df = pd.read_excel(
    'practice.xlsx',
    usecols='A:C'
)
print(df)
#     Name  Age Department
# 0    Ali   25         IT
# 1   Sara   30         HR
# 2   John   28    Finance
# 3  Ahmed   35         IT
# 4  Maria   29         HR
# <<<<<<>>>>>><<<<<<<<<<>>>>>
# Example: Using column names
# <<<<<<>>>>>><<<<<<<<<<>>>>>
df = pd.read_excel(
    'practice.xlsx',
    usecols=['Name', 'Salary']
)
print(df)



# <<<<<<>>>>>><<<<<<<<<<>>>>>><<<<<<<<<<>>>>>><<<<<<<<<<>>>>>><<<<
# 2. skiprows
# Skips a specified number of rows from the top before parsing data. 
# This is useful when spreadsheets contain top-level titles or metadata notes.
# The first row read after the skip boundary is treated as the column header layout
# <<<<<<>>>>>><<<<<<<<<<>>>>>><<<<<<<<<<>>>>>><<<<<<<<<<>>>>>><<<<
df = pd.read_excel(
    'practice.xlsx',
    skiprows=2
)
print(df)
#     Sara  30       HR  60000
# 0   John  28  Finance  55000
# 1  Ahmed  35       IT  70000
# 2  Maria  29       HR  62000


# <<<<<<>>>>>><<<<<<<<<<>>>>>><<<<<<<<<<>>>>>><<<<<<<<<<>>>>>><<<<
# 3. nrows
# Limits the absolute number of data rows loaded into system memory.
# <<<<<<>>>>>><<<<<<<<<<>>>>>><<<<<<<<<<>>>>>><<<<<<<<<<>>>>>><<<<
df = pd.read_excel(
    'practice.xlsx',
    nrows=3
)
print(df)
#    Name  Age Department  Salary
# 0   Ali   25         IT   50000
# 1  Sara   30         HR   60000
# 2  John   28    Finance   55000


# <<<<<<>>>>>><<<<<<<<<<>>>>>><<<<<<<<<<>>>>>><<<<<<<<<<>>>>>><<<<
# 4. na_values
# Converts designated custom text flags directly into operational NaN objects.
# <<<<<<>>>>>><<<<<<<<<<>>>>>><<<<<<<<<<>>>>>><<<<<<<<<<>>>>>><<<<
df = pd.read_excel(
    'practice.xlsx',
    na_values=['N/A', 'Missing']
)

# Combined Parameter Slicing Example:
df_com = pd.read_excel(
    'practice.xlsx',
    sheet_name=0,
    usecols=['Name', 'Department'],
    nrows=5,
    skiprows=0
)
print(df_com)
#     Name Department
# 0    Ali         IT
# 1   Sara         HR
# 2   John    Finance
# 3  Ahmed         IT
# 4  Maria         HR




# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# MULTI-SHEET WORKBOOK GENERATION (EXCELWRITER)
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
excel_data = pd.DataFrame({
    'Name': ['sherry', 'nisar', 'wasio', 'hasaan', 'mujeeb'],
    'Age': [25, 30, 28, 35, 29],
    'Department': ['Development', 'Data Science', 'Data Science', 'Development', 'Data Science'],
    'Salary': [50000, 60000, 55000, 70000, 62000]
})
# <<<<<<>>>>>><<<<<<<<<<>>>>>><<<<<<<<<<>>>>>><<<<<<<<<<>>>>>><<<<
# D. Multi-Sheet Operations using ExcelWriter
# If you attempt to write multiple DataFrames sequentially using basic .to_excel() statements, 
# Pandas will constantly overwrite the physical file, saving only the final command output.
# <<<<<<>>>>>><<<<<<<<<<>>>>>><<<<<<<<<<>>>>>><<<<<<<<<<>>>>>><<<<

# To safely save multiple sheets into a single, cohesive workbook, utilize the pd.ExcelWriter() 
# context manager.
df_dev = excel_data[excel_data['Department'] == 'Development']
df_ds = excel_data[excel_data['Department'] == 'Data Science']

# This context block commands the engine: "Open a new target spreadsheet asset named Department_Reports.xlsx 
# and expose a functional processing interface handle called writer that can safely route independent sheets."
with pd.ExcelWriter('Department_Reports.xlsx', engine='openpyxl') as writer:
    df_dev.to_excel(writer, sheet_name='Development_Team', index=False)
    df_ds.to_excel(writer, sheet_name='Data_Science_Team', index=False)


