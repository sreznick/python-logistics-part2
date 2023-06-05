import sqlite3

with sqlite3.connect('db') as conn:
    print(conn)

