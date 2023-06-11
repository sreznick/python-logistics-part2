import sqlite3

with sqlite3.connect('db') as conn:
    conn.execute("DROP TABLE IF EXISTS movies")
    conn.execute("CREATE TABLE movies(title text, year int, score char(10))")
    conn.execute("INSERT INTO movies VALUES ('some title', 1999, 'good')")
    conn.execute("INSERT INTO movies VALUES ('another title', 1999, 'bad')")
    conn.execute("INSERT INTO movies VALUES ('yet another', 2003, 'good')")
    conn.execute("UPDATE movies SET score = 'cool' WHERE title = 'some title'")
    print(conn.execute("SELECT *  from movies").fetchall())

