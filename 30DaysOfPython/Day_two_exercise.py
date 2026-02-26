# Day 2: 30 Days of Programming

# Level 1 exercises

# Declare a first name variable and assign a value to it
# Declare a last name variable and assign a value to it
# Declare a full name variable and assign a value to it
# Declare a country variable and assign a value to it
# Declare a city variable and assign a value to it
# Declare an age variable and assign a value to it
# Declare a year variable and assign a value to it
# Declare a variable is_married and assign a value to it
# Declare a variable is_true and assign a value to it
# Declare a variable is_light_on and assign a value to it
# Declare multiple variable on one line

first_name = "Perpa"
last_name = "Namae"
full_name = "Sonic the Hedgehog"
country = "Japan"
city = "Kyoto"
age = 42
year = 2049
is_married = "nah"
is_true = True
is_light_on = False
color, name, weight, gender, best_stat = "Tabby", "Riceball", "7lbs", "Male", "Speed"

# Level 2

# Check the data type of all your variables using type() built-in function
# Using the len() built-in function, find the length of your first name
# Compare the length of your first name and your last name
# Declare 5 as num_one and 4 as num_two
# Add num_one and num_two and assign the value to a variable total
# Subtract num_two from num_one and assign the value to a variable diff
# Multiply num_two and num_one and assign the value to a variable product
# Divide num_one by num_two and assign the value to a variable division
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
# Calculate num_one to the power of num_two and assign the value to a variable exp
# Find floor division of num_one by num_two and assign the value to a variable floor_division
# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area.
# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(f" {type(color)}, {type(name)}, {type(weight)}, {type(gender)}, {type(best_stat)}")

print(len(first_name))
print(max(first_name, last_name))

print("==========================")


num_one = 5
num_two = 4

diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two

print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print("==========================")

import math

radius = 30
area_of_circle = math.pi * (radius ** 2)
circum_of_circle = radius * 2 * math.pi

print(area_of_circle)
print(circum_of_circle)
print("==========================")

radius = input("What's the radius of your circle? ")
print(f"The Area is: {area_of_circle}")
print(f"The Circumference is: {circum_of_circle}")
print("==========================")

print("Hello, user! Some questions:")
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
country = input("What country are you from? ")
age = input("How old are you? ")
print(f"Hello {first_name} {last_name}! I see you are {age} years old, and you come from {country}. Neat!")