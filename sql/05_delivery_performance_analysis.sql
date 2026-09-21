SELECT
    order_status,
    COUNT(*) AS total_orders,
    CAST(
        100.0 * COUNT(*) / SUM(COUNT(*)) OVER ()
        AS DECIMAL(5,2)
    ) AS percentage_of_orders
FROM dbo.orders
GROUP BY order_status
ORDER BY total_orders DESC;
----
SELECT
    COUNT(*) AS delivered_orders,
    CAST(
        AVG(
            DATEDIFF(
                DAY,
                order_purchase_timestamp,
                order_delivered_customer_date
            ) * 1.0
        ) AS DECIMAL(10,2)
    ) AS average_delivery_days,
    MIN(
        DATEDIFF(
            DAY,
            order_purchase_timestamp,
            order_delivered_customer_date
        )
    ) AS fastest_delivery_days,
    MAX(
        DATEDIFF(
            DAY,
            order_purchase_timestamp,
            order_delivered_customer_date
        )
    ) AS slowest_delivery_days
FROM dbo.orders
WHERE order_status = 'delivered'
    AND order_purchase_timestamp IS NOT NULL
    AND order_delivered_customer_date IS NOT NULL;
---
SELECT
    CASE
        WHEN order_delivered_customer_date <= order_estimated_delivery_date
            THEN 'On Time'
        ELSE 'Late'
    END AS delivery_status,
    
    COUNT(*) AS total_orders,
    
    CAST(
        100.0 * COUNT(*) / SUM(COUNT(*)) OVER ()
        AS DECIMAL(5,2)
    ) AS percentage_of_delivered_orders,

    CAST(
        AVG(
            CASE
                WHEN order_delivered_customer_date > order_estimated_delivery_date
                    THEN DATEDIFF(
                        DAY,
                        order_estimated_delivery_date,
                        order_delivered_customer_date
                    ) * 1.0
            END
        ) AS DECIMAL(10,2)
    ) AS average_days_late

FROM dbo.orders
WHERE order_status = 'delivered'
    AND order_delivered_customer_date IS NOT NULL
    AND order_estimated_delivery_date IS NOT NULL

GROUP BY
    CASE
        WHEN order_delivered_customer_date <= order_estimated_delivery_date
            THEN 'On Time'
        ELSE 'Late'
    END

ORDER BY total_orders DESC;
----
SELECT
    c.customer_state,

    COUNT(*) AS delivered_orders,

    CAST(
        AVG(
            DATEDIFF(
                DAY,
                o.order_purchase_timestamp,
                o.order_delivered_customer_date
            ) * 1.0
        ) AS DECIMAL(10,2)
    ) AS average_delivery_days,

    CAST(
        100.0 *
        SUM(
            CASE
                WHEN o.order_delivered_customer_date >
                     o.order_estimated_delivery_date
                THEN 1
                ELSE 0
            END
        ) / COUNT(*)
        AS DECIMAL(5,2)
    ) AS late_delivery_rate,

    CAST(
        AVG(
            CASE
                WHEN o.order_delivered_customer_date >
                     o.order_estimated_delivery_date
                THEN DATEDIFF(
                    DAY,
                    o.order_estimated_delivery_date,
                    o.order_delivered_customer_date
                ) * 1.0
            END
        ) AS DECIMAL(10,2)
    ) AS average_days_late

FROM dbo.orders o
INNER JOIN dbo.customers c
    ON o.customer_id = c.customer_id

WHERE o.order_status = 'delivered'
    AND o.order_purchase_timestamp IS NOT NULL
    AND o.order_delivered_customer_date IS NOT NULL
    AND o.order_estimated_delivery_date IS NOT NULL

GROUP BY c.customer_state

ORDER BY late_delivery_rate DESC;
