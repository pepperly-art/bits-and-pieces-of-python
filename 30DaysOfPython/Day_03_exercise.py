
age = 41
height = 5.5
complex_num = (1 + 1j)

print("Triangle Math")
base = input('Base Width: ')
height = input('Height:')
area = 0.5 * float(base) * float(height)

print(f"The area of the triangle is {area}")

print("Triangular Perimites?")
a = int(input("Side a: "))
b = int(input("Side b: "))
c = int(input("Side c: "))
perimeter = a + b + c
print(f"The perimeter of the triangle is {perimeter}")

print("Area of a rectangle")
length = int(input("Length :"))
width = int(input("Width: "))
area = length * width
print(f"The area of this rectangle is {area}")

print("Circle!")
radius = int(input("Radius: "))
area = 3.14 * radius * radius
circumference = 2 * 3.14 * radius
print(f"The area of this circle is {area} and the circumference is {circumference}")

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# I don't know what this means?

print("this one is asking me math I don't want to look up")
x = int(input("x? "))
y = 2 * x - 2
print(f"{y} = 2({x}) - 2")

# I am out of my gourd

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Compare the slopes in tasks 8 and 9.
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

print("Maths??")
x = int(input("x? "))
y = (x ** 2) + (6 * x) + 9
print("try to use different values it says and I say no!")
print(f"{y} - ({x})^2 + (6 x {x}) + 9, do whatever you want")

print(f"The length of python is {len('python')} and jargon is {len('jargon')}")
print(f"Python is longer than jargon: {len('python') > len('jargon')}")

print("'I hope this course is not full of jargon.' ... 'jargon' is in this sentence?")
print('jargon' in 'I hope this course is not full of jargon')

print("There is no 'on' in both 'dragon' and 'python'")
print('on' not in 'python' or 'on' not in 'dragon')

len_py = len("python")
len_py_float = float(len_py)
len_py_str = str(len_py_float)
print(len_py_str)

print("Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?")
num = int(input("number"))
even_or_not = num % 2
print(f"{num} is even: {even_or_not == 0}")

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# huh???

print("Type '10' is equal to type of 10")
print( type('10') is type(10))
print( '10' == 10 )

print("Pay Rate")
hours = int(input("Hours"))
rate = int(input("Rate per hour: $"))
earning = rate * hours
print(f"Your weekly earning is {earning}")

print("Life!?")
years = int(input("Number of years you have lived: "))
seconds = years * 31536000
print(f"You have lived for {seconds} seconds.")

for num in range(1, 6):
    print(f"{num} {int(num / num)} {num * 1} {num * num} {num ** 3}")