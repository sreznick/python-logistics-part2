import sqlite3
import sys

db_name = sys.argv[1]

with sqlite3.connect(db_name) as conn:
    conn.execute("CREATE TABLE movie(title text, year int, score char(3))")
