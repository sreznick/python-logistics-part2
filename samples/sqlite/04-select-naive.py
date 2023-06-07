import sqlite3

with sqlite3.connect('db') as conn:
    conn.execute("DROP TABLE IF EXISTS movies")
    conn.execute("CREATE TABLE movies(title text, year int, score char(10))")
    print(conn.execute("SELECT * from movies"))

