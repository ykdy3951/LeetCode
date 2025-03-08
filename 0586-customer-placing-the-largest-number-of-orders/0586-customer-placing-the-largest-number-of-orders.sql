/* Write your PL/SQL query statement below */
SELECT customer_number
FROM (
    SELECT customer_number, COUNT(customer_number) AS order_count
    FROM orders
    GROUP BY customer_number
    ORDER BY order_count DESC NULLS LAST
) WHERE rownum = 1;