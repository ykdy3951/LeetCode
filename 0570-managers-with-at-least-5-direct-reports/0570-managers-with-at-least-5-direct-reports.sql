/* Write your PL/SQL query statement below */
SELECT E.name
FROM Employee E
WHERE E.id IN (
    SELECT managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(*) > 4
)