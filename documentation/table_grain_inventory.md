# Table Grain Inventory

## 1. Orders

**Grain:**  
One row represents one order.

**Candidate Primary / Unique Key:**  
order_id

**Key Result:**  
Unique

**Foreign Key(s):**  
customer_id

**Table Type:**  
Fact

**Business Purpose:**  
Stores the main order lifecycle information, including order status, purchase timestamp, approval timestamp, delivery timestamps, and estimated delivery date.


## 2. Customers

**Grain:**  
One row represents one customer record associated with an order.

**Candidate Primary / Unique Key:**  
customer_id

**Key Result:**  
Unique

**Foreign Key(s):**  
No foreign key identified within the six-table inventory.

**Table Type:**  
Dimension

**Business Purpose:**  
Stores customer location attributes and the customer_unique_id used to identify repeat customers across different orders.


## 3. Order Items

**Grain:**  
One row represents one item within one order.

**Candidate Primary / Unique Key:**  
order_id + order_item_id

**Key Result:**  
Unique Composite Key

**Foreign Key(s):**  
order_id, product_id, seller_id

**Table Type:**  
Fact

**Business Purpose:**  
Stores item-level transaction details, including product, seller, item price, freight value, and shipping limit date.


## 4. Products

**Grain:**  
One row represents one product.

**Candidate Primary / Unique Key:**  
product_id

**Key Result:**  
Unique

**Foreign Key(s):**  
No foreign key identified within the six-table inventory.

**Table Type:**  
Dimension

**Business Purpose:**  
Stores product attributes, including category, name length, description length, photos, weight, and physical dimensions.


## 5. Sellers

**Grain:**  
One row represents one seller.

**Candidate Primary / Unique Key:**  
seller_id

**Key Result:**  
Unique

**Foreign Key(s):**  
No foreign key identified within the six-table inventory.

**Table Type:**  
Dimension

**Business Purpose:**  
Stores seller location information, including ZIP code prefix, city, and state.


## 6. Payments

**Grain:**  
One row represents one payment record within one order.

**Candidate Primary / Unique Key:**  
order_id + payment_sequential

**Key Result:**  
Unique Composite Key

**Foreign Key(s):**  
order_id

**Table Type:**  
Fact

**Business Purpose:**  
Stores payment transaction information, including payment type, installment count, and payment value.