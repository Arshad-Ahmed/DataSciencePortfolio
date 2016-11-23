## 3. Psycopg2 ##

import  psycopg2 as psy

conn = psy.connect("dbname=dq user=dq")
cur = conn.cursor()

print(cur)

conn.close()

## 4. Creating a table ##

import  psycopg2 as psy

conn = psy.connect("dbname=dq user=dq")
cur = conn.cursor()

q = """
CREATE TABLE notes(
   id interger PRIMARY KEY,
   body text,
   title text);
"""

cur.execute(q)

conn.close()

## 5. SQL Transactions ##

import  psycopg2 as psy

conn = psy.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("CREATE TABLE notes(id integer PRIMARY KEY, body text, title text)")
conn.commit()
conn.close()

## 6. Autocommitting ##

conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit=True
cur = conn.cursor()
cur.execute("CREATE TABLE facts(id integer PRIMARY KEY, country text, value integer)")
conn.close()

## 7. Executing queries ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("INSERT INTO notes VALUES (1,'Do more missions on Dataquest.', 'Dataquest reminder');")
cur.execute("SELECT * FROM notes;")
print(cur.fetchall())

conn.close()

## 8. Creating a database ##

conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit=True
cur = conn.cursor()

cur.execute("CREATE DATABASE income OWNER dq")
conn.close()

## 9. Deleting a database ##

conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit=True
cur = conn.cursor()

cur.execute("DROP DATABASE income")
conn.close()