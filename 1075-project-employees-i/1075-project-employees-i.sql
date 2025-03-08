/* Write your PL/SQL query statement below */
SELECT project_id, ROUND(AVG(experience_years), 2) AS average_years
FROM Project
LEFT JOIN Employee
ON Employee.employee_id = Project.employee_id
GROUP BY project_id