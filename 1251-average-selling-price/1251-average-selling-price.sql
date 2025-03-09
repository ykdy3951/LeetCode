/* Write your PL/SQL query statement below */
SELECT P.product_id, 
    CASE 
        WHEN SUM(U.units) IS NOT NULL THEN ROUND(SUM(P.price * U.units) / SUM(U.units), 2) 
        ELSE 0 
    END AS average_price
FROM UnitsSold U 
FULL OUTER JOIN Prices P
ON U.product_id = P.product_id AND U.purchase_date BETWEEN P.start_date AND P.end_date
GROUP BY P.product_id