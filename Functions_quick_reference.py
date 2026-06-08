# <<<<<<<<<<<<>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>
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