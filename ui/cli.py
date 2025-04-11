from core import tracker

def main():
    tracker.initialize_file()

    while True:
        print("\n==== AI Finance Assistant ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == '1':
            tracker.add_expense()
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            print("See you later!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
