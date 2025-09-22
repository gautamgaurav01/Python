# python file open
f = open("demofile.txt")
print(f.read())

with open("demofile.txt") as f:
    print(f.read())

f = open("demofile.txt")
print(f.readline())
f.close()

with open("demofile.txt") as f:
    print(f.read(5))


with open("demofile.txt") as f:
    print(f.readline())

with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline())

with open("demofile.txt") as f:
    for x in f:
        print(x)


# Python File Write
with open("demofile.txt", "a") as f:
    f.write("\nNow the file has more content!")

# open and read the file after the appending:
with open("demofile.txt") as f:
    print(f.read())

with open("demofile.txt", "w") as f:
    f.write("Woops! I have deleted the content!")

# open and read the file after the overwriting:
with open("demofile.txt") as f:
    print(f.read())

# f = open("myfile.txt", "x")
import os

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("The file does not exist")
