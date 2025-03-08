/* Write your PL/SQL query statement below */
SELECT name
FROM SalesPerson S
WHERE S.sales_id NOT IN (
    SELECT O.sales_id
    FROM Orders O
    LEFT JOIN Company C
    ON O.com_id = C.com_id
    WHERE C.name = 'RED'
)