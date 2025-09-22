# Comments, Variables, Data Types, Operators, Strings, and Formatting


# This is a single-line comment
"""
This is a
multi-line comment
"""

# IF-ELSE STATEMENT
if 5 > 2:
    print("Five is greater than Two")
else:
    print("Two is greater than Five")

# VARIABLES AND DATA TYPES
# Variables store values, and their type can be int, float, str, bool, etc.

name = "Gaurav"  # str
age = 20  # int
print("Name:", name, "Age:", age)

x = 10  # int
y = 3.14  # float
z = "Python"  # str
a = True  # bool

# OPERATORS
a = 5
b = 2
print("Addition:", a + b)  # 7
print("Subtraction:", a - b)  # 3
print("Multiplication:", a * b)  # 10
print("Division:", a / b)  # 2.5
print("Exponentiation:", a**b)  # 25
print("Modulo:", a % b)  # 1
print("Floor division:", a // b)  # 2

# Type conversion
x = int(3.5)  # float to int
y = str(10)  # int to string
print("Converted values:", x, y)

# STRINGS
text = "Python"
print("First character:", text[0])  # Access first character
print("Concatenation:", text + " 3.13")  # Combine strings

# String functions
a = "Hello, World!"
print("Length of string:", len(a))  # 13

# Check if substring exists
txt = "The best things in life are free!"
print("'free' in txt:", "free" in txt)  # True

if "free" in txt:
    print("Yes, 'free' is present.")

# Slicing
b = "Hello, World!"
print("First 5 characters:", b[:5])  # 'Hello'

# Changing case
a = "Hello, World!"
print("Uppercase:", a.upper())
print("Lowercase:", a.lower())

# Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print("Concatenated string:", c)

# STRING FORMATTING
price = 59
txt = f"The price is {price} dollars"
print(txt)  # The price is 59 dollars

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)  # The price is 59.00 dollars
