a = float(input("Enter first number "))
b = float(input("Enter second number "))
cal = int(input("Enter Choise \n1.ADD \n2.SUB \n3.MUl \n4.DIV \n"))
match cal:
    case 1:
        print(f"{a} + {b} = {a+b}")
    case 2:
        print(f"{a} -{b} = {a-b}")
    case 3:
        print(f"{a} * {b} = {a*b}")
    case 4:
        print(f"{a} / {b} = {a/b}")
    case _:
        print("Invalid")
