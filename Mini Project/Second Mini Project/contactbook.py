def add_contact():
    with open("contact.txt", "a") as f:
        name = input("Enter a name: ").capitalize()
        number = input("Enter a number: ")
        while len(number) != 10:
            number = input("Enter a number again number should be 10 digits: ")
        f.write(f"\nName: {name} , Number: {number}")


def view_contact():
    with open("contact.txt") as f:
        print(f.read())


def remove_contact():
    name = input("Enter a name you want to remove: ").capitalize()
    with open("contact.txt") as f:
        lines = f.readlines()
    with open("contact.txt", "w") as f:
        for x in lines:
            if name in x:
                continue
            f.write(x)


while True:
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. View Contact")
    print("4. Exit")
    choice = input("Enter your choice: ")

    match choice:
        case "1":
            add_contact()
        case "2":
            remove_contact()
        case "3":
            view_contact()
        case "4":
            print("Exiting... Thank you for shopping!")
            break
        case _:
            print("Invalid choice. Try again.\n")
