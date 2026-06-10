# Number System Conversion in Python
# Python provides built-in functions to convert numbers
# between Binary, Decimal, Octal, and Hexadecimal.


# Decimal to Binary
x = 10 
print(bin(x))
print(0b1010) # this will print the decimal number


# Decimal to Octal
y = 10 
print(oct(y))
print(0o0101) #this will print the decimal number


# Decimal to Hexadecimal
z = 25 
print(hex(z))
print(0x1010) #this will print the decimal number


# Binary to Decimal
a = "10"
print(int(a,2))


# Octal to Decimal
b = "10"
print(int(b,8))


# Hexadecimal to Decimal
c = "10"
print(int(c , 16))
