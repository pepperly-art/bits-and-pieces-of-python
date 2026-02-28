#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
titles = ["Thirty", "Days", "of", "Python"]
result = " ".join(titles)
print(result)

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
chant = ["Coding", "For", "All"]
result = " ".join(chant)
print(result)

#Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

#Print the variable company using print().
print(company)

#Print the length of the company string using len() method and print().
print(len(company))

#Change all the characters to uppercase letters using upper() method.
print(company.upper())

#Change all the characters to lowercase letters using lower() method.
print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Cut(slice) out the first word of Coding For All string.
first_word = company[0:5]

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index("Coding"))
print(company.find("Coding"))

#Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Python', 'coding'))

#Change "Python for Everyone" to "Python for All" using the replace method or other methods.
stringy = "Python For Everyone"
print(stringy.replace("Everyone", "All"))

#Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
computanies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(computanies.split(', '))

#What is the character at index 0 in the string Coding For All.
print(company[0])

#What is the last index of the string Coding For All.
print(company[-1])

#What character is at index 10 in "Coding For All" string.
print(company[10])

#Create an acronym or an abbreviation for the name 'Python For Everyone'.
print(f"{stringy[0]}{stringy[7]}{stringy[11]}")

#Create an acronym or an abbreviation for the name 'Coding For All'.
print(f"{company[0]}{company[7]}{company[11]}")

#Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))

#Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:53])

#Does 'Coding For All' start with a substring Coding?
print(company.startswith("Coding"))

#Does 'Coding For All' end with a substring coding?
print(company.endswith("coding"))

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
company_big = '   Coding For All      '
print(company_big.strip(" "))

#Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
phrase_one = "30DaysOfPython"
phrase_two = "thirty_days_of_python"
print(f"Is it 30DaysOfPython? {phrase_one.isidentifier()} Or thirty_days_of_python? {phrase_two.isidentifier()}")

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
librariesss = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(librariesss)
print(result)

#Use the new line escape sequence to separate the following sentences.
#I am enjoying this challenge.
#I just wonder what is next.
print("""
I am enjoying this challenge.
I just wonder what is next.
""")

#Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print("Name\tAge\tCountry\tCity\nAsabene\t250\tFinland\tHelsinki")

#Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
print(f"The area of a circle with radius {radius} is {area} meters square")

#Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

a = 8
b = 6
addition = a + b
subtract = a - b
multiply = a * b
division = a / b
modulus = a % b
super_division = a // b
exponents = a ** b

add_string = "{} + {} = {}".format(a, b, addition)
subt_string = "{} - {} = {}".format(a, b, subtract)
mult_string = "{} * {} = {}".format(a, b, multiply)
div_string = "{} / {} = {:.2f}".format(a, b, division)
mod_string ="{} % {} = {}".format(a, b, modulus)
supdiv_string = "{} // {} = {}".format(a, b, super_division)
expo_string = "{} ** {} = {}".format(a, b, exponents)
print(add_string)
print(subt_string)
print(mult_string)
print(div_string)
print(mod_string)
print(supdiv_string)
print(expo_string)