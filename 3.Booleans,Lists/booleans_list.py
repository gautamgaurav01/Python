# Booleans, Lists,

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

