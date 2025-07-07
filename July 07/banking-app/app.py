def main():
    while True:
        print("===== Banking Application =====")
        print("1. Account Creation")
        print("2. User Login")
        print("3. View Account Balance")
        print("4. Transfer Funds")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            view_balance()
        elif choice == "4":
            transfer_funds()
        elif choice == "5":
            view_transaction_history()
        elif choice == "6":
            print("Exiting application")
            break
        else:
            print("Invalid option\n")


if __name__ == "__main__":
    main()