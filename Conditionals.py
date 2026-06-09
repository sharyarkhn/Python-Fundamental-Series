# Python if-else Statements (Conditional Statements)
# In Python, conditional statements are used to make decisions based on conditions. 
# They execute the different blocks of code depending on whether a condition is True or False.

# Python conditional (if else) statements are used to make decisions in a program.
# They allow the program to check a condition and choose what to do next based on whether
# the condition is True or False. If the condition is True, the code inside the if block runs. 
# If it is False, the code insidethe else block runs.This helps control the flow 
# of the program and makes it behave differently in different situations.

# Python provides support for the following types of conditional statements:
# if statement
# if-else statement
# Nested if statement
# if-elif-else statement


# Multiple if bloack
if True: 
    print("Hello")

x = 1
if x>0:
    print("True")
print("Out side") # this is not the part of condition cuz of not matching the spaces with upper
# ont not down : it will only be part of it when we use equal spaces, good practice is to use 
# tab (4 spaces).








# if-else
x = 12
if x>45:
    print("hello there")
else:
    print("Got the idea!!")








# we can check multiple conditions using elif 
x = 2
if x==1:
    print("it's 1")
elif x==2:
    print("it's 2")
elif x==3:
    print("it's 3")
elif x==4:
    print("it's 4")
else:
    print("Got the idea!!") 







# we can use nested if-else
x = 24
if x>10:
    print("it's 1")
    if x%2==0:
        print("it's even and greater than 10")
    else:
        print("it's odd and greater than 10")
else:
    print("it's less than 10") 