# Taking Input from User
# The input() function is used to take input from the user.
# By default, input is stored as a string (str).


name = input("Enter your name: ")
print(name)
print(type(name))




# when we wanna use any int or float we would type cast it first 
# cuz input() function always gives str as input 
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = x+y
print(z)




# How can we input char 
ch = input("Enter char: ")[0] # we will give index here we input fun gives str as input
# it means user can enter many char he want, so using index we will use the specific one
print(ch)



# What if user input any Equation like x + y * z
# then we have a function called eval() which solve it auto
result = eval(input("Enter the Equation: "))
print(result)

