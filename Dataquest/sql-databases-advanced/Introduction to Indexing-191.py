## 1. Introduction ##

import sqlite3 as sql

conn = sql.connect("factbook.db")
cur = conn.cursor()
schema = cur.execute("PRAGMA TABLE_INFO(facts)").fetchall()

for i in schema:
    print(i)

## 3. Explain query plan ##

conn = sqlite3.connect("factbook.db")
query_plan_one = conn.execute("explain query plan select * from facts where area > 40000;").fetchall()
query_plan_two = conn.execute("explain query plan select area from facts where area > 40000;").fetchall()
query_plan_three = conn.execute("explain query plan select * from facts where name = 'Czech Republic';").fetchall()

print(query_plan_one)
print(query_plan_two)
print(query_plan_three)

## 5. Time complexity ##

conn = sqlite3.connect("factbook.db")
query_plan_four = conn.execute("explain query plan select * from facts where id= 20").fetchall()
print(query_plan_four)

## 9. All together now ##

conn = sqlite3.connect("factbook.db")
query_plan_six = conn.execute("explain query plan select * from facts where population > 10000 ;").fetchall()
print(query_plan_six)
conn.execute("create index if not exists pop_idx on facts(population)")
query_plan_seven = conn.execute("explain query plan select * from facts where population > 10000 ;").fetchall()
print(query_plan_seven)