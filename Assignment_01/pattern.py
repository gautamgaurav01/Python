n = int(input("Enter number of rows: "))

# Triangle
triangle = ""
for x in range(1, n + 1):
    triangle += " " * (n - x) + "*" * (2 * x - 1) + "\n"
print("Triangle\n")
print(triangle)


# Diamond
diamond = ""
for x in range(1, n + 1):
    diamond += " " * (n - x) + "*" * (2 * x - 1) + "\n"
for y in range(n - 1, 0, -1):
    diamond += " " * (n - y) + "*" * (2 * y - 1) + "\n"
print("Diamond\n")
print(diamond)
