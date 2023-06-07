import sqlite3

with sqlite3.connect('db') as conn:
    conn.execute("DROP TABLE IF EXISTS movies")
    conn.execute("CREATE TABLE movies(title text, year int, score char(10))")
    conn.execute("INSERT INTO movies VALUES ('some title', 1999, 'good')")
    print(conn.execute("SELECT title, score from movies").fetchall())

