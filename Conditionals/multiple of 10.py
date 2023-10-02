import math

integer = int(input("Enter a non-negative integer: "))

mod10 = integer % 10

if mod10 == 8 or 2:
    print("Your integer is 2 away from a multiple of 10.")
    
else:
    print("Your integer is not 2 away from a multiple of 10.")