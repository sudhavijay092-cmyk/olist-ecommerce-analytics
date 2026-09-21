# Data Model Blueprint

## Project

**Project Name:** SwiftCart Margin Under Pressure

**Dataset:** Brazilian E-Commerce Public Dataset by Olist

**Project Focus:** Delivery Performance, Freight Cost & Customer Experience Analysis

---

# 1. Data Model Design Principle

The dataset contains tables at different levels of detail.

The most important rule for this project is:

> Do not directly join multiple one-to-many fact tables together without aggregation.

For example:

- One order can have multiple order items.
- One order can have multiple payment records.
- One order can have multiple review records.

Directly joining all three detailed tables can multiply rows and produce incorrect totals.

Example:

Order A
├── 3 Order Items
├── 2 Payments
└── 2 Reviews

A direct join could produce:

3 × 2 × 2 = 12 rows

Even though there is only one actual order.

Therefore, table grain must always be respected.

---

# 2. Recommended Logical Data Model

## Central Business Entity

The central entity of the model is:

**Orders**

Each row in Orders represents:

**One order**

The primary identifier is:

`order_id`

Orders provides the main business lifecycle information for an order, including:

- Order status
- Purchase date
- Approval date
- Carrier handoff date
- Customer delivery date
- Estimated delivery date

---

# 3. Table Classification

## 3.1 Fact Tables

### Fact Orders

**Table:** Orders

**Grain:** One row represents one order.

**Key:** `order_id`

**Business Role:** Central order lifecycle fact table.

---

### Fact Order Items

**Table:** Order Items

**Grain:** One row represents one item within one order.

**Composite Key:**

`order_id + order_item_id`

**Business Role:**

Stores item-level commercial and logistics information:

- Product
- Seller
- Item price
- Freight value
- Shipping limit date

---

### Fact Payments

**Table:** Payments

**Grain:** One row represents one payment record within one order.

**Composite Key:**

`order_id + payment_sequential`

**Business Role:**

Stores payment information:

- Payment type
- Installment count
- Payment value

---

### Fact Reviews

**Table:** Reviews

**Grain:** One row represents one review record associated with an order.

**Business Role:**

Stores customer satisfaction information:

- Review score
- Review comments
- Review creation date
- Review answer timestamp

**Important modeling note:**

`review_id` is not unique at the order level because the same review ID can be associated with multiple orders.

Therefore, Reviews must not be treated as a simple dimension table.

---

# 4. Dimension Tables

## Dim Customers

**Table:** Customers

**Grain:** One row represents one customer record associated with an order.

**Key:** `customer_id`

**Important Attribute:**

`customer_unique_id`

This identifies the same real-world customer across multiple orders.

**Business Attributes:**

- Customer city
- Customer state
- Customer ZIP code prefix

---

## Dim Products

**Table:** Products

**Grain:** One row represents one product.

**Key:** `product_id`

**Business Attributes:**

- Product category
- Product weight
- Product dimensions
- Product photo quantity
- Product description length

---

## Dim Sellers

**Table:** Sellers

**Grain:** One row represents one seller.

**Key:** `seller_id`

**Business Attributes:**

- Seller city
- Seller state
- Seller ZIP code prefix

---

# 5. Relationship Blueprint

## Relationship 1: Customers → Orders

Customers

1

|

|

1

Orders

### Cardinality

**ONE-TO-ONE**

### Relationship Key

`Customers.customer_id → Orders.customer_id`

### Important Business Interpretation

The dataset's `customer_id` is unique in both tables, so technically this relationship is one-to-one.

However, `customer_unique_id` is repeated across customer records and represents repeat customers across different orders.

Therefore, `customer_id` should be treated as the order-associated customer record identifier, while `customer_unique_id` should be used for repeat-customer analysis.

---

## Relationship 2: Orders → Order Items

Orders

1

|

|

*

Order Items

### Cardinality

**ONE-TO-MANY**

### Relationship Key

