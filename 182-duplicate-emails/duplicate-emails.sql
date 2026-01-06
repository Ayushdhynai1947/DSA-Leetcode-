# Write your MySQL query statement below
-- select DISTINCT email as Email  
-- from Person
-- limit 1;

SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;
