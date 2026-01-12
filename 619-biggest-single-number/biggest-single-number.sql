select max(num) as num 
from (
    select num 
    from MyNumbers
    Group by num
    Having count(*) = 1

)t;