/* Write your PL/SQL query statement below */
SELECT P.product_name, SUM(O.unit) AS unit
FROM Products P
LEFT JOIN (
    SELECT O.product_id, O.order_date, O.unit
    FROM Orders O
    WHERE TO_CHAR(O.order_date, 'YYYY-MM') = '2020-02'
) O
ON P.product_id = O.product_id
GROUP BY P.product_id, P.product_name
HAVING SUM(O.unit) >= 100