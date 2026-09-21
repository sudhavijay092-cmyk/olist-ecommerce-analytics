# Olist Brazilian E-Commerce: Delivery Performance, Freight Value & Customer Experience Analysis

## Project Overview

This project analyzes the Brazilian E-Commerce Public Dataset by Olist to understand delivery performance, freight value, and customer experience.

The analysis uses Python, SQL Server, Excel, and Power BI to identify patterns in order performance, delivery delays, freight burden, customer reviews, and state-level business performance.

The project is designed as an end-to-end data analytics case study, beginning with data profiling and preparation and ending with an interactive Power BI dashboard.

## Business Context

E-commerce businesses need to balance order volume, delivery performance, freight value, and customer satisfaction.

This project investigates the following business questions:

- How are order and payment values changing over time?
- What percentage of orders were delivered late?
- Which states have higher late-delivery rates?
- How does delivery performance relate to customer review scores?
- Which states have higher freight burden?
- Which delivery-delay categories have lower average review scores?
- Which orders meet the defined criteria for delivery or customer-experience risk?

## Dataset

The project uses the Brazilian E-Commerce Public Dataset by Olist.

The dataset contains anonymized e-commerce information related to:

- Orders
- Customers
- Order items
- Products
- Sellers
- Payments
- Reviews
- Geolocation
- Product-category translations

The dataset represents historical Brazilian e-commerce activity from approximately 2016 to 2018.

## Important Scope Limitation

This project does not calculate actual company profit, contribution margin, or logistics cost.

Freight burden is calculated as freight value divided by product value. It should not be interpreted as profit margin or actual logistics profitability.

The findings describe patterns and associations in the available dataset and do not establish causal relationships.

## Tools and Workflow

### 1. Python

- Profiled the dataset and examined data quality.
- Performed data cleaning and transformation.
- Analyzed delivery delays and customer review patterns.
- Created supporting visualizations.

### 2. SQL Server

- Prepared order-level analysis data.
- Combined related tables using appropriate aggregation.
- Analyzed delivery performance, freight value, customer reviews, and state-level trends.
- Used joins, aggregations, CTEs, and window functions where applicable.

### 3. Excel

- Created business-oriented KPI summaries.
- Reviewed freight, delivery, customer, state, and category-level information.
- Performed management-style exploratory analysis and validation.

### 4. Power BI

- Built an interactive three-page dashboard:
  - Executive Overview
  - Delivery & Customer Experience
  - Freight & Business Pressure
- Created DAX measures for business KPIs.
- Added time-based analysis using a dedicated date table.

## Project Workflow

1. Data understanding and table-grain identification
2. Data cleaning and transformation
3. Python-based data profiling and analysis
4. SQL Server data preparation and business analysis
5. Excel-based business summaries and validation
6. Power BI data modeling and DAX development
7. Interactive dashboard development
8. Business interpretation and documentation

## Project Structure

```text
swiftcart-margin-under-pressure/
│
├── Data/
│   ├── Raw dataset files
│   └── Prepared analysis tables
│
├── Python/
│   └── Python analysis scripts
│
├── sql/
│   └── SQL Server scripts and queries
│
├── excel/
│   └── Excel analysis workbooks
│
├── Powerbi/
│   └── Power BI dashboard files
│
├── documentation/
│   └── Project documentation and analysis notes
│
├── output/
│   └── Python-generated charts and outputs
│
├── screenshots/
│   └── Dashboard screenshots
│
├── scripts/
│   └── Supporting project scripts
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Key Findings

The analysis identified the following patterns in the Olist dataset:

- Delivery performance varied across customer states.
- Late deliveries were associated with lower average review scores.
- Freight burden varied across product categories and states.
- Some states recorded higher freight burden relative to product value.
- Longer delivery delays were associated with lower customer review scores.
- A defined set of orders met the project's delivery or customer-experience risk criteria.

> **Note:** Exact numerical findings and supporting charts are documented in the project analysis files.

## Power BI Dashboard

The project includes a three-page Power BI dashboard.

### Page 1 — Olist E-Commerce Executive Overview

- Total payment value
- Total orders
- Average order value
- Unique customers
- Average review score
- Late delivery rate
- Payment value trend
- State-level order volume
- Delivery status distribution

### Page 2 — Delivery & Customer Experience

- Late delivery rate by state
- Bottom 6 states by average review score
- Late delivery rate over time
- Average review score by delivery-delay category

### Page 3 — Freight & Business Pressure

- Total freight value
- Freight burden percentage
- High freight-burden orders
- At-risk orders
- States with higher freight burden
- Order volume versus freight burden
- Freight value trend

> **Note:** Dashboard screenshots are available in the `screenshots/` folder.
## Dashboard Preview

### Page 1 — Executive Overview

![Executive Overview](screenshots/1%20Executive%20Overview.PNG)

### Page 2 — Delivery & Customer Experience

![Delivery and Customer Experience](screenshots/2%20Delivery%20%26%20Customer%20Experience.PNG)

### Page 3 — Freight & Business Pressure

![Freight and Business Pressure](screenshots/3%20Freight%20%26%20Business%20Pressure.PNG)

## Project Limitations

- The dataset represents historical Brazilian e-commerce activity from approximately 2016 to 2018.
- The dataset does not provide actual company profit or contribution-margin information.
- Freight value is used as a freight-burden indicator, not as confirmed logistics cost.
- The analysis does not establish causal relationships between delivery delays and customer reviews.
- Some orders may have missing delivery, review, or payment information.
- The at-risk order indicator is based on business rules defined for this project.
- State and category comparisons should be interpreted within the scope of the available dataset.

## Future Improvements

- Incorporate more recent e-commerce data.
- Add verified logistics-cost information.
- Include reliable refund and cancellation data.
- Develop a more detailed customer-retention analysis.
- Add statistical testing to investigate relationships between delivery performance and customer satisfaction.

## Disclaimer

This project is an independent portfolio analysis based on publicly available data from Olist. It does not represent Olist's official business analysis, internal operations, or financial performance.