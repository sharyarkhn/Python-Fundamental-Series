# Arrays in Python: An array is a collection of elements of the same data type stored under a single variable name.
# Arrays are useful when you need to store many values of the same type efficiently.We used array instead of creating 
# multiple same data type variable again and again.we use array there do that in one time.

# like:

# Instead of: 
# a = 10 b = 20  c = 30
# Use: 
# from array import *
# arr = array('i', [10, 20, 30])


# Chart To use array proper
# Type 	C Type	        Python Type	        Min. Size (Bytes)
# 'b'	signed char	    int	                1
# 'B'	unsigned char	int	                1
# 'u'	Py_UNICODE	    Unicode character	2
# 'h'	signed short	int	                2
# 'H'	unsigned short	int	                2
# 'i'	signed int	    int	                2
# 'I'	unsigned int	int	                2
# 'l'	signed long	    int	                4
# 'L'	unsigned long	int	                4
# 'f'	float	        float               4
# 'd'	double	        float	            8




# Creating an Array in Python
# To create an array in Python, you need to import the array module and then define the array 
# using a specific data type (typecode) along with initial values. This allows you to store 
# multiple elements of the same type in a single variable.

# Syntax:
# from array import *  
# arrayName = array(typecode, [initializers])   

# Example:
from array import *  
arr = array('i', [85, 90, 78, 92, 88])  
  
for m in arr:  
    print(m)  

# Array Properties:
print(arr.typecode) #Type Code
print(len(arr)) #Length
print(arr.buffer_info()) #Buffer Info (memory_address, length)







# Accessing Elements:
arr = array('i', [12, 34, 56])

print(arr[0])
print(arr[1])

# Output:
# 12
# 34


# Traversing an Array
# Using For Loop:
for i in arr:
    print(i)

# Using Index
for i in range(len(arr)):
    print(arr[i])

# Updating Elements:
arr[1] = 100
print(arr)








# Taking Input into Array:

from array import *

arr = array('i', [])
n = int(input("Enter size: "))
for i in range(n):
    x = int(input("Enter value: "))
    arr.append(x)

print(arr)




# Copying an Array:
newArr = array(arr.typecode, (a for a in arr))
print(newArr)







# # Searching an Element:
from array import*
arr = array('i' , [1,2,3,4,5,6])
search = int(input("Enter thr number you wanna search: "))

ind = 0
for x in arr: #without using any builten fun
    if search == x:
        print(ind)
        break
    ind+=1

print(arr.index(search)) #uding function





# Character Array using array:

from array import *
chars = array('u', "Sherry")
for x in chars:
    print(x)
