# Write your MySQL query statement belowsel
select name 
from SalesPerson
where sales_ID not in (
    SELECT o.sales_id
    FROM Orders o
    JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
)