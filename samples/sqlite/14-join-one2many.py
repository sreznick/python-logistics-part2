import sqlite3

with sqlite3.connect('db') as conn:
    conn.execute('DROP TABLE IF EXISTS users')
    conn.execute('DROP TABLE IF EXISTS orders')

    conn.execute("CREATE TABLE users(user_id char(10), name text)")
    conn.execute("CREATE TABLE orders(order_id char(10), "
                 "user_id char(10), value int)")

    conn.execute("INSERT INTO users VALUES ('12345', 'Ivan Petrov')")
    conn.execute("INSERT INTO users VALUES ('23456', 'Nikolay Sidorov')")
    conn.execute("INSERT INTO users VALUES ('34567', 'Vasily Ivanov')")

    conn.execute("INSERT INTO orders VALUES ('111111', '12345', 1000)")
    conn.execute("INSERT INTO orders VALUES ('111112', '12345', 4500)")
    conn.execute("INSERT INTO orders VALUES ('111113', '34567', 3000)")
    conn.execute("INSERT INTO orders VALUES ('111114', '12345', 500)")
    conn.execute("INSERT INTO orders VALUES ('111113', '34567', 5000)")

    result = conn.execute("SELECT * from users "
                          "JOIN orders ON users.user_id = orders.user_id")
    for record in result:
        print(record)

    print()

    result = conn.execute("SELECT name from users "
                          "LEFT JOIN orders ON users.user_id = orders.user_id "
                          "WHERE orders.user_id IS NULL")
    for record in result:
        print(record)

    print()


