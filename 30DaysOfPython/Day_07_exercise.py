# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercises: Level 1
#Find the length of the set it_companies
print(len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
it_companies.update(['Texas Instruments', 'PayPal', 'Adobe'])
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove('Facebook')
print(it_companies)

#What is the difference between remove and discard
#remove() removes an item and will error if it's not there, discard() will remove an item with no error

print('----- Level 2 -----')
#Exercises: Level 2
#Join A and B
C = A.union(B)
print(C)

#Find A intersection B
print(A.intersection(B))

#Is A subset of B
print('A is a subset of B: ' + str(A.issubset(B)))

#Are A and B disjoint sets
print('A and B are disjoints? ' + str(A.isdisjoint(B)))

#Join A with B and B with A
print(A | B)
print(B | A)

#What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# Delete the sets completely
del A
del B
del it_companies

#Exercises: Level 3
print("----- Level 3 -----")
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_st = set(age)
print(f"The length of set is {len(age_st)}, and the length of list is {len(age)}.")

# Explain the difference between the following data types: string, list, tuple and set
print("String is one input of a list of letters or numbers or whatever, basically just text. List is an ordered collection of values or strings or whatever. Tuples are similar but can't be changed. Sets are unordered and changable but can contain no duplicates.")

# I am a teacher and I love to inspire and teach people.
# How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

sentence = "I am a teacher and I love to inspire and teach people"
words = set(sentence.split())
print(words)
print(len(words))

# 🎉 CONGRATULATIONS ! 🎉