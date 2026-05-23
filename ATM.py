user_info = {
    "Name": "Badrinadh",
    "Mobile Number": "9876543210",
    "ATM PIN": "6600",
    "Balance": 78965,
    "Transaction History": []
}
print("========== WELCOME TO ATM ==========")
print("Insert Your ATM Card")
attempts = 3
while attempts > 0:
    user_pin = input("Enter ATM PIN: ")
    if len(user_pin) == 4 and user_pin.isdigit():
        if user_pin == user_info["ATM PIN"]:
            print("\nLogin Successful")
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
                    "\n\nEnter Your Choice: "
                ))

                # CHECK BALANCE
                if choice == 1:
                    print("\nAvailable Balance: ₹", user_info["Balance"])

                # DEPOSIT
                elif choice == 2:
                    amount = int(input("Enter Deposit Amount: ₹"))
                    if amount > 0:
                        user_info["Balance"] += amount
                        user_info["Transaction History"].append(f"Deposited ₹{amount}")
                        print("Amount Deposited Successfully")
                        print("Updated Balance: ₹", user_info["Balance"])
                    else:
                        print("Invalid Amount")

                # WITHDRAW
                elif choice == 3:
                    amount = int(input("Enter Withdraw Amount: ₹"))
                    if amount <= user_info["Balance"] and amount > 0:
                        user_info["Balance"] -= amount
                        user_info["Transaction History"].append(f"Withdrawn ₹{amount}")
                        print("Please Collect Your Cash")
                        print("Remaining Balance: ₹", user_info["Balance"])
                    else:
                        print("Insufficient Balance or Invalid Amount")

                # MINI STATEMENT
                elif choice == 4:
                    print("\n========== MINI STATEMENT ==========")
                    if len(user_info["Transaction History"]) == 0:
                        print("No Transactions Available")
                    else:
                        for i in user_info["Transaction History"]:
                            print(i)
                    print("Current Balance: ₹", user_info["Balance"])
                    
                # CHANGE PIN
                elif choice == 5:
                    old_pin = input("Enter Old PIN: ")
                    if old_pin == user_info["ATM PIN"]:
                        new_pin = input("Enter New 4-Digit PIN: ")
                        if len(new_pin) == 4 and new_pin.isdigit():
                            confirm_pin = input("Confirm New PIN: ")
                            if new_pin == confirm_pin:
                                user_info["ATM PIN"] = new_pin
                                print("PIN Changed Successfully")
                            else:
                                print("PIN Confirmation Failed")
                        else:
                            print("PIN Must Contain Exactly 4 Digits")
                    else:
                        print("Wrong Old PIN")

                # FORGOT PIN
                elif choice == 6:
                    mobile = input("Enter Registered Mobile Number: ")
                    if mobile == user_info["Mobile Number"]:
                        new_pin = input("Enter New 4-Digit PIN: ")
                        if len(new_pin) == 4 and new_pin.isdigit():
                            user_info["ATM PIN"] = new_pin
                            print("PIN Reset Successfully")
                        else:
                            print("PIN Must Be 4 Digits")
                    else:
                        print("Mobile Number Not Matched")

                # EXIT
                elif choice == 7:
                    print("Thank You For Using ATM")
                    break
                else:
                    print("Invalid Choice")
            break

        else:
            attempts -= 1
            if attempts > 0:
                print(f"Invalid PIN. You Have {attempts} Attempts Left")
            else:
                print("Card Blocked")
    else:
        print("PIN Must Contain Exactly 4 Digits")
