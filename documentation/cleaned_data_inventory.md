# Cleaned Data Inventory

## Project

**Project Name:** SwiftCart Margin Under Pressure

**Dataset:** Brazilian E-Commerce Public Dataset by Olist

**Project Focus:** Delivery Performance, Freight Cost & Customer Experience Analysis

---

# Purpose

This document records the cleaned datasets prepared for the project.

The purpose of this inventory is to document:

- Which cleaned files are available.
- Where the cleaned files are stored.
- What one row represents in each table.
- The primary or unique key of each table.
- Important foreign keys.
- The validation status of each cleaned table.

Raw Olist CSV files were not modified.

---

# Cleaned Data Folder

**Folder Location:**

`D:\swiftcart-margin-under-pressure\Data\cleaned`

---

# 1. Orders

## Table: Orders

**Cleaned File Name:**  
`olist_orders_clean.csv`

**Folder Location:**  
`D:\swiftcart-margin-under-pressure\Data\cleaned`

**Table Grain:**  
One row represents one order.

**Primary / Unique Key:**  
`order_id`

**Foreign Key(s):**  
`customer_id`

**Validation Status:**  
PASSED

**Notes:**  
Orders is the central business entity for the overall project and is the primary table for order-level analysis.

---

# 2. Customers

## Table: Customers

**Cleaned File Name:**  
`olist_customers_clean.csv`

**Folder Location:**  
`D:\swiftcart-margin-under-pressure\Data\cleaned`

**Table Grain:**  
One row represents one customer record associated with an order.

**Primary / Unique Key:**  
`customer_id`

**Foreign Key(s):**  
None within the cleaned core table model.

**Validation Status:**  
PASSED

**Notes:**  
`customer_unique_id` identifies the same real-world customer across multiple orders and can be used for repeat-customer analysis.

---

# 3. Order Items

## Table: Order Items

**Cleaned File Name:**  
`olist_order_items_clean.csv`

**Folder Location:**  
`D:\swiftcart-margin-under-pressure\Data\cleaned`

**Table Grain:**  
One row represents one item within one order.

**Primary / Unique Key:**  
Composite key: `order_id + order_item_id`

**Foreign Key(s):**  
`order_id`  
`product_id`  
`seller_id`

**Validation Status:**  
PASSED

**Notes:**  
Order Items is an item-level fact table. It should not be directly combined with raw Payments and Reviews without aggregation because this can multiply rows.

---

# 4. Products

## Table: Products

**Cleaned File Name:**  
`olist_products_clean.csv`

**Folder Location:**  
`D:\swiftcart-margin-under-pressure\Data\cleaned`

**Table Grain:**  
One row represents one product.

**Primary / Unique Key:**  
`product_id`

**Foreign Key(s):**  
None within the cleaned core table model.

**Validation Status:**  
PASSED

**Notes:**  
Products is a dimension table used for product and product-category analysis.

---

# 5. Sellers

## Table: Sellers

**Cleaned File Name:**  
`olist_sellers_clean.csv`

**Folder Location:**  
`D:\swiftcart-margin-under-pressure\Data\cleaned`

**Table Grain:**  
One row represents one seller.

**Primary / Unique Key:**  
`seller_id`

**Foreign Key(s):**  
None within the cleaned core table model.

**Validation Status:**  
PASSED

**Notes:**  
Sellers is a dimension table used for seller and seller-location analysis.

---

# 6. Payments

## Table: Payments

**Cleaned File Name:**  
`olist_order_payments_clean.csv`

**Folder Location:**  
`D:\swiftcart-margin-under-pressure\Data\cleaned`

**Table Grain:**  
One row represents one payment record within one order.

**Primary / Unique Key:**  
Composite key: `order_id + payment_sequential`

**Foreign Key(s):**  
`order_id`

**Validation Status:**  
PASSED

**Notes:**  
Payments is a payment-level fact table. One order can have multiple payment records.

---

# 7. Reviews

## Table: Reviews

**Cleaned File Name:**  
`olist_order_reviews_clean.csv`

**Folder Location:**  
`D:\swiftcart-margin-under-pressure\Data\cleaned`

**Table Grain:**  
One row represents one review record associated with an order.

**Primary / Unique Key:**  
No simple single-column unique key confirmed for order-level modeling.

**Foreign Key(s):**  
`order_id`

**Validation Status:**  
PASSED

**Notes:**  
One order can have multiple review records. `review_id` should not be assumed to be unique because duplicate review IDs were identified during the raw-data validation.

---

# Cleaned Data Modeling Rules

1. Raw Olist CSV files were not modified.

2. Table grain must be respected during future SQL joins and Power BI relationships.

3. Orders is the central business entity for overall order-level analysis.

4. Order Items is an item-level fact table.

5. Payments is a payment-level fact table.

6. Reviews is a review-level fact table.

7. Order Items, Payments, and Reviews should not be directly joined together at their raw detail level.

8. Before combining multiple one-to-many fact tables for order-level analysis, aggregate them to the required order-level grain.

9. Products and Sellers can be connected to Order Items through their respective keys.

10. Customers can be connected to Orders through `customer_id`.

---

# Final Status

**Cleaned Data Inventory Status:** COMPLETED

**Data Preparation Status:** Cleaned datasets documented and ready for the next project phase after Task 3.8 completion.

**Raw Data Status:** Preserved and unchanged.

**Cleaned Data Folder:**  
`D:\swiftcart-margin-under-pressure\Data\cleaned`