# syntax
#if condition:
#    this part of code runs for truthy conditions

# if checks for true, and if so, executes the block code
a = 3
if a > 0:
    print('A is a postitive number')

# if else is if true the first block will be executed, if not the else is
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

# if elife else
# checks more than two conditions

# if condition:
    #code
# elif condition:
    #code
# else:
    #code which runs if the others are not true

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

# shorthand
# code if condition else code

a = 3
print('A is positive') if a > 0 else print('A is negative')

# nested conditions

# if condition:
    # code
    # if condition:
        # code

a = 0 
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

# avoid writing nested conditions by using "and"
# if condition AND logical operators

# if condition and condition:
    #code

a = 0
if a > 0 and a % 2 == 0:
    print('A is an even and positive integer')
elif a > 0 and a % 2 != 0:
    print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

# if and OR logical operators

# if condition or condition
    #code

user = 'James'
access_level = 3
if user == 'admin' or access_level >=4:
    print('Access granted!')
else:
    print('Access denied!')

# I'M ALREADY GOOD AT THIS 