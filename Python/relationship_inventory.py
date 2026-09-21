import pandas as pd
from pathlib import Path


# ============================================================
# PROJECT PATH
# ============================================================

PROJECT_PATH = Path(r"D:\swiftcart-margin-under-pressure")

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

reviews = pd.read_csv(
    RAW_DATA_PATH / "olist_order_reviews_dataset.csv"
)


# ============================================================
# FUNCTION: CHECK RELATIONSHIP CARDINALITY
# ============================================================

def check_relationship(
    relationship_name,
    left_table,
    left_key,
    right_table,
    right_key
):

    left_counts = left_table[left_key].value_counts()

    right_counts = right_table[right_key].value_counts()

    left_max = left_counts.max()

    right_max = right_counts.max()

    left_duplicate_keys = (left_counts > 1).sum()

    right_duplicate_keys = (right_counts > 1).sum()


    print("\n" + "=" * 70)
    print(relationship_name)
    print("=" * 70)

    print(f"\nLeft table key: {left_key}")
    print(f"Right table key: {right_key}")

    print(f"\nLeft table rows: {len(left_table):,}")
    print(f"Left table unique keys: {left_table[left_key].nunique():,}")
    print(f"Left table duplicated keys: {left_duplicate_keys:,}")
    print(f"Maximum rows per left key: {left_max:,}")

    print(f"\nRight table rows: {len(right_table):,}")
    print(f"Right table unique keys: {right_table[right_key].nunique():,}")
    print(f"Right table duplicated keys: {right_duplicate_keys:,}")
    print(f"Maximum rows per right key: {right_max:,}")


    # --------------------------------------------------------
    # DETERMINE CARDINALITY
    # --------------------------------------------------------

    if left_max == 1 and right_max == 1:
        relationship_type = "ONE-TO-ONE"

    elif left_max == 1 and right_max > 1:
        relationship_type = "ONE-TO-MANY"

    elif left_max > 1 and right_max == 1:
        relationship_type = "MANY-TO-ONE"

    else:
        relationship_type = "MANY-TO-MANY / IRREGULAR"


    print("\nRELATIONSHIP CARDINALITY:")
    print(f"--> {relationship_type}")


# ============================================================
# 1. ORDERS → CUSTOMERS
# ============================================================

check_relationship(
    relationship_name="1. ORDERS → CUSTOMERS",
    left_table=orders,
    left_key="customer_id",
    right_table=customers,
    right_key="customer_id"
)


# ============================================================
# 2. ORDERS → ORDER ITEMS
# ============================================================

check_relationship(
    relationship_name="2. ORDERS → ORDER ITEMS",
    left_table=orders,
    left_key="order_id",
    right_table=order_items,
    right_key="order_id"
)


# ============================================================
# 3. ORDER ITEMS → PRODUCTS
# ============================================================

check_relationship(
    relationship_name="3. ORDER ITEMS → PRODUCTS",
    left_table=order_items,
    left_key="product_id",
    right_table=products,
    right_key="product_id"
)


# ============================================================
# 4. ORDER ITEMS → SELLERS
# ============================================================

check_relationship(
    relationship_name="4. ORDER ITEMS → SELLERS",
    left_table=order_items,
    left_key="seller_id",
    right_table=sellers,
    right_key="seller_id"
)


# ============================================================
# 5. ORDERS → PAYMENTS
# ============================================================

check_relationship(
    relationship_name="5. ORDERS → PAYMENTS",
    left_table=orders,
    left_key="order_id",
    right_table=payments,
    right_key="order_id"
)


# ============================================================
# 6. ORDERS → REVIEWS
# ============================================================

check_relationship(
    relationship_name="6. ORDERS → REVIEWS",
    left_table=orders,
    left_key="order_id",
    right_table=reviews,
    right_key="order_id"
)