# # # Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

# # Enter your age: 30
# # You are old enough to learn to drive.
# # Output:
# # Enter your age: 15
# # You need 3 more years to learn to drive.

# user_age = int(input("Enter your age: "))
# if user_age >= 18:
#     print("You are old enough to learn to drive.")
# else:
#     years_plural = "years"
#     years = 18 - user_age
#     if years == 1:
#         years_plural = "year"
#     print(F"you need {years} more {years_plural} to learn to drive.")

# # Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

# # Enter your age: 30
# # You are 5 years older than me.

# your_age = int(input("Who is older? Me or you? Enter your age: "))
# if your_age > 42:
#     diff = your_age - 42
#     if diff == 1:
#         print("You're only one year older than me.")
#     else:
#         print(f"You're {diff} years older than me.")
# elif your_age == 42:
#     print("We're the same age! :O")
# else:
#     print("You're younger than me.")

# # Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

# a = int(input("Enter a whole number: "))
# b = int(input("Enter another whole number: "))

# if a >= b:
#     print(f"{a} is greater than {b}")
# elif b >= a:
#     print(f"{a} is less than {b}")
# else:
#     print("They're the same number!!")

# # Enter number one: 4
# # Enter number two: 3
# # 4 is greater than 3

# # Exercises: Level 2
# # Write a code which gives grade to students according to theirs scores:

# # ```sh
# # 90-100, A
# # 80-89, B
# # 70-79, C
# # 60-69, D
# # 0-59, F
# # ```

# grade = int(input("Grade? "))
# if grade >= 90 and grade <= 100:
#     print("A")
# elif grade >= 80 and grade <= 89:
#     print("B")
# elif grade >= 70 and grade <= 79:
#     print("C")
# elif grade >= 60 and grade <= 69:
#     print("D")
# else:
#     print("F")



# # Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

# month = input("What Month is it?").lower()

# if month == "september" or  month == "october" or month == "november":
#     print("It's Autumn!")
# elif month == "december" or  month == "january" or  month == "february":
#     print("It's Winter!")
# elif  month == "march" or  month == "april" or  month == "may":
#     print("It's Spring!")
# elif  month == "june" or  month == "july" or  month == "august":
#     print("It's Summer!")
# else:
#     print("Month not Found")

# # The following list contains some fruits:
# # ```sh
# # fruits = ['banana', 'orange', 'mango', 'lemon']
# # ```

# # If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Name a fruit! ")
new_fruit = fruit.lower()
does_exist = new_fruit in fruits

if does_exist:
    print("That fruit's already in the list!")
    print(fruits)
else:
    fruits.append(new_fruit)
    print("Fruit added to list")
    print(fruits)

# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

if person.get('skills') != None:
    print(person['skills'][2])

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

if "Python" in person.get('skills'):
    print("This person knows Python!")
else:
    print("No snakes here")

#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

if "Javascript" in person.get('skills') and "React" in person.get('skills'):
    print("He is a frontend developer")
if "React" in person.get('skills') and "Node" in person.get('skills') and "MongoDB" in person.get('skills'):
    print("He is a fullstack developer")
else:
    print("unknown title")

#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.

if person.get('is_married') and person.get('country') == "Finland":
    print(f"{person.get('first_name')} {person.get('last_name')} lives in {person.get('country')}. They are married.")