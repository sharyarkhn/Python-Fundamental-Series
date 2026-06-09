# Keyword Variable Length Arguments (**kwargs)
# Keyword Variable Length Arguments allow a function to accept any number of keyword arguments.
# The `**kwargs` syntax collects all keyword arguments into a dictionary.
# * `kwargs` stands for **Keyword Arguments**.
# * The name `kwargs` is a convention; you can use any valid variable name after `**`.

## Syntax
# def function_name(**kwargs):
#     statements

## Example
def person(**data):
    print(data)

person(name="Sherry", age=22, city="Delhi")
### Output
# {'name': 'Sherry', 'age': 22, 'city': 'Delhi'}
# Since `**kwargs` creates a dictionary, we can access keys and values just like a normal dictionary.




# Printing Using a For Loop
def person(**data):

    for key, value in data.items():
        print(key, ":", value)

person(name="Sherry", age=22, city="Delhi")
### Output
name : Sherry
age : 22
city : Delhi



# Another Example
def student(**details):

    for key, value in details.items():
        print(f"{key} = {value}")

student(name="Ali", age=20, course="Python")
### Output
# name = Ali
# age = 20
# course = Python






# Difference Between *args and **kwargs
# | Feature        | *args                | **kwargs              |
# | -------------- | -------------------- | --------------------- |
# | Stores Data In | Tuple                | Dictionary            |
# | Accepts        | Positional Arguments | Keyword Arguments     |
# | Symbol         | *                    | **                    |
# | Example        | add(1,2,3)           | person(name="Sherry") |


### Example
# def demo(*args, **kwargs):

#     print("Args:", args)
#     print("Kwargs:", kwargs)

# demo(10, 20, 30, name="Sherry", age=22)
# ### Output
# Args: (10, 20, 30)
# Kwargs: {'name': 'Sherry', 'age': 22}