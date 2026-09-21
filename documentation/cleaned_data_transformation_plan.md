# Cleaned Data Transformation Plan

## Project

**Project Name:** SwiftCart Margin Under Pressure

**Dataset:** Brazilian E-Commerce Public Dataset by Olist

**Project Focus:** Delivery Performance, Freight Cost & Customer Experience Analysis

---

# 1. Cleaning Strategy

The raw Olist CSV files will never be modified.

All transformations will be applied to copies of the raw data and saved separately as cleaned or processed datasets.

The cleaning process must follow these principles:

- Preserve the original raw files.
- Preserve the grain of every table.
- Do not remove valid multi-row business records.
- Handle missing values according to business meaning.
- Do not blindly delete anomalies.
- Create derived fields separately from original columns.
- Document every transformation.
- Avoid transformations that create incorrect joins or row multiplication.

---

# 2. Orders Transformation Plan

## Table Grain

One row represents one order.

## Key

`order_id`

## Planned Transformations

### Timestamp conversion

Convert the following columns from text to datetime format:

- `order_purchase_timestamp`
- `order_approved_at`
- `order_delivered_carrier_date`
- `order_delivered_customer_date`
- `order_estimated_delivery_date`

The original business meaning of each timestamp must be preserved.

---

### Missing approval timestamps

The dataset contains orders with missing approval timestamps.

Do not automatically fill missing approval timestamps.

Missing values should remain missing unless a business-valid replacement rule is later justified.

---

### Missing delivery timestamps

Missing delivery timestamps must be interpreted according to `order_status`.

Examples:

- Missing customer delivery date for a shipped order is expected.
- Missing delivery dates for delivered orders are data-quality issues.

Do not replace missing delivery dates with artificial dates.

---

### Timestamp anomalies

Some records contain:

- Carrier handoff before purchase timestamp.
- Customer delivery before carrier handoff.

These records should not be deleted automatically.

Later analysis may:

- flag anomalous records, or
- exclude them from specific delivery-duration calculations.

The original records must remain preserved.

---

### Delivery delay

Orders delivered after the estimated delivery date should not be treated as invalid records.

A derived delivery-delay field may later be created for analysis.

The original delivery and estimated dates must remain unchanged.

---

### Order status and delivery inconsistencies

Canceled orders can contain delivery dates.

These records should not automatically be removed because they may represent valid operational events or historical process inconsistencies.

The order status and timestamp values should remain preserved.

---

# 3. Customers Transformation Plan

## Table Grain

One row represents one customer record associated with an order.

## Key

`customer_id`

## Important Identifier

`customer_unique_id`

## Planned Transformations

### Customer identifiers

Do not remove repeated `customer_unique_id` values.

Repeated values represent customers who may have placed multiple orders.

`customer_id` remains the unique table-level identifier.

---

### Location attributes

Customer location fields will be preserved:

- ZIP code prefix
- City
- State

No missing values were identified during the initial inspection.

No artificial values should be created.

---

# 4. Order Items Transformation Plan

## Table Grain

One row represents one item within one order.

## Composite Key

`order_id + order_item_id`

## Planned Transformations

### Preserve multiple items per order

Repeated `order_id` values are expected.

They must not be treated as duplicates.

The composite key must remain unique.

---

### Shipping limit date

Convert:

`shipping_limit_date`

to datetime format.

---

### Price and freight values

Preserve:

- `price`
- `freight_value`

as numeric fields.

Do not aggregate these values during cleaning.

Aggregation must happen later depending on the analysis grain.

---

### Product and seller references

Preserve:

- `product_id`
- `seller_id`

These foreign keys are required for relationships with Products and Sellers.

No records should be removed solely because an order contains multiple items.

---

# 5. Products Transformation Plan

## Table Grain

One row represents one product.

## Key

`product_id`

## Planned Transformations

### Missing product category and attributes

Some product records have missing values for:

- `product_category_name`
- Product name length
- Product description length
- Product photos quantity

These missing values should not automatically be replaced with fabricated values.

A future cleaned version may use a clearly documented category label such as:

`Unknown`

for analysis purposes only.

The original missing values should remain identifiable.

---

### Missing physical measurements

A small number of products have missing:

- Weight
- Length
- Height
- Width

Do not automatically impute these values.

They should remain missing unless a later analysis requires a justified treatment.

