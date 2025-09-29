# Task 5: Data Analysis on CSV Files

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load CSV file
df = pd.read_csv("sales_data.csv")

# 2. Basic info
print("First 5 rows:\n", df.head())
print("\nShape of DataFrame:", df.shape)
print("\nColumns:", df.columns)

# 3. Group by 'Region' and sum 'Sales'
region_sales = df.groupby("Region")["Sales"].sum()
print("\nTotal Sales by Region:\n", region_sales)

# 4. Group by 'Product' and average 'Quantity'
product_quantity = df.groupby("Product")["Quantity"].mean()
print("\nAverage Quantity by Product:\n", product_quantity)

# 5. Filter rows where Sales > 500
high_sales = df[df["Sales"] > 500]
print("\nHigh Sales Records:\n", high_sales.head())

# 6. Plot: Sales by Region
region_sales.plot(kind="bar", title="Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

# 7. Plot: Average Quantity by Product
product_quantity.plot(kind="barh", color="orange", title="Avg Quantity by Product")
plt.xlabel("Quantity")
plt.ylabel("Product")
plt.show()
