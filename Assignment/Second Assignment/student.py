def add_student():
    with open("student.csv", "a") as f:
        name = input("Enter a name: ").capitalize()
        grade = input("Enter Pass/Fail: ").capitalize()
        f.write(f"{name},{grade}")


def view_student():
    with open("student.csv") as f:
        print(f.read())


def remove_student():
    name = input("Enter a name you want to remove: ").capitalize()
    with open("student.csv") as f:
        lines = f.readlines()
    with open("student.csv", "w") as f:
        for x in lines:
            if name in x:
                continue
            f.write(x)


def view_pass():
    with open("student.csv") as f:
        for x in f:
            if "Pass" in x:
                print(x)


def view_fail():
    with open("student.csv") as f:
        for x in f:
            if "Fail" in x:
                print(x)


while True:
    print("1. Add Student")
    print("2. Remove Student")
    print("3. View Student")
    print("4. View Pass Student")
    print("5. View Fail Student")
    print("6. Exit")
    choice = input("Enter your choice: ")

    match choice:
        case "1":
            add_student()
        case "2":
            remove_student()
        case "3":
            view_student()
        case "4":
            view_pass()
        case "5":
            view_fail()
        case "6":
            print("Exiting... Thank you for shopping!")
            break
        case _:
            print("Invalid choice. Try again.\n")
