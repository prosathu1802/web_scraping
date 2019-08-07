import sqlite3

conn = sqlite3.connect("mydatabase.db")

c = conn.cursor()

for row in conn.execute('SELECT * FROM celebs'):
    print(row)

c.execute("SELECT * FROM celebs WHERE name=?", ('HEllo West',))
print(c.fetchone())
