/* Write your PL/SQL query statement below */
WITH banned_user AS
(
    SELECT U.users_id AS id
    FROM Users U
    WHERE U.banned = 'Yes'
)

SELECT T.request_at AS Day, ROUND(COUNT(CASE WHEN T.status != 'completed' then 1 end) / COUNT(*), 2) AS "Cancellation Rate"
FROM Trips T
WHERE T.client_id NOT IN (SELECT id FROM banned_user) AND T.driver_id NOT IN (SELECT id FROM banned_user)
AND TO_DATE(T.request_at, 'YYYY-MM-DD') BETWEEN TO_DATE('2013-10-01', 'YYYY-MM-DD') 
AND TO_DATE('2013-10-03', 'YYYY-MM-DD')
GROUP BY T.request_at