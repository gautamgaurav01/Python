class BankAccount:
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"You deposited Rs.{amount} and new balance is Rs.{self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"You withdrew Rs.{amount} and new balance is Rs.{self.balance}")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"The balance is Rs.{self.balance}")


holder = input("Enter account holder name: ")
acc_no = input("Enter account number: ")
bal = int(input("Initialize a balance: "))

h1 = BankAccount(holder, acc_no, bal)

while True:
    print("\n1. Deposit money")
    print("2. Withdraw money")
    print("3. Balance inquiry")
    print("4. Exit")
    try:
        mod = int(input("Choose an option from above: "))
    except ValueError:
        print("Please enter a valid number (1-4)")
        continue
    match mod:
        case 1:
            try:
                depo = int(input("Enter the amount to deposit: "))
                h1.deposit(depo)
            except ValueError:
                print("Please enter a valid amount")
        case 2:
            try:
                withd = int(input("Enter the amount to withdraw: "))
                h1.withdraw(withd)
            except ValueError:
                print("Please enter a valid amount")
        case 3:
            h1.show_balance()
        case 4:
            print("Thank you for banking with us!")
            break
        case _:
            print("Invalid option. Please choose 1-4")
