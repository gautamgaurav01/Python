# Booleans, Lists, If-Else, Match, and Loops

# BOOLEANS
# Booleans are a data type that represents one of two values: True or False.
# They are often used in conditions, loops, and logical operations.

print("========== BOOLEANS ==========")
print("Basic Boolean values:")
print(10 > 9)  # True
print(10 == 9)  # False
print(10 < 9)  # False

# Boolean variables
is_sunny = True
is_raining = False
print("Is it sunny?", is_sunny)
print("Is it raining?", is_raining)

# Boolean conversion using bool()
print("Boolean conversion examples:")
print(bool("Hello"))  # True (non-empty string)
print(bool(""))  # False (empty string)
print(bool(15))  # True (non-zero number)
print(bool(0))  # False
print(bool([]))  # False (empty list)
print(bool([1, 2, 3]))  # True (non-empty list)

# Boolean in if conditions
temperature = 30
if temperature > 25:
    print("It is hot outside!")
else:
    print("Temperature is fine.")

# Logical operators
a = True
b = False
print("AND operation:", a and b)  # False
print("OR operation:", a or b)  # True
print("NOT operation:", not a)  #  False

# LISTS
# A list is an ordered, changeable collection that allows duplicate elements.

print("\n========== LISTS ==========")
fruits = ["apple", "banana", "cherry"]
print("List:", fruits)
print("Length of list:", len(fruits))

# Accessing items
print("First item:", fruits[0])
print("Last item:", fruits[-1])
print("Items from index 1 to 2:", fruits[1:3])

# Changing elements
fruits[1] = "blueberry"
print("Modified list:", fruits)

# Adding elements
fruits.append("orange")
fruits.insert(1, "kiwi")
print("After adding elements:", fruits)

# Removing elements
fruits.remove("cherry")
popped_item = fruits.pop()
print("After removing elements:", fruits)
print("Popped item:", popped_item)

# Looping through a list
print("Looping through list:")
for fruit in fruits:
    print(fruit)

# List comprehension
newlist = [x for x in fruits if "a" in x]
print("Fruits containing 'a':", newlist)

# Nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested list:", nested_list)
print("Access 5 from nested list:", nested_list[1][1])

# IF-ELSE STATEMENTS
# Used to perform decision making. Executes code blocks based on conditions.

print("\n========== IF-ELSE ==========")
a = 50
b = 20
if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")
else:
    print("b is greater than a")

# Nested if-else
x = 15
if x > 10:
    if x > 20:
        print("x is greater than 20")
    else:
        print("x is between 11 and 20")
else:
    print("x is 10 or less")

# Short Hand If
if a > b:
    print("a is greater than b")

# Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")

# Using logical operators in conditions
age = 25
if age > 18 and age < 30:
    print("Age is between 19 and 29")
if age < 18 or age > 65:
    print("Young or senior citizen")


# MATCH STATEMENT
# It selects one code block to execute based on the value of a variable.

print("\n========== MATCH STATEMENT ==========")
day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")

# Match with conditions
month = 5
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case 6 | 7 if month == 5:
        print("Weekend in May")
    case _:
        print("No match")

# FOR LOOPS
# Used to iterate over sequences like list, tuple, string, or range.

print("\n========== FOR LOOPS ==========")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using break in loops
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)

# Using continue in loops
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# Nested loops
colors = ["red", "green"]
sizes = ["S", "M", "L"]
for color in colors:
    for size in sizes:
        print(color, size)

# Using range()
for i in range(5):  # 0 to 4
    print("Range example:", i)

for i in range(2, 10, 2):  # Start=2, Stop=10, Step=2
    print("Step example:", i)

# Loop with else
for i in range(3):
    print(i)
else:
    print("Loop finished without break")


# WHILE LOOPS
# Executes a block of code as long as a condition is True.

print("\n========== WHILE LOOPS ==========")
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

# Using break in while
count = 0
while True:
    print("Infinite loop example count:", count)
    count += 1
    if count >= 3:
        break

# Using continue in while
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print("Continue example count:", count)
