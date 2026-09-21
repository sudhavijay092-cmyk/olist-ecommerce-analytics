import pandas as pd

orders = pd.read_csv(
    "data/raw_public/olist_orders_dataset.csv",
    usecols=["order_id", "customer_id"]
)

customers = pd.read_csv(
    "data/raw_public/olist_customers_dataset.csv",
    usecols=["customer_id"]
)

print("=" * 60)
print("ORDERS → CUSTOMERS REFERENTIAL INTEGRITY")
print("=" * 60)

print("\nOrders:", len(orders))
print("Customers:", len(customers))

print("\nUnique order customer IDs:",
      orders["customer_id"].nunique())

print("Unique customer IDs:",
      customers["customer_id"].nunique())

missing_customers = orders.loc[
    ~orders["customer_id"].isin(customers["customer_id"])
]

print("\nOrders with missing customer reference:",
      len(missing_customers))

print("\nUnique missing customer IDs:",
      missing_customers["customer_id"].nunique())