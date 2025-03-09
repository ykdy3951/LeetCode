/* Write your PL/SQL query statement below */
SELECT *
FROM department
PIVOT (SUM(revenue) Revenue
    FOR month IN (
        'Jan' Jan,
        'Feb' Feb,
        'Mar' Mar,
        'Apr' Apr,
        'May' May,
        'Jun' Jun,
        'Jul' Jul,
        'Aug' Aug,
        'Sep' Sep,
        'Oct' Oct,
        'Nov' Nov,
        'Dec' Dec
    )
)