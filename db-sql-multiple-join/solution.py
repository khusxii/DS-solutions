SELECT u.name AS user_name, p.name AS product_name, o.quantity FROM users u
JOIN orders o ON o.user_id = u.id
JOIN products p ON p.id = o.product_id;
