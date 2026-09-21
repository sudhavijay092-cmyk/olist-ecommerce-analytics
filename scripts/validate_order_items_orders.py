import pandas as pd

order_items = pd.read_csv(
    "data/raw_public/olist_order_items_dataset.csv",
    usecols=["order_id"]
)

orders = pd.read_csv(
    "data/raw_public/olist_orders_dataset.csv",
    usecols=["order_id"]
)

print("=" * 60)
print("ORDER ITEMS → ORDERS REFERENTIAL INTEGRITY")
print("=" * 60)

print("\nOrder item rows:", len(order_items))
print("Unique order IDs in order items:",
      order_items["order_id"].nunique())

print("Orders:", len(orders))
print("Unique order IDs in orders:",
      orders["order_id"].nunique())

missing_orders = order_items.loc[
    ~order_items["order_id"].isin(orders["order_id"])
]

print("\nOrder item rows with missing order reference:",
      len(missing_orders))

print("Unique missing order IDs:",
      missing_orders["order_id"].nunique())