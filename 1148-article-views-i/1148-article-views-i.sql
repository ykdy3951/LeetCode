/* Write your PL/SQL query statement below */
SELECT DISTINCT author_id AS ID
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id ASC