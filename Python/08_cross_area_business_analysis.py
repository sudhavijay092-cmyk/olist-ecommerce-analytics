import pandas as pd
import matplotlib.pyplot as plt
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

OUTPUT_PATH = (
    PROJECT_PATH
    / "output"
    / "python"
)

OUTPUT_PATH.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# 2. LOAD ORDER-LEVEL ANALYSIS DATASET
# ============================================================

order_analysis = pd.read_csv(
    ANALYSIS_DATA_PATH,
    parse_dates=[
        "order_purchase_timestamp",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]
)


# ============================================================
# 3. CREATE DELIVERED ORDER ANALYSIS DATASET
# ============================================================

delivered_orders = order_analysis[
    order_analysis["delivery_status"].notna()
].copy()


# ============================================================
# 4. CREATE LOW-RATING INDICATOR
# ============================================================

# Review scores of 1 or 2 are treated as low ratings.
# Missing reviews remain missing and are excluded from the rate.

delivered_orders["low_rating"] = pd.NA

review_available = (
    delivered_orders["review_score"].notna()
)

delivered_orders.loc[
    review_available,
    "low_rating"
] = (
    delivered_orders.loc[
        review_available,
        "review_score"
    ] <= 2
)


# ============================================================
# 5. CREATE STATE-LEVEL BUSINESS SUMMARY
# ============================================================

state_summary = (
    delivered_orders
    .groupby(
        "customer_state",
        as_index=False
    )
    .agg(
        delivered_orders=(
            "order_id",
            "count"
        ),
        late_delivery_percentage=(
            "delivery_status",
            lambda x: (
                (x == "Late").mean()
            ) * 100
        ),
        average_review_score=(
            "review_score",
            "mean"
        ),
        total_product_value=(
            "total_product_value",
            "sum"
        ),
        total_freight_value=(
            "total_freight_value",
            "sum"
        )
    )
)


# ============================================================
# 6. CALCULATE AVERAGE DAYS LATE
# ============================================================

late_orders = delivered_orders[
    delivered_orders["delivery_status"] == "Late"
]

average_days_late = (
    late_orders
    .groupby(
        "customer_state"
    )["delivery_delay_days"]
    .mean()
    .reset_index(
        name="average_days_late"
    )
)


# ============================================================
# 7. CALCULATE LOW-RATING PERCENTAGE
# ============================================================

reviewed_orders = delivered_orders[
    delivered_orders["review_score"].notna()
].copy()


low_rating_summary = (
    reviewed_orders
    .groupby(
        "customer_state"
    )["low_rating"]
    .mean()
    .mul(100)
    .reset_index(
        name="low_rating_percentage"
    )
)


# ============================================================
# 8. MERGE STATE-LEVEL METRICS
# ============================================================

state_summary = (
    state_summary
    .merge(
        average_days_late,
        on="customer_state",
        how="left"
    )
    .merge(
        low_rating_summary,
        on="customer_state",
        how="left"
    )
)


# ============================================================
# 9. CALCULATE FREIGHT BURDEN
# ============================================================

state_summary["freight_percentage"] = (
    state_summary["total_freight_value"]
    / state_summary["total_product_value"]
) * 100


# ============================================================
# 10. ROUND ANALYSIS METRICS
# ============================================================

display_summary = (
    state_summary
    .sort_values(
        "delivered_orders",
        ascending=False
    )
    .copy()
)

display_summary[
    [
        "late_delivery_percentage",
        "average_days_late",
        "freight_percentage",
        "average_review_score",
        "low_rating_percentage"
    ]
] = display_summary[
    [
        "late_delivery_percentage",
        "average_days_late",
        "freight_percentage",
        "average_review_score",
        "low_rating_percentage"
    ]
].round(2)


# ============================================================
# 11. PRINT STATE-LEVEL RESULTS
# ============================================================

print("\nSWIFTCART — CROSS-AREA BUSINESS ANALYSIS")
print("=" * 75)

print("\n1. STATE-LEVEL BUSINESS PERFORMANCE")
print("-" * 75)

print(
    display_summary[
        [
            "customer_state",
            "delivered_orders",
            "late_delivery_percentage",
            "average_days_late",
            "freight_percentage",
            "average_review_score",
            "low_rating_percentage"
        ]
    ].to_string(
        index=False
    )
)


