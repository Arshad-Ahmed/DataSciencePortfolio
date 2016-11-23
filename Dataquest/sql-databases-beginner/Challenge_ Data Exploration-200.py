## 1. Introduction ##

import sqlite3
conn = sqlite3.connect("factbook.db")

pop_avg = conn.execute("SELECT AVG(population) FROM facts;").fetchall()
pop_growth_avg = conn.execute("SELECT AVG(population_growth) FROM facts;").fetchall() 
birth_rate_avg = conn.execute("SELECT AVG(birth_rate) FROM facts;").fetchall() 
death_rate_avg = conn.execute("SELECT AVG(death_rate) FROM facts;").fetchall()

pop_avg = pop_avg[0][0]
pop_growth_avg = pop_growth_avg[0][0] 
birth_rate_avg = birth_rate_avg[0][0]
death_rate_avg = death_rate_avg[0][0]


## 2. Ranges ##

conn = sqlite3.connect("factbook.db")

averages = "select avg(population), avg(population_growth), avg(birth_rate), avg(death_rate), avg(migration_rate) from facts;"
avg_results = conn.execute(averages).fetchall()
pop_avg = avg_results[0][0]
pop_growth_avg = avg_results[0][1]
birth_rate_avg = avg_results[0][2]
death_rate_avg = avg_results[0][3]
mig_rate_avg = avg_results[0][4]

minimum = "select min(population), min(population_growth), min(birth_rate), min(death_rate), min(migration_rate) from facts;"
min_results = conn.execute(minimum).fetchall()
pop_min = min_results[0][0]
pop_growth_min = min_results[0][1]
birth_rate_min = min_results[0][2]
death_rate_min = min_results[0][3]
mig_rate_min = min_results[0][4]

maxi = "select max(population), max(population_growth), max(birth_rate), max(death_rate), max(migration_rate) from facts;"
max_results = conn.execute(maxi).fetchall()
pop_max = max_results[0][0]
pop_growth_max = max_results[0][1]
birth_rate_max = max_results[0][2]
death_rate_max = max_results[0][3]
mig_rate_max = max_results[0][4]

## 3. Filtering ##

conn = sqlite3.connect("factbook.db")
min_and_max = '''
select min(population), max(population), min(population_growth), max(population_growth),
min(birth_rate), max(birth_rate), min(death_rate), max(death_rate)
from facts where population > 0 and population < 2000000000;
'''
results = conn.execute(min_and_max).fetchall()
print(results)

# population column
pop_min = results[0][0]
pop_max = results[0][1]
# population_growth column
pop_growth_min = results[0][2]
pop_growth_max = results[0][3]
# birth_rate column
birth_rate_min = results[0][4]
birth_rate_max = results[0][5]
# death_rate column
death_rate_min = results[0][6]
death_rate_max = results[0][7]

## 4. Predicting future population growth ##

import sqlite3
conn = sqlite3.connect("factbook.db")


projected_population = conn.execute("select round(population + (population *(population_growth/100)),0)\
             FROM facts\
             where population is not null and population_growth is not null AND population > 0 and population < 7000000000 ;").fetchall()

## 5. Exploring projected population ##

import sqlite3
conn = sqlite3.connect("factbook.db")

proj_pop_query = '''
select round(min(population + population * (population_growth/100)), 0), 
round(max(population + population * (population_growth/100)), 0), 
round(avg(population + population * (population_growth/100)), 0)
from facts 
where population > 0 and population < 7000000000 and 
population is not null and population_growth is not null;
'''

proj_results = conn.execute(proj_pop_query).fetchall()

pop_proj_min = proj_results[0][0]
pop_proj_max = proj_results[0][1]
pop_proj_avg = proj_results[0][2]

