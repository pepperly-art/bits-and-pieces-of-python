# print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
# print('Days\tTopics\tExercises') # adding tab space or 4 spaces
# print('Day 1\t5\t5')
# print('Day 2\t6\t20')
# print('Day 3\t5\t23')
# print('Day 4\t1\t35')
# print('This is a backslash  symbol (\\)') # To write a backslash
# print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

# output
# I hope every one is enjoying the Python Challenge.
# Are you ?
# Days  Topics  Exercises
# Day 1	5	    5
# Day 2	6	    20
# Day 3	5	    23
# Day 4	1	    35
# This is a backslash  symbol (\)
# In every programming language it starts with "Hello, World!"

# # wow tabs!

# # Strings only
# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# language = 'Python'
# formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
# print(formated_string)

# # Strings  and numbers
# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

# python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
# formated_string = 'The following are python libraries:%s' % (python_libraries)
# print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"

# # Django... pwow


first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# # output
# 4 + 3 = 7
# 4 - 3 = 1
# 4 * 3 = 12
# 4 / 3 = 1.33
# 4 % 3 = 1
# 4 // 3 = 1
# 4 ** 3 = 64

#these are significantly worse than fstrings

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)

language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH

language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto

first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, job, age, country)
print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314

"""
capitalize(): Converts the first character of the string to capital letter
count(): returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end is the last index to count.
endswith(): Checks if a string ends with a specified ending
expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
find(): Returns the index of the first occurrence of a substring, if not found returns -1
rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
format(): formats string into a nicer output
index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.
rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
isalnum(): Checks alphanumeric character - Space is not alphanumeric
isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
isdecimal(): Checks if all characters in a string are decimal (0-9)
isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
islower(): Checks if all alphabet characters in the string are lowercase
isupper(): Checks if all alphabet characters in the string are uppercase
join(): Returns a concatenated string
strip(): Removes all given characters starting from the beginning and end of the string
replace(): Replaces substring with a given string
split(): Splits the string, using given string or space as a separator
title(): Returns a title cased string
swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
startswith(): Checks if String Starts with the Specified String
"""