# Bitwise Operators in Python
# Bitwise operators work directly on binary (bits) of numbers.
# Example: 10 = 1010     12 = 1100

# Types of it
# AND                 & 
# OR                  |
# XOR                 ^
# NOT/Complement      ~
# LeftShift           <<
# RightShift          >>


# >>>>>>>>>># NOT/Complement(~)>>>>>>>>>>>
# it will filip all bits
# like o -> 1 vise versa

print(~12) #-13
# cuz 12 = 00001100 after filip 11110011
# and 11110011 = 13 and -13 because first digit is 1

# <<<<<<<<<<<<<<<AND(&)>>>>>>>>>>>>>>>
# Returns 1 if bits are 1 else 0 
print(4 & 6)
# 4 = 0100
# 6 = 0110
#     0100 


# <<<<<<<<<<<<<<<OR(|)>>>>>>>>>>>>>>>
# Returns 1 if any of one is 1
print(4 | 6)
# 4 = 0100
# 6 = 0110
#     0110


# <<<<<<<<<<<<<<<XOR(^)>>>>>>>>>>>>>>>
# Returns 1 if bits are different.and 0 if same
print(4 ^ 7)
# 4 = 0100
# 7 = 0111
#     0011 = 3


# <<<<<<<<<<<<<<LeftShift(<<)>>>>>>>>>>>>>
# It shifts bits from right to left.
# Zeros are added on the right side.
# The quantity of shifting depends on the given number.
# The last bits from the left side are removed. that quantity
print(4 << 1)
# 4 = 00000100
#     00001000 = 8

print(12 << 2)
# 12 = 000001100
#      00110000  = 48



# <<<<<<<<<<<<<<RightShift(>>)>>>>>>>>>>>>>
# It shifts bits from left to right.
# The last bits from the right side are removed.
# Zeros are added on the left side.
# The quantity of shifting depends on the given number.
print(4 >> 1)
# 4 = 00000100
#     000000010 = 2

print(12 >> 2)
# 12 = 00001100
#      00000011  = 3

