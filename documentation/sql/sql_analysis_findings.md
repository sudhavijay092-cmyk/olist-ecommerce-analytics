# SQL Analysis Findings

## Project

**Project Name:** SwiftCart Margin Under Pressure

**Dataset:** Brazilian E-Commerce Public Dataset by Olist

**Analysis Tool:** Microsoft SQL Server

---

# 1. Analysis Objective

The SQL analysis focused on identifying business patterns related to:

- Delivery performance
- Freight cost and freight burden
- Customer experience
- Seller performance
- Product category performance
- Cross-area operational patterns

The analysis was designed to support the project's central business problem:

> Understanding where delivery performance and freight costs may create pressure on customer experience and business margins.

---

# 2. Delivery Performance Findings

## Key Results

- Total delivered orders: 96,478
- On-time delivery percentage: 91.89%
- Late delivery percentage: 8.11%
- Average days late for late orders: 8.87

## Key Finding

The majority of delivered orders (91.89%) were completed on time. However, the 8.11% late-delivery segment represents a meaningful operational issue because late orders experienced an average delay of 8.87 days.

---

# 3. Freight Cost Findings

## Overall Freight Results

- Total freight cost: 2,251,909.54
- Average freight cost per item: 19.99
- Freight percentage of total product value: 16.57%

## Key Finding

Freight represents 16.57% of total product value, indicating a substantial logistics cost relative to merchandise value. This creates potential pressure on transaction economics and should be closely monitored when evaluating margin performance.

---

# 4. Customer Experience Findings

## Overall Customer Satisfaction

- Average review score: 4.09
- Positive review percentage: 77.07%
- Negative review percentage: 14.69%

## Delivery and Customer Satisfaction

- Average review score for on-time orders: 4.29
- Average review score for late orders: 2.57

## Key Finding

Orders delivered late had a significantly lower average review score (2.57) than orders delivered on time (4.29). This shows a clear pattern between delivery delays and reduced customer satisfaction, although the analysis does not prove that late delivery alone caused the lower ratings.

---

# 5. Product Category Performance Findings

## Key Results

- Product category with highest sales value: `beleza_saude` (1,258,681.34)
- Product category with highest meaningful freight burden: `artigos_de_natal`
- Freight percentage for that category: 36.69%

## Key Finding

The `beleza_saude` category generates the highest total product sales value, while the `artigos_de_natal` category carries the highest freight burden relative to product value (36.69%) among categories meeting the minimum-volume threshold.

---

# 6. Seller Performance Findings

## Key Results

- Seller with highest order-item volume: `6560211a19b47992c3666cc44a7e94c0` (2,033 items)
- High-volume seller with highest freight burden: `b76dba6c951ab00dc4edf0a1aa88037e`
- Freight percentage for that seller: 89.60%

## Key Finding

Seller `6560211a19b47992c3666cc44a7e94c0` processes the highest item volume in the dataset, while seller `b76dba6c951ab00dc4edf0a1aa88037e` has a high freight burden of 89.60% relative to product value. This seller should be investigated further to understand the factors contributing to the high freight burden.

---

# 7. Cross-Area Business Findings

The cross-area analysis compared:

- Late delivery percentage
- Average days late
- Freight percentage of product value
- Average review score
- Low-rating percentage

## Key Findings

### Finding 1

State-level results show a pattern in which higher late delivery rates can coincide with lower customer satisfaction. For example, state AL has a 23.93% late delivery rate alongside an average review score of 3.75.

### Finding 2

State SP has the highest delivered order volume (40,495) while maintaining a relatively low late delivery rate (5.89%) and a freight burden of 13.81%. This combination indicates comparatively efficient delivery and freight performance within the dataset.

### Finding 3

State RR exhibits a high relative freight burden of 28.55% and severe delivery delays, averaging 36 days late when deliveries miss the estimated date. This combination identifies RR as a location requiring further logistics investigation.

---

# 8. Main Business Patterns Identified

Based on the SQL analysis, the main patterns identified were:

1. **Delivery Performance and Customer Satisfaction Show a Clear Pattern:** States with higher late delivery percentages often show lower average review scores and higher concentrations of negative reviews. Further statistical analysis is required to measure the strength of this relationship.

2. **High-Volume Regions Can Maintain Strong Operational Performance:** SP processes the highest delivered order volume while maintaining a relatively low late delivery rate and a lower freight burden than several other states.

3. **Multiple Operational Problems Can Appear Together:** Some states show a combination of high freight burden, delayed deliveries, and lower customer satisfaction. These locations should be prioritized for further operational investigation.

---

# 9. Analysis Limitations

The findings should be interpreted carefully.

- The analysis identifies patterns and associations.
- The analysis does not prove causation.
- High freight costs do not automatically mean low profitability because the dataset does not contain complete cost or profit information.
- Low review scores may be influenced by factors other than delivery performance.
- State-level results can be influenced by order volume and customer distribution.

---

# 10. SQL Analysis Status

**Delivery Performance Analysis:** COMPLETED

**Freight Cost Analysis:** COMPLETED

**Customer Experience Analysis:** COMPLETED

**Seller and Product Category Performance Analysis:** COMPLETED

**Cross-Area Business Findings:** COMPLETED

**SQL Analysis Documentation:** COMPLETED