import pandas as pd
from faker import Faker
import random
import os


# Create the raw data folder if it doesn't exist
os.makedirs('data/raw', exist_ok=True)

fake = Faker()
departments = ['Tools', 'Electrical', 'Appliances', 'Paint']
products = {
    'Tools': ['Cordless Drill', 'Wrench Set', 'Hammer', 'Pliers'],
    'Electrical': ['Outlet Extension', 'Light Bulb Pack', 'Wire', 'GFCI Outlet'],
    'Appliances': ['Mini Fridge', 'Microwave', 'Dishwasher', 'Oven'],
    'Paint': ['Interior Paint', 'Brush Kit', 'Sandpaper', 'Behr Primer']
}


def generate_sales_data(n=100):
    data = []
    for _ in range(n):
        dept = random.choice(departments)
        product = random.choice(products[dept])
        row = {
            'date': fake.date_this_month(),
            'department': dept,
            'product_id': f"{dept[0]}{random.randint(100,999)}",
            'product_name': product,
            'quantity_sold': random.randint(1, 10),
            'unit_price': round(random.uniform(10, 150), 2),
            'location': fake.city()
        }
        data.append(row)
    return pd.DataFrame(data)


# Generate data and save to /data/raw/
df = generate_sales_data(200)
save_path = 'data/raw/retail_sales_2025_05_01.csv'
df.to_csv(save_path, index=False)
print(f"CSV file saved: {save_path}")
