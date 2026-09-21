import pandas as pd
from pathlib import Path


# ============================================================
# 1. PROJECT PATHS
# ============================================================

PROJECT_PATH = Path(r"D:\swiftcart-margin-under-pressure")

ANALYSIS_DATA_PATH = (
    PROJECT_PATH
    / "Data"
    / "cleaned"
    / "swiftcart_order_analysis.csv"
)


# ============================================================
# 2. LOAD ORDER-LEVEL ANALYSIS DATASET
# ============================================================

order_analysis = pd.read_csv(
    ANALYSIS_DATA_PATH,
    parse_dates=[
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]
)


# ============================================================
# 3. DATASET OVERVIEW
# ============================================================

print("\nSWIFTCART — EXPLORATORY ANALYSIS AND VALIDATION")
print("=" * 60)

print("\n1. DATASET SHAPE")
print("-" * 60)

print(f"Rows: {order_analysis.shape[0]:,}")
print(f"Columns: {order_analysis.shape[1]}")


# ============================================================
# 4. ORDER-LEVEL GRAIN VALIDATION
# ============================================================

print("\n2. ORDER GRAIN VALIDATION")
print("-" * 60)

duplicate_orders = order_analysis["order_id"].duplicated().sum()

print(f"Duplicate order IDs: {duplicate_orders:,}")


# ============================================================
# 5. MISSING VALUE ANALYSIS
# ============================================================

print("\n3. MISSING VALUES")
print("-" * 60)

missing_values = (
    order_analysis
    .isna()
    .sum()
    .sort_values(ascending=False)
)

print(missing_values)


# ============================================================
# 6. DELIVERY STATUS DISTRIBUTION
# ============================================================

print("\n4. DELIVERY STATUS DISTRIBUTION")
print("-" * 60)

delivery_status_summary = (
    order_analysis["delivery_status"]
    .value_counts(dropna=False)
)

print(delivery_status_summary)


# ============================================================
# 7. REVIEW SCORE DISTRIBUTION
# ============================================================

print("\n5. REVIEW SCORE DISTRIBUTION")
print("-" * 60)

review_score_summary = (
    order_analysis["review_score"]
    .value_counts(dropna=False)
    .sort_index()
)

print(review_score_summary)


# ============================================================
# 8. DESCRIPTIVE STATISTICS
# ============================================================

print("\n6. NUMERICAL SUMMARY")
print("-" * 60)

numerical_columns = [
    "total_items",
    "total_product_value",
    "total_freight_value",
    "total_payment_value",
    "review_score",
    "delivery_delay_days",
    "freight_percentage"
]

print(
    order_analysis[numerical_columns]
    .describe()
)


# ============================================================
# 9. FREIGHT PERCENTAGE VALIDATION
# ============================================================

print("\n7. FREIGHT PERCENTAGE CHECK")
print("-" * 60)

print(
    order_analysis["freight_percentage"]
    .describe()
)


# Check extreme freight percentage values
extreme_freight = order_analysis[
    order_analysis["freight_percentage"] > 100
]

print(f"\nOrders with freight percentage above 100%: {len(extreme_freight):,}")


# ============================================================
# 10. DELIVERY DELAY VALIDATION
# ============================================================

print("\n8. DELIVERY DELAY CHECK")
print("-" * 60)

late_orders = order_analysis[
    order_analysis["delivery_status"] == "Late"
]

print(f"Late orders: {len(late_orders):,}")

print(
    "\nAverage days late:",
    round(late_orders["delivery_delay_days"].mean(), 2)
)


# ============================================================
# 11. FINAL VALIDATION STATUS
# ============================================================

print("\n" + "=" * 60)

if duplicate_orders == 0:
    print("ORDER-LEVEL GRAIN VALIDATION: PASSED")
else:
    print("ORDER-LEVEL GRAIN VALIDATION: FAILED")

print("Exploratory analysis and validation completed.")