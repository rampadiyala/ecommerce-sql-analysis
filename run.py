"""Run SQL analysis on randomly generated sample orders (not real business data)."""
import random, sqlite3
random.seed(1)
db = sqlite3.connect(':memory:')
db.executescript("""CREATE TABLE products(id INTEGER PRIMARY KEY, name TEXT, price REAL);
CREATE TABLE orders(id INTEGER PRIMARY KEY, customer INT, product_id INT, qty INT, day TEXT);""")
db.executemany('INSERT INTO products VALUES(?,?,?)', [(1,'Keyboard',900),(2,'Mouse',400),(3,'Monitor',8000),(4,'Headset',1500)])
db.executemany('INSERT INTO orders VALUES(?,?,?,?,?)', [(i, random.randint(1,80), random.randint(1,4), random.randint(1,3), f'2025-{random.randint(1,12):02}-{random.randint(1,28):02}') for i in range(1,501)])
for q in open('queries.sql').read().split(';'):
    if q.strip():
        cur = db.execute(q)
        print([c[0] for c in cur.description]); print(*cur.fetchmany(12), sep='\n'); print()
