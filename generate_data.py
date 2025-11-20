import pandas as pd
import random
from faker import Faker

fake = Faker()

# --- Products ---
products = []
categories = ['Mobile', 'Laptop', 'Audio', 'Appliances']
brands = ['Samsung', 'Apple', 'Sony', 'LG', 'Dell']
for i in range(1, 11):  # 10 products
    products.append({
        'product_id': i,
        'name': fake.word().capitalize(),
        'category': random.choice(categories),
        'brand': random.choice(brands),
        'cost': random.randint(50, 1000),
        'supplier': fake.company()
    })
df_products = pd.DataFrame(products)
df_products.to_csv('data/products.csv', index=False)

# --- Sales ---
sales = []
platforms = ['Web', 'Shopee', 'Lazada']
for i in range(1, 21):  # 20 orders
    sales.append({
        'order_id': i,
        'product_id': random.randint(1, 10),
        'quantity': random.randint(1, 5),
        'price': random.randint(60, 1200),
        'platform': random.choice(platforms),
        'date': fake.date_this_year()
    })
df_sales = pd.DataFrame(sales)
df_sales.to_csv('data/sales.csv', index=False)

# --- Inventory ---
inventory = []
for i in range(1, 11):
    inventory.append({
        'product_id': i,
        'current_stock': random.randint(10, 100),
        'reorder_level': random.randint(5, 20),
        'lead_time_days': random.randint(3, 10)
    })
df_inventory = pd.DataFrame(inventory)
df_inventory.to_csv('data/inventory.csv', index=False)

print("Sample data created in 'data/' folder!")
