import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "data/expenses.csv"

def plot_spending_by_category():
    try:
        df = pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        print("No data to plot.")
        return

    if df.empty:
        print("No expenses recorded yet.")
        return

    category_totals = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    category_totals.plot(kind='bar')
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Amount Spent ($)")
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
