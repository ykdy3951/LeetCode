/* Write your PL/SQL query statement below */
WITH max_salary AS
(
    SELECT MAX(E.salary) AS salary, E.departmentId AS id
    FROM Employee E
    GROUP BY E.departmentId
)

SELECT D.name AS Department, E.name AS Employee, E.salary
FROM Employee E 
LEFT JOIN Department D
ON E.departmentId = D.id
, max_salary M
WHERE E.salary = M.salary AND E.departmentId = M.id