---

### Category translation

Some product categories do not have a matching English translation.

Do not delete these products.

The missing translations should be documented and handled separately when category translation is required for reporting.

---

# 6. Sellers Transformation Plan

## Table Grain

One row represents one seller.

## Key

`seller_id`

## Planned Transformations

### Seller location

Preserve:

- ZIP code prefix
- City
- State

No missing values were identified during the initial inspection.

No artificial values should be created.

---

# 7. Payments Transformation Plan

## Table Grain

One row represents one payment record within one order.

## Composite Key

`order_id + payment_sequential`

## Planned Transformations

### Preserve multiple payment records

Repeated `order_id` values are valid.

An order can contain multiple payment records.

They must not be removed as duplicates.

---

### Payment values

Preserve:

`payment_value`

as a numeric field.

Do not aggregate payment values during table-level cleaning.

Payment aggregation must occur later when order-level analysis is required.

---

### Payment installments

Preserve:

`payment_installments`

as an integer.

Records with zero installments should not automatically be removed.

Their business meaning should be investigated before any exclusion rule is created.

---

# 8. Reviews Transformation Plan

## Table Grain

One row represents one review record associated with an order.

## Planned Transformations

### Duplicate review IDs

Duplicate `review_id` values should not automatically be removed.

Investigation showed that duplicated review IDs can be associated with multiple orders while review content remains consistent.

Therefore, `review_id` alone must not be treated as a unique table key.

---

### Missing review comments

Missing values in:

- `review_comment_title`
- `review_comment_message`

are expected because customers can submit scores without written comments.

Do not replace missing comments with fabricated text.

---

### Review score

Preserve:

`review_score`

as an integer rating.

No score should be changed or imputed.

---

### Review timestamps

Convert:

- `review_creation_date`
- `review_answer_timestamp`

to datetime format.

---

# 9. Geolocation Data Handling

The geolocation table contains coordinate anomalies and repeated ZIP code prefixes.

This table should not be cleaned or joined directly into the main analytical model until a separate geolocation strategy is defined.

Any future use of geolocation must account for:

- Multiple coordinates per ZIP code prefix.
- Customer ZIP codes without geolocation records.
- Seller ZIP codes without geolocation records.
- Suspicious coordinates outside expected geographic ranges.

---

# 10. Category Translation Handling

The category translation table should remain unchanged.

Products without English category translations should not be removed.

The two identified untranslated categories must remain documented:

- `pc_gamer`
- `portateis_cozinha_e_preparadores_de_alimentos`

A reporting-friendly category treatment may be created later without changing the raw category values.

---

# 11. Orders Without Item Records

Orders without item records should not automatically be removed.

Most belong to statuses such as:

- Unavailable
- Canceled

These orders may be important for operational analysis.

They should only be excluded from calculations where item-level information is explicitly required.

---

# 12. Financial Reconciliation Handling

Some orders show differences between:

- Item value + freight value
- Payment value

These differences should not automatically be corrected.

Possible causes include:

- Orders without item records.
- Canceled orders.
- Unavailable orders.
- Payment records with different business timing.

Financial reconciliation differences should be preserved and investigated during analysis.

---

# 13. Cleaned Data Rules

The following transformations are approved for future implementation:

1. Convert date/time columns to datetime format.
2. Preserve original table grain.
3. Preserve valid repeated foreign keys.
4. Preserve valid multi-row business records.
5. Preserve original missing values unless a documented business rule exists.
6. Preserve anomalies and optionally create analysis flags later.
7. Preserve original identifiers.
8. Preserve original financial values.
9. Create derived fields separately.
10. Save transformed datasets separately from raw data.

---

# 14. Transformations Explicitly Not Allowed

The following actions must not occur without a documented business reason:

- Editing raw CSV files.
- Removing rows only because an ID repeats.
- Removing multiple payments for an order.
- Removing multiple order items for an order.
- Automatically deleting duplicate review IDs.
- Filling missing delivery dates with artificial values.
- Inventing missing product measurements.
- Deleting timestamp anomalies without investigation.
- Aggregating fact tables during basic cleaning.
- Directly flattening Order Items, Payments, and Reviews into one table.

---

# 15. Transformation Plan Status

**Transformation Plan:** COMPLETED

**Python Cleaning Implementation:** NOT STARTED

**Raw Files Modified:** NO