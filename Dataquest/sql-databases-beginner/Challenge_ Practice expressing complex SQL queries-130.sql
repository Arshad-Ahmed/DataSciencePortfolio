## 2. Select and Limit ##

select College_jobs, Median, Unemployment_rate
from recent_grads
LIMIT 20;

## 3. Where ##

select Major
FROM recent_grads
where Major_category= 'Arts'
limit 5;

## 4. Operators ##

select Major, Total, Median, Unemployment_rate
from recent_grads
where Major_category != 'Engineering' AND ((Median <= 50000) OR (Unemployment_rate > 0.065))

## 5. Ordering ##

select Major
from recent_grads
where Major_category != 'Engineering'
order by Major desc
limit 20;