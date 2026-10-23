"""Cleans the Supermart CSV (mixed date formats) and prints the headline numbers.
Run from the project folder:  python scripts/clean_and_summarise.py
"""
import pandas as pd

df = pd.read_csv("data/supermart_grocery_sales_original.csv", encoding="utf-8-sig")

def parse(x):
    # dd-mm-yyyy (with dashes) and m/d/yyyy (with slashes) both appear in the file
    return pd.to_datetime(x, format="%d-%m-%Y") if "-" in x else pd.to_datetime(x, format="%m/%d/%Y")

df["Order Date"] = df["Order Date"].map(parse)
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Profit Margin"] = (df["Profit"] / df["Sales"]).round(4)
df.to_csv("data/supermart_grocery_sales_cleaned.csv", index=False)

print("Total sales :", df.Sales.sum())
print("Total profit:", round(df.Profit.sum(), 2))
print("Margin      :", round(df.Profit.sum() / df.Sales.sum(), 4))
print(df.groupby("Year")[["Sales", "Profit"]].sum())
print(df.groupby("Category")[["Sales", "Profit"]].sum().sort_values("Sales", ascending=False))
print(df.groupby("Region")[["Sales", "Profit"]].sum().sort_values("Sales", ascending=False))
print(df.groupby("City")[["Sales", "Profit"]].sum().sort_values("Sales", ascending=False))
print("Corr(discount, profit):", round(df.Discount.corr(df.Profit), 3))
