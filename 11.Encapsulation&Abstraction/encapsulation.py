# Encapsulation means hiding internal details of a class and only exposing what’s necessary. It helps to protect important data from being changed directly and keeps the code secure and organized.


# 1. Public Members
class Employee:
    def __init__(self, name):
        self.name = name  # public attribute

    def display_name(self):  # public method
        print(self.name)


emp = Employee("John")
emp.display_name()  # Accessible
print(emp.name)  # Accessible


# 2. Protected members
class Employee:
    def __init__(self, name, age):
        self.name = name  # public
        self._age = age  # protected


class SubEmployee(Employee):
    def show_age(self):
        print("Age:", self._age)  # Accessible in subclass


emp = SubEmployee("Ross", 30)
print(emp.name)  # Public accessible
emp.show_age()  # Protected accessed through subclass


# 3. Private members
class Employee:
    def __init__(self, name, salary):
        self.name = name  # public
        self.__salary = salary  # private

    def show_salary(self):
        print("Salary:", self.__salary)


emp = Employee("Robert", 60000)
print(emp.name)  # Public accessible
emp.show_salary()  # Accessing private correctly
# print(emp.__salary)    # Error: Not accessible directly


class BankAccount:
    def __init__(self):
        self.balance = 1000

    def _show_balance(self):
        print(f"Balance: ₹{self.balance}")  # Protected method

    def __update_balance(self, amount):
        self.balance += amount  # Private method

    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)  # Accessing private method internally
            self._show_balance()  # Accessing protected method
        else:
            print("Invalid deposit amount!")


account = BankAccount()
account._show_balance()  # Works, but should be treated as internal
# account.__update_balance(500)  # Error: private method
account.deposit(500)  # Uses both methods internally


# Getter and Setter Methods


class Employee:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def get_salary(self):  # Getter method
        return self.__salary

    def set_salary(self, amount):  # Setter method
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount!")


emp = Employee()
print(emp.get_salary())  # Access salary using getter

emp.set_salary(60000)  # Update salary using setter
print(emp.get_salary())
