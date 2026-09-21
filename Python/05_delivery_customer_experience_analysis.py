import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

OUTPUT_PATH = PROJECT_PATH / "output" / "python"

# Create output folder if it does not exist
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)


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
# 3. CREATE DELIVERED ORDER DATASET
# ============================================================

delivered_orders = order_analysis[
    order_analysis["delivery_status"].notna()
].copy()


# ============================================================
# 4. DELIVERY STATUS AND CUSTOMER EXPERIENCE
# ============================================================

delivery_review_summary = (
    delivered_orders
    .groupby("delivery_status", as_index=False)
    .agg(
        orders=("order_id", "count"),
        average_review_score=("review_score", "mean"),
        median_review_score=("review_score", "median")
    )
)

# Calculate review rate separately
review_counts = (
    delivered_orders
    .groupby("delivery_status")["review_score"]
    .count()
    .reset_index(name="reviewed_orders")
)

delivery_review_summary = delivery_review_summary.merge(
    review_counts,
    on="delivery_status",
    how="left"
)

delivery_review_summary["review_rate_percentage"] = (
    delivery_review_summary["reviewed_orders"]
    / delivery_review_summary["orders"]
) * 100


# ============================================================
# 5. PRINT DELIVERY STATUS RESULTS
# ============================================================

print("\nSWIFTCART — DELIVERY AND CUSTOMER EXPERIENCE ANALYSIS")
print("=" * 65)

print("\n1. DELIVERY STATUS AND REVIEW SCORE")
print("-" * 65)

print(
    delivery_review_summary.round(2)
)


# ============================================================
# 6. ANALYZE LATE ORDER DELAY GROUPS
# ============================================================

late_orders = delivered_orders[
    delivered_orders["delivery_status"] == "Late"
].copy()


# Create delay groups
delay_bins = [0, 3, 7, 14, float("inf")]

delay_labels = [
    "1–3 Days Late",
    "4–7 Days Late",
    "8–14 Days Late",
    "15+ Days Late"
]

late_orders["delay_group"] = pd.cut(
    late_orders["delivery_delay_days"],
    bins=delay_bins,
    labels=delay_labels,
    include_lowest=True
)


delay_review_summary = (
    late_orders
    .groupby(
        "delay_group",
        observed=False
    )
    .agg(
        orders=("order_id", "count"),
        average_days_late=(
            "delivery_delay_days",
            "mean"
        ),
        average_review_score=(
            "review_score",
            "mean"
        )
    )
    .reset_index()
)


print("\n2. REVIEW SCORES BY DELAY GROUP")
print("-" * 65)

print(
    delay_review_summary.round(2)
)


# ============================================================
# 7. CHART 1 — REVIEW SCORE BY DELIVERY STATUS
# ============================================================

chart_data = delivered_orders.dropna(
    subset=["review_score"]
).copy()


average_reviews = (
    chart_data
    .groupby("delivery_status")["review_score"]
    .mean()
    .reindex(["On Time", "Late"])
)


plt.figure(figsize=(8, 5))

plt.bar(
    average_reviews.index,
    average_reviews.values
)

plt.title(
    "Average Customer Review Score by Delivery Status"
)

plt.xlabel("Delivery Status")

plt.ylabel("Average Review Score")

plt.ylim(0, 5)

plt.tight_layout()

plt.savefig(
    OUTPUT_PATH
    / "01_review_score_by_delivery_status.png",
    dpi=300
)

plt.close()


# ============================================================
# 8. CHART 2 — REVIEW SCORE BY LATE DELIVERY GROUP
# ============================================================

delay_chart_data = (
    delay_review_summary
    .dropna(
        subset=["average_review_score"]
    )
)


plt.figure(figsize=(9, 5))

plt.bar(
    delay_chart_data["delay_group"].astype(str),
    delay_chart_data["average_review_score"]
)

plt.title(
    "Average Review Score by Late Delivery Duration"
)

plt.xlabel("Days Late")

plt.ylabel("Average Review Score")

plt.ylim(0, 5)

plt.xticks(rotation=15)

plt.tight_layout()

plt.savefig(
    OUTPUT_PATH
    / "02_review_score_by_late_delivery_duration.png",
    dpi=300
)

plt.close()


# ============================================================
# 9. FINAL SUMMARY
# ============================================================

on_time_score = average_reviews.get("On Time")
late_score = average_reviews.get("Late")

print("\n3. KEY PYTHON FINDING")
print("-" * 65)

print(
    f"Average review score — On Time: {on_time_score:.2f}"
)

print(
    f"Average review score — Late: {late_score:.2f}"
)

print(
    "\nPython delivery and customer experience analysis completed."
)

print(
    f"Charts saved to: {OUTPUT_PATH}"
)