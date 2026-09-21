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
print("ORDER STATUS → DELIVERY DATE LOGIC")
print("=" * 60)

print("\n1. Delivered orders:")
delivered = df[df["order_status"] == "delivered"]

print("Total delivered:", len(delivered))
print(
    "Missing carrier date:",
    delivered["order_delivered_carrier_date"].isna().sum()
)
print(
    "Missing customer delivery date:",
    delivered["order_delivered_customer_date"].isna().sum()
)

print("\n2. Shipped orders:")
shipped = df[df["order_status"] == "shipped"]

print("Total shipped:", len(shipped))
print(
    "Missing carrier date:",
    shipped["order_delivered_carrier_date"].isna().sum()
)
print(
    "Missing customer delivery date:",
    shipped["order_delivered_customer_date"].isna().sum()
)

print("\n3. Canceled orders:")
canceled = df[df["order_status"] == "canceled"]

print("Total canceled:", len(canceled))
print(
    "Has customer delivery date:",
    canceled["order_delivered_customer_date"].notna().sum()
)

print("\n4. Unavailable orders:")
unavailable = df[df["order_status"] == "unavailable"]

print("Total unavailable:", len(unavailable))
print(
    "Has customer delivery date:",
    unavailable["order_delivered_customer_date"].notna().sum()
)

print("\n5. Delivered orders missing BOTH delivery dates:")

missing_both = delivered[
    delivered["order_delivered_carrier_date"].isna()
    &
    delivered["order_delivered_customer_date"].isna()
]

print(len(missing_both))

print("\n6. Delivered orders missing customer delivery date only:")

missing_customer_delivery = delivered[
    delivered["order_delivered_customer_date"].isna()
]

print(len(missing_customer_delivery))