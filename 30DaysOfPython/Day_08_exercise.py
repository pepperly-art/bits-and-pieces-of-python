# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = "Lucky"
dog['color'] = ["White", "Black"]
dog['breed'] = "Dalmation"
dog['legs'] = True
dog['age'] = 2
#wobbledogs skdfjkgj legs = true laksdfjg that's so funny

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "Bobby",
    "last_name": "Hill",
    "gender": "Male",
    "age": 14,
    "maritial_status": "Minor",
    "skills": ["That's my purse, I don't know you", "guitar", "video games", "curiosity"],
    "city": "Arlen",
    "address":{
        "street" : "1234 Freedom Hill",
        "state": "Texas",
        "zip": "48484"
        }
}

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(student.get("skills"))
print(type(student.get("skills")))

# Modify the skills values by adding one or two skills
student['skills'].append('comedy')
print(student.get("skills"))

# Get the dictionary keys as a list
keys = student.keys()
print(keys)
keys2 = dog.keys()
print(keys2)

# Get the dictionary values as a list
values = student.values()
print(values)
values2 = dog.values()
print(values2)

# Change the dictionary to a list of tuples using items() method
print(student.items())
print(dog.items())

# Delete one of the items in the dictionary
student.pop('maritial_status')
dog.pop('color')

# Delete one of the dictionaries
del student