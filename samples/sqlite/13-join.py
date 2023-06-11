import sqlite3

with sqlite3.connect('db') as conn:
    conn.execute("DROP TABLE IF EXISTS info")
    conn.execute("DROP TABLE IF EXISTS insurance")

    conn.execute("CREATE TABLE info(id char(10), name text, position char(20))")
    conn.execute("CREATE TABLE insurance(id char(10), police_id char(10), level int)")

    conn.execute("INSERT INTO info VALUES ('12345', 'Ivan Petrov', 'engineer')")
    conn.execute("INSERT INTO info VALUES ('23456', 'Nikolay Sidorov', 'senior engineer')")

    conn.execute("INSERT INTO insurance VALUES ('12345', 'aaa-2143423', 2)")
    conn.execute("INSERT INTO insurance VALUES ('12345', 'aab-2154523', 3)")

    print(conn.execute("SELECT *  from info").fetchall())
    print(conn.execute("SELECT *  from insurance").fetchall())

    print(conn.execute("SELECT * from info JOIN insurance ON info.id = insurance.id").fetchall())
    print(conn.execute("SELECT info.id, name, position, level from info "
                       " JOIN insurance ON info.id = insurance.id").fetchall())

    print(conn.execute("SELECT info.id, name, position, level from info "
                       " JOIN insurance ON info.id = insurance.id "
                       " WHERE level <= 2;").fetchall())

    print(conn.execute("SELECT info.id, name, position, level from info "
                       " INNER JOIN insurance ON info.id = insurance.id").fetchall())
    print(conn.execute("SELECT info.id, name, position, level from info "
                       " LEFT JOIN insurance ON info.id = insurance.id").fetchall())

