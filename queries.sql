SELECT p.name, SUM(o.qty*p.price) AS revenue FROM orders o JOIN products p ON p.id=o.product_id GROUP BY p.name ORDER BY revenue DESC;
SELECT customer, COUNT(*) AS orders_count FROM orders GROUP BY customer HAVING COUNT(*)>1 ORDER BY orders_count DESC;
WITH m AS (SELECT substr(o.day,1,7) AS month, SUM(o.qty*p.price) AS revenue FROM orders o JOIN products p ON p.id=o.product_id GROUP BY month)
SELECT month, revenue, revenue - LAG(revenue) OVER (ORDER BY month) AS change, SUM(revenue) OVER (ORDER BY month) AS running_total FROM m
