/* Write your PL/SQL query statement below */
WITH max_salary AS 
(
    SELECT departmentId AS id, salary, RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rank
    FROM Employee
    GROUP BY departmentId, salary
);

SELECT D.name AS Department, E.name AS Employee, E.salary
FROM max_salary M, Employee E 
Left JOIN Department D 
ON E.departmentId = D.id
WHERE M.id = D.id AND M.salary = E.salary AND M.rank < 4