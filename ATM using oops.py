class ATM:
    def __init__(self):
        self.name = "Badrinadh"
        self.mobile = "9876543210"
        self.pin = "6600"
        self.balance = 78965
        self.transaction_history = []

    def check_balance(self):
        print("\nAvailable Balance: ", self.balance)

    def deposit(self):
        amount = int(input("Enter Deposit Amount: "))
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited {amount}")
            print("Amount Deposited Successfully")
            print("Updated Balance: ", self.balance)
        else:
            print("Invalid Amount")

    def withdraw(self):
        amount = int(input("Enter Withdraw Amount: "))
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn {amount}")
            print("Please Collect Your Cash")
            print("Remaining Balance: ", self.balance)
        else:
            print("Insufficient Balance or Invalid Amount")

    def mini_statement(self):
        print("\n========== MINI STATEMENT ==========")

        if len(self.transaction_history) == 0:
            print("No Transactions Available")
        else:
            for transaction in self.transaction_history:
                print(transaction)

        print("Current Balance: ", self.balance)

    def change_pin(self):
        old_pin = input("Enter Old PIN: ")

        if old_pin == self.pin:
            new_pin = input("Enter New 4-Digit PIN: ")

            if len(new_pin) == 4 and new_pin.isdigit():
                confirm_pin = input("Confirm New PIN: ")

                if new_pin == confirm_pin:
                    self.pin = new_pin
                    print("PIN Changed Successfully")
                else:
                    print("PIN Confirmation Failed")
            else:
                print("PIN Must Contain Exactly 4 Digits")
        else:
            print("Wrong Old PIN")

    def forgot_pin(self):
        mobile = input("Enter Registered Mobile Number: ")

        if mobile == self.mobile:
            new_pin = input("Enter New 4-Digit PIN: ")

            if len(new_pin) == 4 and new_pin.isdigit():
                self.pin = new_pin
                print("PIN Reset Successfully")
            else:
                print("PIN Must Be 4 Digits")
        else:
            print("Mobile Number Not Matched")
    def menu(self):
        while True:
            choice = int(input(
                "\n========== ATM MENU =========="
                "\n1. Check Balance"
                "\n2. Deposit"
                "\n3. Withdraw"
                "\n4. Mini Statement"
                "\n5. Change PIN"
                "\n6. Forgot PIN"
                "\n7. Exit"
                "\n\nEnter Your Choice: "))
            if choice == 1:
                self.check_balance()

            elif choice == 2:
                self.deposit()

            elif choice == 3:
                self.withdraw()

            elif choice == 4:
                self.mini_statement()

            elif choice == 5:
                self.change_pin()

            elif choice == 6:
                self.forgot_pin()

            elif choice == 7:
                print("Thank You For Using ATM")
                break

            else:
                print("Invalid Choice")

    def login(self):
        print("========== WELCOME TO ATM ==========")
        print("Insert Your ATM Card")

        attempts = 3

        while attempts > 0:

            user_pin = input("Enter ATM PIN: ")

            if len(user_pin) == 4 and user_pin.isdigit():

                if user_pin == self.pin:
                    print("\nLogin Successful")
                    self.menu()
                    break

                else:
                    attempts -= 1

                    if attempts > 0:
                        print(f"Invalid PIN. You Have {attempts} Attempts Left")
                    else:
                        print("Card Blocked")

            else:
                print("PIN Must Contain Exactly 4 Digits")


# Object Creation
atm = ATM()

# Method Calling
atm.login()
