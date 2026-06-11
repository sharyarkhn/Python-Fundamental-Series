# # Copying NumPy Arrays
# When working with NumPy arrays, there are three ways to assign or copy arrays:
# 1. Aliasing
# 2. Shallow Copy
# 3. Deep Copy




# 1. Aliasing
# In aliasing, two variables refer to the same array object in memory.
# Any change made through one variable affects the other because both point to the same memory location.
## Example:
from numpy import *
arr1 = array([1, 2, 3, 4, 5])
arr2 = arr1
print(arr1) #[1 2 3 4 5]
print(id(arr1)) #140567890123456

print(arr2) #[1 2 3 4 5]
print(id(arr2)) #140567890123456

### Note
# Since both arrays have the same address, modifying one array will also modify the other.













# # 2. Shallow Copy (view())
# A shallow copy creates a new array object with a different address, but both arrays share the same data.
# Changes to the data in one array are reflected in the other.
## Example
from numpy import *
arr1 = array([1, 2, 3, 4, 5])
arr2 = arr1.view()
arr1[1] = 12
print(arr1)  #[ 1 12  3  4  5]

print(id(arr1)) #140567890123456
print(arr2) #[ 1 12  3  4  5]
print(id(arr2)) #140567890654321

### Note
# * Memory addresses are different.
# * Data is shared.
# * A change in one array affects the other.









# 3. Deep Copy (copy())
# A deep copy creates a completely independent copy of the array.
# Both the memory address and the data are separate.
# Changes made to one array do not affect the other.
## Example
from numpy import *
arr1 = array([1, 2, 3, 4, 5])
arr2 = arr1.copy()
arr1[1] = 12
print(arr1) #[ 1 12  3  4  5]

print(id(arr1)) #140567890123456
print(arr2) #[1 2 3 4 5]
print(id(arr2)) #140567890654321

### Note
# * Memory addresses are different.
# * Data is independent.
# * Changes in one array do not affect the other.









# What is the difference between view() and copy()?
# view()                           copy()                                 
# Creates a shallow copy           Creates a deep copy                    
# Shares data with original array  Creates independent data               
# Changes affect both arrays       Changes affect only the modified array 
# Faster                           Slightly slower                        




