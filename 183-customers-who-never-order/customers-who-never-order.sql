# Write your MySQL query statement belowse
select c.name as Customers
from Customers c
LEFT JOIN Orders o
on c.id = o.customerId
where o.customerId is Null
