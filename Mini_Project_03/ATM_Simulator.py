class ATM:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def save_account(self):
        with open("atm.csv", "a") as f:
            f.write(f"{self.account_number},{self.pin},{self.balance}\n")

    def deposit(self, amount):
        amount = float(amount)
        updated_lines = []
        with open("atm.csv", "r") as f:
            lines = f.readlines()
        for line in lines:
            acc, pin, bal = line.strip().split(",")
            if acc == self.account_number:
                bal = float(bal) + amount
                updated_lines.append(f"{acc},{pin},{bal}\n")
                print(f"Deposited Rs.{amount}. New Balance = Rs.{bal}")
            else:
                updated_lines.append(line)
        with open("atm.csv", "w") as f:
            f.writelines(updated_lines)

    def withdraw(self, amount):
        amount = float(amount)
        updated_lines = []
        with open("atm.csv", "r") as f:
            lines = f.readlines()
        for line in lines:
            acc, pin, bal = line.strip().split(",")
            if acc == self.account_number:
                bal = float(bal)
                if bal >= amount:
                    bal -= amount
                    print(f"Withdrawn Rs.{amount}. Remaining Balance = Rs.{bal}")
                else:
                    print("Insufficient balance!")
                updated_lines.append(f"{acc},{pin},{bal}\n")
            else:
                updated_lines.append(line)
        with open("atm.csv", "w") as f:
            f.writelines(updated_lines)

    def view_balance(self):
        with open("atm.csv", "r") as f:
            for line in f:
                acc, pin, bal = line.strip().split(",")
                if acc == self.account_number:
                    print(f"Balance: Rs.{bal}")
                    return
        print("Account not found!")

    def change_pin(self, old_pin, new_pin):
        updated_lines = []
        with open("atm.csv", "r") as f:
            lines = f.readlines()
        for line in lines:
            acc, pin, bal = line.strip().split(",")
            if acc == self.account_number:
                if pin == old_pin:
                    pin = new_pin
                    print(" PIN changed successfully!")
                else:
                    print("Incorrect old PIN!")
            updated_lines.append(f"{acc},{pin},{bal}\n")
        with open("atm.csv", "w") as f:
            f.writelines(updated_lines)


acc_no = input("Enter your account number: ")
pin = input("Enter PIN: ")
atm_obj = ATM(acc_no, pin)

while True:
    print("\n--- ATM Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Balance")
    print("4. Change PIN")
    print("5. Exit")
    choice = input("Enter your choice: ")

    match choice:
        case "1":
            amt = input("Enter amount to deposit: ")
            atm_obj.deposit(amt)
        case "2":
            amt = input("Enter amount to withdraw: ")
            atm_obj.withdraw(amt)
        case "3":
            atm_obj.view_balance()
        case "4":
            old = input("Enter old PIN: ")
            new = input("Enter new PIN: ")
            atm_obj.change_pin(old, new)
        case "5":
            print("Exiting... Thank you!")
            break
        case _:
            print("Invalid choice. Try again.")
