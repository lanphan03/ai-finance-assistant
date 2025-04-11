import pandas as pd

DATA_FILE = "data/expenses.csv"

def load_data():
    try:
        return pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        print("No expenses found yet.")
        return pd.DataFrame()

def show_summary():
    df = load_data()
    if df.empty:
        return

    print("\n==== Summary ====")
    print(f"Total spent: ${df['Amount'].sum():.2f}")
    print(f"Average expense: ${df['Amount'].mean():.2f}")
    print(f"Largest expense: ${df['Amount'].max():.2f}")

    print("\nSpending by category:")
    category_totals = df.groupby('Category')['Amount'].sum()
    for category, amount in category_totals.items():
        print(f"  - {category}: ${amount:.2f}")
