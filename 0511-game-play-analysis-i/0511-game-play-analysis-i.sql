/* Write your PL/SQL query statement below */
SELECT a.player_id, TO_CHAR(MIN(a.event_date),'YYYY-MM-DD') as first_login
FROM Activity a
GROUP BY a.player_id