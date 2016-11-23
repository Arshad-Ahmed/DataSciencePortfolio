## 2. And operator ##

SELECT Major,ShareWomen,Employed
FROM recent_grads
WHERE ShareWomen > 0.5 AND Employed > 10000 LIMIT 10;

## 3. Or operator ##

SELECT Major, Median, Unemployed
FROM recent_grads
WHERE Median >= 10000 OR Unemployed < 1000 LIMIT 20;

## 4. Grouping operators ##

select Major, Major_category, ShareWomen, Unemployment_rate
from recent_grads
where (Major_category = 'Engineering') and (ShareWomen > 0.5 or Unemployment_rate < 0.051);

## 5. Practice grouping operators ##

SELECT Major, Major_category, Employed, Unemployment_rate
FROM recent_grads
WHERE (Major_category='Business' or Major_category='Arts' or
Major_category='Health') AND (Employed > 20000 or Unemployment_rate< 0.051);

## 6. Order by ##

SELECT Major 
from recent_grads
Order by Major desc
LIMIT 10;

## 7. Order using multiple columns ##

select Major_category, Median, Major
from recent_grads
order by Major asc, Median desc
limit 20;