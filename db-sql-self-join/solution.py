SELECT e.name AS employee, m.name as manager FROM employees e
JOIN employees m
ON m.id = e.manager_id;
