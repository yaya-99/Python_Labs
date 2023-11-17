from Account import Account

def Start():
    account_number = input("Enter Account Number: ")
    account_name = input("Enter Account Name: ")
    initial_balance = float(input("Enter Initial Balance: "))

    account = Account(account_number, account_name, initial_balance)

    while True:
        print("\nMenu:")
        print("1. Display Account Details")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Transaction History")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            account.d_acc_details()
        elif choice == "2":
            amount = float(input("Enter the deposit amount: "))
            account.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter the withdrawal amount: "))
            account.withdraw(amount)
        elif choice == "4":
            account.check_transaction_history()
        elif choice == "5":
            print("Exiting program. Thank You!!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

Start()

