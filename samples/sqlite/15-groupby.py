import sqlite3

with sqlite3.connect('db') as conn:
    conn.execute('DROP TABLE IF EXISTS orders')

    conn.execute("CREATE TABLE orders(order_id char(10), "
                 "user_id char(10), value int)")

    conn.execute("INSERT INTO orders VALUES ('111111', '12345', 1000)")
    conn.execute("INSERT INTO orders VALUES ('111112', '12345', 4500)")
    conn.execute("INSERT INTO orders VALUES ('111113', '34567', 3000)")
    conn.execute("INSERT INTO orders VALUES ('111114', '12345', 500)")
    conn.execute("INSERT INTO orders VALUES ('111113', '34567', 5000)")

    result = conn.execute("SELECT user_id, COUNT(user_id), SUM(value) "
                          "FROM orders GROUP BY user_id "
                          )
    for record in result:
        print(record)
