/* Write your PL/SQL query statement below */
SELECT a.id
FROM Weather a
LEFT JOIN Weather b
ON a.recordDate - 1 = b.recordDate
WHERE a.temperature > b.temperature