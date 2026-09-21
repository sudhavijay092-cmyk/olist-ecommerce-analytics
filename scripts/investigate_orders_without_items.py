import pandas as pd

orders = pd.read_csv(
    "data/raw_public/olist_orders_dataset.csv",
    usecols=["order_id", "order_status"]
)

items = pd.read_csv(
    "data/raw_public/olist_order_items_dataset.csv",
    usecols=["order_id"]
)

orders_without_items = orders[
    ~orders["order_id"].isin(items["order_id"])
]

print("=" * 60)
print("ORDERS WITHOUT ORDER ITEMS")
print("=" * 60)

print("\n1. Orders without item records:")
print(len(orders_without_items))

print("\n2. Order status distribution:")
print(
    orders_without_items["order_status"]
    .value_counts()
)

print("\n3. Percentage by order status:")
print(
    orders_without_items["order_status"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)