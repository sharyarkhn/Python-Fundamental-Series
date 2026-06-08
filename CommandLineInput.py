# Command line arguments allow passing values while running the program from the terminal.
# To use them, import the sys module.
# we use arvg[] to Takes input when starting the program from the terminal.
# WE start index from 1 cuz on the 0 index class name  will be there on 0 index

import sys

x = int(sys.argv[1])
y = int(sys.argv[2])

z = x + y
print(z)
