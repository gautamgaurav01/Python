class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area of circle = {3.14 * (self.radius ** 2)} cm²")

    def perimeter(self):
        print(f"Perimeter of circle = {2 * 3.14 * self.radius} cm")


class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        print(f"Area of triangle = {0.5 * self.base * self.height} cm²")

    def perimeter(self):
        print(f"Perimeter of triangle = {self.side1 + self.side2 + self.side3} cm")


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(f"Area of rectangle = {self.length * self.breadth} cm²")

    def perimeter(self):
        print(f"Perimeter of rectangle = {2 * (self.length + self.breadth)} cm")


while True:
    print("\n=== Shape Menu ===")
    print("1. Circle")
    print("2. Triangle")
    print("3. Rectangle")
    print("4. Exit")
    choice = input("Enter choice: ")
    match choice:
        case "1":
            r = float(input("Enter radius (cm): "))
            c = Circle(r)
            c.area()
            c.perimeter()
        case "2":
            b = float(input("Enter base (cm): "))
            h = float(input("Enter height (cm): "))
            s1 = float(input("Enter side1 (cm): "))
            s2 = float(input("Enter side2 (cm): "))
            s3 = float(input("Enter side3 (cm): "))
            t = Triangle(b, h, s1, s2, s3)
            t.area()
            t.perimeter()
        case "3":
            l = float(input("Enter length (cm): "))
            w = float(input("Enter breadth (cm): "))
            r = Rectangle(l, w)
            r.area()
            r.perimeter()
        case "4":
            print("Exiting...")
            break
        case _:
            print("Invalid choice. Try again.")
