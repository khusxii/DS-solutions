SELECT user_id, COUNT(id) AS order_count FROM orders
GROUP BY user_id;
