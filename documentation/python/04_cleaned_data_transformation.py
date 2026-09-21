import pandas as pd
from pathlib import Path


# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_PATH = Path(r"D:\swiftcart-margin-under-pressure")

RAW_DATA_PATH = PROJECT_PATH / "Data" / "raw_public"

CLEANED_DATA_PATH = PROJECT_PATH / "Data" / "cleaned"


# ============================================================
# CREATE CLEANED DATA FOLDER IF IT DOES NOT EXIST
# ============================================================

CLEANED_DATA_PATH.mkdir(parents=True, exist_ok=True)


# ============================================================
# LOAD RAW DATA
# ============================================================

orders = pd.read_csv(
    RAW_DATA_PATH / "olist_orders_dataset.csv"
)

customers = pd.read_csv(
    RAW_DATA_PATH / "olist_customers_dataset.csv"
)

order_items = pd.read_csv(
    RAW_DATA_PATH / "olist_order_items_dataset.csv"
)

products = pd.read_csv(
    RAW_DATA_PATH / "olist_products_dataset.csv"
)

sellers = pd.read_csv(
    RAW_DATA_PATH / "olist_sellers_dataset.csv"
)

payments = pd.read_csv(
    RAW_DATA_PATH / "olist_order_payments_dataset.csv"
)

reviews = pd.read_csv(
    RAW_DATA_PATH / "olist_order_reviews_dataset.csv"
)


# ============================================================
# CLEANING COPIES
# ============================================================

# Create copies so the original loaded DataFrames remain unchanged.

orders_clean = orders.copy()

customers_clean = customers.copy()

order_items_clean = order_items.copy()

products_clean = products.copy()

sellers_clean = sellers.copy()

payments_clean = payments.copy()

reviews_clean = reviews.copy()


# ============================================================
# SAVE CLEANED COPIES
# ============================================================

orders_clean.to_csv(
    CLEANED_DATA_PATH / "olist_orders_clean.csv",
    index=False
)

customers_clean.to_csv(
    CLEANED_DATA_PATH / "olist_customers_clean.csv",
    index=False
)

order_items_clean.to_csv(
    CLEANED_DATA_PATH / "olist_order_items_clean.csv",
    index=False
)

products_clean.to_csv(
    CLEANED_DATA_PATH / "olist_products_clean.csv",
    index=False
)

sellers_clean.to_csv(
    CLEANED_DATA_PATH / "olist_sellers_clean.csv",
    index=False
)

payments_clean.to_csv(
    CLEANED_DATA_PATH / "olist_order_payments_clean.csv",
    index=False
)

reviews_clean.to_csv(
    CLEANED_DATA_PATH / "olist_order_reviews_clean.csv",
    index=False
)


# ============================================================
# COMPLETION MESSAGE
# ============================================================

print("=" * 70)
print("CLEANED DATA TRANSFORMATION SCRIPT CREATED")
print("=" * 70)

print("\nRaw data source:")
print(RAW_DATA_PATH)

print("\nCleaned data destination:")
print(CLEANED_DATA_PATH)

print("\nTables prepared for transformation:")

for table_name in [
    "Orders",
    "Customers",
    "Order Items",
    "Products",
    "Sellers",
    "Payments",
    "Reviews"
]:
    print(f"- {table_name}")