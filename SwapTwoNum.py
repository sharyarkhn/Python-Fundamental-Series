# Swap Two variable with the help of third variable
x = 2
y = 4
print("x: ",x," y:",y)

temp = x 
x = y 
y = temp
print("x: ",x," y:",y)



# Swap Two variable without any help of third variable
x = x^y
y = x^y
x = x^y 
print("x: ",x," y:",y)



# More good way without any loss of extra bit
x = x^y
y = x^y
x = x^y 
print("x: ",x," y:",y)




# but in python we have a magic to do this in one line
x,y = y,x  #thats it
print("x: ",x," y:",y)
