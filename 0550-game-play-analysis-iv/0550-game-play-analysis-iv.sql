/* Write your PL/SQL query statement below */
SELECT ROUND(COUNT(A2.player_id) / COUNT(A1.player_id), 2) AS fraction
FROM Activity A1 LEFT JOIN Activity A2 ON A1.event_date + 1 = A2.event_date AND A1.player_id = A2.player_id 
WHERE (A1.player_id, A1.event_date) IN (
    SELECT player_id, MIN(event_date) FROM Activity GROUP BY player_id
)