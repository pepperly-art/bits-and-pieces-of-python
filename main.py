import random

print("Welcome to Madlibs!")
print("Here, we're writing a... something. You'll see.")
print("First of all, we need your name!")
you = input()

while you == "":
    print("You did not enter your name.")
    you = input("Enter your name:   ")

you = you.capitalize()

print("Are you Male, Female, or something else?")
gender = input()
gender = gender.lower()
pronouns = []
plurality = False

match gender:
    case "male" | "m" | "boy" | "man":
        pronouns = ["he", "him", "his", "man"]
    case "female" | "f" | "girl" | "woman":
        pronouns = ["she", "her", "hers", "woman"]
    case _:
        pronouns = ["they", "them", "theirs", "specialist"]
        plurality = "plural"

# ================================ #
year = None
year_plurality = "years"
while year is None:
    try:
        year = int(input("Number: "))
        if year < 0:
            print("It can't be negative, sorry.")
            year = None
        elif year == 1:
            year_plurality = "year"
    except ValueError:
        print("That's not a valid number, try again.   ")
        year = None

number = None
while number is None:
    try:
        number = int(input("Number from 1 to 100: "))
        if number < 1:
            print("Too small")
            number = None
        elif number > 100:
            print("Too big.")
            number = None
    except ValueError:
        print("that's not a valid number")
        number = None

# ================================ #
adverb_one = ""
noun_one = ""
noun_one_plural = ""
noun_two = ""
noun_three = ""
adjective_one = ""
adjective_two = ""
adjective_three = ""
adjective_four = ""
adjective_five = ""
adjective_six = ""
hobby_one = ""
hobby_two = ""

def blankCheck(variable, request, grammar):
    variable = input(request)
    while variable == "":
        print("No input, try again")
        variable = input(request)
    if grammar == "lower":
        variable = variable.lower()
    elif grammar == "caps":
        variable = variable.capitalize()
    elif grammar == "upper":
        variable = variable.upper()
    return variable

adverb_one =blankCheck(adverb_one, "Adverb, a descriptor that ends in -ly: ", "lower")
noun_one = blankCheck(noun_one, "Noun, a thing: ", "caps")
noun_two = blankCheck(noun_two, "Noun, things plural: ", "lower")
noun_three = blankCheck(noun_three, "Noun but plural creatures: ", "lower")
adjective_one = blankCheck(adjective_one, "Adjective, describes a noun: ", "lower")
adjective_two = blankCheck(adjective_two, "Adjective: ", "lower")
adjective_three = blankCheck(adjective_three, "Adjective: ", "lower")
adjective_four = blankCheck(adjective_four, "Adjective: ", "lower")
adjective_five = blankCheck(adjective_five, "Adjective: ", "lower")
adjective_six = blankCheck(adjective_six, "Adjective, but ending in -est or the equivalent: ", "lower")
hobby_one = blankCheck(hobby_one, "A hobby: ", "")
hobby_two = blankCheck(hobby_two, "A different hobby: ", "")

# ======================================== #

an = adjective_five[0]

match an:
    case "a" | "e" | "i" | "o" | "u":
        an = "an"
    case _:
        an = "a"

has_check = "has"
is_check = "is"

if plurality:
    has_check = "have"
    is_check = "are"

ungreetings = ["Sincerely", "With Love", "With my Deepest Regrets", "My Warmest Regards", "ROFL"]
closure = random.choice(ungreetings)

print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
print(f"A Letter of Recommendation, auto-filled by the wonderful {you}") 
print(f"""
To whom it may concern:

    I have known {you} for {year} {year_plurality}, and {adverb_one} recommend {pronouns[1]}
    for the position of Assistant {noun_one} in your {adjective_one} Company.
    {you} is {adjective_two}, {adjective_three}, and has a way with {noun_two}.
    Not only that, but {pronouns[0]} cannot get enough of {noun_three}, {hobby_one},
    or {hobby_two}. {you} is your {pronouns[3]} for the job, as you will find that {pronouns[0]}
    would make {an} {adjective_five} Assistant {noun_one}. {pronouns[0].capitalize()} {has_check} 
    the {adjective_six} recommendation for {adjective_one} Company. In my experience, 
    {pronouns[0]} {is_check} in the top {number}% of any group of {noun_one} specialists
    you may ever meet. 

{closure}, Perpa.
""" )
print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")