#Age Intro Thing

import datetime
date = datetime.datetime.now()
year = int(date.strftime("%Y"))
userAge = None

print("Hello, what is your name?")
userName = input()

while userName == "":
    print("You did not enter your name.")
    userName = input("Enter your name: ")

print(f"Hello, {userName}! How old are you?")

while userAge is None:
    try:
        userAge = int(input())
        if userAge < 0:
            print("Your age can't be negative!")
            userAge = None
    except ValueError:
        print("That is not a valid number. Try again.")
        userAge = None

def AreTheyOld():
    if userAge > 25:
        print(f"Wow, {userAge} huh?  That's pretty old.")
    elif userAge < 13:
        print(f"{userAge}? Should you even be on the internet?")
    else:
        print(f"Only {userAge}? You've got plany of time...")

AreTheyOld()        
print(f"Your age multiplied by 5 is {userAge * 5}")
print(f"Assuming your birthday happened this year, your birth year was {(year - userAge) - 1}")


#helloWorldString = str("Hello World")

#def ThisIsAFunction():
#    return helloWorldString
    
#print(ThisIsAFunction())

# while(True):
#     try:
#         userAge = int(userAge)
#     except ValueError:
#         print(f"{userAge} is not a number! Try again.")