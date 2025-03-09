/* Write your PL/SQL query statement below */
SELECT *
FROM products
WHERE REGEXP_LIKE(description, 'SN[0-9]{4}-[0-9]{4}([^0-9]|$)')
ORDER BY product_id