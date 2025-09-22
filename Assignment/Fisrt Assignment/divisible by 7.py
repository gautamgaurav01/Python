count = 0
for x in range(1000, 3000 + 1):
    if x % 7 == 0 and x % 5 != 0:
        print(x)
        count += 1
print(f"Total number between 1000 to 3000 divisible by 7 but not by 5 is {count}")
