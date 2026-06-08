# Variables in Python
# A variable is a name used to store data in memory.
# Think of it like a container holding a value.

num1 = 3
print(num1)
print(id(num1))

num2 = num1
print(num2)
print(id(num2))

num3 = 3
print(num3)
print(id(num3))


# ## Explanation
# * In Python, variables store references to objects.
# * If multiple variables contain the same immutable value (like integers, strings, etc.), Python may give them the same reference (same memory address).


# Example:
num1 = 3
num2 = num1
num3 = 3
# Here, `num1`, `num2`, and `num3` may all point to the same
#  object in memory, so `id()` can return the same value.





## Important Point
# # If we assign one variable to another:
num2 = num1
# then `num2` refers to the same object as `num1`.
# But if we later change `num2`:
num2 = 10
# it does NOT affect `num1`.

# Reason:
# * Python creates a new object for `10`.
# * `num2` now points to the new object.
# * `num1` still points to `3`.
# Example:

num1 = 3
num2 = num1
num2 = 10
print(num1)   # 3
print(num2)   # 10

## Conclusion
# * Variables in Python are references to objects.
# * Same values can share the same reference.
# * Reassigning a variable changes its reference only, not the other variables.
# * Python executes code from top to bottom.
# * if any memory is not pointing any variable which is avaible in the heap it 
# will garbage collected leater