# ============================================================
# 12. IDENTIFY KEY STATE EXTREMES
# ============================================================

highest_late_state = state_summary.loc[
    state_summary[
        "late_delivery_percentage"
    ].idxmax()
]

highest_freight_state = state_summary.loc[
    state_summary[
        "freight_percentage"
    ].idxmax()
]

lowest_review_state = state_summary.loc[
    state_summary[
        "average_review_score"
    ].idxmin()
]

highest_volume_state = state_summary.loc[
    state_summary[
        "delivered_orders"
    ].idxmax()
]


# ============================================================
# 13. PRINT KEY FINDINGS
# ============================================================

print("\n2. KEY CROSS-AREA FINDINGS")
print("-" * 75)

print(
    f"Highest late delivery rate: "
    f"{highest_late_state['customer_state']} "
    f"({highest_late_state['late_delivery_percentage']:.2f}%)"
)

print(
    f"Highest freight burden: "
    f"{highest_freight_state['customer_state']} "
    f"({highest_freight_state['freight_percentage']:.2f}%)"
)

print(
    f"Lowest average review score: "
    f"{lowest_review_state['customer_state']} "
    f"({lowest_review_state['average_review_score']:.2f})"
)

print(
    f"Highest delivered order volume: "
    f"{highest_volume_state['customer_state']} "
    f"({highest_volume_state['delivered_orders']:,} orders)"
)


# ============================================================
# 14. CHART 1 — LATE DELIVERY RATE BY STATE
# ============================================================

late_chart = (
    state_summary
    .sort_values(
        "late_delivery_percentage",
        ascending=True
    )
)


plt.figure(
    figsize=(10, 8)
)

plt.barh(
    late_chart["customer_state"],
    late_chart["late_delivery_percentage"]
)

plt.title(
    "Late Delivery Percentage by Customer State"
)

plt.xlabel(
    "Late Delivery Percentage"
)

plt.ylabel(
    "Customer State"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_PATH
    / "08_late_delivery_percentage_by_state.png",
    dpi=300
)

plt.close()


# ============================================================
# 15. CHART 2 — FREIGHT BURDEN BY STATE
# ============================================================

freight_chart = (
    state_summary
    .sort_values(
        "freight_percentage",
        ascending=True
    )
)


plt.figure(
    figsize=(10, 8)
)

plt.barh(
    freight_chart["customer_state"],
    freight_chart["freight_percentage"]
)

plt.title(
    "Freight Burden by Customer State"
)

plt.xlabel(
    "Freight Percentage"
)

plt.ylabel(
    "Customer State"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_PATH
    / "09_freight_burden_by_state.png",
    dpi=300
)

plt.close()


# ============================================================
# 16. CHART 3 — DELIVERY PERFORMANCE VS CUSTOMER EXPERIENCE
# ============================================================

scatter_data = state_summary.dropna(
    subset=[
        "late_delivery_percentage",
        "average_review_score"
    ]
)


plt.figure(
    figsize=(9, 6)
)

plt.scatter(
    scatter_data[
        "late_delivery_percentage"
    ],
    scatter_data[
        "average_review_score"
    ],
    alpha=0.7
)


for _, row in scatter_data.iterrows():
    plt.annotate(
        row["customer_state"],
        (
            row["late_delivery_percentage"],
            row["average_review_score"]
        ),
        fontsize=8
    )


plt.title(
    "Late Delivery Rate vs Average Customer Review Score"
)

plt.xlabel(
    "Late Delivery Percentage"
)

plt.ylabel(
    "Average Review Score"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_PATH
    / "10_late_delivery_vs_review_score_by_state.png",
    dpi=300
)

plt.close()


# ============================================================
# 17. SAVE STATE SUMMARY
# ============================================================

STATE_SUMMARY_PATH = (
    PROJECT_PATH
    / "Data"
    / "cleaned"
    / "swiftcart_state_business_summary.csv"
)

state_summary.to_csv(
    STATE_SUMMARY_PATH,
    index=False
)


# ============================================================
# 18. FINAL STATUS
# ============================================================

print(
    "\nPython cross-area business analysis completed."
)

print(
    f"State summary saved to: "
    f"{STATE_SUMMARY_PATH}"
)

print(
    f"Charts saved to: "
    f"{OUTPUT_PATH}"
)