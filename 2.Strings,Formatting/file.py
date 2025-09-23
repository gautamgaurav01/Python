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