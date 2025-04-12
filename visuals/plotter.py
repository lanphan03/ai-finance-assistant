import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "data/expenses.csv"

# Plot Spending by Category (BAR CHART)
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

# Plot Spending Distribution (PIE CHART)
def plot_spending_pie_chart():
    try:
        df = pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        print("No data to plot.")
        return

    if df.empty:
        print("No expenses recorded yet.")
        return

    category_totals = df.groupby("Category")["Amount"].sum()

    plt.figure(figsize=(8, 8))
    plt.pie(
        category_totals,
        labels=category_totals.index,
        autopct="%1.1f%%",
        startangle=140
    )
    plt.title("Spending Distribution by Category")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from core.tracker import DATA_FILE

def plot_spending_over_time():
    try:
        df = pd.read_csv(DATA_FILE, parse_dates=["Date"])
    except FileNotFoundError:
        print("No data to plot.")
        return

    if df.empty:
        print("No expenses recorded.")
        return

    df["Date"] = pd.to_datetime(df["Date"])
    df.sort_values("Date", inplace=True)
    daily_totals = df.groupby("Date")["Amount"].sum()

    plt.figure(figsize=(10, 5))
    plt.plot(daily_totals.index, daily_totals.values, marker="o", linestyle="-", color="blue")
    plt.title("Spending Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Amount Spent")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

