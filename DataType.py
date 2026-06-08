# # Data Types in Python
# Data types define the type of data a variable can store in Python. 
# Different data types are used to store numbers, text, collections, 
# and key-value data. Python provides several built-in data types 
# such as:

# 1. None       (None)
# 2. Numeric    (int ,float ,complex)
# 3. Boolean    (bool)
# 4. Sequence   (List ,Tuple , set , String , Range)
# 5. Dictionary (dictionary)



#                         <<<<<<<<<<<<<<<< None >>>>>>>>>>>>>
# In python "None" is key word for not asssigned values like in java it is 
# null . we know every thinh in python is object so is is auto initialaize
# None means: no value , empty value,nothing assigned

x = None
print(x)










#                          <<<<<<<<<<<<<<<<<bool>>>>>>>>>>>>>>>>>>
a = True
print(a)
print(type(a))

a =2
b=4
c = a>b
print(c)


# True
# <class 'bool'>
# False

















                            # # <<<<<<<<<<<<<<<< Numeric >>>>>>>>>>>>>
# there are four types of it
# 1. int
# 2. float
# 3. complex
# 4. bool


# # <int>>>>>>>>>>>>>>>>>
x = 10
print(x)
print(type(x))
print(float(x))

# 5.5
# <class 'float'>



# <float>>>>>>>>>>>>>>>>>
y = 5.5
print(y)
print(type(y))
print(int(y))

# 5.5
# <class 'float'>



# <complex>>>>>>>>>>>>>>>>>>>>>
z = 2 + 3j
print(z)
print(type(z))

# we can make complex using two int 
x = 23
y = 3
print(complex(x,y))
print(complex(x))

# (2+3j)
# <class 'complex'>
# (23 + 3j)
# (23 + oj)













#                       <<<<<<<<<<<<<<<<<<<<Sequence>>>>>>>>>>>>>>>>>
# there are 5 types of it
# List
# Tuple
# set
# String 
# Range


# Mutable vs Immutable
# Mutable
# Values can be changed after creation.
# Example:
# List
# Set

# Immutable
# Values cannot be changed after creation.
# Example:
# Tuple
# String
# Range


# <List>>>>>>>>>>>>>>>>
# Repetation allowed 
# Mutable can ne edit
# can carry every type of data type(mix)
listEg = [12, "hello" , 3.4 , 23 , 12]
print(listEg)
print(listEg[0])
listEg[3] = 12
print(listEg)
print(type(listEg))



# <Set>>>>>>>>>>>>>>>>>>
# duplicates are removed
# items are unordered
# you cannot access items using indexes
setEg = {12,34,12,"sherry" , 3.04}
print(setEg)
# setEg[1] = 23 //cuz there is no proper indexing in set
setEg.add(21)
print(setEg)
print(type(setEg))



# <Touple>>>>>>>>>>>>>>>>>>>>>
# Repetation allowed 
# you cannot override any index
toupleEg = (12 ,12 ,"sherry" , 4.5)
print(toupleEg[2])
# toupleEg[1] = 13 //error touple do not support indexing in Python
print(toupleEg)
print(type(toupleEg))




# <str>>>>>>>>>>>>>>>>>>>>>
# you cannot override any index

doubleQuote1 = "hi i am sherry"
doubleQuote2 = """hello"""

singleQuote1 = 'she is so cute'
singleQuote2 = '''Learning Python  
is fun with  
Tpoint Tech'''  

print(len(singleQuote1))
print(doubleQuote1[0] , doubleQuote1[-1])
print(doubleQuote1[0:14])
print(doubleQuote1[:10])
print(doubleQuote1[10:])
x = doubleQuote1[::-1]
print(x)


# <Range>>>>>>>>>>>>>>>>>>>>
x = range(0,10)
r = range(10 , 20 , 2)

print(x)
print(r)
print(type(r))
print(list(r))
print(list(x))
print(set(x))






# <                  <<<<<<<<<<<<<<<<<Dictionary>>>>>>>>>>>>>>>>>>>>>>>>>>

# In Python, a dictionary stores data in key-value pairs.
# Think of it like a real dictionary:
# word → meaning
# key → value
# it is mutable


DicEg = {1:"sherry" , 2:23 , 3:34.45 , 4:"hyder"}
print(DicEg[1]) #sherry
# DicEg[0] #error this index can't exist
DicEg[2] = "nisar"
print(DicEg)


# if we use methods
print(DicEg.get(1))  
print(DicEg.get(0)) # no error None ll print
print(DicEg.get(0 , 'Noting found')) # we can print massage like this if nothing available there  





# i can make two list to dictiinary
keys = [1 , 3, 4]
values = ["sherry" , "khn" , "hyder"]
dic = dict (zip(keys,values))
print(dic)
# we can add and del value from it

dic[0] = "rehan"
print(dic)

del dic[0]
print(dic)




# More on dictionary 
# like:
# -> list in side dictionary 
# -> dictionary inside dictionary
prog = {'JS' : "Atom" , 'CS' : 'VS' , 'Python':['sublime' , 'Pycharm'] ,
         'JAVA' : {'JSE':'Netbeans' , 'JEE' : 'Eclipse'}}

print(prog)
print(prog['JS'])
print(prog['Python'])
print(prog['Python'][0])
print(prog['JAVA']['JSE'])
print(prog.keys())
print(prog.values())