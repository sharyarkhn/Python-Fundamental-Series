# Local Variables and Global Variables in Python
# Variables in Python can be classified based on their scope (where they can be accessed).
# There are two types:
# 1. Local Variable
# 2. Global Variable




# 1. Local Variable
# A variable declared inside a function is called a Local Variable.
# It can only be accessed within that function.

# Example:
def something():

    a = 10      # Local Variable
    print("Inside Function:", a)

something()
### Output: Inside Function: 10



# Example:
###Note: Trying to access a local variable outside the function will result in an error.
def something():

    a = 10

something()
# print(a)
### Output:    NameError: name 'a' is not defined







# 2. Global Variable
# A variable declared outside all functions is called a Global Variable.
# It can be accessed from anywhere in the program.

## Example
a = 10
def something():

    print("Inside Function:", a)

something()
print("Outside Function:", a)

### Output
# Inside Function: 10
# Outside Function: 10



# Local and Global Variable with Same Name
# Every the Time local Have more Access then Global
## Example
a = 10
def something():

    a = 15
    print("Inside Function:", a)

something()
print("Outside Function:", a)

### Output
# Inside Function: 15
# Outside Function: 10
### Explanation






# Global Keyword:The `global` keyword is used when we want to modify a global variable inside a function.
# Note: Without `global`, Python creates a new local variable.
## Example Without global
a = 10
def something():
    a = 15
    print("Inside Function:", a)

something()
print("Outside Function:", a)
### Output
# Inside Function: 15
# Outside Function: 10
# The global variable remains unchanged.Beacuse we have not used global() key word.



## Example Using global
a = 10
def something():

    global a
    a = 15
    print("Inside Function:", a)

something()
print("Outside Function:", a)
### Output
# Inside Function: 15
# Outside Function: 15
### Explanation: The `global` keyword tells Python.
# "Use the global variable instead of creating a local variable."





# Accessing Both Local and Global Variables
# Sometimes we want to use both local and global variables.
## Example
a = 10
def something():

    a = 15
    print("Local a =", a)
    print("Global a =", globals()['a'])

something()
### Output
# Local a = 15
# Global a = 10





# globals() Function
# The `globals()` function returns a dictionary containing all global variables in the current program.
## Syntax
# globals()
### Example
a = 10
b = 20
print(globals())
### Output
# {
#  'a': 10,
#  'b': 20,
# }
# Since it returns a dictionary, values can be accessed using keys.




# Using globals()['variable_name']
## Example
a = 10
def something():

    x = globals()['a']
    print(x)

something()
### Output: 10



# Modifying a Global Variable Using globals()
## Example
a = 10
b = 21
def something():

    globals()['a'] = 50
    globals()['b'] = 25

something()
print(a)
print(b)
### Output: 50 , 35
### Explanation
# Since `globals()` returns a dictionary of global variables, we can update values directly through the dictionary.
