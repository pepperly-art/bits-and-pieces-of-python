# Exercises: Level 1
# Create an empty tuple
hungry_tuple = tuple()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ("Berpa", "Cerpa", "Derpa")
brothers = ("Lerpa", "Merpa", "Nerpa")

# Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(siblings)

# How many siblings do you have?
print(len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to parents

parents = ("Salt", "Paprika")
family_members = parents + siblings
print(family_members)

# Exercises: Level 2
# Unpack siblings and parents from family_members
father, mother, *siblings = family_members
print(mother)
print(father)
print(siblings)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("mango", "apple", "banana", "strawberry")
vegetables = ("bok choy", "broccoli", "spinch")
animal_products = ("milk", "honey", "steak", "feesh")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
sliced = food_stuff_tp[5]

# Slice out the first three items and the last three items from food_stuff_lt list
sliced_three = food_stuff_lt[:3]
sliced_negative_three = food_stuff_lt[:-3]

# Delete the food_stuff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
print("Estonia" in nordic_countries)

# Check if 'Iceland' is a nordic country
print("Iceland" in nordic_countries)
