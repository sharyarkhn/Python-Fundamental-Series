# Loops are used to execute a block of code repeatedly until a condition is met.
# There are two main types of loops in Python:
# for loop
# while loop


# # <<<<<<<<<<<<<<<<<<<<<<<<for Loop->>>>>>>>>>>>>>>>>>>>>>>>
# The for loop is used to iterate over a sequence such as a list, tuple, string, or range.
# Syntax:
# for variable in sequence:
#     statements


# For loop-------------------
listEg = ["sherry" , 12 ,0.3]
for j in listEg:
    print(j)

for z in (12 , 34 ,5): 
    print(z)

for i in range(5): #it will print 0 1 2 3 4
    print(i)


for k in range(10 , 21 , 2): #it will print 10,12,14,16,18,20
    print(k)

for l in range(20 , 0 , -1): # it will print in reverse order 20-1
    print(l)

 

# Nested For loop-------------------
for i in range(5):
    for j in range(5):
        print("*" , end="")
    print()














# # <<<<<<<<<<<<<<<<<<<<<<<<while Loop>>>>>>>>>>>>>>>>>>>>>>>>
# # The while loop executes as long as the condition is True.

# # Syntax:
# # while condition:
# #     statements


# While loop--------------
i = 1

while i <= 5:
    print(i)
    i += 1



# Nested While loop-----------
i = 1
while i <= 3:
    print(i , end=": ")

    j = 1
    while j<=i:
        print("hello" , j , end=", ")
        j=j+1

    print()
    i += 1