# Write your MySQL query statement below
SELECT email
FROM Person
group by email
having count(email) > 1