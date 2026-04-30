# Dictionaries
# JSON, my beloved

empty_dict = {}
#dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

person = {
    'first_name':'Joe',
    'last_name':'Schmoe',
    'age': 250,
    'country': 'Arcadea',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02589'
    }
}
# The dictionary above shows that a value could be any data types:string, boolean, list, tuple, set or a dictionary.

# length
# the number of key:value pairs in the dictionary

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4

print(len(person)) #7

# access dictionary items by referring to the key name

dct = {"key":"value1", "key2":"value2", "key3":"value3", "key4":"value4" }
print(dct['key1']) #value1)
print(dct['key4']) #value4)

print(person['first_name'])         # Joe
print(person['country'])            # Arcadea
print(person['skills'])             # that whole list
print(person['skills[0]'])          # Javascript
print(person['address']['street'])  # Space street
print(person['city'])               # error

# Accessing an item by name will raise an error if the key doesn't exist. Use the get() method to chec, and will return None, a NoneType object, if it doesn't get it.abs

print(person.get('first_name'))     # Joe
print(person.get('country'))        # Finland
print(person.get('skills'))         # that whole list
print(person.get('city'))           # None

# Adding items

dct['key5'] = 'value5'

person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)

# Modifying Items
dct['key1'] ='value-one'

person['first_name'] = 'Jessica'
person['age'] = 252

# Checking keys
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False

# Removing Key and Value Pairs

# pop(key) removes the item with the specified key name
# popitem() removes the last item
# del removes an item with the specified key name

dct.pop('key1') # removes key1
dct.popitem() # removes the last item
del dct['key2'] # removes key2
print(dct)

person = {
    'first_name':'Joe',
    'last_name':'Schmoe',
    'age': 250,
    'country': 'Arcadea',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02589'
    }
}
person.pop('first_name')    # goodbye first_name
person.popitem()            # goodbye address
del person['is_married']    # goodbye is_married

print(person)

# changing dictionary to a list of items
# items changes the dictionary to a list of tuples

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1','value1), ('key2','value2'), ('key3', 'value3'), ('key4', 'value4)])
# yikes lol

# clearing
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None

# deleting
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

# copying, to avoid mutation of the original
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

# keys and values as a list, to split them up!
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)         # dict_keys(['key1', 'key2', 'key3', 'key4'])
values = dct.values()
print(values)       # dict_values(['value1', 'value2', 'value3', 'value4'])