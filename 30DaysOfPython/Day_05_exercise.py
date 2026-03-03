# Declare an empty list
new_list = []

# Declare a list with more than 5 items
pokemon = ["Bulbasaur", "Charmander", "Squirtle", "Pikachu", "Eevee", "Mewtwo", "Mew"]

# Find the length of your list
print(len(pokemon))

# Get the first item, the middle item and the last item of the list
print(pokemon[1])
print(pokemon[-1])
middle = round(len(pokemon) / 2)
print(pokemon[middle])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Perpa", 41, "7'11", "Unmarried", "1234 Somewhere Ln, Michigan"]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0])
print(it_companies[-1])
middle = int(round(len(it_companies)) / 2)
print(it_companies[middle])

# Print the list after modifying one of the companies
it_companies[0] = "Nvidia" 
print(it_companies)

# Add an IT company to it_companies
it_companies.append("Sony")
print(it_companies)

# Insert an IT company in the middle of the companies 
it_companies.insert(2, "Intel")
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
capitalize = it_companies[2].upper()
it_companies[2] = capitalize
print(it_companies)

# Join the it_companies with a string '#;  '
joined = '#; '.join(it_companies)
print(joined)

# Check if a certain company exists in the it_companies list.
print(it_companies.index("IBM"))

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
print(it_companies[:3])

# Slice out the last 3 companies from the list
print(it_companies[-3:])

# Slice out the middle IT company or companies from the list
print(it_companies[1:-1])

# Remove the first IT company from the list
print(it_companies.pop(0))

# Remove the middle IT company or companies from the list
print(it_companies.pop(3))

# Remove the last IT company from the list
print(it_companies.pop(-1))

# Remove all IT companies from the list
print(it_companies.clear())

# Destroy the IT companies list
del it_companies

# Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined_ends = front_end + back_end
print(joined_ends)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = joined_ends.copy()
full_stack.insert(4, "Python")
full_stack.insert(5, "SQU")


# The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age

ages.sort()
print(min(ages))
print(max(ages))

# Add the min age and the max age again to the list
ages.append(min(ages))
ages.append(max(ages))
print(ages)

# Find the median age (one middle item or two middle items divided by two)
count = len(ages)
if count % 2 == 0:
    countlow = int(count / 2 - 0.5)
    counthigh = int(count / 2 + 0.5)
    medianlow = ages[countlow]
    medianhigh = ages[counthigh]
    print(int((medianlow + medianhigh) / 2))
else:
    print(ages(count / 2))

# Find the average age (sum of all items divided by their number )
total_age = 0

for each in ages:
    total_age  = total_age + each
print(total_age / len(ages))

# Find the range of the ages (max minus min)
print(max(ages) - min(ages))

# Compare the value of (min - average) and (max - average), use abs() method
average = total_age / len(ages)
print(abs(min(ages) - average))
print(abs(max(ages) - average))

# Find the middle country(ies) in the countries list
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
count = len(countries)

if count % 2 == 0:
    halfcount = count / 2
    print(countries[0:halfcount])
    print(countries[halfcount:])
else:
    halfcount = count // 2 + 1
    print(countries[0:halfcount])
    print(countries[halfcount:])

one, two, three, *scandic = countries
print(one)
print(two)
print(three)
print(scandic)