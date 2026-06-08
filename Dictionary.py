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