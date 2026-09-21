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

print("=" * 60)
print("ORDER TIMESTAMP VALIDATION")
print("=" * 60)

print("\n1. Rows where approval is before purchase:")
print(
    (df["order_approved_at"] < df["order_purchase_timestamp"]).sum()
)

print("\n2. Rows where carrier handoff is before purchase:")
print(
    (df["order_delivered_carrier_date"] < df["order_purchase_timestamp"]).sum()
)

print("\n3. Rows where customer delivery is before purchase:")
print(
    (df["order_delivered_customer_date"] < df["order_purchase_timestamp"]).sum()
)

print("\n4. Rows where customer delivery is before carrier handoff:")
print(
    (
        df["order_delivered_customer_date"]
        < df["order_delivered_carrier_date"]
    ).sum()
)

print("\n5. Rows where estimated delivery is before purchase:")
print(
    (
        df["order_estimated_delivery_date"]
        < df["order_purchase_timestamp"]
    ).sum()
)

print("\n6. Rows where delivered customer date is after estimated date:")
print(
    (
        df["order_delivered_customer_date"]
        > df["order_estimated_delivery_date"]
    ).sum()
)

print("\n7. Missing timestamp counts:")
print(df[date_columns].isna().sum())