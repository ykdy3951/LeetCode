/* Write your PL/SQL query statement below */
SELECT C.name AS NAME
FROM Customer C
WHERE C.referee_id IS NULL OR C.referee_id != 2