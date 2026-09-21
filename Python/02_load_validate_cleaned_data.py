import pandas as pd
from pathlib import Path


# Project paths
PROJECT_PATH = Path(r"D:\swiftcart-margin-under-pressure")
CLEANED_DATA_PATH = PROJECT_PATH / "Data" / "cleaned"


# Load cleaned datasets
customers = pd.read_csv(
    CLEANED_DATA_PATH / "olist_customers_clean.csv"
)

orders = pd.read_csv(
    CLEANED_DATA_PATH / "olist_orders_clean.csv",
    parse_dates=[
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]
)

order_items = pd.read_csv(
    CLEANED_DATA_PATH / "olist_order_items_clean.csv",
    parse_dates=[
        "shipping_limit_date"
    ]
)

order_payments = pd.read_csv(
    CLEANED_DATA_PATH / "olist_order_payments_clean.csv"
)

order_reviews = pd.read_csv(
    CLEANED_DATA_PATH / "olist_order_reviews_clean.csv",
    parse_dates=[
        "review_creation_date",
        "review_answer_timestamp"
    ]
)

products = pd.read_csv(
    CLEANED_DATA_PATH / "olist_products_clean.csv"
)

sellers = pd.read_csv(
    CLEANED_DATA_PATH / "olist_sellers_clean.csv"
)


# Store datasets for validation
datasets = {
    "customers": customers,
    "orders": orders,
    "order_items": order_items,
    "order_payments": order_payments,
    "order_reviews": order_reviews,
    "products": products,
    "sellers": sellers
}


# Print dataset validation summary
print("\nSWIFTCART — CLEANED DATA VALIDATION")
print("-" * 50)

for name, df in datasets.items():
    print(f"\nDataset: {name}")
    print(f"Rows: {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]}")
    print("Column Names:")
    print(df.columns.tolist())


# Check important date column data types
print("\nDATE COLUMN VALIDATION")
print("-" * 50)

date_checks = {
    "orders": [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ],
    "order_items": [
        "shipping_limit_date"
    ],
    "order_reviews": [
        "review_creation_date",
        "review_answer_timestamp"
    ]
}

for dataset_name, columns in date_checks.items():
    print(f"\n{dataset_name}:")

    for column in columns:
        print(f"{column}: {datasets[dataset_name][column].dtype}")


print("\nValidation completed successfully.")