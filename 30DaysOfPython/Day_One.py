# Exercise: Level 2
####################################

# 1. Check the python version you are using

import sys

print(sys.version)

# 2. Do the following operations. The operands are 3 and 4.
"""
addition(+)
subtraction(-)
multiplication(*)
modulus(%)
division(/)
exponential(**)
floor division operator(//)
"""

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(4 % 3)
print(4 / 3)
print(4 ** 3)
print(4 // 3)

# 3. Write the following strings:
"""Your name
Your family name
Your country
I am enjoying 30 days of python
"""
print("Perpa")
print("I am not disclosing that information")
print("USA")
print("I am enjoying 30 days of python because it's easy so far")

# 4. Check the data types of the following data:

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(["Perpa", "Python", "Finland"]))
print(type("Perpa"))
print(type("I am still not disclosing that information"))
print(type("USA"))

# Exercise: Level 3
"""Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary."""
print(42)                               # Integer
print(4.2)                              # Float
print(3 + 2j)                           # Complex (huh only j?)
print("This is a string")               # String
print(True)                             # Boolean
print(["Pikachu", "Jolteon", "Luxray"]) # List
print((456, 234, 789))                  # Tuple
print({123, 567, 876})                  # Set
print({"Electric":"Jolteon","Fire":"Flareon", "Water":"Vaporeon"})                

"""Find an Euclidean distance between (2, 3) and (10, 8)"""
import math

print(math.sqrt( (10 - 2) ** 2 + (8 - 3) ** 2 ))