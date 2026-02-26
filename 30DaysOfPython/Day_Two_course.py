# print('Hello, World!') # The text Hello, World! is an argument
# print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
# print(len('Hello, World!')) # it takes only one argument

# Variables in Python
# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# country = 'Finland'
# city = 'Helsinki'
# age = 250
# is_married = True
# skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
# person_info = {
#    'firstname':'Asabeneh',
#    'lastname':'Yetayeh',
#    'country':'Finland',
#    'city':'Helsinki'
#    }

#    # Printing the values stored in the variables

# print('First name:', first_name)
# print('First name length:', len(first_name))
# print('Last name: ', last_name)
# print('Last name length: ', len(last_name))
# print('Country: ', country)
# print('City: ', city)
# print('Age: ', age)
# print('Married: ', is_married)
# print('Skills: ', skills)
# print('Person information: ', person_info)

# first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

# print(first_name, last_name, country, age, is_married)
# print('First name:', first_name)
# print('Last name: ', last_name)
# print('Country: ', country)
# print('Age: ', age)
# print('Married: ', is_married)


##### 

# first_name = input('What is your name: ')
# age = input('How old are you? ')

# print(first_name)
# print(age)


### Casting ####


# # int to float
# num_int = 10
# print('num_int',num_int)         # 10
# num_float = float(num_int)
# print('num_float:', num_float)   # 10.0

# # float to int
# gravity = 9.81
# print(int(gravity))             # 9

# # int to str
# num_int = 10
# print(num_int)                  # 10
# #num_str = str(num_int)
# #print(num_str)                  # '10' -- this doesn't work

# # str to int or float
# num_str = '10.6'
# num_float = float(num_str)  # Convert the string to a float first
# num_int = int(num_float)    # Then convert the float to an integer
# print('num_int', int(num_str))      # 10 -- this also doesn't work
# print('num_float', float(num_str))  # 10.6
# num_int = int(num_float)
# print('num_int', int(num_int))      # 10

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']