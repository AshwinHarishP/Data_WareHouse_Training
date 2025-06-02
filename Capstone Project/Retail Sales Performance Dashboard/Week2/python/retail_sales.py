import pandas as pd
import numpy as np

"""
    Loading the data from CSV file
"""
sales_df = pd.read_csv('sales.csv')
products_df = pd.read_csv('products.csv')

# Displaying only 5 records from each csv file
print("\nProducts Data:")
print(products_df.head())

print("\nSales Data:")
print(sales_df.head())

"""
    Correcting and cleaning the data
"""
# Data Cleaning
sales_df['quantity'] = sales_df['quantity'].fillna(0)
products_df['price'] = products_df['price'].fillna(0)

# Correcting data types
sales_df['sale_date'] = pd.to_datetime(sales_df['sale_date'])
sales_df['quantity'] = sales_df['quantity'].astype(int)
products_df['price'] = products_df['price'].astype(float)

"""
    Calculations
"""
# 1. Adding Discount
discount_rate = 0.40
products_df['discount'] = products_df['price'] * discount_rate
products_df['discounted_price'] = products_df['price'] - products_df['discount']

merged_df = pd.merge(sales_df, products_df, on='product_id', how='left')

# 2. Revenue Calculation
merged_df['revenue'] = merged_df['quantity'] * merged_df['discounted_price']
print("\n merged data")
print(merged_df)

# 3. Adding Profit Margin
cost_rate = 0.50
merged_df['cost'] = merged_df['quantity'] * merged_df['price'] * cost_rate

merged_df['profit_margin'] = np.where(
    merged_df['revenue'] > 0, #condition
    (merged_df['revenue'] - merged_df['cost']) / merged_df['revenue'] * 100, # True statement
    0 # False statement
)

# 4. Calculating Total Revenue of Product and Store
product_revenue = merged_df.groupby('product_name')['revenue'].sum().reset_index(name='TotalRevenue').sort_values(by='TotalRevenue', ascending=False)
store_revenue = merged_df.groupby('store_id')['revenue'].sum().reset_index(name='TotalRevenue').sort_values(by='TotalRevenue', ascending=False)

"""
    Storing the summary in csv file
"""
product_revenue.to_csv("product_revenue_summary.csv", index=True)
store_revenue.to_csv("store_revenue_summary.csv", index=True)
print("Summary exported to summary.csv")

"""
    Displaying the summary
"""
print("\nTotal Revenue: Product:")
print(product_revenue)

print("\nTotal Revenue: Store:")
print(store_revenue)