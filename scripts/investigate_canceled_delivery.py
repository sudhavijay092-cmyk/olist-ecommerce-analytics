import pandas as pd

file_path = "data/raw_public/olist_orders_dataset.csv"

df = pd.read_csv(file_path)

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors="coerce")

canceled = df[df["order_status"] == "canceled"]

canceled_with_delivery = canceled[
    canceled["order_delivered_customer_date"].notna()
]

print("=" * 60)
print("CANCELED ORDERS WITH DELIVERY DATES")
print("=" * 60)

print("\n1. Canceled orders:")
print(len(canceled))

print("\n2. Canceled orders with carrier date:")
print(
    canceled["order_delivered_carrier_date"].notna().sum()
)

print("\n3. Canceled orders with customer delivery date:")
print(
    canceled["order_delivered_customer_date"].notna().sum()
)

print("\n4. Canceled orders with any delivery date:")
print(
    (
        canceled["order_delivered_carrier_date"].notna()
        |
        canceled["order_delivered_customer_date"].notna()
    ).sum()
)

print("\n5. Details of canceled orders with customer delivery date:")

print(
    canceled_with_delivery[
        [
            "order_id",
            "order_status",
            "order_purchase_timestamp",
            "order_approved_at",
            "order_delivered_carrier_date",
            "order_delivered_customer_date",
            "order_estimated_delivery_date"
        ]
    ].to_string(index=False)
)