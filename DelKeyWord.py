# In Python, the del keyword is used to delete objects, 
# variables, or items from collections like lists and dictionaries.


x = 23
print(x)
del x
# print(x) not defined error


listEg = [23,43.45, 34,5,2]
del listEg[1]
print(listEg)


dicEg = {0:12 , 1:34 , 2:"pookie"}
del dicEg[2]
print(dicEg)