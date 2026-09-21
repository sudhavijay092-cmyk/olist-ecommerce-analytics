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

carrier_before_purchase = df[
    df["order_delivered_carrier_date"]
    < df["order_purchase_timestamp"]
]

customer_before_carrier = df[
    df["order_delivered_customer_date"]
    < df["order_delivered_carrier_date"]
]

print("=" * 60)
print("TIMESTAMP ANOMALY INVESTIGATION")
print("=" * 60)

print("\n1. Carrier before purchase — order status:")
print(
    carrier_before_purchase["order_status"]
    .value_counts()
)

print("\n2. Carrier before purchase — count:")
print(len(carrier_before_purchase))

print("\n3. Customer delivery before carrier — order status:")
print(
    customer_before_carrier["order_status"]
    .value_counts()
)

print("\n4. Customer delivery before carrier — count:")
print(len(customer_before_carrier))

print("\n5. Example carrier-before-purchase records:")
print(
    carrier_before_purchase[
        [
            "order_id",
            "order_status",
            "order_purchase_timestamp",
            "order_delivered_carrier_date",
            "order_delivered_customer_date"
        ]
    ]
    .head(10)
    .to_string(index=False)
)