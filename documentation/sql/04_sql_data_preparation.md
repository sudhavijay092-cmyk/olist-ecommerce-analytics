# SQL Data Preparation

## Project

**Project:** SwiftCart Margin Under Pressure

**Dataset:** Brazilian E-Commerce Public Dataset by Olist

**Database:** SwiftCart_Margin_Under_Pressure

---

# 1. Objective

The objective of this phase was to prepare the cleaned Olist data for SQL analysis.

The process included:

- Creating the SQL Server project database
- Creating the required table structure
- Importing cleaned CSV files
- Verifying imported row counts
- Verifying table relationships
- Creating a SQL data validation summary

No business analysis was performed during this phase.

---

# 2. Database Created

Database name:

`SwiftCart_Margin_Under_Pressure`

The database contains seven main tables:

1. customers
2. orders
3. products
4. sellers
5. order_items
6. payments
7. reviews

---

# 3. Cleaned Data Imported

The following cleaned CSV files were imported into SQL Server:

| Cleaned File | SQL Table |
|---|---|
| olist_customers_clean.csv | dbo.customers |
| olist_orders_clean.csv | dbo.orders |
| olist_products_clean.csv | dbo.products |
| olist_sellers_clean.csv | dbo.sellers |
| olist_order_items_clean.csv | dbo.order_items |
| olist_order_payments_clean.csv | dbo.payments |
| olist_order_reviews_clean.csv | dbo.reviews |

Cleaned CSV files were imported using:

`BULK INSERT`

The raw Olist CSV files were not modified.

---

# 4. Table Structure

The SQL tables preserve the grain of the original cleaned datasets.

## Customers

Grain:

One row represents one customer record associated with an order.

Key:

`customer_id`

---

## Orders

Grain:

One row represents one order.

Key:

`order_id`

---

## Products

Grain:

One row represents one product.

Key:

`product_id`

---

## Sellers

Grain:

One row represents one seller.

Key:

`seller_id`

---

## Order Items

Grain:

One row represents one item within one order.

Composite key:

`order_id + order_item_id`

---

## Payments

Grain:

One row represents one payment record within one order.

Composite key:

`order_id + payment_sequential`

---

## Reviews

Grain:

One row represents one review record associated with an order.

Relationship key:

`order_id`

---

# 5. Imported Data Verification

After importing the cleaned datasets, SQL row counts were checked for all seven tables.

The expected approximate dataset sizes were:

| Table | Approximate Rows |
|---|---:|
| customers | 99,441 |
| orders | 99,441 |
| products | 32,951 |
| sellers | 3,095 |
| order_items | 112,650 |
| payments | 103,886 |
| reviews | 99,224 |

The imported tables were verified to ensure that they contained data before relationship testing.

---

# 6. Relationship Verification

The following relationships were checked after importing the cleaned data.

## Orders → Customers

Relationship key:

`orders.customer_id → customers.customer_id`

Expected unmatched rows:

`0`

---

## Order Items → Orders

Relationship key:

`order_items.order_id → orders.order_id`

Expected unmatched rows:

`0`

---

## Order Items → Products

Relationship key:

`order_items.product_id → products.product_id`

Expected unmatched rows:

`0`

---

## Order Items → Sellers

Relationship key:

`order_items.seller_id → sellers.seller_id`

Expected unmatched rows:

`0`

---

## Payments → Orders

Relationship key:

`payments.order_id → orders.order_id`

Expected unmatched rows:

`0`

---

## Reviews → Orders

Relationship key:

`reviews.order_id → orders.order_id`

Expected unmatched rows:

`0`

The SQL relationship verification was completed successfully.

---

# 7. SQL Data Validation Summary

A combined SQL validation summary was created to check:

- Table row counts
- Relationship integrity
- PASS or FAIL status

The validation summary included:

- 7 table row-count checks
- 6 relationship checks

Total validation checks:

`13`

The SQL data preparation validation was completed successfully.

---

# 8. Important Modeling Decisions

The following decisions must be respected during SQL analysis.

## Main Overall Analysis Grain

Order level.

The central business entity is:

`orders`

---

## Detailed Fact Tables

The following tables can contain multiple records for the same order:

- order_items
- payments
- reviews

These tables must not be directly joined together at raw detail level.

---

## Row Multiplication Risk

A direct join between:

`order_items`

`payments`

and

`reviews`

can multiply rows for the same order.

This can produce incorrect totals for:

- Item price
- Freight value
- Payment value
- Item counts
- Review counts

---

## Safe Modeling Rule

Before combining detailed tables at order level:

- Aggregate order_items to order level when needed.
- Aggregate payments to order level when needed.
- Aggregate reviews to order level when needed.

Then join the aggregated result to:

`orders`

---

# 9. Phase Result

The cleaned Olist datasets were successfully prepared and validated in SQL Server.

Completed:

- Database creation
- SQL table structure
- Cleaned data import
- Row-count verification
- Relationship verification
- Combined validation summary
- SQL data preparation documentation

The SQL database is ready for the next phase: business-focused data analysis.

---

# 10. Next Step

The next phase will define the business questions and analysis scope for:

- Delivery performance
- Freight cost
- Customer experience