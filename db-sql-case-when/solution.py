SELECT name, 
  CASE
    WHEN age<18 THEN 'minor'
    WHEN age>64 THEN 'senior'
    ELSE 'adult'
  END AS age_group
FROM users;
