## 3. Connect to the database ##

import sqlite3 

conn = connect('jobs.db')


## 6. Running a query ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = "select Major from recent_grads;"
cursor.execute(query)
majors = cursor.fetchall()
print(majors[0:2])

## 8. Fetching a specific number of results ##

import sqlite3
conn = sqlite3.connect("jobs.db")
query ="select major, Major_category from recent_grads;"
cursor = conn.cursor()
five_results = cursor.execute(query).fetchmany(5)
print(five_results)

## 9. Closing the connection ##

conn = sqlite3.connect("jobs.db")
conn.close()

## 10. Practice ##

conn = sqlite3.connect('jobs.db')
query= 'select Major from recent_grads order by major desc;'
reverse_alphabetical = conn.execute(query).fetchall()
print(reverse_alphabetical[:5])
conn.close()