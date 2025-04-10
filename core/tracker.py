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


# Run this file directly to add an expense
if __name__ == "__main__":
    initialize_file()
    add_expense()
