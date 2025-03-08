# Write your MySQL query statement below
SELECT name as Customers
FROM Customers as a 
LEFT JOIN Orders as b
ON a.id = b.customerId
WHERE b.id is NULL