# Get marks for each subject
ds = float(input("Enter Discrete Structure Marks: "))
oop = float(input("Enter OOP Marks: "))
mp = float(input("Enter Microprocessor Marks: "))
mth = float(input("Enter Mathematics-I Marks: "))
stat = float(input("Enter Statistics-II Marks: "))


def to_gpa(marks):
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


ds_gpa = to_gpa(ds)
oop_gpa = to_gpa(oop)
mp_gpa = to_gpa(mp)
mth_gpa = to_gpa(mth)
stat_gpa = to_gpa(stat)

cgpa = (ds_gpa * 3 + oop_gpa * 3 + mp_gpa * 3 + mth_gpa * 3 + stat_gpa * 3) / 15
percentage = ((ds + oop + mp + mth + stat) / 500) * 100
# Display results
print(f"\nYour CGPA: {cgpa:.2f}")
print(f"Equivalent Percentage: {percentage:.2f}%")
