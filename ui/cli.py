from core import tracker
from ml.categorizer import ExpenseCategorizer

def main():
    tracker.initialize_file()
    categorizer = ExpenseCategorizer()
    
    if not categorizer.load_model():
        categorizer.train()

    while True:
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Retrain Category Model")
        print("4. Show Summary")
        print("5. Plot Spending by Category")
        print("5. Plot Spending by Category (Bar)")
        print("6. Plot Spending Distribution (Pie)")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()

        if choice == '1':
            # Get user input for description
            date = input("Enter date (YYYY-MM-DD): ").strip()
            date = date if date else None

            description = input("Enter description: ").strip()

            # Predict category
            suggested = categorizer.predict(description)
            if suggested:
                print(f"Suggested category: {suggested}")

            category = input("Enter category: ").strip()
            category = suggested if category == "" and suggested else category

            amount = float(input("Enter amount: ").strip())

            # Add the expense
            tracker.add_expense(date=date, category=category, amount=amount, description=description)
            
        elif choice == '2':
            tracker.view_expenses()
            
        elif choice == '3':
            print("Retraining the model on updated data...")
            categorizer.train()
            print("Model updated.")

        elif choice == '4':
            from core import stats
            stats.show_summary()

        elif choice == '5':
            from visuals import plotter
            plotter.plot_spending_by_category()

        elif choice == '6':
            from visuals import plotter
            plotter.plot_spending_pie_chart()
            
        elif choice == '7':
            print("See you later!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
