import pandas as pd

payments = pd.read_csv(
    "data/raw_public/olist_order_payments_dataset.csv",
    usecols=["order_id"]
)

orders = pd.read_csv(
    "data/raw_public/olist_orders_dataset.csv",
    usecols=["order_id"]
)

print("=" * 60)
print("PAYMENTS → ORDERS REFERENTIAL INTEGRITY")
print("=" * 60)

print("\nPayment rows:", len(payments))
print("Unique order IDs in payments:",
      payments["order_id"].nunique())

print("Orders:", len(orders))
print("Unique order IDs in orders:",
      orders["order_id"].nunique())

missing_orders = payments.loc[
    ~payments["order_id"].isin(orders["order_id"])
]

orders_without_payment = orders.loc[
    ~orders["order_id"].isin(payments["order_id"])
]

print("\nPayment rows with missing order reference:",
      len(missing_orders))

print("Unique missing order IDs:",
      missing_orders["order_id"].nunique())

print("\nOrders without payment record:",
      len(orders_without_payment))

print("Order IDs without payment:",
      orders_without_payment["order_id"].tolist())