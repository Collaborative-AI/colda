import sqlite3
import sys
import functools
# create database and database connection
sql_db = sqlite3.connect("Test.db")

# create a cursor object
cur = sql_db.cursor()

# create a simple table
cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name TEXT,age INTEGER)")

# add new data
cur.execute("INSERT OR IGNORE INTO test values(?,?,?)", (6, "test_user_1", 20))

# event commit
sql_db.commit()

# close cursor object and database connection (close cursor first)
cur.close()
sql_db.close()



