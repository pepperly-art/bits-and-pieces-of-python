# loops!

# while loop
#  execute a block of statements repeatedly until a given condition is satisfied. when the condition becomes false, the lines of code after the loop will be continued to be executed

# while condition:
#   code

count = 0

while count < 5:
    print(count)
    count = count +1

#prints from 0 to 4
# the condition becomes false when count is 5, so the loop stops. 
# use else to perform while the condition is no longer true

# while condition:
#   code
# else
#   code

count = 0
while count < 5:
    print(count)
    count - count + 1
else:
    print(count)

# will count up until five, and then the else is executed

# break: we use break when we like to get out or stop a loop

# while condition:
#   code goes here
#   if another_condition:
#       # break

# prints only 0, 1, 2, and stops when 3

# continue: skip the current iteration and continue with the next

# while condition:
#   code goes here
#   if another_condition:
#       continue

count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count +1

# the above loop only prints 0, 1, 2, and 4 (skips 3)
# maybe more of a return-to-start?

# for loop

# for iterating over a sequence (list, tuple, dict, set, or string)

# for iterator in lst:
#   code goes here

numbers [0, 1 , 2, 3, 4, 5]
for number in numbers: # number is a temp name to refer to the lists items and only valid inside this loop
    print(number)       # the numbers will be printed line by line, 0 - 5

# strings
language = "Python"
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

# tuple

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

# Break and Continue

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

# In the example above, if the number equals 3, the step after the condition (but inside the loop) is skipped and the execution of the loop continues if there are any iterations left.

# range
# range() used to return a list of numbers
# The range(start, end, step) takes three parameters: starting, ending and increment. By default it starts from 0 and the increment is 1. The range sequence needs at least 1 argument (end). Creating sequences using range

lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# for backward from start to end 
lst = list(range(11,0,-2))
print(lst) # [11,9,7,5,3,1]

for number in range(11):
    print(number)   # prints 0 to 10, not including 11

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

# for else

for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)

# pass, when a statement is required but we don't want to execute any code, or as a placeholder

for number in range(6):
    pass


