import pandas as pd
from pathlib import Path


# ============================================================
# 1. PROJECT PATHS
# ============================================================

PROJECT_PATH = Path(r"D:\swiftcart-margin-under-pressure")
CLEANED_DATA_PATH = PROJECT_PATH / "Data" / "cleaned"


# ============================================================
# 2. LOAD REQUIRED CLEANED DATASETS
# ============================================================

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


# ============================================================
# 3. CREATE ORDER-ITEM SUMMARY
# ============================================================

order_items_summary = (
    order_items
    .groupby("order_id", as_index=False)
    .agg(
        total_items=("order_item_id", "count"),
        total_product_value=("price", "sum"),
        total_freight_value=("freight_value", "sum")
    )
)


# ============================================================
# 4. CREATE ORDER-PAYMENT SUMMARY
# ============================================================

order_payments_summary = (
    order_payments
    .groupby("order_id", as_index=False)
    .agg(
        total_payment_value=("payment_value", "sum"),
        payment_installments=("payment_installments", "max")
    )
)


# ============================================================
# 5. CREATE ORDER-REVIEW SUMMARY
# ============================================================

order_reviews_summary = (
    order_reviews
    .groupby("order_id", as_index=False)
    .agg(
        review_score=("review_score", "mean")
    )
)


# ============================================================
# 6. MERGE ORDER-LEVEL DATA
# ============================================================

order_analysis = (
    orders
    .merge(
        customers[
            [
                "customer_id",
                "customer_unique_id",
                "customer_city",
                "customer_state"
            ]
        ],
        on="customer_id",
        how="left"
    )
    .merge(
        order_items_summary,
        on="order_id",
        how="left"
    )
    .merge(
        order_payments_summary,
        on="order_id",
        how="left"
    )
    .merge(
        order_reviews_summary,
        on="order_id",
        how="left"
    )
)


# ============================================================
# 7. CREATE ANALYSIS FEATURES
# ============================================================

# Delivery delay in days
order_analysis["delivery_delay_days"] = (
    order_analysis["order_delivered_customer_date"]
    - order_analysis["order_estimated_delivery_date"]
).dt.total_seconds() / 86400


# Delivery status
order_analysis["delivery_status"] = pd.NA

delivered_mask = (
    order_analysis["order_delivered_customer_date"].notna()
    & order_analysis["order_estimated_delivery_date"].notna()
)

order_analysis.loc[
    delivered_mask
    & (order_analysis["delivery_delay_days"] <= 0),
    "delivery_status"
] = "On Time"

order_analysis.loc[
    delivered_mask
    & (order_analysis["delivery_delay_days"] > 0),
    "delivery_status"
] = "Late"


# Freight percentage of product value
order_analysis["freight_percentage"] = (
    order_analysis["total_freight_value"]
    / order_analysis["total_product_value"]
) * 100


# ============================================================
# 8. VALIDATE ORDER-LEVEL GRAIN
# ============================================================

duplicate_orders = order_analysis["order_id"].duplicated().sum()


# ============================================================
# 9. PRINT VALIDATION RESULTS
# ============================================================

print("\nSWIFTCART — ORDER ANALYSIS DATASET")
print("-" * 55)

print(f"\nTotal rows: {order_analysis.shape[0]:,}")
print(f"Total columns: {order_analysis.shape[1]}")

print(f"\nDuplicate order IDs: {duplicate_orders:,}")

print("\nDelivery Status:")
print(
    order_analysis["delivery_status"]
    .value_counts(dropna=False)
)

print("\nMissing Values:")
print(
    order_analysis[
        [
            "total_items",
            "total_product_value",
            "total_freight_value",
            "total_payment_value",
            "review_score",
            "delivery_status"
        ]
    ]
    .isna()
    .sum()
)


# ============================================================
# 10. SAVE ORDER-LEVEL ANALYSIS DATASET
# ============================================================

OUTPUT_PATH = (
    PROJECT_PATH
    / "Data"
    / "cleaned"
    / "swiftcart_order_analysis.csv"
)

order_analysis.to_csv(
    OUTPUT_PATH,
    index=False
)


print("\nOrder-level analysis dataset created successfully.")
print(f"Saved to: {OUTPUT_PATH}")