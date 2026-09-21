import pandas as pd
from pathlib import Path


# ============================================================
# PROJECT PATH
# ============================================================

PROJECT_PATH = Path(r"D:\swiftcart-margin-under-pressure")


# ============================================================
# RAW DATA PATH
# ============================================================

RAW_DATA_PATH = PROJECT_PATH / "data" / "raw_public"


# ============================================================
# LOAD RAW OLIST TABLES
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


# ============================================================
# FUNCTION TO CHECK A SINGLE COLUMN KEY
# ============================================================

def check_single_key(df, table_name, key_column):

    total_rows = len(df)

    unique_values = df[key_column].nunique()

    duplicate_rows = total_rows - unique_values

    max_rows_per_key = df[key_column].value_counts().max()

    print("=" * 70)
    print(table_name.upper())
    print("=" * 70)

    print(f"Candidate key: {key_column}")
    print(f"Total rows: {total_rows:,}")
    print(f"Unique key values: {unique_values:,}")
    print(f"Duplicate key values: {duplicate_rows:,}")
    print(f"Maximum rows per key: {max_rows_per_key}")

    if total_rows == unique_values:
        print("\nKEY RESULT:")
        print("--> UNIQUE KEY")
    else:
        print("\nKEY RESULT:")
        print("--> NOT UNIQUE")

    print()


# ============================================================
# FUNCTION TO CHECK A COMPOSITE KEY
# ============================================================

def check_composite_key(df, table_name, key_columns):

    total_rows = len(df)

    unique_combinations = df[key_columns].drop_duplicates().shape[0]

    duplicate_rows = total_rows - unique_combinations

    print("=" * 70)
    print(table_name.upper())
    print("=" * 70)

    print(f"Candidate composite key: {key_columns}")
    print(f"Total rows: {total_rows:,}")
    print(f"Unique key combinations: {unique_combinations:,}")
    print(f"Duplicate key combinations: {duplicate_rows:,}")

    if total_rows == unique_combinations:
        print("\nKEY RESULT:")
        print("--> UNIQUE COMPOSITE KEY")
    else:
        print("\nKEY RESULT:")
        print("--> NOT UNIQUE COMPOSITE KEY")

    print()


# ============================================================
# TABLE GRAIN CHECKS
# ============================================================


# 1. ORDERS
check_single_key(
    orders,
    "1. Orders",
    "order_id"
)


# 2. CUSTOMERS
check_single_key(
    customers,
    "2. Customers",
    "customer_id"
)


# 3. ORDER ITEMS
check_composite_key(
    order_items,
    "3. Order Items",
    ["order_id", "order_item_id"]
)


# 4. PRODUCTS
check_single_key(
    products,
    "4. Products",
    "product_id"
)


# 5. SELLERS
check_single_key(
    sellers,
    "5. Sellers",
    "seller_id"
)


# 6. PAYMENTS
check_composite_key(
    payments,
    "6. Payments",
    ["order_id", "payment_sequential"]
)