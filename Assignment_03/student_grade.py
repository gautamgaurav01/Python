class Student:
    def __init__(self, mark1, mark2, mark3, mark4, mark5):
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        self.mark4 = mark4
        self.mark5 = mark5

    def average(self):
        total = self.mark1 + self.mark2 + self.mark3 + self.mark4 + self.mark5
        avg = total / 5
        print(f"The average marks of the student is: {avg:.2f}")

    def to_gpa(self, marks):
        if 90 <= marks <= 100:
            return 4.0
        elif 80 <= marks < 90:
            return 3.7
        elif 70 <= marks < 80:
            return 3.3
        elif 60 <= marks < 70:
            return 3.0
        elif 50 <= marks < 60:
            return 2.7
        else:
            return 0.0

    def calculate_gpa(self):
        ds_gpa = self.to_gpa(self.mark1)
        oop_gpa = self.to_gpa(self.mark2)
        mp_gpa = self.to_gpa(self.mark3)
        mth_gpa = self.to_gpa(self.mark4)
        stat_gpa = self.to_gpa(self.mark5)

        cgpa = (ds_gpa * 3 + oop_gpa * 3 + mp_gpa * 3 + mth_gpa * 3 + stat_gpa * 3) / 15
        print(f"\nYour CGPA: {cgpa:.2f}")
        return cgpa

    def grade(self, full):
        total_obtained = self.mark1 + self.mark2 + self.mark3 + self.mark4 + self.mark5
        total_possible = full * 5
        percent = (total_obtained / total_possible) * 100

        if 90 <= percent <= 100:
            print("Your grade is A")
        elif 80 <= percent < 90:
            print("Your grade is A-")
        elif 70 <= percent < 80:
            print("Your grade is B+")
        elif 60 <= percent < 70:
            print("Your grade is B")
        elif 50 <= percent < 60:
            print("Your grade is B-")
        else:
            print("You failed")


while True:
    fm = float(input("Enter the full marks per subject: "))
    ds = float(input("Enter the marks in subject 1: "))
    oop = float(input("Enter the marks in subject 2: "))
    mp = float(input("Enter the marks in subject 3: "))
    mth = float(input("Enter the marks in subject 4: "))
    stat = float(input("Enter the marks in subject 5: "))
    s1 = Student(ds, oop, mp, mth, stat)
    s1.average()
    s1.grade(fm)
    s1.calculate_gpa()
