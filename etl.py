import pandas as pd

# --- Step 1: Load CSVs ---
df_products = pd.read_csv('data/products.csv')
df_sales = pd.read_csv('data/sales.csv')
df_inventory = pd.read_csv('data/inventory.csv')

# --- Step 2: Basic cleaning ---
df_products.drop_duplicates(inplace=True)
df_sales.drop_duplicates(inplace=True)
df_inventory.drop_duplicates(inplace=True)

df_products.fillna({'cost': 0, 'brand': 'Unknown'}, inplace=True)
df_sales.fillna({'quantity': 1, 'price': 0}, inplace=True)
df_inventory.fillna({'current_stock': 0}, inplace=True)

# --- Step 3: Merge sales with product info ---
df_merged = df_sales.merge(df_products, on='product_id', how='left')

# --- Step 4: Calculate revenue per product ---
df_merged['revenue'] = df_merged['quantity'] * df_merged['price']
revenue_per_product = df_merged.groupby(
    ['product_id', 'name', 'category']
).agg(
    total_revenue=('revenue', 'sum'),
    total_units=('quantity', 'sum')
).reset_index()

# --- Step 4b: Calculate stockout risk ---
# For simplicity, estimate average daily sales per product
df_sales['date'] = pd.to_datetime(df_sales['date'])
daily_sales = df_sales.groupby('product_id').agg(
    avg_daily_sales=('quantity', lambda x: x.sum() / x.nunique())
).reset_index()

# Merge with inventory
inventory_merged = df_inventory.merge(daily_sales, on='product_id', how='left')
inventory_merged['avg_daily_sales'].fillna(1, inplace=True)  # avoid divide by zero
inventory_merged['stockout_days'] = inventory_merged['current_stock'] / inventory_merged['avg_daily_sales']

# Low-stock alert
inventory_merged['low_stock_alert'] = inventory_merged['current_stock'] < inventory_merged['reorder_level']

# --- Step 4c: Merge stock info with revenue data ---
final_df = revenue_per_product.merge(
    inventory_merged[['product_id', 'current_stock', 'stockout_days', 'low_stock_alert']],
    on='product_id',
    how='left'
)

# --- Step 5: Save final enriched data ---
final_df.to_csv('data/revenue_inventory.csv', index=False)

print("ETL complete! Revenue + inventory insights saved.")
print(final_df)


# --- Step 5: Save processed data ---
revenue_per_product.to_csv('data/revenue_per_product.csv', index=False)

print("ETL complete! Revenue per product calculated and saved.")
print(revenue_per_product)
