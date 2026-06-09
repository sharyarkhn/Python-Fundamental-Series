# For-else loop: we use it when all the conditions become false and 
# # we want to print any massage once at last it will print we must use 
# break with it



# Example:
for num in [12,23,2,3,11]:
    pass
else:
    print("not found")




# Example:
# We use break when we use forelse loop cuz else will always print
# other wise we use break go out when condition becomes true 
target = 5
for num in [12, 23, 2, 3, 11]:
    if num == target:
        print("Found")
        break
else:
    print("Not Found")