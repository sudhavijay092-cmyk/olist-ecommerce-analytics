USE SwiftCart_Margin_Under_Pressure;
GO


WITH delivery_by_state AS (

    SELECT
        c.customer_state,

        COUNT(DISTINCT o.order_id) AS delivered_orders,

        ROUND(
            AVG(
                CASE
                    WHEN o.order_delivered_customer_date
                         > o.order_estimated_delivery_date
                    THEN DATEDIFF(
                        DAY,
                        o.order_estimated_delivery_date,
                        o.order_delivered_customer_date
                    )
                END
            ),
            2
        ) AS average_days_late,

        ROUND(
            SUM(
                CASE
                    WHEN o.order_delivered_customer_date
                         > o.order_estimated_delivery_date
                    THEN 1
                    ELSE 0
                END
            ) * 100.0
            / NULLIF(COUNT(DISTINCT o.order_id), 0),
            2
        ) AS late_delivery_percentage

    FROM dbo.orders AS o

    INNER JOIN dbo.customers AS c
        ON o.customer_id = c.customer_id

    WHERE
        o.order_delivered_customer_date IS NOT NULL
        AND o.order_estimated_delivery_date IS NOT NULL

    GROUP BY
        c.customer_state
),


freight_by_state AS (

    SELECT
        c.customer_state,

        ROUND(
            SUM(oi.freight_value),
            2
        ) AS total_freight_cost,

        ROUND(
            SUM(oi.freight_value) * 100.0
            / NULLIF(SUM(oi.price), 0),
            2
        ) AS freight_percentage_of_product_value

    FROM dbo.orders AS o

    INNER JOIN dbo.customers AS c
        ON o.customer_id = c.customer_id

    INNER JOIN dbo.order_items AS oi
        ON o.order_id = oi.order_id

    GROUP BY
        c.customer_state
),


reviews_by_state AS (

    SELECT
        c.customer_state,

        COUNT(DISTINCT o.order_id) AS orders_with_reviews,

        ROUND(
            AVG(CAST(r.review_score AS DECIMAL(10,2))),
            2
        ) AS average_review_score,

        ROUND(
            SUM(
                CASE
                    WHEN r.review_score <= 2
                    THEN 1
                    ELSE 0
                END
            ) * 100.0
            / NULLIF(COUNT(*), 0),
            2
        ) AS low_rating_percentage

    FROM dbo.orders AS o

    INNER JOIN dbo.customers AS c
        ON o.customer_id = c.customer_id

    INNER JOIN dbo.reviews AS r
        ON o.order_id = r.order_id

    WHERE
        r.review_score IS NOT NULL

    GROUP BY
        c.customer_state
)


SELECT
    d.customer_state,

    d.delivered_orders,

    d.late_delivery_percentage,

    d.average_days_late,

    f.total_freight_cost,

    f.freight_percentage_of_product_value,

    r.orders_with_reviews,

    r.average_review_score,

    r.low_rating_percentage

FROM delivery_by_state AS d

LEFT JOIN freight_by_state AS f
    ON d.customer_state = f.customer_state

LEFT JOIN reviews_by_state AS r
    ON d.customer_state = r.customer_state

ORDER BY
    d.late_delivery_percentage DESC,
    f.freight_percentage_of_product_value DESC,
    r.average_review_score ASC;
GO