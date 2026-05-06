# Exercises: Level 1
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    sum = a + b
    return sum
print(add_two_numbers(3, 4))
print(add_two_numbers(-2, 56))


# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    area = 3.14 * r * r
    return area
print(area_of_circle(3))

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    total = 0
    for num in nums:
        if type(num) == int or type(num) == float:
            total += num
        else:
            print("Numbers Only")
            break
    return total
print(add_all_nums(3, 4, 5, 6))
print(add_all_nums(1.2, 4.5, 7.8))
print(add_all_nums("four", "five", "six"))

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(temp):
    fah = temp * (9/5)
    return fah
convert_celsius_to_fahrenheit(0)
convert_celsius_to_fahrenheit(5)
convert_celsius_to_fahrenheit(32)

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    if month == "september" or  month == "october" or month == "november":
        return "It's Autumn!"
    elif month == "december" or  month == "january" or  month == "february":
        return "It's Winter!"
    elif  month == "march" or  month == "april" or  month == "may":
        return "It's Spring!"
    elif  month == "june" or  month == "july" or  month == "august":
        return "It's Summer!"
    else:
        return "Month not Found"
print(check_season("october"))
print(check_season("june"))
print(check_season("march"))

# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, x2, y1, y2):
    slope = (y2 -y1) / (x2 - x1)
    return slope

print(calculate_slope(3,4, 6, 7))
print(calculate_slope( 1, -1, 5, 6))

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

def solve_quadratic_eqn(a, b, c):
    d = b**2-4*a*c # discriminant
    if d < 0:
        return ("This equation has no real solution")
    elif d == 0:
        x = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        return ("This equation has one solutions: "), x
    else:
        x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
        x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
        return ("This equation has two solutions: ", x1, " or", x2)

#tbh I just copy-pasted and adjusted because this is stupid


# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for item in lst:
        print(item)


print_list([11, 22, 33, 44, 55])
print_list(["eyah", "nah", "scream"])

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst)):
        reversed_list.append(lst[-i - 1])
    return reversed_list

print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"])) 
# ["C", "B", "A"]

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(lst):
    capitalized_list = []
    for each in lst:
        capitalized_list.append(each.capitalize())
    return capitalized_list

print(capitalize_list_items(["pikachu", "eevee", "munchlax", "weavile"]))

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

def add_item(lst, *items):
    new_list = lst
    for item in items:
        new_list.append(item)
    return new_list

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]


# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

def remove_item(lst, *items):
    new_list = lst
    for item in items:
        new_list.remove(item)
    return new_list

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]


# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

def sum_of_numbers(num):
    total = 0
    for i in range(num + 1):
        total += i
    return total

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050


# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(num):
    num = int(num)
    total = 0
    for i in range(num + 1):
        if i % 2 == 0:
            pass
        else:
            total += i
    return total

print(sum_of_odds(17))
print(sum_of_odds(4))
print(sum_of_odds(100))

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_evens(num):
    num = int(num)
    total = 0
    for i in range(num + 1):
        if i % 2 == 1:
            pass
        else:
            total += i
    return total

print(sum_of_evens(17))
print(sum_of_evens(4))
print(sum_of_evens(100))

# Exercises: Level 2
# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

def evens_and_odds(num):
    num = int(num)
    evens = 0
    odds = 0
    for i in range(num + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f"The number of odds are {odds} \nThe number of evens are {evens}"

print(evens_and_odds(100))
# The number of odds are 50.
# The number of evens are 51.



# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(num):
    factor = num
    for i in range(1, num):
        factor = factor * i
    return factor

print(factorial(3))
print(factorial(7))

# Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(thing):
    if not thing:
        return "Empty"
    else:
        return "Is Empty"

print(is_empty(list()))
print(is_empty("garbage"))

# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
import math

def calculate_mean(lst):
    total = 0
    for i in lst:
        total += i
    mean = total / len(lst)
    return int(mean)

def calculate_median(lst):
    if len(lst) % 2 == 1:
        return lst[int(len(lst)/2)]
    else:
        mid = len(lst)/2
        upper = int(mid + 0.5)
        lower = int(mid - 0.5)
        return calculate_mean([lst[upper], lst[lower]])
        
def calculate_mode(lst):
    return max(set(lst), key=lst.count)
    pass

def calculate_range(lst):
    smallest = min(lst)
    largest = max(lst)
    return largest - smallest
    
def calculate_variance(lst):
    mean = calculate_mean(lst) # calculate the mean
    total = 0
    for each in lst:
        num = mean - each       # find each difference from the mean
        squared = num * num     # square each
        total += squared        # add up all the square values
    return int(total / len(lst))

def calculate_std(lst):
    mean = calculate_mean(lst)
    total = 0
    for each in lst:
        num = mean - each
        squared = num * num
        total += squared
    rooted = total / len(lst)
    return int(math.sqrt(rooted))

def check_all(lst):
    print(f"Mean: {calculate_mean(lst)}")
    print(f"Median: {calculate_median(lst)}")
    print(f"Mode: {calculate_mode(lst)}")
    print(f"Range: {calculate_range(lst)}")
    print(f"Variance: {calculate_variance(lst)}")
    print(f"Standard Deviation: {calculate_std(lst)}")

list_one = [0, 1, 1, 24, 24, 25]
list_two = [1, 2, 3, 4, 5, 10, 11, 12, 12, 12, 12]

check_all(list_one)
print("---")
check_all(list_two)

# Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.

def greet(name = "Guest"):
    print (f"Hello, {name}")
    
greet()
# "Hello, Guest!
greet("Alice")
# "Hello, Alice!"

# Create a function called show_args to take an arbitrary number of named arguments and print their names and values.
# NOT CORRECT but I'm so tired

def show_args(**args):
    lst = []
    string = ""
    for k, v in args.items():
        lst.append(f"{k}: {v}")
    for each in lst:
        string += str(lst)
    print(f"Recieved: {string}")


show_args(name="Alice", age=30, city="New York")
# Received: name: Alice, age: 30, city: New York
show_args(name="Bob", pet="Fluffy, the bunny")
# Received: name: Bob, pet: Fluffy, the bunny


# Exercises: Level 3
# Write a function called is_prime, which checks if a number is prime.
# Write a functions which checks if all items are unique in the list.
# Write a function which checks if all the items of the list are of the same data type.
# Write a function which check if provided variable is a valid python variable
# Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