`Orders.order_id → Order_Items.order_id`

### Meaning

One order can contain multiple items.

Example:

Order A

├── Item 1

├── Item 2

└── Item 3

---

## Relationship 3: Products → Order Items

Products

1

|

|

*

Order Items

### Cardinality

From the Order Items perspective:

**MANY-TO-ONE**

From the Products perspective:

**ONE-TO-MANY**

### Relationship Key

`Products.product_id → Order_Items.product_id`

### Meaning

One product can appear in many order-item records.

---

## Relationship 4: Sellers → Order Items

Sellers

1

|

|

*

Order Items

### Cardinality

From the Order Items perspective:

**MANY-TO-ONE**

From the Sellers perspective:

**ONE-TO-MANY**

### Relationship Key

`Sellers.seller_id → Order_Items.seller_id`

### Meaning

One seller can sell many order items.

---

## Relationship 5: Orders → Payments

Orders

1

|

|

*

Payments

### Cardinality

**ONE-TO-MANY**

### Relationship Key

`Orders.order_id → Payments.order_id`

### Meaning

One order can contain multiple payment records.

---

## Relationship 6: Orders → Reviews

Orders

1

|

|

*

Reviews

### Cardinality

**ONE-TO-MANY**

### Relationship Key

`Orders.order_id → Reviews.order_id`

### Meaning

The dataset can contain multiple review records associated with the same order.

---

# 6. Logical Model Structure

The logical structure is:

Customers ─── Orders ───< Order Items >─── Products

                 |

                 ├────< Payments

                 |

                 └────< Reviews


Order Items >──── Sellers

---

# 7. Safe Analysis Grains

## Order-Level Analysis

Use when analyzing:

- Delivery performance
- Order status
- Delivery delays
- Customer experience
- Order-level payment totals
- Order-level review metrics

Primary table:

**Orders**

---

## Order-Item-Level Analysis

Use when analyzing:

- Product performance
- Seller performance
- Item prices
- Freight cost
- Product categories

Primary table:

**Order Items**

---

## Payment-Level Analysis

Use when analyzing:

- Payment types
- Installments
- Payment behavior

Primary table:

**Payments**

---

## Review-Level Analysis

Use when analyzing:

- Review scores
- Customer satisfaction
- Review timing

Primary table:

**Reviews**

---

# 8. Main Modeling Risk

The biggest data-model risk is row multiplication.

The following tables should **not** be directly combined at their raw detail level:

- Order Items
- Payments
- Reviews

All three can contain multiple rows for the same `order_id`.

Unsafe example:

Orders

↓

Order Items

↓

Payments

↓

Reviews

This can duplicate:

- Revenue values
- Freight values
- Payment values
- Item counts
- Review counts

---

# 9. Safe Modeling Rule

Before combining detailed fact tables at the order level:

`Order Items → Aggregate to Order Level`

`Payments → Aggregate to Order Level`

`Reviews → Aggregate to Order Level`

Then combine the resulting order-level summaries with:

**Orders**

This preserves the correct grain.

---

# 10. Recommended Main Analysis Grain

For the overall project:

**PRIMARY ANALYSIS GRAIN: ORDER LEVEL**

Reason:

The project focus is:

- Delivery Performance
- Freight Cost
- Customer Experience

Orders provides the safest central business entity for connecting these topics.

Order-item, payment, and review information should remain at their native grains unless they are aggregated appropriately for order-level analysis.

---

# 11. Data Model Decision

## Central Fact / Business Entity

**Orders**

## Supporting Fact Tables

- Order Items
- Payments
- Reviews

## Dimension Tables

- Customers
- Products
- Sellers

## Critical Modeling Rule

> Never combine raw Order Items, Payments, and Reviews through order_id in one flat join without aggregation.

---

# 12. Blueprint Status

**Data Model Blueprint:** COMPLETED

**Logical Modeling Design:** COMPLETED

**Physical SQL Model:** NOT STARTED

**Power BI Model:** NOT STARTED