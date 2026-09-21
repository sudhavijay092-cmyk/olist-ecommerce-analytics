# Business Questions and SQL Analysis Scope

## Project

**Project:** SwiftCart Margin Under Pressure

**Dataset:** Brazilian E-Commerce Public Dataset by Olist

**Project Focus:** Delivery Performance, Freight Cost & Customer Experience Analysis

---

# 1. Business Problem

The Olist marketplace involves customers, sellers, products, freight costs, payments, deliveries, and customer reviews.

The business problem for this project is to understand:

> Where are delivery delays, freight costs, and poor customer experiences creating potential business pressure, and which operational areas should be prioritized for improvement?

The analysis will focus on identifying patterns rather than simply reporting totals.

---

# 2. Main Analysis Areas

The SQL analysis will focus on three areas:

1. Delivery Performance
2. Freight Cost
3. Customer Experience

---

# 3. Delivery Performance Questions

## Q1. How many orders were delivered successfully?

Measure:

- Total orders
- Delivered orders
- Canceled orders
- Unavailable orders
- Other order statuses

Business purpose:

Understand the overall order completion situation.

---

## Q2. How long does delivery take?

Measure:

- Average delivery time
- Median delivery time
- Fastest and slowest deliveries

Business purpose:

Understand typical customer waiting time.

---

## Q3. How many delivered orders were late?

Compare:

`order_delivered_customer_date`

with:

`order_estimated_delivery_date`

Measure:

- On-time deliveries
- Late deliveries
- Late delivery rate
- Average days late

Business purpose:

Identify delivery reliability problems.

---

## Q4. Which customer states have the worst delivery performance?

Measure by customer state:

- Number of delivered orders
- Average delivery time
- Late delivery rate
- Average delay

Business purpose:

Identify geographic areas with delivery problems.

---

## Q5. Which sellers are associated with the worst delivery performance?

Measure seller-related delivery performance using order-item information.

Business purpose:

Identify whether certain sellers are associated with slower delivery outcomes.

Important:

Seller analysis must respect order-level delivery grain.

Multiple order items must not multiply delivery records.

---

# 4. Freight Cost Questions

## Q6. What is the overall freight cost burden?

Measure:

- Total freight value
- Total item value
- Average freight per order
- Freight as a percentage of item value

Business purpose:

Understand how significant freight costs are relative to product sales.

---

## Q7. Which product categories have the highest freight burden?

Measure by product category:

- Total freight
- Average freight
- Item value
- Freight-to-item-value ratio

Business purpose:

Identify categories where logistics costs are disproportionately high.

---

## Q8. Which customer states have the highest freight burden?

Measure by customer state:

- Total freight
- Average freight
- Freight per order
- Freight-to-item-value ratio

Business purpose:

Identify geographic areas where freight costs are relatively high.

---

## Q9. Does freight burden vary by order value?

Measure freight relative to item value across different order-value levels.

Business purpose:

Determine whether low-value orders carry disproportionately high freight costs.

---

# 5. Customer Experience Questions

## Q10. What is the overall customer review score?

Measure:

- Average review score
- Review score distribution
- Percentage of low ratings
- Percentage of high ratings

Business purpose:

Understand overall customer satisfaction.

---

## Q11. Does late delivery affect customer review scores?

Compare:

- On-time delivered orders
- Late delivered orders

Measure:

- Average review score
- Low-rating rate
- Review score distribution

Business purpose:

Measure the relationship between delivery reliability and customer satisfaction.

---

## Q12. Does longer delivery time affect customer satisfaction?

Compare review scores across delivery-time groups.

Business purpose:

Identify whether customers who wait longer are less satisfied.

---

## Q13. Does higher freight burden affect customer satisfaction?

Compare freight burden with review scores.

Business purpose:

Determine whether relatively expensive freight is associated with lower customer satisfaction.

Important:

Order items must be aggregated to order level before combining freight information with reviews.

---

# 6. Priority Business Questions

The highest-priority questions for the project are:

1. What percentage of delivered orders are late?
2. Which customer states have the highest late delivery rates?
3. Which product categories have the highest freight burden?
4. Which customer states have the highest freight burden?
5. How does late delivery affect customer review scores?
6. How does freight burden affect customer review scores?

These questions directly connect:

Delivery Performance

↓

Freight Cost

↓

Customer Experience

---

# 7. SQL Analysis Scope

The SQL analysis will use the following main tables:

- orders
- customers
- order_items
- products
- sellers
- payments
- reviews

The main overall analysis grain will remain:

**Order level**

Detailed tables will remain at their native grain unless aggregation is required.

---

# 8. Safe SQL Modeling Rules

## Order-Level Analysis

Use:

`orders`

as the central table.

---

## Freight Analysis

Aggregate:

`order_items`

to order level when freight must be combined with:

- reviews
- delivery performance
- other order-level measures

---

## Payment Analysis

Aggregate:

`payments`

to order level before combining payment totals with other order-level measures.

---

## Review Analysis

Use reviews carefully because multiple review records can exist for an order.

Aggregate reviews to order level when combining them with order-level metrics.

---

# 9. Joins to Avoid

Do not directly join the following detailed tables together:

- order_items
- payments
- reviews

using `order_id` without aggregation.

This can multiply rows and produce incorrect results.

Example:

One order:

- 3 order items
- 2 payment records
- 2 review records

A raw join could create:

3 × 2 × 2 = 12 rows

This would incorrectly multiply:

- Freight
- Item value
- Payment value
- Review counts

---

# 10. Expected Final Business Outcome

The analysis should produce actionable findings about:

- Where delivery performance is weakest
- Where freight burden is highest
- Whether delivery delays are associated with poor customer satisfaction
- Whether freight burden is associated with poor customer satisfaction

The final recommendations should be based on the analysis results, not assumptions.