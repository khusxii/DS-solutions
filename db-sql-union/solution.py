SELECT u.id, u.name, u.email FROM users u
UNION 
SELECT a.id, a.name, a.email FROM archive_users a;
