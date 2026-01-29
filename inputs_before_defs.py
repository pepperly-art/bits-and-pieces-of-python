#ignore this, backup / notes

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

match gender:
    case "male" | "m" | "boy" | "man":
        pronouns = ["he", "him", "his", "man"]
    case "female" | "f" | "girl" | "woman":
        pronouns = ["she", "her", "hers", "woman"]
    case _:
        pronouns = ["they", "them", "theirs", "specialist"]

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

# ================================ #

#not entirely sure how to check them all for non-blank fills... I know repeated code is bad.

adverb_one = input("Adverb: a descriptor that ends in -ly.   ")
while adverb_one == "":
    print("No input. Try again.")
    adverb_one = input("Adverb: a descriptor that ends in -ly.   ")
adverb_one = adverb_one.lower()

noun_one = input("Noun, a thing:   ")
while noun_one == "":
    print("No input. Try again.")
    noun_one = input("Noun, a thing:   ")
noun_one = noun_one.capitalize()

noun_one_plural = input("Same noun but plural this time:   ")
while noun_one_plural == "":
    print("No input. Try again.")
    noun_one_plural = input("Same noun but plural this time:   ")
noun_one_plural = noun_one_plural.lower()

noun_two = input("Noun: thing, plural:   ")
while noun_two == "":
    print("No input. Try again.")
    noun_two = input("Noun: thing, plural:   ")
noun_two = noun_two.lower()

noun_three = input("Noun: creature, plural:   ")
while noun_three  == "":
    print("No input. Try again.")
    noun_three = input("Noun: creature, plural:   ")
noun_three = noun_three.lower()

adjective_one = input("Adjective: describes a noun:   ")
while adjective_one == "":
    print("No input. Try again.")
    adjective_one = input("Adjective: describes a noun:   ")
adjective_one = adjective_one.lower()

adjective_two = input("Adjective:   ")
while adjective_two == "":
    print("No input. Try again.")
    adjective_two = input("Adjective:   ")
adjective_two = adjective_two.lower()

adjective_three = input("Adjective:   ")
while adjective_three == "":
    print("No input. Try again.")
    adjective_three = input("Adjective:   ")
adjective_three = adjective_three.lower()

adjective_four = input("Adjective:   ")
while adjective_four == "":
    print("No input. Try again.")
    adjective_four = input("Adjective:   ")
adjective_four = adjective_four.lower()

adjective_five = input("Adjective:   ")
while adjective_five == "":
    print("No input. Try again.")
    adjective_five = input("Adjective:   ")
adjective_five = adjective_five.lower()

adjective_six = input("Adjective, but this time ending in -est or the equivalent:   ")
while adjective_six == "":
    print("No input. Try again.")
    adjective_six = input("Adjective, but this time ending in -est or the equivalent:   ")
adjective_six = adjective_six.lower()

hobby_one = input("A hobby:   ")
while nhobby_one == "":
    print("No input. Try again.")
    hobby_one = input("A hobby:   ")

hobby_two = input("A different hobby:   ")
while hobby_two == "":
    print("No input. Try again.")
    hobby_two = input("A different hobby:   ")

ungreetings = ["Sincerely", "With Love", "With my Deepest Regrets", "My Warmest Regards", "ROFL"]
closure = random.choice(ungreetings)

print(f"A Letter of Recommendation, auto-filled by the wonderful {you}") 
print(f"""
To whom it may concern:

    I have known {you} for {year} {year_plurality}, and {adverb_one} recommend {pronouns[1]} for the position
    of Assistant {noun_one} in your {adjective_one} Company. {you} is {adjective_two}, 
    {adjective_three}, and has a way with {noun_two}. Not only that, but {pronouns[0]} cannot get
    enough of {noun_three}, {hobby_one}, or {hobby_two}. {you} is your {pronouns[3]} for the job,
    as you will find that {pronouns[0]} would make {an} {adjective_five} Assistant {noun_one}.
    {pronouns[0].capitalize} has the {adjective_six} recommendation for {adjective_one} Company.
    In my experience, {pronouns[0]} is in the top {number}% of any group of {noun_one_plural} you
    may ever meet. 

{closure}, Perpa.
""" )