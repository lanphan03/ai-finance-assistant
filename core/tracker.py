import csv
import os
from datetime import datetime

DATA_FILE = "data/expenses.csv"
FIELDNAMES = ["Date", "Category", "Amount", "Description"]

def initialize_file():
    if not os.path.exists(DATA_FILE):
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()

def add_expense(date=None, category=None, amount=None, description=None):
    if date is None:
        date = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
        date = date if date else datetime.today().strftime('%Y-%m-%d')

    if category is None:
        category = input("Enter category (e.g., Food, Transport, Rent): ").strip()

    if amount is None:
        amount = float(input("Enter amount: ").strip())

    if description is None:
        description = input("Enter description (optional): ").strip()

    expense = {
        "Date": date,
        "Category": category,
        "Amount": round(amount, 2),
        "Description": description
    }

    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow(expense)

    print("Expense successfully added.")

def view_expenses():
    initialize_file()
    with open(DATA_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        expenses = list(reader)

    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- Expense History ---")
    for row in expenses:
        print(f"{row['Date']} | {row['Category']} | ${row['Amount']} | {row['Description']}")

def filter_expenses_by_category():
    try:
        df = pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        print("No expense data found.")
        return

    if df.empty:
        print("No expenses recorded.")
        return

    category = input("Enter category to filter by: ").strip()
    filtered_df = df[df["Category"].str.lower() == category.lower()]

    if filtered_df.empty:
        print(f"No expenses found for category '{category}'.")
    else:
        print(f"Expenses for category '{category}':")
        print(filtered_df.to_string(index=False))

# Run this file directly to add an expense
if __name__ == "__main__":
    initialize_file()
    add_expense()
